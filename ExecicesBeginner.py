#Author : Fassiatou OUANRE
#this is my python training exercices
#these exercices are done in simple enghish for beginner
#because my mother tongue is french and I'm learning english

"""my goal is to start with simple exercices and progress to more dificult ones. 
 as I want to develop strong python skills. This will help me to undertand
 and create advanced AI programs"""

                                        # Biginner Exeercices (1-50)

# Exercise 1 : Print "Learn Python" on the screen 

"""print("Learn Python")"""

# Exercise 2 :Ask the user for their name. Print “Hello, [name]!”.

"""name = input("what's your name? ")
print(f"hello, {name}!")"""

# Exercise 3 : Ask the user for a number. Print the number tripled

"""numb = input("give me a number: ")
numb_int = int(numb)
numb_result = numb_int*3
print(f"the number is : {numb_result}")"""

# Exercice 4 : Ask the user for two numbers. Print their sum

"""numb_first = int(input("inter a first number : "))
numb_second = int(input("inter a second number : "))
sum = numb_first + numb_second
print(f"the sum is : {sum}")""" #fist way to resolve this problem

"""numb = input("enter 2 numbers: ")
x,y = numb.split()
x= int(x)
y= int(y)
sum = x+y 
print(f"the sum is : {sum}")""" #the second way to resolve this exercice but here when 
                                #I put numbers and I don't separat them by spaces I get a ValueError, 
                                #so you must to saparat numbers by spaces.


