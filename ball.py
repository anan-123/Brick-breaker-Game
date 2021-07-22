from colorama import Fore, Back, Style 
class ball:
    def __init__(self):
        self.vx = -1
        self.vy = 0
        self.x = 14
        self.y = 0
    def change_x_ball(self,q):
        self.x+=q
    def change_y_ball(self,q):
        self.y+=q
    