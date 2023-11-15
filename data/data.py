"""
Used to read the data from an uploaded csv file to pass the data
into the figure canvas and draw the approriate graphs.
It will also update the DES header to display the file name. 
"""

import sys
from os import path
import argparse
from typing import Dict

class DataMgmt():
    dict_list = []
    value_list = []
    def __init__(self) -> None:
        self.status:Dict = {}
        self.current_file = None

    def get_file(self, path_to_file):
        try:
            self.current_file = open(path_to_file)
            return self.current_file
        except FileNotFoundError:
            file_not_found = ("No file found", path_to_file)
            return None
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            return None
        
    def close_file(self, file_object):
        file_object.close()

    def read_file(self, filter= None, has_header=False, csv_file= sys.stdin):
        """
        Defaults to csv reading
        """
        result = []
        values = []
        do_header = has_header
        header_names = {}
        try:
            lines = [aline for aline in csv_file if filter(aline)] if filter != None else csv_file
            for aline in lines:
                this_line = aline.strip().split(',')
                if do_header:
                    header_names = this_line
                    print(f" header names {header_names}")
                    do_header = False
                else:
                    a_dict = {}
                    i = 0
                    max_header_index = len(header_names) -1
                    for column in this_line:
                        if i > max_header_index :
                            break

                        a_dict[header_names[i]] = column
                    else:
                        a_dict[i] = column
                    i = i + 1

                result += [a_dict]
                values += [this_line]
        except:
            print("Unexpected erro:", sys.exc_info()[0])
            return None,None
        DataMgmt.dict_list = result
        DataMgmt.value_list = values
        return result, values
    
    def sum_of(self, column_name, a_list_of_dictionary):
        """
        Returns the sum of the values in the column_name.
        """
        current_sum = 0
        for row in a_list_of_dictionary:
            current_sum += row[column_name]
        return current_sum
    

    def multply_columns(self, column_names, a_list_of_dictionary):
        """
        Dictionary list of new rows is returned which
        multiplies the values of the columns.
        """

        result_list = []
        for a_row in a_list_of_dictionary:
            row_product = 1
            for a_name in column_names:
                row_product *= a_row[a_name]
            result_list += [{'Multi':row_product}]
        return result_list
    
    def show_table(self, a_list_of_dictionary):
        """
        Returns the data in tabular format with a header
        """
        if a_list_of_dictionary != [] :
            lines = ""
            #Retrieves header line
            a_dictionary = a_list_of_dictionary[0]
            header_line = ""
            for key in a_dictionary:
                header_line += f'{key}\t'
            header_line = header_line.strip()
        
            lines += header_line

            for a_dictionary in a_list_of_dictionary:
                a_line = ' '
                for key,value in a_dictionary.items():
                    a_line += a_line.strip()
                    lines += f'\n{a_line}'
                print(lines)

            else:
                print("No data found")
def line_col(x, num):
    col = (x.strip().split(',')[num]).strip()
    print(col)
    return col
    
if __name__ == "__main__":
    csv_file_name = "data.csv"
    data_mgmt = DataMgmt()
    csv_file_obj = data_mgmt.get_file(csv_file_name)
    print(f"STATUS [{data_mgmt.status}]")
    if not('File Error') in data_mgmt.status:
        dict_list,values_list = data_mgmt.scan(filter=lambda line: '5' in [line_col(line,4)], has_header = False,csv_file = csv_file_obj)
        data_mgmt.close_file(csv_file_obj)
        if not ('File Error') in data_mgmt.status: data_mgmt.display_table(dict_list)




        
    
                          
