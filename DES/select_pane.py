"""
DES selection pane on homescreen and new windows.
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import view.graph_exp as ge

def accept (event, values, state):
    view = state['view']
    view.draw_graph_list(values)
    return True