"""
Open file system and function button.
"""
import PySimpleGUI as sg
import sys
sys.dont_write_bytecode = True


# <<< ACCEPT Needed more parameters(event, values, state) AND needed to return True:
def accept(event, values, state):
    keep_going = True
    if event == 'Open CSV file':

        file_name = sg.PopupGetFile('Select CSV file', file_types=(
            ("Comma Separated Values", "*.csv"),))
        if file_name != None:
            print(f"File name: {file_name}")
        keep_going = True

    return keep_going
