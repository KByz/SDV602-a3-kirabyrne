from tkinter.constants import S
from data.data import DataMgmt

class Model():
    def __init__(self, data_source = None) -> None:
        self.record_set = None
        self.values = None
        self.field_names = None
        self.data_mgmnt = DataMgmt()

        if data_source != None:
            csv_file_obj = self.data_mgmnt.get_file(data_source)
            self.record_set, self.values = self.data_mgmnt.read_file(csv_file=csv_file_obj, has_header=True)
            self.field_names = [key for key in self.record_set[0]]
    def merge(self, source, target):
        self.data_mgmnt.merge(source, target)

    def get_column(self, column_name):
        if self.record_set and column_name in self.field_names:
            return [record[column_name] for record in self.record_set]
