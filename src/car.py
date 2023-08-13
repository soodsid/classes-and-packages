class car:
    def __init__(self, name, type):
        self.name = name
        self.type =type
    
    def display(self):
        print (f"the car is {self.name} type is {self.type}")
