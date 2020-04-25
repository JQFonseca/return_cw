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
    name = askopenfilename(initialdir=".",
                                filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                title="Open the name and emails file"
                               )
    return name


def open_files():
    '''
    Returns a list of coursework files that will
    be sent back to students.
    '''
    file_list = askopenfilenames(initialdir=".",
                                      filetypes=(("PDF files","*.pdf"),
                                                 ("Notebook File", "*.ipynb"),
                                                 ("All Files", "*.*")),
                                      title="Select all coursework to email"
                                     )
    return file_list

def get_body_file():
    '''
    Open file to read in names and emails
    '''
    name = askopenfilename(initialdir=".",
                                filetypes=(("HTML file", "*.html"), ("All Files", "*.*")),
                                title="Open the email message file"
                               )
    return name


def get_username():
    '''
    Prompts for Exchange username and password
    '''
    username = input('Enter Exchange email: ')
    if username == '':
        username = 'joao.fonseca@manchester.ac.uk'
    passwd = getpass.getpass(prompt='Password: ')
    return username, passwd
