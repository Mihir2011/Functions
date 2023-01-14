import os 

#To clear the terminal before running
os.system('cls')

#This is a basic Lambda Code in a variable so we can call it by doing print(a(with some value)) as shown bellow
a = lambda x: x + 1

#This is an example to print a lambda function here 10 is the origanal vaule x for us in this case
print(a(10))

#this is a bit more complex lambda function which will add the numbers you give it
simple_calculater = lambda a,b: a + b

#Here 2 and 3 are the number i want to add but you can add any number
print(simple_calculater(2,3))



