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
    textbox.insert(index=0, string='Hi')
    #textbox.pack(anchor='nw')

    button = tk.Button(root, text="Create")
    button.config(command=click, bg='#484E70', activebackground='#393A40', width=10)
    button.pack(ipadx=0, ipady=0, padx=20, pady=10, anchor='w')

    button = tk.Button(root, text="Open")
    button.config(command=click, bg='#484E70', activebackground='#393A40', width=10)
    button.pack(ipadx=0, ipady=0, padx=20, pady=10, anchor='w')

    button = tk.Button(root, text="Save")
    button.config(command=click, bg='#484E70', activebackground='#393A40', width=10)
    button.pack(ipadx=0, ipady=0, padx=20, pady=10, anchor='w')

    button = tk.Button(root, text="Remove")
    button.config(command=click, bg='#484E70', activebackground='#393A40', width=10)
    button.pack(ipadx=0, ipady=0, padx=20, pady=10, anchor='w')

    scroll_bar = tk.Scrollbar(root)
    mylist = tk.Listbox(root, yscrollcommand = scroll_bar.set ) 
    for line in range(1, 26): 
        mylist.insert('end', "Geeks " + str(line)) 
    scroll_bar.config( command = mylist.yview ) 
    mylist.pack(ipadx=1, ipady=0, pady=5, anchor='w', side='right')
    
    scroll_bar = tk.Scrollbar(root)
    text_info = tk.Text(root, yscrollcommand=scroll_bar.set, height=10) 
    text_info.pack(ipadx=0, ipady=2,side='right', anchor='n')
    # configuring the scrollbar 
    scroll_bar.config(command=text_info.yview, width=50) 
    root.mainloop()

main()