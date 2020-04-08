import time
import random




print("Think of a number between 1-100. You will have 5 seconds to do this. This computer will start guessing and you have to say if the number is too high, too low, or correct.")
time.sleep(1)
global y
y=50
g=0
global x
x=input(y)
while x != "correct":
    if x != "too low" and x != "too high":
        print("proper format please")
        break
    if x == "too low":
        g+=1 
        y = y+random.randint(1,4)
        x = input(y)
    if x== "too high":
        g+=1
        y=y-random.randint(1,4)
        x = input(y)
  
    
    
    
    
    
    
    
    '''
    
    
    if x=="too high":
        g=g+1
    y=y-5
    x=input(y)
    continue
    if x=="too low":
        g=g+1
    y=y+1
    x=input(y)
    continue
    '''


if x == "correct":
    print("That took me " +str(g)+ " guesses.")
        
        
        
        
        
        
    

