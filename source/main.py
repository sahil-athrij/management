import empl
import os.path as path
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import tkinter.messagebox as messagebox
from tkinter import ttk
import pickle

class management:

    def __init__(self,filename= False):
        self.employeelist = {}
        self.employeename = ["select"]



        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        self.spacingframe = tkinter.Frame(self.root,height = 10 ,relief = tkinter.FLAT)
        self.spacingframe.pack()



        #buttons


        self.buttonframe = ttk.Frame(self.root, height=50,relief=tkinter.FLAT)
        self.buttonframe.pack(pady = 2)
        self.createemp = ttk.Button(self.buttonframe,text = "add employee",command = self.addemployee)
        self.createemp.pack(pady = 2)



        #makeing drop down list
        self.spacingframe1 = ttk.Frame(self.root, height=10, relief=tkinter.FLAT)
        self.spacingframe1.pack(pady = 2)
        self.selectionframe = ttk.Frame(self.root, height=50, relief=tkinter.FLAT)
        self.selectionframe.pack(pady = 2)

        self.selectlable = ttk.Label(self.selectionframe, text="employee ")
        self.selectlable.pack(side=tkinter.LEFT)

        self.choice = tkinter.StringVar(self.root)
        self.choice.set("select")
        self.employees = tkinter.ttk.Combobox(self.selectionframe, textvariable=self.choice, state="readonly")
        self.employees["values"] = self.employeename
        self.employees.pack(pady = 2)

        if filename:
            self.load(filename)


        #more buttons
        self.buttonframe1 = ttk.Frame(self.root, relief=tkinter.FLAT)
        self.buttonframe1.pack(pady = 2)

        self.checkinbutton = ttk.Button(self.buttonframe1,text = "checkin" , command  = self.checkinfun)
        self.checkinbutton.pack(side = tkinter.LEFT,pady = 10, padx = 25)

        self.checkoutbutton = ttk.Button(self.buttonframe1, text="checkuout",command  = self.checkoutfun )
        self.checkoutbutton.pack(pady = 10, padx = 25)

        self.exitbutton = ttk.Button(self.root, text="exit" , command = self.exit)
        self.exitbutton.pack(pady = 10, padx = 25)
        self.root.protocol("WM_DELETE_WINDOW",self.exit)
        self.root.mainloop()



    def addemployee(self):
        self.addempwindow = tkinter.Toplevel(self.root)
        self.addempwindow.geometry("200x200")

        nameframe = ttk.Frame(self.addempwindow, height=50, relief=tkinter.FLAT)
        nameframe.pack(pady=4)

        namelable = ttk.Label(nameframe, text="name ")
        namelable.pack(side=tkinter.LEFT)

        self.nameentry = ttk.Entry(nameframe)
        self.nameentry.pack()

        ageframe = ttk.Frame(self.addempwindow, height=50, relief=tkinter.FLAT)
        ageframe.pack(pady=4)

        agelable = ttk.Label(ageframe, text="age  ")
        agelable.pack(side=tkinter.LEFT)

        self.ageentry = ttk.Entry(ageframe)
        self.ageentry.pack()

        roleframe = ttk.Frame(self.addempwindow, height=50, relief=tkinter.FLAT)
        roleframe.pack(pady=4)

        rolelable = ttk.Label(roleframe, text="role ")
        rolelable.pack(side=tkinter.LEFT)

        self.roleentry = ttk.Entry(roleframe)
        self.roleentry.pack()

        saveframe = ttk.Frame(self.addempwindow, height=50, relief=tkinter.FLAT)
        saveframe.pack(pady=4)

        savebutton = ttk.Button(saveframe, text="ok" , command = self.getnewentry)
        savebutton.pack(side=tkinter.LEFT)




    def exit(self):
        for i in self.employeelist:
            self.employeelist[i].checkout()
        if messagebox.showinfo("exit", "saving"):
            self.root.destroy()

    def checkinfun(self):
        if self.choice.get()!="select":
            self.employeelist[self.choice.get()].checkin()

    def checkoutfun(self):
        if self.choice.get()!="select":
            self.employeelist[self.choice.get()].checkout()

    def getnewentry(self):
        self.employeelist[self.nameentry.get()]=empl.Employee(self.nameentry.get(),self.ageentry.get(),self.roleentry.get())
        self.employeename.append((self.nameentry.get()))
        self.employees["values"] = self.employeename
        self.addempwindow.destroy()

    def save(self,filename):
        fn = open(filename, "wb")
        pickle.dump(self.employeelist,fn)
        pickle.dump(self.employeename,fn)

    def load(self,filename):
        fn = open(filename, "rb")
        self.employeelist = pickle.load(fn)
        self.employeename = pickle.load(fn)
        self.employees["values"] = self.employeename


filename = "everyone.bin"


if path.isfile(filename):
    a = management(filename)
else:
    a = management()



a.save(filename)
