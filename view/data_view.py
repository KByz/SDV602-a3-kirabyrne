"""
The full background app.
"""

import sys
sys.dont_write_bytecode = True
from typing import Text
#import view.ChartExamples as ce INTO your mock data
import DES.new_screen as ns
import DES.select_pane as sp
import PySimpleGUI as sg
import inspect
import csv.opn_file as open_file
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class DES_win(object):
    des_list = []
    current_win = 0
    def __init__(self):

        self.window = None
        self.figure_agg = None
        self.layout = []
        self.components = {"has_components":False}
        self.controls = []
        self.my_lastfig = None
        """
        CHART EXAMPLES
        self.fig_dict = {'Line Plot':(ce.line_plot)}
        """
        DES_win.current_win +=1
        DES_win.des_list += [self]
    
    def graph_selected(self,values):
        return len(values['-GRAPH LIST-']) > 0
    
    def update_graph_text(self, component_name, text):
        if component_name in self.components:
            self.components[component_name].update(text)
    
    def update_current_data(self,values,file_name=None, **kwargs):
        if self.have_select_graph(values) :
            the_file_name = file_name
            choice = values['-GRAPH LIST-'][0]
            (func,args) = self.graph_dict[choice]
            for arg_name in kwargs:
                args[arg_name] = kwargs[arg_name]
            
            if 'file_name' in args:
                the_file_name = args['file_name']
            if the_file_name != None :
                args['file_name'] = the_file_name
            else:
                the_file_name = "No data selected"
            self.update_component_text('data_file_name', the_file_name)
            self.graph_dict[choice] = (func,args)
            self.draw_graph_list(values)

    def draw_graph(self, canvas, figrue):
        graph_canvas_agg = FigureCanvasTkAgg(figrue, canvas)
        graph_canvas_agg.draw()
        graph_canvas_agg.get_th_widget().pack(side='top', fill='both', exapand=1)
        return graph_canvas_agg
        
    def close_graph(self, fig_agg):
        if self.graph_agg:
         self.graph_agg.get_th_widget().forget()
        plt.close('all')
    
    def draw_graph_list(self, values):

        if self.have_selected_graph(values):
            choice = values['-GRAPH LIST-'][0]
            func_tuple = self.graph_dict[choice]
            kwargs = func_tuple[1]

            func = func_tuple[0]

            self.window['-MULTILINE-'].update(inspect.getsource(func))
            self.window['-GRAPH NAME-'].update(choice)

            fig = func(**kwargs)

            self.close_graph(self.figure_agg)

            the_file_name = "No Data"
            if 'file_name' in kwargs:
                the_file_name = kwargs['file_name']
            self.update_graph_text('data_file_name', the_file_name)

            self.figure_agg = self.draw_graph(self.window['-CANVAS-'].TKCanvas, fig)
        
    def create_layout(self, **kwargs):

        sg.theme('Darkgrey')
        figure_w, figure_h = 500, 500
        listbox_values = ['Trend Chart', 'Bar Chart', 'Pie Chart']
        print(f"GOT List box {listbox_values}")
        self.components['graphs_list'] = sg.Listbox(values==listbox_values, enable_events=True, size=(30, len(listbox_values)), key='-GRAPH LIST-')
        self.controls += [graphs_list_select.accept]

        self.components['text_spacer'] = sg.Text(' ', size=(30,1)) # check orginal code
        self.components['new_screen'] = sg.Button(button_text="New Graph Screen", size=(10,2))
        self.controls += [new_screen.accept]
        self.components['file_name'] = sg.Text('No data to display', size=(30,1), key='-FILE NAME-')
        self.components['graph_name'] = sg.Text('No graph selected', size=(30,1), key='-GRAPH NAME-')
        self.components['select_file'] = sg.Button(button_text="Select CSV file", size=(10,2))
        self.controls += [select_file.accept]

        col_listbox = [
                    [self.components['graphs_list']],
                    [self.components['text_spacer'], self.components['new_screen']]
                 
                 ]
        self.components['header'] =  sg.Text(f'DES {DES_win.current_win}', size=(30,1), font=("Helvetica", 25))
        self.components['list_box_padding'] = sg.Col(col_listbox, pad=(5, (3, 330)))
        self.components['canvas'] = sg.Canvas(size=(70, 35), pad=(5, (3, 90)), key='-MULTILINE-')
        self.layout = [
                [self.components['header']], [self.components['data_file_name']],
                [self.components['list_box_padding'],self.compoents['canvas'],
                 self.componants['MLine']]

                ]
    def render(self):
            if self.layout != []:
                self.window =sg.Window(f"DES {DES_win.current_win}", self.layout, finalize=True)

    def accept_input(self):
            if self.window != None :
                keep_going = True

                while keep_going == True:
                    event, values = self.window.read()
                    for accept_conteols in self.controls:
                        keep_going = accept_control(event,values,{'view':self})
                    self.window.close()
            





        











