from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, simpledialog, messagebox

class Driver:
    def __init__(self, name, cnic, pswd, ser_no):
        self.name = name
        self.cnic = cnic
        self.drv_pswd = pswd
        self.seats = 0
        self.ser_no = ser_no

class Student:
    def __init__(self, name, reg_no, pswd):
        self.name = name
        self.reg_no = reg_no
        self.std_pswd = pswd
        self.ser_no = ""
        self.status = False

class Time_slot:
    def __init__(self, time, ser_no):
        self.drv_name = " "
        self.time = time
        self.ser_no = ser_no

class TransportSystem:
    def __init__(self):
        self.drivers = {} 
        self.students = {}
        self.time_slots = {}
        self.num_students = 0
        self.ser_no = 1
        self.total_seats = 10

    def add_driver(self, name, cnic, pswd, ser_no):
        self.drivers[cnic] = Driver(name, cnic, pswd, ser_no)
    
    def add_student(self, name, reg_no, pswd):
        self.students[reg_no] = Student(name, reg_no, pswd)

    def add_time_slot(self, time):
        sno = str(self.ser_no)
        self.time_slots[sno] = Time_slot(time, sno)
        self.ser_no += 1 

    def admin_login(self, username, password):
        if username == "admin" and password == "123":
            return True
        return False
    
    def driver_login(self, cnic, password):
        if cnic in self.drivers and password == self.drivers[cnic].drv_pswd:
            return True
        return False

    def student_login(self, reg_no, password):
        if reg_no in self.students and password == self.students[reg_no].std_pswd:
            return True
        return False

    def booking_functions(self, reg_no):
        if reg_no in self.students and self.students[reg_no].status == False:
            details = f"\nAvailable Time Slots: {len(self.time_slots)}\n"
            for ser_no, slot in self.time_slots.items():
                details += f"{ser_no} : {slot.time}\n"
            # messagebox.showinfo("Available Times", details)     
            booking_for = simpledialog.askstring("Chose Timing", details)   
            if booking_for in tra_sys.time_slots:
                tra_sys.booking(booking_for, reg_no)
            else:
                messagebox.showerror("Error", "Invalid Selection!")
        else:
            messagebox.showerror("Error", "You Already Booked a Ride!")

    def check_driver(self, booking_for):
        for cnic in self.drivers:
            if booking_for == self.drivers[cnic].ser_no:
                return True
        return False

    def booking(self, booking_for, student_reg_no):
            if tra_sys.check_driver(booking_for):
                for cnic in self.drivers:
                    if booking_for == self.drivers[cnic].ser_no:
                        if self.drivers[cnic].seats < self.total_seats:
                            self.drivers[cnic].seats += 1
                            self.num_students += 1
                            self.students[student_reg_no].ser_no = booking_for
                            self.students[student_reg_no].status = True
                            messagebox.showinfo("Success", f"You Successfully booked for {self.time_slots[booking_for].time}!")
                        else:
                            messagebox.showerror("Error", "No seats available for this slot!")
            else:
                messagebox.showerror("Error", "No Driver available for this time slot!")

    def cancel_ride(self, reg_no):
        if reg_no in self.students and self.students[reg_no].status == True:
            for cnic, driver in self.drivers.items():
                if self.students[reg_no].ser_no == self.drivers[cnic].ser_no:
                    self.drivers[cnic].seats -= 1
                    self.num_students -= 1
                    self.students[reg_no].ser_no = None
                    self.students[reg_no].status = False
                    messagebox.showinfo("Success", f"You Successfully Cancelled for {self.time_slots[driver.ser_no].time}!")
        else:
            messagebox.showerror("Error", "You have not Booked a Ride!")

    def view_seats(self, cnic):
        result = "\nSeats Booked: "
        result += f"{self.drivers[cnic].seats} / {self.total_seats}\n" 
        for reg_no, student in self.students.items():
            if student.ser_no == self.drivers[cnic].ser_no:
                result += f"{student.name}\n"        
                
        messagebox.showinfo("Seat Details", result)
    
    def compl_details(self):
        details = f"\nEnrolled Drivers: {len(self.drivers)}\n"
        for cnic, driver in self.drivers.items():
            details += f"{driver.name} :\n CNIC = {cnic}\n Password = {driver.drv_pswd}\n Time Slot = {driver.ser_no} shift\n Seats Available = {self.total_seats - driver.seats}\n\n"
        
        details += f"\nAvailable Time Slots: {len(self.time_slots)}\n"
        for ser_no, slot in self.time_slots.items():
            details += f"{ser_no} : {slot.time}\n"

        details += f"\nEnrolled Students: {len(self.students)}\n"
        for reg_no, student in self.students.items():
            details += f"{student.name} :\n Registration Number = {reg_no}\n Password = {student.std_pswd}\n"
            if student.status:
                details += " Status : Booked\n"
            else:
                details += " Status : Not Booked\n"
        
        messagebox.showinfo("Complete Details", details)

    def change_driver_password(self, cnic, old_pswd, new_pswd, confirm_pswd):
        if old_pswd == self.drivers[cnic].drv_pswd:
            if new_pswd == confirm_pswd:
                self.drivers[cnic].drv_pswd = new_pswd
                messagebox.showinfo("Success", "Password changed successfully!")
            else:
                messagebox.showerror("Error", "New Password didn't match!")
        else:
            messagebox.showerror("Error", "Old Password is Incorrect!")

    def valid_driver(self, cnic):
        return cnic not in self.drivers

    def valid_student(self, reg_no):
        return reg_no not in self.students

tra_sys = TransportSystem()
tra_sys.add_time_slot("12 O'Clock")
tra_sys.add_time_slot("2 O'Clock")
tra_sys.add_time_slot("4 O'Clock")
tra_sys.add_driver("Haris", "111", "123", "1")
tra_sys.add_driver("Waleed", "122", "123", "2")
tra_sys.add_driver("Rohin", "133", "123", "3")
tra_sys.add_student("Ali", "211", "123")
