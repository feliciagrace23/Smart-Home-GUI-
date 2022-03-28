#updated file 1.1 fix error and bug
from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
import configparser
import time
import threading
import services.py as sv


class Smarthome:
    def __init__(self):
        self.window = Tk()
        self.window.wm_iconbitmap("CIT Logo square compact.ico")
        self.window.title('Smart Home Application')

        #         self.canvas = Canvas(self.window, width=600, height=400, bg='red')
        #         self.canvas.pack(expand=YES, fill=BOTH)

        width = self.window.winfo_screenmmwidth()
        height = self.window.winfo_screenmmheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)

        sv.init_db()
        sv.update_all_room(1,1,1,1,1,1,1,1,1,1,1)

        str1 = "500x800"
        self.window.geometry(str1)

    def addframe(self):
        self.frame = Frame(self.window, height=1000, width=2000)
        self.frame.place(x=0, y=0)

        x, y = 40, 20
        self.label = Label(self.frame)
        self.label.place(x=-325, y=-150)

        self.label = Label(self.frame, text='User Login')
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y=y + 150)

        self.emlabel = Label(self.frame, text='Enter User')
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y=y + 230)

        self.em = Entry(self.frame, font='Courier 12')
        self.em.place(x=200, y=y + 230)

        self.pslabel = Label(self.frame, text='Enter Pass')
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=y + 260)

        self.ps = Entry(self.frame, show='*', font='Courier 12')
        self.ps.place(x=200, y=y + 260)

        self.button = Button(self.frame, text='Login', activebackground = "black", font='Courier 15 bold', \
                             activeforeground= "white", command=self.Login)
        self.button.place(x=190, y=y + 290)

        self.label2 = Label(self.frame, text="Dont have \naccount? ")
        self.label2.config(font=("Courier", 12, 'bold'))
        self.label2.place(x=50, y=y + 350)

        self.button2 = Button(self.frame, text="Register Now", font='Courier 15 bold', command=self.Register)
        self.button2.place(x=190, y=y + 350)

        self.window.mainloop()

    def Login(self):
        data = (
            self.em.get(),
            self.ps.get()
        )
        if self.em.get() == "" or self.ps.get() == "":
            messagebox.showinfo("System Error", "Please enter email/password")
        else:
            res = sv.user_login(data)
            if res:
                messagebox.showinfo("Login Succesful", "Have a Nice day")
                self.user = sv.get_status(data[0])
                # print(self.user)
                if self.user == "PARENT":
                    self.SmartSettingParent()
                if self.user == "CHILD":
                    self.SmartSettingChild()
                if self.user == "ADMIN":
                    self.ControlPanelAdmin()
                if self.user == "GUEST":
                    messagebox.showwarning("Unauthorized Login", "Please ask parent permission")
                # self.window.destroy()
            else:
                # text = "%s, %s" % (data[0], data[1])
                messagebox.showinfo("Alert", "Wrong Username/Password")

    def Register(self):
        self.window2 = Tk()
        self.window2.wm_iconbitmap("CIT Logo square compact.ico")
        self.window2.title("Sign Up as Our User")

        self.regbutton = StringVar()
        self.regbutton1 = Radiobutton(self.window2, text="Parent", value="PARENT", variable=self.regbutton)
        self.regbutton1.grid(row=0, column=0)
        self.regbutton2 = Radiobutton(self.window2, text="Child", value="CHILD", variable=self.regbutton)
        self.regbutton2.grid(row=0, column=1)
        self.regbutton3 = Radiobutton(self.window2, text="Admin", value="ADMIN", variable=self.regbutton1)
        self.regbutton3.grid(row=0, column=2)

        self.regbutton.set("PARENT")

        self.emslabel = Label(self.window2, text='Enter Your Email')
        self.emslabel.grid(column=0, row=1, sticky=W)

        self.emsentry = Entry(self.window2, font='Courier 12')
        self.emsentry.grid(column=1, row=1, sticky=W)

        self.psslabel = Label(self.window2, text='Enter Your Password')
        self.psslabel.grid(column=0, row=2, sticky=W)

        self.pssentry = Entry(self.window2, show='*', font='Courier 12')
        self.pssentry.grid(column=1, row=2, sticky=W)

        self.sbutton = Button(self.window2, text='Register', command=self.Signup)
        self.sbutton.grid(column=1, row=3, sticky=W)

        # self.label3 = Label(self.window2, text='Have an account?')
        # self.label3.grid(column=0, row=3, sticky=W)
        # self.button = Button(self.window2, text= 'Login now')
        # self.button.grid(column=1, row=3, sticky=W)

    def Signup(self):
        data = (
            self.emsentry.get(),
            self.pssentry.get(),
            self.regbutton.get()
        )

        if self.emsentry.get() == "":
            messagebox.showinfo("Alert", "Please enter email first")
        elif self.pssentry.get() == "":
            messagebox.showinfo("Alert", "Please enter password")
        else:
            res = sv.user_register(data)
            messagebox.showinfo("Confirmation", "Registration Done")
            self.window2.destroy()

    def checkk(self):
        def read_file():
            while (self.auto == True):
                # print(self.auto)
                conf = configparser.ConfigParser()
                conf.read('testing.ini')
                self.Kitchen(conf)
                self.Living_room(conf)
                self.Bathroom(conf)
                self.Bedroom(conf)
                time.sleep(5)
                if self.auto == False:
                    break
        thread = threading.Thread(target=read_file)
        thread.start()

    def manual(self):
        # global auto
        self.auto = False

        self.R1buttonLight["state"] = "normal"
        self.R1buttonAC["state"] = "normal"
        self.R1buttonspeaker["state"] = "normal"
        self.R2buttonLight["state"] = "normal"
        self.R2buttonAC["state"] = "normal"
        self.R2buttonspeaker["state"] = "normal"
        self.R3buttonLight["state"] = "normal"
        self.R3buttonspeaker["state"] = "normal"
        self.R4buttonLight["state"] = "normal"
        self.R4buttonAC["state"] = "normal"
        self.R4buttonspeaker["state"] = "normal"


        self.R1buttonLight["image"] = self.iconon
        self.R1buttonAC["image"] = self.iconon
        self.R1buttonspeaker["image"] = self.iconon
        self.R2buttonLight["image"] = self.iconon
        self.R2buttonAC["image"] = self.iconon
        self.R2buttonspeaker["image"] = self.iconon
        self.R3buttonLight["image"] = self.iconon
        self.R3buttonspeaker["image"] = self.iconon
        self.R4buttonLight["image"] = self.iconon
        self.R4buttonAC["image"] = self.iconon
        self.R4buttonspeaker["image"] = self.iconon

        sv.update_all_room(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    def automatic(self):
        # global auto
        self.auto = True

        self.R1buttonLight["state"] = "disabled"
        self.R1buttonAC["state"] = "disabled"
        self.R1buttonspeaker["state"] = "disabled"
        self.R2buttonLight["state"] = "disabled"
        self.R2buttonAC["state"] = "disabled"
        self.R2buttonspeaker["state"] = "disabled"
        self.R3buttonLight["state"] = "disabled"
        self.R3buttonspeaker["state"] = "disabled"
        self.R4buttonLight["state"] = "disabled"
        self.R4buttonAC["state"] = "disabled"
        self.R4buttonspeaker["state"] = "disabled"

        self.checkk()
        # self.R1buttonLight["image"] = self.iconoff
        # self.R1buttonAC["image"] = self.iconoff
        # self.R1buttonspeaker["image"] = self.iconoff
        # self.R2buttonLight["image"] = self.iconoff
        # self.R2buttonAC["image"] = self.iconoff
        # self.R2buttonspeaker["image"] = self.iconoff
        # self.R3buttonLight["image"] = self.iconoff
        # self.R3buttonspeaker["image"] = self.iconoff
        # self.R4buttonLight["image"] = self.iconoff
        # self.R4buttonAC["image"] = self.iconoff
        # self.R4buttonspeaker["image"] = self.iconoff

    def on_click_light_R1(self):
        if self.R1buttonLight["text"] == "on":
            val = 0
            self.R1buttonLight["image"] = self.iconoff
            self.R1buttonLight["text"] = "off"
            # print("off")
            sv.update_room_actuator("db_kitchen", "lampu", 0)
            sv.print_table_content("db_kitchen")
        else:
            val = 1
            self.R1buttonLight["image"] = self.iconon
            self.R1buttonLight["text"] = "on"
            # print("on")
            sv.update_room_actuator("db_kitchen", "lampu", 1)
            sv.print_table_content("db_kitchen")

    def on_click_AC_R1(self):
        if self.R1buttonAC["text"] == "on":
            val = 0
            self.R1buttonAC["text"] = "off"
            self.R1buttonAC["image"] = self.iconoff
            sv.update_room_actuator("db_kitchen", "ac", 0)
            sv.print_table_content("db_kitchen")
        else:
            val = 1
            self.R1buttonAC["text"] = "on"
            self.R1buttonAC["image"] = self.iconon
            sv.update_room_actuator("db_kitchen", "ac", 1)
            sv.print_table_content("db_kitchen")

    def on_click_speaker_R1(self):
        if self.R1buttonspeaker["text"] == "on":
            val = 0
            self.R1buttonspeaker["text"] = "off"
            self.R1buttonspeaker["image"] = self.iconoff
            sv.update_room_actuator("db_kitchen", "musik", 0)
            sv.print_table_content("db_kitchen")
        else:
            val = 1
            self.R1buttonspeaker["text"] = "on"
            self.R1buttonspeaker["image"] = self.iconon
            sv.update_room_actuator("db_kitchen", "musik", 1)
            sv.print_table_content("db_kitchen")

    def on_click_light_R2(self):
        if self.R2buttonLight["text"] == "on":
            val = 0
            self.R2buttonLight["text"] = "off"
            self.R2buttonLight["image"] = self.iconoff
            sv.update_room_actuator("db_livingroom", "lampu", 0)
            sv.print_table_content("db_livingroom")
        else:
            val = 1
            self.R2buttonLight["text"] = "on"
            self.R2buttonLight["image"] = self.iconon
            sv.update_room_actuator("db_livingroom", "lampu", 1)
            sv.print_table_content("db_livingroom")

    def on_click_AC_R2(self):
        if self.R2buttonAC["text"] == "on":
            val = 0
            self.R2buttonAC["text"] = "off"
            self.R2buttonAC["image"] = self.iconoff
            sv.update_room_actuator("db_livingroom", "ac", 0)
            sv.print_table_content("db_livingroom")
        else:
            val = 1
            self.R2buttonAC["text"] = "on"
            self.R2buttonAC["image"] = self.iconon
            sv.update_room_actuator("db_livingroom", "ac", 1)
            sv.print_table_content("db_livingroom")

    def on_click_speaker_R2(self):
        if self.R2buttonspeaker["text"] == "on":
            val = 0
            self.R2buttonspeaker["text"] = "off"
            self.R2buttonspeaker["image"] = self.iconoff
            sv.update_room_actuator("db_livingroom", "musik", 0)
            sv.print_table_content("db_livingroom")
        else:
            val = 1
            self.R2buttonspeaker["text"] = "on"
            self.R2buttonspeaker["image"] = self.iconon
            sv.update_room_actuator("db_livingroom", "musik", 1)
            sv.print_table_content("db_livingroom")

    def on_click_light_R3(self):
        if self.R3buttonLight["text"] == "on":
            val = 0
            self.R3buttonLight["text"] = "off"
            self.R3buttonLight["image"] = self.iconoff
            sv.update_room_actuator("db_bathroom", "lampu", 0)
            sv.print_table_content("db_bathroom")
        else:
            val = 1
            self.R3buttonLight["text"] = "on"
            self.R3buttonLight["image"] = self.iconon
            sv.update_room_actuator("db_bathroom", "lampu", 1)
            sv.print_table_content("db_bathroom")

    def on_click_speaker_R3(self):
        if self.R3buttonspeaker["text"] == "on":
            val = 0
            self.R3buttonspeaker["text"] = "off"
            self.R3buttonspeaker["image"] = self.iconoff
            sv.update_room_actuator("db_bathroom", "musik", 0)
            sv.print_table_content("db_bathroom")

        else:
            val = 1
            self.R3buttonspeaker["text"] = "on"
            self.R3buttonspeaker["image"] = self.iconon
            sv.update_room_actuator("db_bathroom", "musik", 1)
            sv.print_table_content("db_bathroom")

    def on_click_light_R4(self):
        if self.R4buttonLight["text"] == "on":
            val = 0
            self.R4buttonLight["image"] = self.iconoff
            self.R4buttonLight["text"] = "off"
            # print("off")
            sv.update_room_actuator("db_bedroom", "lampu", 0)
            sv.print_table_content("db_bedroom")

        else:
            val = 1
            self.R4buttonLight["image"] = self.iconon
            self.R4buttonLight["text"] = "on"
            # print("on")
            sv.update_room_actuator("db_bedroom", "lampu", 1)
            sv.print_table_content("db_bedroom")

    def on_click_AC_R4(self):
        if self.R4buttonAC["text"] == "on":
            val = 0
            self.R4buttonAC["text"] = "off"
            self.R4buttonAC["image"] = self.iconoff
            sv.update_room_actuator("db_bedroom", "ac", 0)
            sv.print_table_content("db_bedroom")
        else:
            val = 1
            self.R4buttonAC["text"] = "on"
            self.R4buttonAC["image"] = self.iconon
            sv.update_room_actuator("db_bedroom", "ac", 1)
            sv.print_table_content("db_bedroom")

    def on_click_speaker_R4(self):
        if self.R4buttonspeaker["text"] == "on":
            val = 0
            self.R4buttonspeaker["text"] = "off"
            self.R4buttonspeaker["image"] = self.iconoff
            sv.update_room_actuator("db_bedroom", "musik", 0)
            sv.print_table_content("db_bedroom")
        else:
            val = 1
            self.R4buttonspeaker["text"] = "on"
            self.R4buttonspeaker["image"] = self.iconon
            sv.update_room_actuator("db_bedroom", "musik", 1)
            sv.print_table_content("db_bedroom")

    def send_info(self):
        data = (
            self.ementr.get(),
            self.passentr.get()
        )
        who = self.button1.get()
        if data[0] == "" or data[1] == "":
            messagebox.showinfo("System Error", "Please enter new email/password")
        else:
            sv.update_email(who, data[0])
            sv.update_password(who, data[1])
            # sv.print_table_content("user")
            messagebox.showinfo("Change Success", "Please relog")
            print("{} login info has been changed.\nNew Email = {}\nNew Pass = {}".format(who, data[0], data[1]))
            self.window5.destroy()

    def Bathroom(self, config):
        lastest_value, items, lampu_value, musik_value = sv.bathroom_services(config)
        if items == lastest_value:
            pass
        else:
            # cursor.execute("UPDATE db_bathroom SET lampu=? WHERE rowid =1", (lampu_value,))
            # cursor.execute("UPDATE db_bathroom SET musik=? WHERE rowid =1", (musik_value,))
            if lampu_value and musik_value == 1:
                self.R3buttonLight["image"] = self.iconon
                self.R3buttonspeaker["image"] = self.iconon
                print("Lampu dan Musik pada ruangan bathroom menyala")
            elif (lampu_value == 1 and musik_value == 0):
                self.R3buttonLight["image"] = self.iconon
                self.R3buttonspeaker["image"] = self.iconoff
                print("Di ruangan bathroom lampu menyala dan musik mati")
            elif (lampu_value == 0 and musik_value == 1):
                self.R3buttonLight["image"] = self.iconoff
                self.R3buttonspeaker["image"] = self.iconon
                print("Di ruangan bathroom lampu mati dan musik menyala")
            else:
                self.R3buttonLight["image"] = self.iconoff
                self.R3buttonspeaker["image"] = self.iconoff
                print("Lampu dan musik pada bathroom mati")
            print("")

    def Bedroom(self, config):
        lastest_value, items, lampu_value, musik_value, ac_value = sv.bedroom_services(config)
        if items == lastest_value:
            pass
        else:
            if lampu_value == 1  and musik_value == 1 and ac_value == 1:
                self.R4buttonLight["image"] = self.iconon
                self.R4buttonspeaker["image"] = self.iconon
                self.R4buttonAC["image"] = self.iconon
                print("Lampu, musik dan AC pada ruangan bedroom menyala")
            elif (lampu_value == 1 and musik_value == 0 and ac_value == 1):
                self.R4buttonLight["image"] = self.iconon
                self.R4buttonspeaker["image"] = self.iconoff
                self.R4buttonAC["image"] = self.iconon
                print("Di ruangan bedroom lampu dan AC menyala,  musik mati")
            elif (lampu_value == 0 and musik_value == 1 and ac_value == 1):
                self.R4buttonLight["image"] = self.iconoff
                self.R4buttonspeaker["image"] = self.iconon
                self.R4buttonAC["image"] = self.iconon
                print("Di ruangan bedroom lampu mati, musik dan AC menyala")
            elif (lampu_value == 1 and musik_value == 1 and ac_value == 0):
                self.R4buttonLight["image"] = self.iconon
                self.R4buttonspeaker["image"] = self.iconon
                self.R4buttonAC["image"] = self.iconoff
                print("Di ruangan bedroom AC mati, musik dan lampu menyala")
            elif (lampu_value == 1 and musik_value == 0 and ac_value == 0):
                self.R4buttonLight["image"] = self.iconon
                self.R4buttonspeaker["image"] = self.iconoff
                self.R4buttonAC["image"] = self.iconoff
                print("Di ruanganbedroom lampu menyala, musik dan AC mati")
            elif (lampu_value == 0 and musik_value == 0 and ac_value == 1):
                self.R4buttonLight["image"] = self.iconoff
                self.R4buttonspeaker["image"] = self.iconoff
                self.R4buttonAC["image"] = self.iconon
                print("Di ruangan bedroom AC menyala, musik dan lampu ,mati")
            elif (lampu_value == 0 and musik_value == 1 and ac_value == 0):
                self.R4buttonLight["image"] = self.iconoff
                self.R4buttonspeaker["image"] = self.iconon
                self.R4buttonAC["image"] = self.iconoff
                print("Di ruangan bedroom musik hidup, lampu dan AC mati")
            else:
                self.R4buttonLight["image"] = self.iconoff
                self.R4buttonspeaker["image"] = self.iconoff
                self.R4buttonAC["image"] = self.iconoff
                print("Lampu, AC dan  bedroom bedroom mati")
            print("")

    def Kitchen(self, config):
        lastest_value, items, lampu_value, musik_value, ac_value = sv.kitchen_services(config)
        if items == lastest_value:
            pass
        else:
            if lampu_value and musik_value == 1 and ac_value == 1:
                self.R1buttonLight["image"] = self.iconon
                self.R1buttonspeaker["image"] = self.iconon
                self.R1buttonAC["image"] = self.iconon
                print("Lampu, musik dan AC pada ruangan kitchen menyala")
            elif (lampu_value == 1 and musik_value == 0 and ac_value == 1):
                self.R1buttonLight["image"] = self.iconon
                self.R1buttonspeaker["image"] = self.iconoff
                self.R1buttonAC["image"] = self.iconon
                print("Di ruangan kitchen lampu dan AC menyala,  musik mati")
            elif (lampu_value == 0 and musik_value == 1 and ac_value == 1):
                self.R1buttonLight["image"] = self.iconoff
                self.R1buttonspeaker["image"] = self.iconon
                self.R1buttonAC["image"] = self.iconon
                print("Di ruangan kitchen lampu mati, musik dan AC menyala")
            elif (lampu_value == 1 and musik_value == 1 and ac_value == 0):
                self.R1buttonLight["image"] = self.iconon
                self.R1buttonspeaker["image"] = self.iconon
                self.R1buttonAC["image"] = self.iconoff
                print("Di ruangan kitchen AC mati, musik dan lampu menyala")
            elif (lampu_value == 1 and musik_value == 0 and ac_value == 0):
                self.R1buttonLight["image"] = self.iconon
                self.R1buttonspeaker["image"] = self.iconoff
                self.R1buttonAC["image"] = self.iconoff
                print("Di ruangan kitchen lampu menyala, musik dan AC mati")
            elif (lampu_value == 0 and musik_value == 0 and ac_value == 1):
                self.R1buttonLight["image"] = self.iconoff
                self.R1buttonspeaker["image"] = self.iconoff
                self.R1buttonAC["image"] = self.iconon
                print("Di ruangan kitchen AC menyala, musik dan lampu ,mati")
            elif (lampu_value == 0 and musik_value == 1 and ac_value == 0):
                self.R1buttonLight["image"] = self.iconoff
                self.R1buttonspeaker["image"] = self.iconon
                self.R1buttonAC["image"] = self.iconoff
                print("Di ruangan kitchen musik nyala, lampu dan AC mati")
            else:
                self.R1buttonLight["image"] = self.iconoff
                self.R1buttonspeaker["image"] = self.iconoff
                self.R1buttonAC["image"] = self.iconoff
                print("Lampu, AC dan  musik pada kitchen mati")
            print("")

    def Living_room(self, config):
        lastest_value, items, lampu_value, musik_value, ac_value = sv.livingroom_services(config)
        if items == lastest_value:
            pass
        else:
            if lampu_value and musik_value == 1 and ac_value == 1:
                self.R2buttonLight["image"] = self.iconon
                self.R2buttonspeaker["image"] = self.iconon
                self.R2buttonAC["image"] = self.iconon
                print("Lampu, musik dan AC pada ruangan livingroom menyala")
            elif (lampu_value == 1 and musik_value == 0 and ac_value == 1):
                self.R2buttonLight["image"] = self.iconon
                self.R2buttonspeaker["image"] = self.iconoff
                self.R2buttonAC["image"] = self.iconon
                print("Di ruangan livingroom lampu dan AC menyala,  musik mati")
            elif (lampu_value == 0 and musik_value == 1 and ac_value == 1):
                self.R2buttonLight["image"] = self.iconoff
                self.R2buttonspeaker["image"] = self.iconon
                self.R2buttonAC["image"] = self.iconon
                print("Di ruangan livingroom lampu mati, musik dan AC menyala")
            elif (lampu_value == 1 and musik_value == 1 and ac_value == 0):
                self.R2buttonLight["image"] = self.iconon
                self.R2buttonspeaker["image"] = self.iconon
                self.R2buttonAC["image"] = self.iconoff
                print("Di ruangan livingroom AC mati, musik dan lampu menyala")
            elif (lampu_value == 1 and musik_value == 0 and ac_value == 0):
                self.R2buttonLight["image"] = self.iconon
                self.R2buttonspeaker["image"] = self.iconoff
                self.R2buttonAC["image"] = self.iconoff
                print("Di ruangan livingroom lampu menyala, musik dan AC mati")
            elif (lampu_value == 0 and musik_value == 0 and ac_value == 1):
                self.R2buttonLight["image"] = self.iconoff
                self.R2buttonspeaker["image"] = self.iconoff
                self.R2buttonAC["image"] = self.iconon
                print("Di ruangan livingroom AC menyala, musik dan lampu ,mati")
            elif (lampu_value == 0 and musik_value == 1 and ac_value == 0):
                self.R2buttonLight["image"] = self.iconoff
                self.R2buttonspeaker["image"] = self.iconon
                self.R2buttonAC["image"] = self.iconoff
                print("Di ruangan livingroom musik mati, lampu dan AC menyala")
            else:
                self.R2buttonLight["image"] = self.iconoff
                self.R2buttonspeaker["image"] = self.iconoff
                self.R2buttonAC["image"] = self.iconoff
                print("Lampu, AC dan  musik pada livingroom mati")
            print("")

    def SmartSettingParent(self):
        self.window3 = Toplevel()
        self.window3.wm_iconbitmap("CIT Logo square compact.ico")
        self.window3.title("Smart Home Settings")
        self.window3.geometry("500x700")

        # mainmenu = Menu(self.window3)
        # filemenu = Menu(mainmenu, tearoff=0)
        # filemenu.add_command(label="Open")
        # filemenu.add_command(label="Save")
        # filemenu.add_separator()
        # filemenu.add_command(label="Exit", command=self.window3.destroy)
        # mainmenu.add_cascade(label="File", menu=filemenu)

        self.text = Label(self.window3, text="Mode", font="Verdana 15")
        self.text.grid(row=0, column=0)

        kalimat = "User: {}".format(self.user)
        self.curuser = Label(self.window3, text=kalimat, font="Verdana 15")
        self.curuser.grid(row=0, column=3)

        Var1 = IntVar()

        self.RBttn = Radiobutton(self.window3, text="Manual", variable=Var1, value=1,  command= lambda: self.manual())
        self.RBttn.grid(row=1, column=0)
        Var1.set(1)
        self.auto = False

        self.RBttn2 = Radiobutton(self.window3, text="Automatic", variable=Var1, value=2, command= lambda: self.automatic())
        self.RBttn2.grid(row=1, column=1)

        self.kitchen = Label(self.window3, text="Kitchen", font="Verdana 15 underline")
        self.kitchen.grid(row=2, column=0)

        self.kitchenlight = Label(self.window3, text="Light")
        self.kitchenlight.grid(row=3, column=0)

        self.kitchenAC = Label(self.window3, text="Air Conditioner")
        self.kitchenAC.grid(row=4, column=0)

        self.kitchenspeaker = Label(self.window3, text="Speaker")
        self.kitchenspeaker.grid(row = 3, column = 2)

        PhotoImage(master= self.window3)
        self.iconon = ImageTk.PhotoImage(Image.open("onbutton.png").resize((80,40)))
        self.iconoff = ImageTk.PhotoImage(Image.open("offbutton.png").resize((80,40)))

        self.R1buttonLight = Button(self.window3, text="on", state = "normal", image=self.iconon, bd=0, command= lambda: self.on_click_light_R1())
        self.R1buttonLight.grid(row=3, column=1)

        self.R1buttonAC = Button(self.window3, text="on", state = "normal", image=self.iconon,bd=0, command= lambda: self.on_click_AC_R1())
        self.R1buttonAC.grid(row=4, column=1)

        self.R1buttonspeaker = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0,command=lambda: self.on_click_speaker_R1())
        self.R1buttonspeaker.grid(row=3, column=3)

        self.Livingroom = Label(self.window3, text="Livingroom", font="Verdana 15 underline")
        self.Livingroom.grid(row=5, column=0)

        self.LRlight = Label(self.window3, text="Light")
        self.LRlight.grid(row=6, column=0)

        self.LRAC = Label(self.window3, text="Air Conditioner")
        self.LRAC.grid(row=7, column=0)

        self.LRspeaker = Label(self.window3, text="Speaker")
        self.LRspeaker.grid(row=6, column=2)

        self.R2buttonLight = Button(self.window3, text="on", state = "normal", image=self.iconon,bd=0, command= lambda: self.on_click_light_R2())
        self.R2buttonLight.grid(row=6, column=1)

        self.R2buttonAC = Button(self.window3, text="on", state = "normal", image=self.iconon, bd=0, command= lambda: self.on_click_AC_R2())
        self.R2buttonAC.grid(row=7, column=1)

        self.R2buttonspeaker = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0,command=lambda: self.on_click_speaker_R2())
        self.R2buttonspeaker.grid(row=6, column=3)

        self.bathroom = Label(self.window3, text="Bathroom", font="Verdana 15 underline")
        self.bathroom.grid(row = 11, column = 0)

        self.bathlight = Label(self.window3, text="Light")
        self.bathlight.grid(row = 12, column = 0)

        self.bathspeaker = Label(self.window3, text="Speaker")
        self.bathspeaker.grid(row = 12, column = 2)

        self.R3buttonLight = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command =lambda: self.on_click_light_R3())
        self.R3buttonLight.grid(row = 12, column = 1)

        self.R3buttonspeaker = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_speaker_R3())
        self.R3buttonspeaker.grid(row = 12, column = 3)

        self.bedroom = Label(self.window3, text="Bedroom", font="Verdana 15 underline")
        self.bedroom.grid(row=8, column=0)

        self.bedlight = Label(self.window3, text="Light")
        self.bedlight.grid(row=9, column=0)

        self.bedAC = Label(self.window3, text="Air Conditioner")
        self.bedAC.grid(row=10, column=0)

        self.bedspeaker = Label(self.window3, text="Speaker")
        self.bedspeaker.grid(row=9, column=2)

        self.R4buttonLight = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_light_R4())
        self.R4buttonLight.grid(row=9, column=1)

        self.R4buttonAC = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_AC_R4())
        self.R4buttonAC.grid(row=10, column=1)

        self.R4buttonspeaker = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_speaker_R4())
        self.R4buttonspeaker.grid(row=9, column=3)

        self.guestbttn = Button(self.window3, text="Guest Mode", command=lambda: self.SmartSettingGuest())
        self.guestbttn.grid(row = 15, column=0)

        self.window3.mainloop()

    def SmartSettingGuest(self):
        self.window4 = Toplevel()
        self.window4.wm_iconbitmap("CIT Logo square compact.ico")
        self.window4.title("Smart Home Settings")
        self.window4.geometry("500x700")
        cur = self.window4
        # mainmenu = Menu(self.window3)
        # filemenu = Menu(mainmenu, tearoff=0)
        # filemenu.add_command(label="Open")
        # filemenu.add_command(label="Save")
        # filemenu.add_separator()
        # filemenu.add_command(label="Exit", command=self.window3.destroy)
        # mainmenu.add_cascade(label="File", menu=filemenu)

        self.text = Label(cur, text="Mode", font="Verdana 15")
        self.text.grid(row=0, column=0)

        self.user = "Guest"
        kalimat = "User: {}".format(self.user)
        self.curuser = Label(cur, text=kalimat, font="Verdana 15")
        self.curuser.grid(row=0, column=3)

        Var1 = IntVar()

        self.RBttn = Radiobutton(cur, text="Manual", variable=Var1, value=1, command= lambda: self.manual())
        self.RBttn.grid(row=1, column=0)
        Var1.set(1)
        self.auto = False

        self.RBttn2 = Radiobutton(cur, text="Automatic", variable=Var1, value=2, command= lambda: self.automatic())
        self.RBttn2.grid(row=1, column=1)

        self.kitchen = Label(cur, text="Kitchen", font="Verdana 15 underline")
        self.kitchen.grid(row=2, column=0)

        self.kitchenlight = Label(cur, text="Light")
        self.kitchenlight.grid(row=3, column=0)

        self.kitchenAC = Label(cur, text="Air Conditioner")
        self.kitchenAC.grid(row=4, column=0)

        self.kitchenspeaker = Label(cur, text="Speaker")
        self.kitchenspeaker.grid(row = 3, column = 2)

        PhotoImage(master= cur)
        self.iconon = ImageTk.PhotoImage(Image.open("onbutton.png").resize((80,40)))
        self.iconoff = ImageTk.PhotoImage(Image.open("offbutton.png").resize((80,40)))

        self.R1buttonLight = Button(cur, text="on", state = "normal", image=self.iconon, bd=0, command= lambda: self.on_click_light_R1())
        self.R1buttonLight.grid(row=3, column=1)

        self.R1buttonAC = Button(cur, text="on", state = "normal", image=self.iconon,bd=0, command= lambda: self.on_click_AC_R1())
        self.R1buttonAC.grid(row=4, column=1)

        self.R1buttonspeaker = Button(cur, text="on", state="normal", image=self.iconon, bd=0,command=lambda: self.on_click_speaker_R1())
        self.R1buttonspeaker.grid(row=3, column=3)

        self.Livingroom = Label(cur, text="Livingroom", font="Verdana 15 underline")
        self.Livingroom.grid(row=5, column=0)

        self.LRlight = Label(cur, text="Light")
        self.LRlight.grid(row=6, column=0)

        self.LRAC = Label(cur, text="Air Conditioner")
        self.LRAC.grid(row=7, column=0)

        self.LRspeaker = Label(cur, text="Speaker")
        self.LRspeaker.grid(row=6, column=2)

        self.R2buttonLight = Button(cur, text="on", state = "normal", image=self.iconon,bd=0, command= lambda: self.on_click_light_R2())
        self.R2buttonLight.grid(row=6, column=1)

        self.R2buttonAC = Button(cur, text="on", state = "normal", image=self.iconon, bd=0, command= lambda: self.on_click_AC_R2())
        self.R2buttonAC.grid(row=7, column=1)

        self.R2buttonspeaker = Button(cur, text="on", state="normal", image=self.iconon, bd=0,command=lambda: self.on_click_speaker_R2())
        self.R2buttonspeaker.grid(row=6, column=3)

        self.bathroom = Label(cur, text="Bathroom", font="Verdana 15 underline")
        self.bathroom.grid(row = 11, column = 0)

        self.bathlight = Label(cur, text="Light")
        self.bathlight.grid(row = 12, column = 0)

        self.bathspeaker = Label(cur, text="Speaker")
        self.bathspeaker.grid(row = 12, column = 2)

        self.R3buttonLight = Button(cur, text="on", state="normal", image=self.iconon, bd=0, command =lambda: self.on_click_light_R3())
        self.R3buttonLight.grid(row = 12, column = 1)

        self.R3buttonspeaker = Button(cur, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_speaker_R3())
        self.R3buttonspeaker.grid(row = 12, column = 3)

        self.bedroom = Label(cur, text="Bedroom", font="Verdana 15 underline")
        self.bedroom.grid(row=8, column=0)

        self.bedlight = Label(cur, text="Light")
        self.bedlight.grid(row=9, column=0)

        self.bedAC = Label(cur, text="Air Conditioner")
        self.bedAC.grid(row=10, column=0)

        self.bedspeaker = Label(cur, text="Speaker")
        self.bedspeaker.grid(row=9, column=2)

        self.R4buttonLight = Button(cur, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_light_R4())
        self.R4buttonLight.grid(row=9, column=1)

        self.R4buttonAC = Button(cur, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_AC_R4())
        self.R4buttonAC.grid(row=10, column=1)

        self.R4buttonspeaker = Button(cur, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_speaker_R4())
        self.R4buttonspeaker.grid(row=9, column=3)

        self.window3.destroy()
        cur.mainloop()

    def SmartSettingChild(self):
        self.window3 = Toplevel()
        self.window3.wm_iconbitmap("CIT Logo square compact.ico")
        self.window3.title("Smart Home Settings")
        self.window3.geometry("500x700")

        # mainmenu = Menu(self.window3)
        # filemenu = Menu(mainmenu, tearoff=0)
        # filemenu.add_command(label="Open")
        # filemenu.add_command(label="Save")
        # filemenu.add_separator()
        # filemenu.add_command(label="Exit", command=self.window3.destroy)
        # mainmenu.add_cascade(label="File", menu=filemenu)

        self.text = Label(self.window3, text="Mode", font="Verdana 15")
        self.text.grid(row=0, column=0)

        kalimat = "User: {}".format(self.user)
        self.curuser = Label(self.window3, text=kalimat, font="Verdana 15")
        self.curuser.grid(row=0, column=3)

        Var1 = IntVar()

        self.RBttn = Radiobutton(self.window3, text="Manual", variable=Var1, state="disabled", value=1,  command= lambda: self.manual())
        self.RBttn.grid(row=1, column=0)

        self.RBttn2 = Radiobutton(self.window3, text="Automatic", variable=Var1, value=2, command= lambda: self.automatic())
        self.RBttn2.grid(row=1, column=1)

        Var1.set(2)

        self.kitchen = Label(self.window3, text="Kitchen", font="Verdana 15 underline")
        self.kitchen.grid(row=2, column=0)

        self.kitchenlight = Label(self.window3, text="Light")
        self.kitchenlight.grid(row=3, column=0)

        self.kitchenAC = Label(self.window3, text="Air Conditioner")
        self.kitchenAC.grid(row=4, column=0)

        self.kitchenspeaker = Label(self.window3, text="Speaker")
        self.kitchenspeaker.grid(row = 3, column = 2)

        PhotoImage(master= self.window3)
        self.iconon = ImageTk.PhotoImage(Image.open("onbutton.png").resize((80,40)))
        self.iconoff = ImageTk.PhotoImage(Image.open("offbutton.png").resize((80,40)))

        self.R1buttonLight = Button(self.window3, text="on", state = "normal", image=self.iconon, bd=0, command= lambda: self.on_click_light_R1())
        self.R1buttonLight.grid(row=3, column=1)

        self.R1buttonAC = Button(self.window3, text="on", state = "normal", image=self.iconon,bd=0, command= lambda: self.on_click_AC_R1())
        self.R1buttonAC.grid(row=4, column=1)

        self.R1buttonspeaker = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0,command=lambda: self.on_click_speaker_R1())
        self.R1buttonspeaker.grid(row=3, column=3)

        self.Livingroom = Label(self.window3, text="Livingroom", font="Verdana 15 underline")
        self.Livingroom.grid(row=5, column=0)

        self.LRlight = Label(self.window3, text="Light")
        self.LRlight.grid(row=6, column=0)

        self.LRAC = Label(self.window3, text="Air Conditioner")
        self.LRAC.grid(row=7, column=0)

        self.LRspeaker = Label(self.window3, text="Speaker")
        self.LRspeaker.grid(row=6, column=2)

        self.R2buttonLight = Button(self.window3, text="on", state = "normal", image=self.iconon,bd=0, command= lambda: self.on_click_light_R2())
        self.R2buttonLight.grid(row=6, column=1)

        self.R2buttonAC = Button(self.window3, text="on", state = "normal", image=self.iconon, bd=0, command= lambda: self.on_click_AC_R2())
        self.R2buttonAC.grid(row=7, column=1)

        self.R2buttonspeaker = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0,command=lambda: self.on_click_speaker_R2())
        self.R2buttonspeaker.grid(row=6, column=3)

        self.bathroom = Label(self.window3, text="Bathroom", font="Verdana 15 underline")
        self.bathroom.grid(row = 11, column = 0)

        self.bathlight = Label(self.window3, text="Light")
        self.bathlight.grid(row = 12, column = 0)

        self.bathspeaker = Label(self.window3, text="Speaker")
        self.bathspeaker.grid(row = 12, column = 2)

        self.R3buttonLight = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command =lambda: self.on_click_light_R3())
        self.R3buttonLight.grid(row = 12, column = 1)

        self.R3buttonspeaker = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_speaker_R3())
        self.R3buttonspeaker.grid(row = 12, column = 3)

        self.bedroom = Label(self.window3, text="Bedroom", font="Verdana 15 underline")
        self.bedroom.grid(row=8, column=0)

        self.bedlight = Label(self.window3, text="Light")
        self.bedlight.grid(row=9, column=0)

        self.bedAC = Label(self.window3, text="Air Conditioner")
        self.bedAC.grid(row=10, column=0)

        self.bedspeaker = Label(self.window3, text="Speaker")
        self.bedspeaker.grid(row=9, column=2)

        self.R4buttonLight = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_light_R4())
        self.R4buttonLight.grid(row=9, column=1)

        self.R4buttonAC = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_AC_R4())
        self.R4buttonAC.grid(row=10, column=1)

        self.R4buttonspeaker = Button(self.window3, text="on", state="normal", image=self.iconon, bd=0, command=lambda: self.on_click_speaker_R4())
        self.R4buttonspeaker.grid(row=9, column=3)

        self.automatic()

        self.window3.mainloop()

    def ControlPanelAdmin(self):
        self.window5 = Toplevel()
        self.window5.wm_iconbitmap("CIT Logo square compact.ico")
        self.window5.title("Admin Control Panel")
        # self.window5.geometry("500x700")

        kalimat = "User: {}".format(self.user)
        self.curuser = Label(self.window5, text=kalimat, font="Verdana 15")
        self.curuser.grid(row=0, column=2)

        self.button1 = StringVar()
        # button2 = StringVar()
        # button3 = StringVar()
        # button4 = StringVar()

        self.radiobutton1 = Radiobutton(self.window5, text="Parent", value="PARENT", variable=self.button1)
        self.radiobutton1.grid(row=1,column=0)
        self.radiobutton2 = Radiobutton(self.window5, text="Child", value="CHILD", variable=self.button1)
        self.radiobutton2.grid(row=1,column=1)
        self.radiobutton3 = Radiobutton(self.window5, text="Admin", value="ADMIN", variable=self.button1)
        self.radiobutton3.grid(row=1,column=2)

        self.button1.set('Parent')

        self.emlab = Label(self.window5, text="New Email")
        self.emlab.grid(row=2, column=0)
        self.passlab = Label(self.window5, text="New Password")
        self.passlab.grid(row=3, column=0)

        self.ementr = Entry(self.window5, font='Courier 12')
        self.ementr.grid(row=2, column=1)
        self.passentr = Entry(self.window5, font='Courier 12')
        self.passentr.grid(row=3, column=1)

        self.updatebutton = Button(self.window5, text="Update Login Info", command= lambda: self.send_info())
        self.updatebutton.grid(row=4, column=1)

