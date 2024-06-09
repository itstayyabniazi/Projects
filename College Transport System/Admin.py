
from pathlib import Path
import Transport as transport_system
import tkinter as tk

from tkinter import Tk, Canvas, Button, PhotoImage, simpledialog, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Tayyab\Desktop\Tayyab\CTS-Pro\TEST Series\build 2\assets\Admin")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class NewDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.cnic = None
        self.username = None
        self.password = None
        self.who_is = title
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("300x100")  # Set the dimensions of the dialog
        icon_path = relative_to_assets("icon.png")
        self.iconphoto(False, PhotoImage(file=icon_path))
        if self.who_is == "Add Driver":
            tk.Label(master, text="Enter CNIC:").grid(row=1)
        elif self.who_is == "Add Student":
            tk.Label(master, text="Enter Registration No:").grid(row=1)
        
        self.cnic_entry = tk.Entry(master)
        self.cnic_entry.grid(row=1, column=1)

        tk.Label(master, text="Enter Name:").grid(row=2)
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=2, column=1)

        tk.Label(master, text="Enter Password:").grid(row=3)
        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.grid(row=3, column=1)
        return self.username_entry  # initial focus

    def apply(self):
        self.cnic = self.cnic_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

def get_add_student():
    dialog = NewDialog(window, "Add Student")
    return dialog.cnic, dialog.username, dialog.password

def get_add_driver():
    dialog = NewDialog(window, "Add Driver")
    return dialog.cnic, dialog.username, dialog.password

def add_driver():
    cnic, name, password = get_add_driver()
    if cnic != None or name != None:
        if transport_system.tra_sys.valid_driver(cnic):
            time_slots = "Given Time Slots are: \n"
            time_slots += "\n".join([f"{ser_no}: {slot.time}" for ser_no, slot in transport_system.tra_sys.time_slots.items()])
            ser_no = simpledialog.askstring("Add Driver", time_slots)
            if ser_no in transport_system.tra_sys.time_slots:
                transport_system.tra_sys.add_driver(name, cnic, password, ser_no)
                messagebox.showinfo("Success", f"{name} has been added as a Driver.")
            else:
                messagebox.showerror("Error", "Invalid Time Slot!")
        else:
            messagebox.showerror("Error", "Driver Already Exists!")


def add_student():
    cnic, name, password = get_add_student()
    if cnic != None or name != None:
        if transport_system.tra_sys.valid_student(cnic):
            transport_system.tra_sys.add_student(name, cnic, password)
            messagebox.showinfo("Success", f"{name} has been added as a Student.")
        else:
            messagebox.showerror("Error", "Student Already Exists!")

def add_time_slot():
    time = simpledialog.askstring("Add Time", "Enter the Arival Time at College:")
    if time != None:
        transport_system.tra_sys.add_time_slot(time)
        messagebox.showinfo("Success", f"{transport_system.tra_sys.ser_no - 1}: {time} has been added!")

def driver_details():
    details = f"\nEnrolled Drivers: {len(transport_system.tra_sys.drivers)}\n"
    for cnic, driver in transport_system.tra_sys.drivers.items():
        details += f"        {driver.name} :\n CNIC = {cnic}\n Password = {driver.drv_pswd}\n Time Slot = {driver.ser_no} shift\n Seats Available = {transport_system.tra_sys.total_seats - driver.seats}\n\n"
    messagebox.showinfo("Drivers Details", details)
    
def student_details():
    details = f"\nEnrolled Students: {len(transport_system.tra_sys.students)}\n"
    for reg_no, student in transport_system.tra_sys.students.items():
        details += f"\t{student.name} :\n Registration Number = {reg_no}\n Password = {student.std_pswd}\n"
        if student.status:
            details += " Status : Booked\n"
        else:
            details += " Status : Not Booked\n"
    messagebox.showinfo("Students Details", details)

def time_details():
    details = f"\nAvailable Time Slots: {len(transport_system.tra_sys.time_slots)}\n"
    for ser_no, slot in transport_system.tra_sys.time_slots.items():
        details += f"{ser_no} : {slot.time}\n"
    messagebox.showinfo("Time Slots Details", details)


images = {}
def admin_canvas(back_to_main_window):
    global window
    window = Tk()
    window.geometry("569x364")
    window.configure(bg = "#FFFFFF")
    window.title("Admin Login")

    icon_path = relative_to_assets("icon.png")
    window.iconphoto(False, PhotoImage(file=icon_path))

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 364,
        width = 569,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        284.0,
        182.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), back_to_main_window()),
        relief="flat"
    )
    button_1.place(
        x=49.0,
        y=245.0,
        width=135.0,
        height=30.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_time_slot(),
        relief="flat"
    )
    button_2.place(
        x=48.0,
        y=203.0,
        width=135.0,
        height=30.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_student(),
        relief="flat"
    )
    button_3.place(
        x=48.0,
        y=161.0,
        width=135.0,
        height=30.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_driver(),
        relief="flat"
    )
    button_4.place(
        x=48.0,
        y=119.0,
        width=135.0,
        height=30.0
    )

    images['img_2'] = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(125.0, 52.0, image=images['img_2'])

    canvas.create_text(
        80.0,
        11.0,
        anchor="nw",
        text="CTS",
        fill="#FFFFFF",
        font=("Itim", 40 * -1)
    )

    canvas.create_text(
        33.0,
        54.0,
        anchor="nw",
        text="Admin Page",
        fill="#FFFFFF",
        font=("Itim", 32 * -1)
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: student_details(),
        relief="flat"
    )
    button_5.place(
        x=268.0,
        y=302.0,
        width=99.0,
        height=22.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: driver_details(),
        relief="flat"
    )
    button_6.place(
        x=367.0,
        y=302.0,
        width=99.0,
        height=22.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: time_details(),
        relief="flat"
    )
    button_7.place(
        x=466.0,
        y=302.0,
        width=99.0,
        height=22.0
    )
    window.resizable(False, False)
    window.mainloop()
