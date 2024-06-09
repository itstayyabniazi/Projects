from pathlib import Path
import Transport
import tkinter as tk

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, simpledialog, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Tayyab\Desktop\Tayyab\CTS-Pro\TEST Series\build 2\assets\Driver")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class PswdDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.new_pswd = None
        self.old_pswd = None
        self.confirm_pswd = None
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("300x100")  # Set the dimensions of the dialog
        icon_path = relative_to_assets("icon.png")
        self.iconphoto(False, PhotoImage(file=icon_path))
        tk.Label(master, text="Old Password:").grid(row=1)
        self.old_pswd_entry = tk.Entry(master)
        self.old_pswd_entry.grid(row=1, column=1)

        tk.Label(master, text="New Password:").grid(row=2)
        self.new_pswd_entry = tk.Entry(master)
        self.new_pswd_entry.grid(row=2, column=1)

        tk.Label(master, text="Confirm Password:").grid(row=3)
        self.confirm_pswd_entry = tk.Entry(master)
        self.confirm_pswd_entry.grid(row=3, column=1)
        return self.old_pswd_entry  # initial focus

    def apply(self):
        self.old_pswd = self.old_pswd_entry.get()
        self.new_pswd = self.new_pswd_entry.get()
        self.confirm_pswd = self.confirm_pswd_entry.get()

def get_pswd_details():
    dialog = PswdDialog(window, "Change Password")
    return dialog.old_pswd, dialog.new_pswd, dialog.confirm_pswd


def change_pswd(cnic):
    old, new, confirm = get_pswd_details()
    if old != None or new != None:
        Transport.tra_sys.change_driver_password(cnic, old, new, confirm)
    else:
        messagebox.showerror("Error", "You Cancelled!")

images = {}
def driver_canvas(back_to_main_window, cnic):
    global window
    name = "Login as " + Transport.tra_sys.drivers[cnic].name
    window = Tk()
    window.geometry("569x364")
    window.configure(bg = "#FFFFFF")
    window.title(name)

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
        x=48.0,
        y=211.0,
        width=135.0,
        height=30.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Transport.tra_sys.view_seats(cnic),
        relief="flat"
    )
    button_2.place(
        x=47.0,
        y=169.0,
        width=135.0,
        height=30.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_pswd(cnic),
        relief="flat"
    )
    button_3.place(
        x=38.0,
        y=123.0,
        width=154.0,
        height=34.0
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
        text="Driver Page",
        fill="#FFFFFF",
        font=("Itim", 32 * -1)
    )

    window.resizable(False, False)
    window.mainloop()

# driver_canvas(None, "111")