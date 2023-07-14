import os
import filereader as fr

class ReadFiles:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        
    # function to read all files in a directory and return as a dictionary
    def read(self):
        try:
            file_list = os.listdir(self.dir_path)
            data = {}

            for file_name in file_list:
              file = fr.ReadFile(self.dir_path + '/' + file_name)
              name = file_name.split(".")[0]
              ext = file_name.split(".")[-1]
              data[name] = {
                  "data" : [line.strip() for line in file.readline()],
                  "type" :  ext,
                  }
            return data
        except FileNotFoundError:
            print("Directory not found")
            return None
        except Exception as e:
            print("Error while reading files: ", e)
            return None

    #function to count files in a directory
    def count(self):
      try:
        return len(os.listdir(self.dir_path))
      except FileNotFoundError:
            print("Directory not found")
            return None
      except Exception as e:
            print("Error while reading file: ", e)
            return None