from colorama import Fore, Back, Style 
class paddle:
    def __init__(self,h,len):
        self.length = len       #length
        self.x = 0              #x coordinate
    def change_x_paddle(self,q):
        self.x+=q
    def x_paddle(self):
        return self.x
    def change_paddle_length(self,l):
        self.length = l
    def return_paddle_length(self):
        return self.length

        

       
