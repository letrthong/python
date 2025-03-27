import json
import os
import time
import re

class tJsonData:
    def __init__(self, name):
        self.file_path = name

    def add_item(self, item_path):
        folder_path = os.path.dirname(self.file_path)
        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            return False

        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                json_object = json.load(file)
        else:
            json_object = []

        if not os.path.exists(item_path):
            print(f"The folder '{item_path}' does not exist.")
            return False

        with open(item_path, 'r') as file:
            json_item = json.load(file)

        json_object.append(json_item)

        # Sort the array by 'epochTime'
        sorted_data = sorted(json_object, key=lambda x: x['epochTime'],  reverse=False)

        # Write the list to a file
        with open(self.file_path, 'w') as f:
            json.dump(sorted_data, f)
        return True

    # map<key,value>
    def create_item(self, items, item_path):
        epoch_time = int(time.time())

        json_object = {}
        json_object['epochTime'] = epoch_time
        
        data_oject = []
        for key, value in items.items():
            # Regular expression pattern for matching numbers (integers and floats)
            pattern = r'^-?\d+(\.\d+)?$'
            if bool(re.match(pattern, value)):
                item = {"key": key, "value" : value}
                data_oject.append(item)
           
        json_object['data'] = data_oject

        with open(item_path, 'w') as f:
            json.dump(json_object, f)

    def remove_first_item(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                json_object = json.load(file)
        else:
            json_object = []

        if len(json_object) > 0:
            json_object.pop()
        
        # Write the list to a file
        with open(self.file_path, 'w') as f:
            json.dump(json_object, f)
        return True
    
    def get_size(self):
        size_of_array = 0
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                json_object = json.load(file)
        else:
            json_object = []

        size_of_array = len(json_object)
        return  size_of_array
    
    def remove_file(self):
        try:
            os.remove(self.file_path)
            print(f"{self.file_path} has been deleted successfully.")
        except FileNotFoundError:
            print(f"{self.file_path} not found.")
        except PermissionError:
            print(f"Permission denied to delete {self.file_path}.")
        except Exception as e:
            print(f"Error occurred: {e}")
