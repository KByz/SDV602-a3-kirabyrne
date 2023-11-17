"""
Home screen of the application.

Will import:
    - Login page connected to NewSimLand tokens
    - Register page connected to NewSimLand tokens
    - Main home for DES selection
    - DES selection pane
    - New DES button
    - Open CSV button
    - Open chat button
"""
import sys
sys.dont_write_bytecode = True
from view.data_view import DES_win

if __name__ == "__main__":
    des_obj = DES_win()
    des_obj.create_layout()
    des_obj.render()

    des_obj.accept_input()

    pass