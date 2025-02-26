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
    
    #layout

    root.geometry('600x300')
    root.title('Crypt Note')
    root.configure(background='#262728')

    left_frame = tk.Frame()
    left_frame.config(bg='#222f3e', width=250)
    left_frame.pack(side='left', fill='y')

    right_frame = tk.Frame()
    right_frame.config(bg='#222f3e', width=550)
    right_frame.pack(side='left', fill='both', expand=True)

    #widgets

    input_box = tk.Entry(left_frame)
    input_box.config(textvariable='entry_title')
    input_box.pack(fill='x', padx=10, pady=(10,0))
    
    create_btn = tk.Button(left_frame)
    create_btn.config(bg='#10ac84', text='Create', width=25, activebackground='#393A40')
    create_btn.pack(fill='x', padx=10, pady=(10,5))

    edit_btn = tk.Button(left_frame)
    edit_btn.config(bg='#10ac84', text='Edit', width=25, activebackground='#393A40')
    edit_btn.pack(fill='x', padx=10)

    save_btn = tk.Button(left_frame)
    save_btn.config(bg='#10ac84', text='Save', width=25, activebackground='#393A40')
    save_btn.pack(fill='x', padx=10)

    delete_btn = tk.Button(left_frame)
    delete_btn.config(bg='#10ac84', text='Delete', width=25, activebackground='#393A40')
    delete_btn.pack(fill='x', padx=10)


    

    selection_box = tk.Listbox(left_frame, height=10, selectmode=tk.EXTENDED)
    selection_box.pack(expand=True, fill='both', pady=10, padx=10)

    selection_scroll = tk.Scrollbar(left_frame, orient=tk.VERTICAL, command=selection_box.yview)
    selection_box['yscrollcommand'] = selection_scroll.set

    selection_scroll.pack(side='left', expand=True, fill='y')

    yay=['Yomama', 'joe biden', 'zeleski', 'donetsk', 'russia', 'ploy']
    for item in yay:
        selection_box.insert(tk.END, item)


    # adding scrollbar 
    editor_scroll = tk.Scrollbar(right_frame) 
    
    # packing scrollbar 
    editor_scroll.pack(side='right', fill='y', padx=(0,10), pady=10) 
    
    editor_text = tk.Text(right_frame, 
                    yscrollcommand=editor_scroll.set) 
    editor_text.pack(fill='both', padx=(10,0), pady=10) 
    
    # configuring the scrollbar 
    editor_scroll.config(command=editor_text.yview) 

    root.mainloop()

    

    
    
main()