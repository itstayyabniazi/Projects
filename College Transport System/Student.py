from pathlib import Path
import Transport
import tkinter as tk

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, simpledialog, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Tayyab\Desktop\Tayyab\CTS-Pro\TEST Series\build 2\assets\Student")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

images = {}
def student_canvas(back_to_main_window, reg_no):
    global window
    name = "Login as " + Transport.tra_sys.students[reg_no].name
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
        command=lambda: Transport.tra_sys.cancel_ride(reg_no),
        relief="flat"
    )
    button_2.place(
        x=41.0,
        y=169.0,
        width=148.0,
        height=33.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Transport.tra_sys.booking_functions(reg_no),
        relief="flat"
    )
    button_3.place(
        x=38.0,
        y=123.0,
        width=158.0,
        height=33.0
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
        27.0,
        52.0,
        anchor="nw",
        text="Student Page",
        fill="#FFFFFF",
        font=("Itim", 32 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

# student_canvas(None, "211")