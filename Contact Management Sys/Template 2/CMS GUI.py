from pathlib import Path
import csv
import tkinter as tk

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox, simpledialog
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Tayyab\Desktop\Tayyab\#PROJECTS\Contact Management Sys\Template 2\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("528x421")
window.configure(bg = "#FFFFFF")
window.title("Contact Management System")

icon_path = relative_to_assets("icon.png")
window.iconphoto(False, PhotoImage(file=icon_path))

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 421,
    width = 528,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

file_source = canvas.create_text(
    198.0,
    304.0,
    anchor="nw",
    text= "No file selected",
    fill="#FFFFFF",
    font=("Itim", 20 * -1)
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    264.0,
    210.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: file_manage.select_file(),
    relief="flat"
)
button_1.place(
    x=88.0,
    y=351.0,
    width=162.0,
    height=36.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.quit(),
    relief="flat"
)
button_2.place(
    x=293.0,
    y=351.0,
    width=162.0,
    height=36.0
)

canvas.create_text(
    90.0,
    20.0,
    anchor="nw",
    text="Contact Management ",
    fill="#000000",
    font=("Itim", 36 * -1)
)

canvas.create_text(
    200.0,
    60.0,
    anchor="nw",
    text="System",
    fill="#000000",
    font=("JejuHallasan", 32 * -1)
)


class FileManager:
    def __init__(self):
        self.file_path = None

    def select_file(self):
        # Open a file dialog and get the path of the selected file
        self.file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
    
    def get_file(self):
        # print(self.file_path)
        return self.file_path

class LoginDialog(simpledialog.Dialog):
    def __init__(self, parent, name, title=None):
        self.email = None
        self.name = name
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("300x100")  # Set the dimensions of the dialog
        icon_path = relative_to_assets("icon.png")
        self.iconphoto(False, PhotoImage(file=icon_path))
        text = "Enter Email ID for " + self.name + ":"  
        tk.Label(master, text=text).grid(row=1, column=1)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)
        return self.email_entry  # initial focus

    def apply(self):
        self.email = self.email_entry.get()

def get_email_id(name):
    dialog = LoginDialog(window, name, "Empty Email ID")
    return dialog.email


output_file = 'output.csv'
file_manage = FileManager()

data = []        # Create a list to hold the dictionaries

def read_file():
    global input_file
    input_file = file_manage.get_file()
    # Open the CSV file
    file = open(input_file, mode='r', newline='')
    # Create a DictReader object
    csv_reader = csv.DictReader(file)
    # Iterate over each row and add it to the list
    for row in csv_reader:
        data.append(row)

# Check for Duplicate Names
def duplicate_check(check, i):
    name = check["first_name"]
    for j in range(i+1, len(data)):
        checking = data[j]
        if name == checking["first_name"]:
            return False
    return True

# Check for Empty Numbers
def number_check(check):
    number = check["phone"]
    if number == "":
        return False
    return True

# Input for Blank Email Entries
def email_enter(check):
    name = check["first_name"]
    # text = "Enter Email ID for " + name + ":"
    email = get_email_id(name)
    # print(f"{name} have no email ID.")
    # email = input("Enter Email:")
    return email

def write_file():
    alt_file = file_manage.get_file()
    if alt_file == None:
        messagebox.showerror("Error", "No File Selected!")
    else:
        read_file()

        headers = data[0].keys()
        # Open the CSV file for writing
        out_file = open(output_file, mode='w', newline='')
        # Create a DictWriter object
        writer = csv.DictWriter(out_file, fieldnames=headers)

        # Write the header
        writer.writeheader()
        for i in range(len(data)):
            got_error = False
            to_check = data[i]
            if to_check["email"] == "":
                to_check["email"] = email_enter(to_check)
                if to_check["email"] == None:
                    text = "Empty Email for " + to_check["first_name"]
                    messagebox.showerror("Error while Parsing", text)
                    got_error = True
                    break
            if  duplicate_check(to_check, i) and number_check(to_check):
                writer.writerow(data[i])
        if got_error == True:
            text = "Can not save the file as some Emails are empty, parse again."
            messagebox.showerror("Error", text)
        else:
            sent = "The Contact have been parsed & succesfully saved to " + output_file
            messagebox.showinfo("File Parsed Succesfuly", sent)



window.resizable(False, False)
window.mainloop()
