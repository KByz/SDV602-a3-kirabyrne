"""
Open new DES from initiated DES.
"""

import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def open_des(event, values, state):
    from view.data_view import DES_win

    keep_going = True
    if event == 'New DES':
        des_obj = DES_win()
        des_obj.set_up_layout()
        des_obj.render()
        des_obj.take_input()
    return keep_going

