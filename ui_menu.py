import tkinter as tk
import database as db
import tkinter.messagebox

class UI():
    def __init__(self):
        self.root = tk.Tk()

        #layout

        self.root.geometry('600x300')
        self.root.title('Crypt Note')
        self.root.configure(background='#262728')

        self.left_frame = tk.Frame()
        self.left_frame.config(bg='#222f3e', width=250)
        self.left_frame.pack(side='left', fill='y')

        self.right_frame = tk.Frame()
        self.right_frame.config(bg='#222f3e', width=550)
        self.right_frame.pack(side='left', fill='both', expand=True)

        #widgets

        self.input_box = tk.Entry(self.left_frame)
        self.input_box.config(textvariable='entry_title')
        self.input_box.pack(fill='x', padx=10, pady=(10,0))

        self.create_btn = tk.Button(self.left_frame)
        self.create_btn.config(bg='#10ac84', text='Create', width=25, activebackground='#393A40', command=self.create_note)
        self.create_btn.pack(fill='x', padx=10, pady=(10,5))

        self.edit_btn = tk.Button(self.left_frame)
        self.edit_btn.config(bg='#10ac84', text='Edit', width=25, activebackground='#393A40')
        self.edit_btn.pack(fill='x', padx=10)

        self.save_btn = tk.Button(self.left_frame)
        self.save_btn.config(bg='#10ac84', text='Save', width=25, activebackground='#393A40')
        self.save_btn.pack(fill='x', padx=10)

        self.create_btn = tk.Button(self.left_frame)
        self.create_btn.config(bg='#10ac84', text='Refresh', width=25, activebackground='#393A40', command=self.refresh_list)
        self.create_btn.pack(fill='x', padx=10)

        self.delete_btn = tk.Button(self.left_frame)
        self.delete_btn.config(bg='#10ac84', text='Delete', width=25, activebackground='#393A40', command=self.delete_note)
        self.delete_btn.pack(fill='x', padx=10)

        self.selection_box = tk.Listbox(self.left_frame, height=10, selectmode=tk.EXTENDED)
        self.selection_box.pack(expand=True, fill='both', pady=10, padx=10)

        self.selection_scroll = tk.Scrollbar(self.left_frame, orient=tk.VERTICAL, command=self.selection_box.yview)
        self.selection_box['yscrollcommand'] = self.selection_scroll.set

        self.selection_scroll.pack(side='left', expand=True, fill='y')

        notes= db.list_all(db.connectDB())
        for item in notes:
            self.selection_box.insert(tk.END, item[2])


        self.editor_scroll = tk.Scrollbar(self.right_frame) 
        self.editor_scroll.pack(side='right', fill='y', padx=(0,10), pady=10) 
        self.editor_text = tk.Text(self.right_frame, yscrollcommand=self.editor_scroll.set) 
        self.editor_text.pack(fill='both', padx=(10,0), pady=10) 

        self.editor_scroll.config(command=self.editor_text.yview) 

        self.root.mainloop()

    def get_entry(self):
        return self.input_box.get()

    def create_note(self):
        if self.get_entry() == '':
            title = 'untitled note'
        else:
            title = self.get_entry()
        db.create_row(db.connectDB(), title)

    def refresh_list(self):
        self.selection_box.delete(0, 'end')

        new_list = db.list_all(db.connectDB())
        for item in new_list:
            self.selection_box.insert(tk.END, item[2])

    def delete_note(self):
        selected = self.selection_box.curselection()
        titles = []
        for index in selected:
            row = db.get_row(db.connectDB(), index)
            if row:
                title = row[2]
                titles.append(title)
        
            
        result=tkinter.messagebox.askquestion('Confirmation',f'Are you sure you want to delete: {titles}')
        if result == 'yes':
            #implement deletion in the database
            for items in selected[::-1]:
                self.selection_box.delete(items)
                print(items)
        else:
            pass
