import pymysql.cursors


manager_ip = "10.2.65.163"
mysql_user = "bids_dnd"
mysql_password = "xv7AUpuZmZ5jW8z0lJz5"
db_name = "bids_dnd"

def create_database():
    connection = pymysql.connect(host=manager_ip,
                                user=mysql_user,
                                password=mysql_password
                                )

    with connection:
        with connection.cursor() as create_cursor:
            sql = "SHOW DATABASES"
            create_cursor.execute(sql)
            status =  [x for x in create_cursor if db_name in x]
            if not status:
                # Create database
                sql = " ".join(["CREATE DATABASE", db_name])
                create_cursor.execute(sql)

                # Create tables
                connection.select_db(db_name)
                sql = "CREATE TABLE IF NOT EXISTS device (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name NVARCHAR(255), mac NVARCHAR(30) NOT NULL, ip NVARCHAR(30), type NVARCHAR(255), os NVARCHAR(100), manager NVARCHAR(255), unit NVARCHAR(255), location NVARCHAR(255))"
                create_cursor.execute(sql)

                sql = "CREATE TABLE new_device (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, mac NVARCHAR(30) NOT NULL, ip NVARCHAR(30))"
                create_cursor.execute(sql)
        connection.commit()

def connect_to_db():
    return pymysql.connect(host=manager_ip,
                            user=mysql_user,
                            password=mysql_password,
                            database=db_name,
                            cursorclass=pymysql.cursors.DictCursor)

def select_white_list(connection):
    with connection:
        with connection.cursor() as select_cursor:
            # Read all record
            sql = "SELECT mac FROM device"
            select_cursor.execute(sql)
            result = select_cursor.fetchall()
            return result

def count_mac_in_new_device(connection, mac):
    with connection:
        with connection.cursor() as select_cursor:
            sql = "SELECT COUNT(mac) FROM new_device WHERE mac = %s"
            select_cursor.execute(sql, (mac))
            result = select_cursor.fetchone()
            return result

def insert_new_device(connection, mac, ip):
    with connection:
        with connection.cursor() as insert_cursor:
            # Create a new record
            sql = "INSERT INTO new_device (mac, ip) VALUES (%s, %s)"
            insert_cursor.execute(sql, (mac, ip))
        connection.commit()
