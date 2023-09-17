import tkinter as tk
from tkhtmlview import HTMLLabel

def update_label_text():
    new_text = "This is the updated text."
    label.set_html(new_text)

root = tk.Tk()

initial_text = "This is the initial text."

label = HTMLLabel(root, html=initial_text)
label.pack()

update_button = tk.Button(root, text="Update Text", command=update_label_text)
update_button.pack()

root.mainloop()
