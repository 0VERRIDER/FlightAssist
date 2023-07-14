import json

class ReadFile:
    def __init__(self, file_path):
        self.file_path = file_path

    # function to read file
    def read(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read()

        except FileNotFoundError:
            print("File not found")
            return None
        except Exception as e:
            print("Error while reading file: ", e)
            return None  

    # function to read file line by line
    def readline(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
                
        except FileNotFoundError:
            print("File not found")
            return None
        except Exception as e:
            print("Error while reading file: ", e)
            return None

    # function to read json file
    def read_json(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
                
        except FileNotFoundError:
            print("File not found")
            return None
        except Exception as e:
            print("Error while reading file: ", e)
            return None