from colorama import Fore, Back, Style 
import os
import sys
from input import input_to,Get
from layout import *
from paddle import *
from ball import *
from brick import *
from config import *
import time
#setting layout
l1 = layout(20,75)
p1 = paddle(24,4)
b1 = ball()
def time_convert(sec):
  mins = round(sec // 60,2)      # // is for floor division
  sec = round(sec % 60,0)
  hours = round(mins // 60,2)
  mins = round(mins % 60,2)
  print("Time = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def initialize():
    level = l1.level
    for i in range(0,15):
        for j in range(0,15):
            arr[i][j]=' '
    #b1
    
    for j in range(4,6+level):
       list_b1.append(b1brick(3,j))
       if active_arr[3][j]=='1':
            arr[3][j]='b1'
    #wall and explosion
    
    for j in range(4,6+level):
        if j%2 == 0 :
            list_w.append(wbrick(4,j))
            if active_arr[4][j]=='1':
                arr[4][j]='w'
        else :
            list_d.append(dbrick(4,j))
            if active_arr[4][j]=='1':
                arr[4][j]='d'
    #b2
    
    for j in range(4,6+level):
       list_b2.append(b2brick(5,j))
       if active_arr[5][j]=='1':
        arr[5][j]='b2'
    #b3
    
    for j in range(4,6+level):
       list_b3.append(b3brick(6,j))
       if active_arr[6][j]=='1':
            arr[6][j]='b3'
    
    #paddle
    for j in range(p1.x,p1.x+p1.length):
        arr[14][j] = '_'

    #ball
    if arr[b1.x][b1.y] == ' ':
        arr[b1.x][b1.y] = 'b'
    else :
        arr[b1.x][b1.y] = 'b'+arr[b1.x][b1.y]

def ball_update(p,q=-10):
    b1.y = p
    if q!=-10:
        b1.x = q

def move_ball():
    #collision with b3
    incf = 0
    for obj in list_b3 :
        if(obj.x == b1.x and obj.y == b1.y and active_arr[b1.x][b1.y]=='1'):
            if incf == 0:
                l1.increase_score(obj.score)
                incf =1
            b1.vx = 1
            active_arr[b1.x][b1.y]='0'
    #collision with b2
    incf = 0
    for obj in list_b2 :
        if(obj.x == b1.x and obj.y == b1.y and active_arr[b1.x][b1.y]=='1'):
            if incf == 0:
                l1.increase_score(obj.score)
                incf =1
            b1.vx = 1
            active_arr[b1.x][b1.y]='0'
    #collision with b1
    incf = 0
    for obj in list_b1 :
        if(obj.x == b1.x and obj.y == b1.y and active_arr[b1.x][b1.y]=='1'):
            if incf == 0:
                l1.increase_score(obj.score)
                incf =1
            b1.vx = 1
            active_arr[b1.x][b1.y]='0'
    #wall brick
    for obj in list_w :
        if(obj.x == b1.x and obj.y == b1.y and active_arr[b1.x][b1.y]=='1'):
            b1.vx = 1
    #destroy brick
    incf = 0
    for obj in list_d :
        if(obj.x == b1.x and obj.y == b1.y and active_arr[b1.x][b1.y]=='1'):
            if incf == 0:
                l1.increase_score(320)
                incf =1
            b1.vx = 1
            active_arr[b1.x][b1.y]='0'
            active_arr[b1.x+1][b1.y]='0'
            active_arr[b1.x-1][b1.y]='0'
            active_arr[b1.x][b1.y+1]='0'
            active_arr[b1.x+1][b1.y+1]='0'
            active_arr[b1.x-1][b1.y+1]='0'
            active_arr[b1.x][b1.y-1]='0'
            active_arr[b1.x+1][b1.y-1]='0'
            active_arr[b1.x-1][b1.y-1]='0'

    #meeting the top wall collision
    if b1.x <=0 :
        b1.vx = 1
    #meeting the paddle collision
    if b1.x == 14 :
        if b1.y == p1.x:
            b1.vx = -1
            b1.y-=1
            
        elif b1.y ==p1.x+1 :
            b1.vx = -1
            b1.y-=1
            
        elif b1.y ==p1.x+2 :
            b1.vx = -1
            b1.y+=1
            
        elif b1.y ==p1.x+3:
            b1.vx = -1
            b1.y+=1
            
        else :
            l1.decrease_life()
            b1.vx = -1
    if b1.x >=0 :
        b1.x+=b1.vx

    
def print_screen():
    print(l1.print_navbar(),end = " ")
    print(" TIME : ", end= " ")
    time_convert(t3)
    print("W/w to exit!!!                                            X/x to start the ball shoot!")
    print("A/a to move paddle to left                              D/d to move paddle to right  ")
    print("L/l to go to next level")
    print("--------------------------------------------------------------------------------------")
    for i in range(0,15):
        for j in range(0,15):
            flag = 0
            if arr[i][j]=='b1':
                print(Back.BLUE+'b'+Style.RESET_ALL,end='')
                flag =1
            if arr[i][j]=='b2':
                print(Back.GREEN+'b'+Style.RESET_ALL,end='')
                flag =1
            if arr[i][j]=='b3' and active_arr[i][j]=='1':
                print(Back.CYAN+'b'+Style.RESET_ALL,end='')
                flag =1
            if arr[i][j]=='w':
                print(Back.RED+'w'+Style.RESET_ALL,end='')
                flag =1
            if arr[i][j]=='d':
                print(Back.YELLOW+'d'+Style.RESET_ALL,end='')
                flag =1
            if arr[i][j] =='b' or arr[i][j]=='bb1' or arr[i][j]=='bb2' or arr[i][j]=='bb3' or arr[i][j]=='bw' or arr[i][j]=='bd' or arr[i][j]=='b_':
                print(Back.WHITE+Fore.BLACK+'*'+Style.RESET_ALL,end = '')
                flag =1
            if flag == 0 :
                print(arr[i][j],end='')
        print()

if __name__ == '__main__':
        start_time = time.time()
        while(1):
            t3 = time.time()- start_time
            initialize()
            print_screen()
            #takes input of character from the keyboard
            get_char = Get()
            ch = input_to(get_char)
            #move left
            if(ch == 'a' or ch == 'A'):
                if p1.x>0 :
                    p1.x-=1
                    if f == 0:
                        ball_update(p1.x)
            #move right
            if(ch == 'd' or ch == 'D'):
                if p1.x<11:
                    p1.x+=1
                    if f == 0:
                        ball_update(p1.x)
            #to exit
            if(ch == 'w' or ch == 'W'):
                os.system('clear')
                print("GAME OVER !! ")
                print("LEVEL FINISHED",end = " ")
                print(l1.level)
                print(" TIME : ", end= " ")
                time_convert(t3)
                print("LIFE : ",end=" ")
                print(l1.get_life())
                print("SCORE : ",end = " ")
                print(l1.get_score())
                print()
                break
            #to go to next level
            if(ch == 'l' or ch == 'L'):
                l1.level = l1.level + 1
                active_arr = [['1' for i in range(col)] for j in range(row)]  
            if(l1.level == 4):
                print("GAME OVER !! ")
                print("all levels completed!")
                print(" TIME : ", end= " ")
                time_convert(t3)
                print("LIFE : ",end=" ")
                print(l1.get_life())
                print("SCORE : ",end = " ")
                print(l1.get_score())
                print()
                break
            #to start the ball
            if(ch == 'x' or ch == 'X'):
                b1.vx = 1
                f = 1
            if f ==1 :
                move_ball()
            os.system('clear')
            if(l1.get_life() == 0):
                print("GAME OVER !! ")
                print("LEVEL FINISHED",end = " ")
                print(l1.level)
                print(" TIME : ", end= " ")
                time_convert(t3)
                print("sec")
                print("LIFE : ",end=" ")
                print(l1.get_life())
                print("SCORE : ",end = " ")
                print(l1.get_score())
                print()
                break
            