import tkinter as tk
import setup
from os import path
import ui_menu



def main():
    
    #Checks if setup has been completed previously.
    if not path.exists('setup_complete.flag'):
        setup.setup()
        print('Setup complete!')
    display_menu = ui_menu.UI()
    

main()