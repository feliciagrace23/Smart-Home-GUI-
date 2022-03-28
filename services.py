import db.py as db

def user_login(tup):
    return db.user_login(tup)

def user_register(tup):
    db.user_register(tup)

def update_email(status, new):
    db.update_email(status, new)

def update_password(status, new):
    db.update_password(status, new)

def update_room_actuator(room, actuator, val):
    db.update_room_actuator(room, actuator, val)

def print_table_content(room):
    db.print_table_content(room)

def init_db():
    db.initiate_database()

def update_all_room(k1, k2, k3, bath1, bath2, l1, l2, l3, bed1, bed2, bed3):
    db.update_all_room(k1, k2, k3, bath1, bath2, l1, l2, l3, bed1, bed2, bed3)

def get_status(email):
    return db.get_status(email)

def bathroom_services(config):
    lampu = int(config['BATHROOM']['ldr_bathroom'])
    motion = int(config['BATHROOM']['motion_sensor_bathroom'])
    if motion >= 1:
        musik_value = 1
        if lampu >= 33:
            lampu_value = 0
        if lampu < 33:
            lampu_value = 1
    if motion < 1:
        musik_value = 0
        lampu_value = 0

    lastest_value = db.check_table_content("db_bathroom")
    db.update_room_actuator("db_bathroom", "lampu", lampu_value)
    db.update_room_actuator("db_bathroom", "musik", musik_value)
    items = db.check_table_content("db_bathroom")

    return lastest_value, items, lampu_value, musik_value

def bedroom_services(config):
    lampu = int(config['BEDROOM']['ldr_bedroom'])
    motion = int(config['BEDROOM']['motion_sensor_bedroom'])
    temp = int(config['BEDROOM']['temp_bedroom'])
    time = int(config['BEDROOM']['time'])
    if time > 6 and time < 22:
        if motion >= 1:
            musik_value = 1
            if lampu >= 33:
                lampu_value = 0
            if lampu < 33:
                lampu_value = 1
            if temp >= 33:
                ac_value = 1
            if temp < 33:
                ac_value = 0
        if motion < 1:
            musik_value = 0
            lampu_value = 0
            ac_value = 0
    else:
        lampu_value = 0
        musik_value = 0
        if motion == 1 and temp > 33:
            ac_value = 1
        else:
            ac_value = 0
    # cursor.execute("SELECT rowid,* FROM db_bedroom")
    # items = check_table_content("db_bedroom")
    lastest_value = db.check_table_content("db_bedroom")
    db.update_room_actuator("db_bedroom", "lampu", lampu_value)
    db.update_room_actuator("db_bedroom", "musik", musik_value)
    db.update_room_actuator("db_bedroom", "ac", ac_value)
    # cursor.execute("UPDATE db_bedroom SET lampu=? WHERE rowid =1", (lampu_value,))
    # cursor.execute("UPDATE db_bedroom SET musik=? WHERE rowid=1", (musik_value,))
    # cursor.execute("UPDATE db_bedroom SET ac=? WHERE rowid=1", (ac_value,))
    # connection.commit()
    # cursor.execute("SELECT rowid,* FROM db_bedroom")
    items = db.check_table_content("db_bedroom")

    return lastest_value, items, lampu_value, musik_value, ac_value

def kitchen_services(config):
    lampu = int(config['KITCHEN']['ldr_kitchen'])
    motion = int(config['KITCHEN']['motion_sensor_kitchen'])
    temp = int(config['KITCHEN']['temp_kitchen'])
    if motion >= 1:
        musik_value = 1
        if temp >= 33:
            ac_value = 1
        if temp < 33:
            ac_value = 0
        if lampu >= 33:
            lampu_value = 0
        if lampu < 33:
            lampu_value = 1
    if motion < 1:
        musik_value = 0
        ac_value = 0
        lampu_value = 0
    # cursor.execute("SELECT rowid,* FROM db_kitchen")
    # items = cursor.fetchall()
    lastest_value = db.check_table_content("db_kitchen")
    db.update_room_actuator("db_kitchen", "lampu", lampu_value)
    db.update_room_actuator("db_kitchen", "musik", musik_value)
    db.update_room_actuator("db_kitchen", "ac", ac_value)
    # cursor.execute("UPDATE db_kitchen SET lampu=? WHERE rowid =1", (lampu_value,))
    # cursor.execute("UPDATE db_kitchen SET musik=? WHERE rowid=1", (musik_value,))
    # cursor.execute("UPDATE db_kitchen SET ac=? WHERE rowid=1", (ac_value,))
    # connection.commit()
    # cursor.execute("SELECT rowid,* FROM db_kitchen")
    items = db.check_table_content("db_kitchen")

    return lastest_value, items, lampu_value, musik_value, ac_value

def livingroom_services(config):
    lampu = int(config['LIVINGROOM']['ldr_livingroom'])
    motion = int(config['LIVINGROOM']['motion_sensor_livingroom'])
    temp = int(config['LIVINGROOM']['temp_livingroom'])
    if motion >= 1:
        musik_value = 1
        if temp >= 33:
            ac_value = 1
        if temp < 33:
            ac_value = 0
        if lampu >= 33:
            lampu_value = 0
        if lampu < 33:
            lampu_value = 1
    if motion < 1:
        musik_value = 0
        ac_value = 0
        lampu_value = 0

    # cursor.execute("SELECT rowid,* FROM db_livingroom")
    # items = cursor.fetchall()
    lastest_value = db.check_table_content("db_livingroom")
    db.update_room_actuator("db_livingroom", "lampu", lampu_value)
    db.update_room_actuator("db_livingroom", "musik", musik_value)
    db.update_room_actuator("db_livingroom", "ac", ac_value)
    # cursor.execute("UPDATE db_livingroom SET lampu=? WHERE rowid =1", (lampu_value,))
    # cursor.execute("UPDATE db_livingroom SET musik=? WHERE rowid =1", (musik_value,))
    # cursor.execute("UPDATE db_livingroom SET ac=? WHERE rowid =1", (ac_value,))
    # connection.commit()
    # cursor.execute("SELECT rowid,* FROM db_livingroom")
    items = db.check_table_content("db_livingroom")

    return lastest_value, items, lampu_value, musik_value, ac_value




