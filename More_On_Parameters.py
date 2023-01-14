import os

#Clearing the terminal before running the script
os.system('cls')

#List unpacking
def print_all(*arguments):
    
    #Print all arguments
    for argument in arguments:
        print(argument)

#keuword unpacking
def print_more(**arguments):
    print(arguments)

#Keyword and List unpacking
def print_even_more(*args, **kwargs):
    print(args)
    print(kwargs)

#Printing the list
print_all([1,2,3,4,5,'hello',1,3,213,321,3,123,123,12,])

#Printing the keyword
print_more(arg1 = '1', arg2 = 'test', arg3 = [1,2,3])

#Printing keywords and lists 
print_even_more(1,2,3,4,5,43,43,324,54,'hello', 'anything', 'everything can get printed',True,test = 1, test2 = 5)