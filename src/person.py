class person:
    def __init__(self, firstname,lastname):
        self.first=firstname
        self.last=lastname
    
    def display (self):
        print (f"the name is {self.first} and the lastname is {self.last}")