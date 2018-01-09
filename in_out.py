'''
Module with functions for IO
'''

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
from tkinter import *
import getpass

#This is where we launch the file manager bar.
def open_file():
    '''
    Open file to read in names and emails
    '''
    root = Tk()
    root.name = askopenfilename(initialdir=".",
                                filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                title="Open the name and emails file"
                               )
    root.destroy()
    return root.name


def open_files():
    '''
    Returns a list of coursework files that will
    be sent back to students.
    '''

    root = Tk()
    root.file_list = askopenfilenames(initialdir=".",
                                      filetypes=(("Notebook File", "*.ipynb"),
                                                 ("All Files", "*.*")),
                                      title="Select all coursework to email"
                                     )
    root.destroy()
    return root.file_list

def get_username():
    '''
    Prompts for Exchange username and password
    '''
    username = input('Enter Exchange email: ')
    passwd = getpass.getpass(prompt='Password: ')
    return username, passwd
