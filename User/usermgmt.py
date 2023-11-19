from  JSNdrop.jsnDrop import JSNDrop as jsnDrop
from time import gmtime
from datetime import datetime

class UserMGMT(object):
    current_user = None
    current_pass = None
    current_status = None
    current_screen = None
    msg_list = []
    msg_thread = None
    stop_thread = False
    this_user_mgmt = None
    thread_lock = False
    jsn_tok = "ENTER TOKEN"
    lastest_time = None

    def real_time_stamp(self):
        current_time = datetime.now() #display current time stamp
        current_time.timestamp()
        return current_time.timestamp()
    
    def __init__(self) -> None:
        super(). __init__()

        self.JsnDrop = jsnDrop(UserMGMT.jsn_tok, "https://newsimland.com/~kira/JSON")

        result = self.jsnDrop.create("tblUser", {"UserID PK":"USERNAME"+('X'*50),
                                                 "Password": "PASSWORD"+('X'*50),
                                                 "Chat": "MSG_ENTRY"+('X'*255),
                                                 "Time": self.current_time_stamp()})
        result = self.jsnDrop.create("tblChat", {"UserID PK":"USERNAME"+('X'*50),
                                                 "DESID":"DESID"+('X'*50),
                                                 "Chat": "MSG_ENTRY"+('X'*255),
                                                 "Time": self.current_time_stamp()})
        UserMGMT.this_user_mgmt = self

    def sign_up(self, user_id, password):
        api_result = self.jsnDrop.select("tblUser",f"UserID = '{user_id}'")
        if ("DATA_ERROR" in self.jsnDrop.jsnStatus):
            result = self.jsnDrop.store("tblUser", [{'UserID':user_id, 'Password':password, 'Status':'Registered'}])
            UserMGMT.current_user = user_id
            UserMGMT.current_status = 'Logged Out'
            result = 'Account Successfully Created!'
        else:
            result = 'Account Already Exists!'

        return result

    def login(self, user_id, password):
        result = None
        api_result = self.jsnDrop.select("tblUser",f"UserID = '{user_id}' AND Password = '{password}'")
        if ("DATA_ERROR" in self.jsnDrop.jsnStatus):
            result = "Failed to login! Criteria incorrect or account does not exist"
            UserMGMT.current_status = 'Logged Out'
            UserMGMT.current_uder = None

        else:
            UserMGMT.current_status = "Logged In"
            UserMGMT.current_user = user_id
            UserMGMT.current_pass = password
            api_result = self.jsnDrop.store("tblUser")




    