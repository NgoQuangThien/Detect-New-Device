import pymysql.cursors
import time


def connect_to_db():
    return pymysql.connect(host='10.10.10.3',
                            user='root',
                            password='xv7AUpuZmZ5jW8z0lJz5',
                            database='bids_detect_new_device',
                            cursorclass=pymysql.cursors.DictCursor)

def select_white_list(connection):
    with connection:
        with connection.cursor() as select_cursor:
            # Read a single record
            sql = "SELECT mac FROM white_list"
            select_cursor.execute(sql)
            result = select_cursor.fetchall()
            return result

def insert_new_device(connection, mac, ip):
    with connection:
        with connection.cursor() as insert_cursor:
            # Create a new record
            sql = "INSERT INTO new_devices (`mac`, `ip`) VALUES (%s, %s)"
            insert_cursor.execute(sql, (mac, ip))
        connection.commit()
