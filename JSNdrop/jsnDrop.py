import requests
import json


class JSNDrop(object):

    def __init__(self, tok = None, url = None) -> None:
        self.tok = tok
        self.url = url
        self.jsdnStatus = ""
        self.jsnResult = {}

        self.decode = json.JSONDecoder().decode
        self.encode = json.JSONEncoder().encode

        self.jsnDropRecord = self.decode('{"tok":"","cmd":{}}')
        self.jsnDropCreate = self.decode('{"CREATE":"aTableName","EXAMPLE":{}}')
        self.jsnDropStore = self.decode('{"STORE":"aTableName","VALUE":{}}')
        self.jsnDropAll = self.decode('{"ALL":"aTableName"}')
        self.jsnDropSelect = self.decode('{"SELECT":"aTableName","WHERE":"aField = b"{}}')
        self.jsnDropDelete = self.decode('{"DELETE":"aTableName","WHERE":"aField = b"{}}')
        self.jsnDropDrop = self.decode('{"DROP":"aTableName"}')
        self.jsnDropUpdate = self.decode('{"UPDATE":"aTableName","SET":"aField = b"{}}')

    def jsnDropAPI(self, command):
        api_call = self.jsnDropRecord
        api_call["tok"] = self.tok
        api_call["cmd"] = command
        payload = {'tok': self.encode(api_call)}

        r = requests.get(self.url, payload)

        jsnResponse = r.json()
        self.jsnStatus = jsnResponse["JsnMsg"]
        self.jsnResult = jsnResponse["Msg"]

        print(f"Status = {self.jsnStatus}, Result = {self.jsnResult}")
        return self.jsnResult
    
    def create(self, table_name, example):
        command = self.jsnDropStore
        command["CREATE"] = table_name
        command["EXAMPLE"] = example
        return self.jsnDropAPI(command)
    
    def all(self, table_name):
        command = self.jsnDropAll
        command["ALL"] = table_name
        return self.jsnDropAPI(command)
    
    def select(self, table_name, where):
        command = self.jsnDropAll
        command["ALL"] = table_name
        return self.jsnDropAPI(command)
    
    def delete(self, table_name, where):
        command = self.jsnDropDelete
        command["DELETE"] = table_name
        command["WHERE"] = where
        return self.jsnDropAPI(command)
    
    def drop(self, table_name):
        command = self.jsnDropDrop
        command["DROP"] = table_name
        return self.jsnDropAPI(command)
    