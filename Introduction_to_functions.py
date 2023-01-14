import os

#To clear the terminal before running
os.system('cls')

#Making a function
def test_function():
    print('hello')
    test = 1 + 2
    print(test)

#Making a simple calculater function
def calculater(num1,num2):
    if option == '+':
        result = num1 + num2
    if option == '-':
        result = num1 - num2
    if option == '*':
        result = num1 * num2
    if option == '/':
        result = num1 / num2

    print (result)

#Asking for the operator
option = input('what do you want to do') 

#calling out the calculater function
calculater(10,9)

#calling out the test function
test_function()