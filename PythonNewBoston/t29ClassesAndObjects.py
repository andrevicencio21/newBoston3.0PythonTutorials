class Enemy:
    life = 3
    
    def attack(self): #self is like 'this' in Java, but not as a construction like java, self is default first argument in a class function
        print('ouch!\n')
        self.life -= 1
    
    def checkLife(self):
        if self.life <= 0:
            print('enemy dead!\n')
        else:
            print(str(self.life), "life left!\n")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()
