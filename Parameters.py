import os

#to clear the terminal before running
os.system('cls')

#Giving the parameters their values and arg stands for argument
def text_function(arg1,arg2,arg3,arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

#Its not needed to put arg1 = 1 or arg2 = 'hello' its just so the code doesn't get messy
text_function(arg1 = 1,arg2 = 'hello',arg3 = True,arg4 = ['1',2,'test'])

#Another way of organizing the code is to make it like this
text_function(
    arg1 = 1,
    arg2 = 'hello',
    arg3 = True,
    arg4 = ['1',2,'test'])

#Simple welcome codes
def greeter(person = 'Person', greet = 'Hello', weekday = 'Monday'):
    print(f'{person} {greet}')
    print(f'It is {weekday}')

#To excecute the function we made above
greeter('Bob', weekday = 'Sunday')