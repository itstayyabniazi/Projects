from pathlib import Path
import tkinter as tk
import Admin, Student, Driver
import Transport as transport_system

from tkinter import Tk, Canvas, Button, PhotoImage, simpledialog, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Tayyab\Desktop\Tayyab\CTS-Pro\TEST Series\build 2\assets\main")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LoginDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.username = None
        self.password = None
        self.who_is = title
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("300x100")  # Set the dimensions of the dialog
        icon_path = relative_to_assets("icon.png")
        self.iconphoto(False, PhotoImage(file=icon_path))
        if self.who_is == "Admin Login":
            tk.Label(master, text="Enter Username:").grid(row=1)
        elif self.who_is == "Driver Login":
            tk.Label(master, text="Enter CNIC:").grid(row=1)
        elif self.who_is == "Student Login":
            tk.Label(master, text="Enter Registration No:").grid(row=1)
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=1, column=1)

        tk.Label(master, text="Enter Password:").grid(row=2)
        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.grid(row=2, column=1)
        return self.username_entry  # initial focus

    def apply(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

def get_admin_login():
    dialog = LoginDialog(window, "Admin Login")
    return dialog.username, dialog.password

def get_driver_login():
    drv_dialog = LoginDialog(window, "Driver Login")
    return drv_dialog.username, drv_dialog.password

def get_student_login():
    std_dialog = LoginDialog(window, "Student Login")
    return std_dialog.username, std_dialog.password

def admin_login():
        username, password = get_admin_login()
        if username == None or password == None:
            pass
        else:
            if transport_system.tra_sys.admin_login(username, password):
                messagebox.showinfo("Login Success", "Admin logged in successfully!")
                admin_menu()
            else:
                messagebox.showerror("Login Failed", "Wrong Username or Password!")

def driver_login():
        cnic, password = get_driver_login()
        if cnic == None or password == None:
            pass
        else:
            if transport_system.tra_sys.driver_login(cnic, password):
                name = "Login as Driver: " + transport_system.tra_sys.drivers[cnic].name
                messagebox.showinfo("Login Success", name)
                driver_menu(cnic)
            else:
                messagebox.showerror("Login Failed", "Wrong Username or Password!")

def student_login():
        reg_no, password = get_student_login()
        if reg_no == None or password == None:
            pass
        else:
            if transport_system.tra_sys.student_login(reg_no, password):
                name = "Login as Student: " + transport_system.tra_sys.students[reg_no].name
                messagebox.showinfo("Login Success", name)
                student_menu(reg_no)
            else:
                messagebox.showerror("Login Failed", "Wrong Username or Password!")

def exit():
    window.quit()

def admin_menu():
    window.destroy()
    Admin.admin_canvas(main_window)

def driver_menu(cnic):
    window.destroy()
    Driver.driver_canvas(main_window, cnic)
    
def student_menu(reg_no):
    window.destroy()
    Student.student_canvas(main_window, reg_no)


def main_window():
    global window
    window = Tk()
    window.geometry("569x364")
    window.configure(bg = "#FFFFFF")
    window.title("College Transport System")

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
        command=lambda: exit(),
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
        command=lambda: student_login(),
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
        command=lambda: driver_login(),
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
        command=lambda: admin_login(),
        relief="flat"
    )
    button_4.place(
        x=48.0,
        y=119.0,
        width=135.0,
        height=30.0
    )

    canvas.create_text(
        51.0,
        11.0,
        anchor="nw",
        text="College",
        fill="#FFFFFF",
        font=("Itim", 40 * -1)
    )

    canvas.create_text(
        5.0,
        52.0,
        anchor="nw",
        text="Transport System",
        fill="#FFFFFF",
        font=("Itim", 30 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

main_window()