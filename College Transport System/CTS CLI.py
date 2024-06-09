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
        # Add admin login functionality here
        # For example, # If they are, check if the username and password are correct allow the admin to add drivers and view results
        if username == "admin" and password == "123":
            return True
        return False
    
    def driver_login(self, cnic, password):
            #Add candidate login functionality here
            # For example, check if the username and password are correct
            # If they are, allow the candidate to view their results 
            if cnic in self.drivers and password in self.drivers[cnic].drv_pswd:
                return True
            return False

    def student_login(self, reg_no, password):
            # Add bookingr login functionality here
            #For example, check if the username and password are conrect
            #If they are, allow the bookingr to cast their booking
            if reg_no in self.students and password in self.students[reg_no].std_pswd:
                return True
            return False

    def booking(self, booking_for):
        if booking_for in self.time_slots:
            for cnic in self.drivers:
                if booking_for == self.drivers[cnic].ser_no:
                    if self.drivers[cnic].seats < self.total_seats:
                        self.drivers[cnic].seats += 1
                        self.num_students += 1
                        print(f"You Succesfully booked for {self.time_slots[booking_for].time}!")
        else:
            print("Invalid Selection!")

    def driver_result(self, cnic):
        print("\nResults:")
        for dcnic in self.drivers.items():
            if dcnic == cnic:
                print(f"{self.drivers[cnic].name}: {self.drivers[cnic].booked} booked")
        print(f"Total number of students: {self.num_students}")
    
    def compl_details(self):
        print(f"\nEnrolled Drivers are: {len(self.drivers)}")
        for cnic, driver in self.drivers.items():
            print(f"{driver.name} : \n CNIC = {cnic}  \n Password = {driver.drv_pswd}  \n Time Slot = {driver.ser_no} shift  \n Seats Available =  {self.total_seats - driver.seats}")
            print()
        
        print(f"\nAvailable Time Slots are: {len(self.time_slots)}")
        for ser_no in vm.time_slots:
            print(f"{ser_no} : {self.time_slots[ser_no].time}")

        print(f"\nEnrolled Students are: {len(self.students)}")
        for cnic, student in self.students.items():
            print(f"{student.name} : \n CNIC = {cnic}  \n Password = {student.std_pswd}  ")
            if student.status == True:
                print(" Status : Booked")
            else:
                print(" Status : Not Booked")

    def pswd_change(self):
        old_pswd = input("Enter Old Password: ")
        if old_pswd == self.drivers[cnic].drv_pswd:
            new_pswd = input("Enter New Password: ")
            confirm_pswd = input("Confirm New Password: ")
            if new_pswd == confirm_pswd:
                self.drivers[cnic].drv_pswd = new_pswd
            else:
                print("Your New Password didn't match!")
        else:
            print("Your Password is Incorrect!")

    def driver_functions(self, cnic):
        print(f"\n>> Logged In as {self.drivers[cnic].name}<<")
        print("\nDriver Functions:")
        print("1. Change Password")
        print("2. View Booked Seats") 
        print("3. Logout")
        while True:
            choice = input("Enter the function you want to perform: ")
            if choice == "1":
                vm.pswd_change()
            elif choice == "2":
                vm.driver_result(cnic)
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
           
            print("\nDriver Functions:")
            print("1. Change Details")
            print("2. View Result") 
            print("3. Logout")

    def booking_functions(self, reg_no):
        print(f"\n>> Logged In as {self.students[reg_no].name}<<")
        if reg_no in self.students and self.students[reg_no].status == False:
            print("Drivers:")
            for ser_no in vm.time_slots:
                print(f"{ser_no} : {self.time_slots[ser_no].time}")
            booking_for = input("Select the Time Slot: ")
            if booking_for in vm.time_slots:
                vm.booking(booking_for)
                self.students[cnic].status = True
            else:
                print("Invalid Selection!")
        else:
            print("You have already booked.")

    def valid_driver(self, dcnic):
        if dcnic in self.drivers:
            return False
        return True

    def valid_student(self, scnic):
        if scnic in self.students:
            return False
        return True

    def admin_functions(self):
            print("\nAdmin Functions:")
            print("1. Add Drivers")
            print("2. Add Student")
            print("3. Add Time Slot")
            print("4. Check Details")
            print("5. Logout")
            while True:
                choice = input("Enter the function you want to perform: ")
                if choice == "1":
                    cnic = input("Enter the CNIC of the Driver: ")
                    if vm.valid_driver(cnic):
                        username = input("Enter the name of the Driver: ")
                        password = input("Enter the Password for the Driver: ")
                        print("Available Time Slots are;")
                        for ser_no in vm.time_slots:
                            print(f"{ser_no} : {self.time_slots[ser_no].time}")
                        sno = input("Select the Time Slot: ")
                        if sno in vm.time_slots:
                            vm.add_driver(username, cnic, password, sno)
                            print(f" {username} has been added as a Driver.")
                        else:
                            print("Invalid Selection!")
                    else:
                        print(">> Error : Driver Already Exist! <<")
                            
                elif choice == "2":
                    cnic = input("Enter the Registration Number of the Student: ")
                    if vm.valid_student(cnic):
                        name = input("Enter the name of the Student: ")
                        password = input("Enter the Password for the Student: ")
                        vm.add_student(name, cnic, password)
                        print(f" {name} has been added as a Student.")
                    else:
                        print(">> Error : Student Already Exist! <<")

                elif choice == "3":
                    time = input("Enter the Time: ")
                    vm.add_time_slot(time)
                    print(f" {self.ser_no - 1} : {time} has been added!")

                elif choice == "4":
                    vm.compl_details()

                elif choice == "5":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")

                print("\nAdmin Functions:")
                print("1. Add Drivers")
                print("2. Add Student")
                print("3. Add Time Slot")
                print("4. Check Details")
                print("5. Logout")

if __name__ == "__main__":
    vm = TransportSystem()
    vm.add_time_slot("12 O'Clock")
    vm.add_time_slot("2 O'Clock")
    vm.add_time_slot("4 O'Clock")
    vm.add_driver("Haris", "111", "123", "1")
    vm.add_student("Ali", "211", "123")

    print("Welcome!\t1.0\n1.Admin Login\n2.Driver Login\n3.Student Login\n4.Exit\n------------------")
    login = input("")
    while True:
        if login == "1":
            # Admin login
            username = input("Enter Username: ")
            password = input("Enter password: ")
            if vm.admin_login(username, password):
                # Allow the admin to add drivers and view results
                print("\n>> Loged In! <<")
                vm.admin_functions()
            else:
                print("Wrong Password or Username!")
                
        elif login == "2":
            # Driver login
            cnic = input("Enter CNIC: ")
            password = input("Enter password: ")
            if vm.driver_login(cnic, password):
                #Allow the candidate to view their results
                vm.driver_functions(cnic)
            else:
                print("Wrong Password or Username!")
                
        elif login == "3":
            # Student login
            cnic = input("Enter Registration Number: ")
            password = input("Enter password: ")
            if vm.student_login(cnic, password):
                # Allow the bookingr to cast their booking
                vm.booking_functions(cnic)        
            else:
                print("Wrong CNIC!")    
            
        elif login == "4":
            break
        
        else:
            print("Invalid Selection!")
        print("\n1.Admin Login\n2.Driver Login\n3.Student Login\n4.Exit\n------------------")
        login = input("")
        
