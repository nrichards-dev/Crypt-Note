import tkinter as tk
import database as db
import tkinter.messagebox
from tkinter import ttk

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
        self.edit_btn.config(bg='#10ac84', text='Edit', width=25, activebackground='#393A40', command=self.edit_note)
        self.edit_btn.pack(fill='x', padx=10)

        self.save_btn = tk.Button(self.left_frame)
        self.save_btn.config(bg='#10ac84', text='Save', width=25, activebackground='#393A40', command=self.save_note)
        self.save_btn.pack(fill='x', padx=10)

        self.create_btn = tk.Button(self.left_frame)
        self.create_btn.config(bg='#10ac84', text='Refresh', width=25, activebackground='#393A40', command=self.refresh_list)
        self.create_btn.pack(fill='x', padx=10)

        self.delete_btn = tk.Button(self.left_frame)
        self.delete_btn.config(bg='#10ac84', text='Delete', width=25, activebackground='#393A40', command=self.delete_note)
        self.delete_btn.pack(fill='x', padx=10)

        #
        # New selection box implementation
        #

        self.notes_frame = tk.Frame(self.left_frame)
        self.notes_list = ttk.Treeview(self.notes_frame)
        self.notes_list['columns'] = ('id', 'Title')

        self.notes_list.column('#0', width=0, stretch=tk.NO)
        self.notes_list.column('id', width=0, stretch=tk.NO)
        self.notes_list.column('Title', width=25, stretch=tk.YES)

        self.notes_list.heading("id", text="id")
        self.notes_list.heading('Title', text='Note title')

        self.notes_frame.pack(fill='x', padx=10, pady=10)
        self.notes_list.pack(expand=True, side='left',fill='both')

        self.refresh_list() #initial list populating
        #
        # -----------------------------------
        #

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
        self.notes_list.delete(*self.notes_list.get_children())

        new_list = db.list_all(db.connectDB())
        for item in new_list:
            self.notes_list.insert('',index='end', values=(item[0],item[2]))

    def delete_note(self):
        selected = self.notes_list.selection()
        if selected:
            titles = []
            for index in selected:
                row = db.get_row(db.connectDB(), self.notes_list.item(index).get('values')[0])
                if row:
                    titles.append(self.notes_list.item(index).get('values')[1])
            
                
            result=tkinter.messagebox.askquestion('Confirmation',f'Are you sure you want to delete: {titles}')
            if result == 'yes':
                for items in selected[::-1]:
                    db.remove_row(db.connectDB(), self.notes_list.item(index).get('values')[0])
                    self.notes_list.delete(items)
                    print(items)
            else:
                pass
        selected = None

    def edit_note(self):
        selection = self.notes_list.selection()
        self.editor_text.delete(1.0, tk.END)
        if len(selection) > 1:
            self.editor_text.insert(1.0, 'YOU CAN ONLY EDIT ONE NOTE AT A TIME! CHECK YOUR SELECTIONS IN THE BOTTOM LEFT.')
        else:
            self.editor_text.insert(1.0, str(db.get_row(db.connectDB(), self.notes_list.item(selection[0]).get('values')[0])[1]))
        selection = None

    def save_note(self):
        data = self.editor_text.get(1.0, tk.END)
        db_id = self.notes_list.item(self.notes_list.selection()[0]).get('values')[0]
        db.edit_data(db.connectDB(), data, db_id)
        data = None
        db_id = None
