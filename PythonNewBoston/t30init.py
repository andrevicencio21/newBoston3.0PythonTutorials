class Tuna:
    
    def __init__(self): #Think of this like a constructor in Java
        print('Blrbblrblrbbllr\n')
    
    def swim(self):
        print('I am swimming\n')

flipper = Tuna()
flipper.swim()

# Useful case of init
class Enemy():
    
    def __init__(self, x):
        self.energy = x
    
    def get_energy(self):
        print(self.energy)

jason = Enemy(20)
sandy = Enemy(40)
jason.get_energy()
sandy.get_energy()
        