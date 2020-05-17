import copy
import random
import os
print("THE GAME OF 2048")
print("***GAME IS STARTING***")
boardsize=int(input("enter your game board size:"))
v=int(input("enter the winning tile:"))

def newvalue():
    return 2
def nextnum():
    row=random.randint(0,boardsize-1)
    col=random.randint(0,boardsize-1)
    
    while not board[row][col]==0:
        row=random.randint(0,boardsize-1)
        col=random.randint(0,boardsize-1)
    board[row][col]=newvalue()    
board=[[0 for x in range(boardsize)] for y in range(boardsize)]
inival=1
row=random.randint(0,boardsize-1)
col=random.randint(0,boardsize-1)
while inival>0:
    if board[row][col]==0:
       board[row][col]=newvalue()
       inival-=1
#here is the formation of board
def display():
    l=board[0][0]
    for row in board:
        for item in row:
            if item>l:
                l=item
    maxS=len(str(l))
    for row in board:
        line='|'
        for item in row:
            if item==0:
                line+=' '*maxS+'|'
            else:
                line+=(' '*(maxS-len(str(item))))+str(item)+'|'
        print(line)
    
#here it is merging left

def tninrow(row):
    count=0
    for i in row:
        if i!=0:
            count+=1
    return count        
    
def merge1row(row):
    for j in range(tninrow(row)):
        
        for i in range(boardsize-1,0,-1):
            if row[i-1]==0:
                row[i-1]=row[i]
                row[i]=0
    
    
    for i in range(boardsize-1):
        if row[i]==row[i+1]:
            row[i]=row[i]*2
            row[i+1]=0 
    for i in range(boardsize-1,0,-1):
            if row[i-1]==0:
                row[i-1]=row[i]
                row[i]=0        
    return row        
def merge_left(currentboard):
    for i in range(boardsize):
        currentboard[i]=merge1row(currentboard[i])
    return currentboard
#this is merging right    
    
def reverse(row):
    revrow=[]
    for i in range(boardsize-1,-1,-1):
        revrow.append(row[i])
    return revrow 
def merge_right(currentboard):
    for i in range(boardsize):
        currentboard[i]=reverse(currentboard[i])
        currentboard[i]=merge1row(currentboard[i])
        currentboard[i]=reverse(currentboard[i])
    return currentboard 
 
def transpose(currentboard):
    temp=[[0 for x in range(boardsize)] for y in range(boardsize)]
    for i in range(boardsize):
        for j in range(boardsize):
            temp[j][i]=currentboard[i][j]
           
    return temp
#merge up
def merge_up(currentboard):
    currentboard=transpose(currentboard)
    currentboard=merge_left(currentboard)
    currentboard=transpose(currentboard)
    
    return currentboard
def merge_down(currentboard):
    currentboard=transpose(currentboard)
    currentboard=merge_right(currentboard)
    currentboard=transpose(currentboard)
    
    return currentboard
#winner is declared
def won():
    for row in board:
        for item in row:
            if item==v:
                return True
    return False 
#loser is declared    
def lose():
    b1=copy.deepcopy(board)
    b2=copy.deepcopy(board)
    b1=merge_up(b1)
    if b1==b2:
        b1=merge_down(b1)
        if b1==b2:
            b1=merge_left(b1)
            if b1==b2:
                b1=merge_right(b1)
                if b1==b2:
                    return True
    return False                
    
print("here is your game board:")    
display()

gameover=False
while not gameover:
    m=str(input("write letter to move:"))
    os.system('clear')
    correctinput=True
    dupliboard=copy.deepcopy(board)
    if m =="w":
       board=merge_up(board)
        
        
    elif m =="s":
       board=merge_down(board)
        
    elif m =="a":
       board=merge_left(board)
       
        
    elif m =="d":
       board=merge_right(board)
        
        
    else:
       correctinput=False
    
    if not correctinput:
        print("your input was wrong,Please try again:")
        display()
    else:
        if won():
            display()
            print("You Win by luck.XD!!!")
            gameover=True
        else:    
            nextnum()
            display()
            if lose():
                print("sorry, you lost you dont have more moves to play")
                gameover=True
      
        
        
   






  






 


    









    
     
