import re


regex_mac = r"mac:[-+]?[\d]+"
regex_ip = r"ip:[-+]?[\d]+"

def get_mac_addr(dump_str):
    matches = re.finditer(regex_mac, dump_str)
    for matchNum, match in enumerate(matches, start=1):
        return ("{match}".format(match = match.group()))

def get_ip_addr(dump_str):
    matches = re.finditer(regex_ip, dump_str)
    for matchNum, match in enumerate(matches, start=1):
        return ("{match}".format(match = match.group()))
