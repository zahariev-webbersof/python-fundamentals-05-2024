import re
import tkinter as tk
from tkinter import PhotoImage

def validate_email():
    email = entry_email.get()

    if "@" not in email:
        result = "Invalid email: Missing '@'."
        color = "red"
    elif "." not in email:
        result = "Invalid email: Missing '.'"
        color = "red"
    else:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            result = "Email is valid!"
            color = "green"
        else:
            result = "Invalid email: Contains forbidden characters or wrong format."
            color = "red"

    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)
    entry_result.config(fg=color)

def add_background():
    background_image = PhotoImage(file="lab.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = background_image

root = tk.Tk()
root.geometry("500x500")  # Window size
root.title('Email Validator')

# Add background image
add_background()

label_instructions = tk.Label(root, text="Enter an email address. It should include '@' and '.domain'.")
label_instructions.pack(pady=10)

entry_email = tk.Entry(root, width=60)
entry_email.pack(pady=10)
entry_email.delete(0, tk.END)  # Clear field

button_validate = tk.Button(root, text="Validate Email", command=validate_email)
button_validate.pack(pady=10)

entry_result = tk.Entry(root, width=60)
entry_result.pack(pady=10)
entry_result.delete(0, tk.END)  # Clear field

root.mainloop()