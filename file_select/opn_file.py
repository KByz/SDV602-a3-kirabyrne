"""
Open file system and function button.
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg



def accept(event):
    keep_going = True
    if event == 'Open CSV file':

        file_name = sg.PopupGetFile('Select CSV file', file_types=(("Comma Separated Values", "*.csv"),))
        if file_name != None:
            print(f"File name: {file_name}")
        keep_going = True

    
        