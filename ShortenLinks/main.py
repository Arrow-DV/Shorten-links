# Made By Arrow-Dev (Ali-Hany) <3
# Made in 2/8/2024 | Last Updated in 2/8/2024
# visit us https://arrow-dev.rf.gd




# Import Needed Library's
from pathlib import Path
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, messagebox
import requests
import os
import pyperclip  # Library for clipboard operations

# Function to generate the path relative to the script directory
def relative_to_assets(path: str) -> Path:
    try:
        script_directory = Path(__file__).parent
        return script_directory / "assets/frame0" / Path(path)
    except Exception as error:
        messagebox.showerror("Error",message=f"{error}")
# Function Short
def short():
    try:
        input_link = entry_var.get().strip().lower()
        request = requests.get("http://tinyurl.com/api-create.php", {"url": input_link})
        entry_2.config(state="normal")  # Enable entry_2 for editing
        entry_2.delete(0, "end")  # Clear the current content
        entry_2.insert(0, request.text.strip())  # Set the shortened URL
    except Exception as e:
        print(f"Error: {e}")
    finally:
        os.system("start https://arrow-dev.rf.gd/bio")

# Function to copy content of entry_2 to clipboard
def copy_to_clipboard():
    pyperclip.copy(entry_2.get())
    messagebox.showinfo("Copied", "The shortened URL has been copied to the clipboard.")

# Setting up the window
window = Tk()
window.title("Arrow-Dev | Short Links")
window.geometry("550x276")
window.configure(bg="#282828")

# Creating the canvas
canvas = Canvas(
    window,
    bg="#282828",
    height=276,
    width=516,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Entry 1 for Link
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(348.5, 89.0, image=entry_image_1)

# Use StringVar for dynamic entry_1 value
entry_var = StringVar()
entry_1 = Entry(
    bd=0,
    bg="#6F00DF",
    fg="WHITE",
    highlightthickness=0,
    textvariable=entry_var
)
entry_1.place(x=199.0, y=75.0, width=299.0, height=26.0)

# Entry 2 for Output (Read-only)
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(348.5, 171.0, image=entry_image_2)
entry_2 = Entry(
    bd=0,
    fg="GREEN",
    highlightthickness=0,
    state="readonly",
    disabledbackground="#6F00DF",
)
entry_2.place(x=199.0, y=157.0, width=299.0, height=26.0)

# Button
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=short,
    takefocus=False,
    relief="flat"
)
button_1.place(x=339.0, y=215.0, width=159.0, height=41.0)

# Copy Button
copy_icon = PhotoImage(file=relative_to_assets("copy_icon.png"))
copy_button = Button(
    image=copy_icon,
    borderwidth=0,
    highlightthickness=0,
    command=copy_to_clipboard,
    relief="flat"
)
copy_button.place(x=510.0, y=157.0, width=26.0, height=26.0)

# Rectangle
canvas.create_rectangle(0.0, 0.0, 174.0, 276.0, fill="#7000DF", outline="")

# Image
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(87.0, 75.0, image=image_image_1)

# Text
canvas.create_text(199.0, 30.0, anchor="nw", text="Link", fill="#FFFFFF", font=("Inter", 36 * -1))
canvas.create_text(199.0, 109.0, anchor="nw", text="Output", fill="#FFFFFF", font=("Inter", 36 * -1))

# Making the window non-resizable
window.resizable(False, False)

# Running the main event loop
window.mainloop()
