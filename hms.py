from tkinter import *
import sqlite3
import tkinter.messagebox
import pyttsx3

conn = sqlite3.connect('database.db')
c = conn.cursor()

print("1.To get the appointment")
print("2.To update the patient details")
print("3.To display the appointments")
op = int(input("\nplease choose the option:"))

if(op==1):
    ids = []
    class Application:
        def __init__(self, master):
            self.master = master

            self.left = Frame(master, width=890, height=720, bg='white')
            self.left.pack(side=LEFT)

            self.right = Frame(master, width=390, height=720,bg='steelblue')
            self.right.pack(side=RIGHT)

            self.heading = Label(self.left, text="AQUIB HOSPITAL APPOINTMENTS", font=('arial 40 bold'), fg="black")
            self.heading.place(x=0,y=0)

            self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='white')
            self.name.place(x=0, y=100)

            self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='white')
            self.age.place(x=0, y=140)

            self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='white')
            self.gender.place(x=0, y=180)

            self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='white')
            self.location.place(x=0, y=220)

            self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='white')
            self.time.place(x=0, y=260)

            self.phone = Label(self.left, text="Phone number", font=('arial 18 bold'), fg='black', bg='white')
            self.phone.place(x=0, y=300)

            self.spec = Label(self.left, text="Doc_Specification", font=('arial 18 bold'), fg='black', bg='white')
            self.spec.place(x=0,y=340)



            self.name_ent = Entry(self.left, width=30, bg='grey')
            self.name_ent.place(x=250, y=110)

            self.age_ent = Entry(self.left, width=30, bg='grey')
            self.age_ent.place(x=250, y=150)

            self.gender_ent = Entry(self.left, width=30, bg='grey')
            self.gender_ent.place(x=250, y=190)

            self.location_ent = Entry(self.left, width=30, bg='grey')
            self.location_ent.place(x=250, y=230)

            self.time_ent = Entry(self.left, width=30, bg='grey')
            self.time_ent.place(x=250, y=270)

            self.phone_ent = Entry(self.left, width=30, bg='grey')
            self.phone_ent.place(x=250, y=310)

            var = StringVar()
            
            self.spec_ent = OptionMenu(master, var, "Dr. subhash","Dr. A K Sahu","Dr. Neelam jha","Dr. N K Mishra","Dr. P K Das","Dr. prashant kumar")
            self.spec_ent.place(x=250, y=340)
            self.spec_ent.configure(font=('arial 10 bold'), width=20)
          
            #self.spec_ent1=var.get()
            #buttons to perform a command
            self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
            self.submit.place(x=270, y=390)

            sql2 = "SELECT ID FROM appointments "
            self.result = c.execute(sql2)
            for self.row in self.result:
               self.id = self.row[0]
               ids.append(self.id)
            
            #ordering the ids
            self.new = sorted(ids)
            self.final_id = self.new[len(ids)-1]

            #displaying the logs in our right frame
            self.logs = Label(self.right, text = "Logs", font = ('arial 18 bold'), fg='white', bg='steelblue')
            self.logs.place(x=20, y=0)
            self.box = Text(self.right, width=39, height=40)
            self.box.place(x=20, y=30)
            self.box.insert(END, "Total appointment till now " + str(self.final_id))


        def add_appointment(self):
                #for getting user input
                self.val1 = self.name_ent.get()
                self.val2 = self.age_ent.get()
                self.val3 = self.gender_ent.get()
                self.val4 = self.location_ent.get()
                self.val5 = self.time_ent.get()
                self.val6 = self.phone_ent.get()
                #self.val7 = self.spec_ent1.get()
                                
                
                #checking if the user input is empty
                if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '':
                    tkinter.messagebox.showinfo("warning", "please fill up all the details")
                else:
                    
                    sql = "INSERT INTO 'appointments' (name,age,gender,location,scheduled_time,phone) VALUES(?,?,?,?,?,?)"
                    c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
                    conn.commit()
                    
                    tkinter.messagebox.showinfo("success", "Appointment for " +str(self.val1) + " has been successfully created")
           
                    self.box.insert(END, "\nAppointment fixed for " + str(self.val1) + " at " + str(self.val5))
elif(op == 2):
    class Application:
        def __init__(self, master):
            self.master = master
            # heading label
            self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
            self.heading.place(x=150, y=0)

            # search criteria -->name 
            self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
            self.name.place(x=0, y=60)

            # entry for  the name
            self.namenet = Entry(master, width=30)
            self.namenet.place(x=280, y=62)

            # search button
            self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
            self.search.place(x=350, y=102)
    # function to search
        def search_db(self):
            self.input = self.namenet.get()
            # execute sql 

            sql = "SELECT * FROM appointments WHERE name LIKE ?"
            self.res = c.execute(sql, (self.input,))
            for self.row in self.res:
                self.name1 = self.row[1]
                self.age = self.row[2]
                self.gender = self.row[3]
                self.location = self.row[4]
                self.time = self.row[5]
                self.phone = self.row[6]
             # creating the update form
            self.uname = Label(self.master, text="Patient's Name", font=('arial 18 bold'))
            self.uname.place(x=0, y=140)

            self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
            self.uage.place(x=0, y=180)

            self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
            self.ugender.place(x=0, y=220)

            self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
            self.ulocation.place(x=0, y=260)

            self.utime = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
            self.utime.place(x=0, y=300)

            self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
            self.uphone.place(x=0, y=340)

            # entries for each labels==========================================================
            # ===================filling the search result in the entry box to update
            self.ent1 = Entry(self.master, width=30)
            self.ent1.place(x=300, y=140)
            self.ent1.insert(END, str(self.name1))

            self.ent2 = Entry(self.master, width=30)
            self.ent2.place(x=300, y=180)
            self.ent2.insert(END, str(self.age))

            self.ent3 = Entry(self.master, width=30)
            self.ent3.place(x=300, y=220)
            self.ent3.insert(END, str(self.gender))

            self.ent4 = Entry(self.master, width=30)
            self.ent4.place(x=300, y=260)
            self.ent4.insert(END, str(self.location))

            self.ent5 = Entry(self.master, width=30)
            self.ent5.place(x=300, y=300)
            self.ent5.insert(END, str(self.time))

            self.ent6 = Entry(self.master, width=30)
            self.ent6.place(x=300, y=340)
            self.ent6.insert(END, str(self.phone))

            # button to execute update
            self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
            self.update.place(x=400, y=380)

            # button to delete
            self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
            self.delete.place(x=150, y=380)
        def update_db(self):
            # declaring the variables to update
            self.var1 = self.ent1.get() #updated name
            self.var2 = self.ent2.get() #updated age
            self.var3 = self.ent3.get() #updated gender
            self.var4 = self.ent4.get() #updated location
            self.var5 = self.ent5.get() #updated phone
            self.var6 = self.ent6.get() #updated time

            query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
            c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
            conn.commit()
            tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
        def delete_db(self):
            # delete the appointment
            sql2 = "DELETE FROM appointments WHERE name LIKE ?"
            c.execute(sql2, (self.namenet.get(),))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Deleted Successfully")
            self.ent1.destroy()
            self.ent2.destroy()
            self.ent3.destroy()
            self.ent4.destroy()
            self.ent5.destroy()
            self.ent6.destroy()
elif(op == 3):
    # connection to database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # empty lists to append later
    number = []
    patients = []

    sql = "SELECT * FROM appointments"
    res = c.execute(sql)
    for r in res:
        ids = r[0]
        name = r[1]
        number.append(ids)
        patients.append(name)

    # window
    class Application:
        def __init__(self, master):
            self.master = master

            self.x = 0
        
            # heading
            self.heading = Label(master, text="Appointments", font=('arial 60 bold'), fg='green')
            self.heading.place(x=350, y=0)

            # button to change patients
            self.change = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
            self.change.place(x=500, y=600)

            # empty text labels to later config
            self.n = Label(master, text="", font=('arial 200 bold'))
            self.n.place(x=500, y=100)

            self.pname = Label(master, text="", font=('arial 80 bold'))
            self.pname.place(x=300, y=400)
            # function to speak the text and update the text
        def func(self):
            self.n.config(text=str(number[self.x]))
            self.pname.config(text=str(patients[self.x]))
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-50)
            engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
            engine.runAndWait()
            self.x += 1
else:
    tkinter.messagebox.showinfo("failed","please choose an appropriate answer")
    


root=Tk()
b = Application(root)
root.geometry('1250x720+0+0')
root.resizable(True,True)
root.mainloop()