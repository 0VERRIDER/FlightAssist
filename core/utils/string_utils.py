class StringUtils:
    def __init__(self, string):
        self.string = string

    # function to convert string to list
    def to_list(self):
        self.string = self.string.strip('][').split(', ')
        return [x.strip('\'') for x in self.string]

    
