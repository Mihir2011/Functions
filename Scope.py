import os

#To clear the terminal before running
os.system('cls')

#This is a Global variable
a = 10

def test_func():

    #this a variable is local so that means it will not work out of this function and python makes another a variable
    a = 2
    print(a)

def test_func2():
    
    #Now this a variable is different too as its in another function which also means its local and will print seperatly
    a = 200
    print(a)

#Calling out test_func
test_func()

#Calling out test_func2
test_func2()    
