from colorama import Fore, Back, Style 
class brick:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.active = 1     #brick exists or not
#power up class 
class pbrick(brick):
    def __init__(self,x,y):
        brick.__init__(self,x,y)
        self.score = 0
        self.powerup = 1

#colored bricks : 
class b1brick(brick):
    def __init__(self,x,y):
        brick.__init__(self,x,y)
        self.score = 30

class b2brick(brick):
    def __init__(self,x,y):
        brick.__init__(self,x,y)
        self.score = 20

class b3brick(brick):
    def __init__(self,x,y):
        brick.__init__(self,x,y)
        self.score = 10

#destroy adjascent bricks: 
class dbrick(brick):
    def __init__(self,x,y):
        brick.__init__(self,x,y)
        self.score = 60
        self.color = 'YELLOW'
#wall bricks: 
class wbrick(brick):
    def __init__(self,x,y):
        brick.__init__(self,x,y)
        self.score = 100
        self.color = 'BLUE'
        

