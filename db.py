import mysql.connector
import sqlite3
import time
# con = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = "",
#     database = ""
# )
con = sqlite3.connect("smarthome.db")
cursor = con.cursor()


def check_all_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())

def reset_all(): # buat hilangin yg udah di tambah
    cursor.execute("DROP TABLE `user`")
    cursor.execute("CREATE TABLE IF NOT EXISTS `user` (`email` TEXT AUTO_INCREMENT, `password` TEXT, `status` TEXT)")
    many_customers = [
        ('parent', 'parent', 'PARENT'),
        ('guest', 'guest', 'GUEST'),
        ('admin', 'admin', 'ADMIN'),
        ('andy', 'andy', 'CHILD')]
    cursor.executemany("INSERT INTO `user` VALUES (?,?,?)", many_customers)
    con.commit()

def initiate_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS db_bathroom (lampu TEXT AUTO_INCREMENT, musik TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS db_livingroom (lampu TEXT AUTO_INCREMENT, musik TEXT, ac TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS db_kitchen (lampu TEXT AUTO_INCREMENT, musik TEXT, ac TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `user` (email TEXT AUTO_INCREMENT, password TEXT, status TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS db_bedroom (lampu TEXT AUTO_INCREMENT, musik TEXT, ac TEXT)")

    cursor.execute("DROP TABLE db_livingroom")
    cursor.execute("DROP TABLE db_bedroom")
    cursor.execute("DROP TABLE db_bathroom")
    cursor.execute("DROP TABLE db_kitchen")

    cursor.execute("CREATE TABLE IF NOT EXISTS db_bedroom (lampu TEXT AUTO_INCREMENT, musik TEXT, ac TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS db_livingroom (lampu TEXT AUTO_INCREMENT, musik TEXT, ac TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS db_kitchen (lampu TEXT AUTO_INCREMENT, musik TEXT, ac TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS db_bathroom (lampu TEXT AUTO_INCREMENT, musik TEXT)")
    new_value = (0, 0)
    cursor.execute("INSERT INTO db_bathroom VALUES (?,?)", new_value)
    new_value = (0, 0, 0)
    cursor.execute("INSERT INTO db_kitchen VALUES (?,?, ?)", new_value)
    cursor.execute("INSERT INTO db_livingroom VALUES (?,?, ?)", new_value)
    cursor.execute("INSERT INTO db_bedroom VALUES (?,?, ?)", new_value)
    reset_all()
    con.commit()

def user_login(tup):
    try:
        cursor.execute("Select * FROM `user` WHERE `email`=? AND `password`=? ", tup)
        return (cursor.fetchone())
    except:
        return False

def get_status(email):
    cursor.execute("Select `status` FROM `user` WHERE `email`=?", (email,))
    return (cursor.fetchone()[0])

def user_register(tup):
    cursor.execute("INSERT INTO `user` (`email`, `password`, 'status') VALUES (?, ?, ?)", tup)
    con.commit()

def update_email(status, new_email):
    cursor.execute("UPDATE `user` SET email=? WHERE status=?", (new_email,status))
    con.commit()

def update_password(status, new_pass):
    cursor.execute("UPDATE `user` SET password=? WHERE status=?", (new_pass,status))
    con.commit()

def update_all_room(k1, k2, k3, bath1, bath2, l1, l2, l3, bed1, bed2, bed3):
    update_room_actuator("db_kitchen", "lampu", k1)
    update_room_actuator("db_kitchen", "musik", k2)
    update_room_actuator("db_kitchen", "ac", k3)

    update_room_actuator("db_bedroom", "lampu", bed1)
    update_room_actuator("db_bedroom", "musik", bed2)
    update_room_actuator("db_bedroom", "ac", bed3)

    update_room_actuator("db_livingroom", "lampu", l1)
    update_room_actuator("db_livingroom", "musik", l2)
    update_room_actuator("db_livingroom", "ac", l3)

    update_room_actuator("db_bathroom", "lampu", bath1)
    update_room_actuator("db_bathroom", "musik", bath2)

def check_table_content(room):
    con = sqlite3.connect("smarthome.db")
    cursor = con.cursor()
    cursor.execute("SELECT rowid,* FROM {}".format(room))
    items = cursor.fetchall()
    return items

def print_table_content(room):
    con = sqlite3.connect("smarthome.db")
    cursor = con.cursor()
    cursor.execute("SELECT rowid,* FROM {}".format(room))
    items = cursor.fetchall()
    print("{}= {}".format(room, items))

def update_room_actuator(room, actuator, val):
    con = sqlite3.connect("smarthome.db")
    cursor = con.cursor()
    cursor.execute("UPDATE {} SET {}={} WHERE rowid =1".format(room, actuator, val))
    con.commit()






