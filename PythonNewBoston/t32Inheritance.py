class Parent():
    
    def print_last_name(self):
        print('Roberts')
        
class Child(Parent):
    
    def print_first_name(self):
        print('Bucky')

    def print_last_name(self):
        super(Child, self).print_last_name() # Example of appending by calling the super() function first
        print('Fucker')
        
        
bucky = Child()
bucky.print_first_name()
bucky.print_last_name()