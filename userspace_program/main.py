import json
import time
from datetime import datetime
import threading

from lib import regex_host_info
from lib import alert_logging
from lib import converter
from lib import db_processor


ignore_interval = 3600 # 1 hour
ignore_list = {}
white_list = []
log_path = "/home/soc/Detect-New-Device/userspace_program/log/"
message_template = """{
                        "@timestamp": "*",
                        "rule": {
                            "name": "Detected new device"
                        },
                        "host": {
                            "ip": "*",
                            "mac": "*"
                        },
                        "event": {
                            "dataset": "alert",
                            "event.severity_label": "critical",
                            "module": "bids"
                        }
                    }"""

def get_device_list(connection):
    temp = db_processor.select_white_list(connection)
    white_list = [device.get('mac').lower() for device in temp]
    return white_list

def message_processor(current_time, mac_addr, ip_addr):
    msg = json.loads(message_template)
    msg['@timestamp'] = current_time
    msg['host']['ip'] = ip_addr
    msg['host']['mac'] = mac_addr
    return msg

def interval_countdown_ignore():
    temp_list = []
    while True:
        current_time = datetime.now().timestamp()
        if len(ignore_list):
            for value in ignore_list:
                if ((current_time - ignore_list[value]) > ignore_interval) and value not in temp_list:
                    temp_list.append(value)

            if temp_list:
                for value in temp_list: 
                    del ignore_list[value]
                    temp_list.remove(value)

        time.sleep(1)

def white_list_reload():
    global white_list
    while True:
        connection = db_processor.connect_to_db()
        white_list = get_device_list(connection)
        time.sleep(5)

def logging_to_mysql(mac, ip):
    connection = db_processor.connect_to_db()
    db_processor.insert_new_device(connection ,mac, ip)

if __name__ == "__main__":
    # Create database if not exists
    db_processor.create_database()

    # Get white_list
    connection = db_processor.connect_to_db()
    white_list = get_device_list(connection)

    # Start worker logging to file
    alert_logging.create_time_based_rotating_log(log_path)

    # Thread for remove the device from ignore_list when the time period ends
    countdown_thread = threading.Thread(name='interval_countdown_ignore', target=interval_countdown_ignore)
    countdown_thread.setDaemon(True)
    countdown_thread.start()

    # Thread for reload white_list
    reload_white_list_thread = threading.Thread(name='white_list_reload', target=white_list_reload)
    reload_white_list_thread.setDaemon(True)
    reload_white_list_thread.start()

    with open("/sys/kernel/debug/tracing/trace_pipe", 'r', encoding='UTF-8') as f:
        while True:
            line = f.readline().rstrip()
            # get MAC integer format
            mac_addr = regex_host_info.get_mac_addr(line)
            if mac_addr:
                # Split regex string
                mac_addr = mac_addr[4:len(mac_addr)]

                # Convert address
                mac_addr = converter.u64_to_mac(int(mac_addr))

                # Processor
                # Has new device
                if mac_addr not in white_list and mac_addr not in ignore_list:
                    # get IP integer format
                    ip_addr = regex_host_info.get_ip_addr(line)

                    # Split regex string
                    ip_addr = ip_addr[3:len(ip_addr)]

                    # Convert address
                    ip_addr = converter.u32_to_ip(int(ip_addr))

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

                    # Logging event to file
                    message = message_processor(current_time, mac_addr, ip_addr)
                    logger = alert_logging.logging.getLogger("Rotating Log")
                    logger.propagate = False
                    logger.critical(message)

                    # Logging event to MySQL
                    logging_to_mysql(mac_addr, ip_addr)

                    # Add device to ignore_list
                    ignore_list[mac_addr] = now.timestamp()

                    # Keep alive countdown_thread
                    if not countdown_thread.isAlive: countdown_thread.start()
                    if not reload_white_list_thread.isAlive: reload_white_list_thread.start()
