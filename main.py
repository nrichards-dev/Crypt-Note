import tkinter as tk
import setup
from os import path

#Checks if setup has been completed previously.
if not path.exists('setup_complete.flag'):
    setup.setup()
    print('Setup complete!')

def prnt():
    print("hello!")

def click():
    print("Hello!")

def main():
    root = tk.Tk()
    root.geometry('800x500')
    root.title('Crypt Note')
    root.configure(background='#262728')
    
    textbox = tk.Entry()
    textbox.pack(anchor='nw')

    button = tk.Button(root, text="Create")
    button.config(command=click, bg='#484E70', activebackground='#393A40')
    button.pack(anchor='nw')

    button = tk.Button(root, text="Open")
    button.config(command=click, bg='#484E70', activebackground='#393A40')
    button.pack(anchor='nw')

    button = tk.Button(root, text="Save")
    button.config(command=click, bg='#484E70', activebackground='#393A40')
    button.pack(anchor='nw')

    button = tk.Button(root, text="Remove")
    button.config(command=click, bg='#484E70', activebackground='#393A40')
    button.pack(anchor='nw')

    root.mainloop()

main()