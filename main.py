import tkinter as tk
import setup
from os import path
import menu

#Checks if setup has been completed previously.
if not path.exists('setup_complete.flag'):
    setup.setup()
    print('Setup complete!')

def main():
    
    ui = menu.Menu()
    
main()