import sqlite3
con = sqlite3.connect("smarthome.db")
cursor = con.cursor()

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

    con.commit()
initiate_database()
def update_room_actuator(room, actuator, val):
    con = sqlite3.connect("smarthome.db")
    cursor = con.cursor()
    cursor.execute("UPDATE {} SET {}={} WHERE rowid =1".format(room, actuator, val))
    con.commit()
update_room_actuator(1, 1,1)


