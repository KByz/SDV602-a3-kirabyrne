"""
Open new DES from initiated DES.
"""

def open_des():
    from view.data_explorer_view import DES_View

    steadfast = True
    if event == 'New DES':
        des_obj = DES_View()
        des_obj.layout()
        des.obj.render()
        des_obj.take_input()
    return steadfast

