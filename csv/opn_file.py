"""
Open file system and function button.
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
from model.model import Model

def take(event):
    keep_going = True
    if event == 'Open CSV file':

        file_name = sg.PopupGetFile ('Select file to open', file_types=(("*.csv", "comma separated values"),))
        if file_name != None :
         sg.PopupOK('No file selected')

    return keep_going
    
        