"""
Create a login window that take username and password.
Login criteria will be retrived from JSNDrop token. 

Create account will create and store a login token. 
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def login(event, values, state):

    def __init__(self):

        self.window = None
        self.layout - []
        self.components = {"has_components":False}
        self.controls = []
    
    def create_layout(self, **kwargs):

        sg.theme('DarkGrey')
        
        self.components['User'] = sg.InputText('', key='User',size=(10,40))
        self.components['Password'] = sg.InputText('', key='Password',size=(10,40))

        self.components['Login'] = sg.Button('Login',size=(10, 2))
        self.controls += [login_button.accept]
        
        self.components ['SignUp'] = sg.Button('SignUp',size=(10, 2))
        self.controls += [signup_button.accept]

        row_buttons = [
                 [self.components['Login']],
                 [self.components['SignUp']]
                ]
        
    def render(self):

            if self.layout != []:
                 self.window = sg.Window(f"Login", self.layout, finalize=True)

    def accept_input(self):

            if self.window != None:
                  keep_going = True

                  while keep_going == True:
                        event, values = self.window.read()
                        for accept_control in self.controls:
                            keep_going = accept_control(event,values,{'view':self})
                        self.window.close()

        

