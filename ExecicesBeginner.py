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


# Exercice 5 : Ask the user for a number. Print if it is even or odd.

"""while True :
    try :
        numb = int(input("enter a number: "))
        remainder = numb % 2 
        if remainder == 0 :
            print(f"{numb} is even")
        else : 
            print(f"{numb} is odd")
        break
    except ValueError :
        numb = print("please enter a number only ")""" #here try-except help me to corect the ValueError
                                                    #when the user put a letter instead of a number 
                                        #but when my code print the message I put in my except,it finish after
                                        #so I use while to ask again the user if he do that 
                                        #and break permit me to exit in the loop
 

# Exercice 6 : Print numbers from 1 to 6 using a for loop.

"""for n in range(1,7) : 
    print(n)"""


# Exercice 7 : Print numbers from 5 to 1 using a while loop

"""num = 5
while num >= 1 : 
    print(num)
    num = num -1"""

# Exercice 8 : Ask the user for a number. Print if it is positive or negative

"""while True:
    try : 
        num = float(input("give me a number: "))
        if num > 0 : 
            print(f"{num} is a positive number")
        elif num < 0 : 
            print(f"{num} is a negative number") 
        else : 
            print(f"{num} is zero")
        break
    except ValueError :
        print("please enter a number only")"""

# Exercice 9 : Create a list with 3 fruits. Print the list.

"""l = ["mangoes","oranges","banana"]
print(l)"""

# Exercice10:Create a tuple with 4 colors. Print the tuple.
"""t = ("black","yellow","red","white")
print(t)"""

# Exercice11: Ask the user for a number. Print its square using a for loop.
"""num = input("enter a number ")
num = int(num)
square = pow(num,2)
print(f"the scare of {num} is {square}")""" #here I on't think I need to use loop
                                        #to resolve this exercise

# Exercice 12: Print all odd numbers from 1 to 9 using a for loop
"""for n in range(1,10): 
    remainder = n % 2
    if remainder == 1: 
        print(n, end="")""" #here I use end = "" to print the results in the same line

# Exercise 13: Ask the user for a word. Print each letter on a new line using a for loop
"""word = input("input a sentence ")
for element in word:
    print(element)"""

# Exercise 14: Create a list with 5 numbers. Print the last number.
"""l = [1,2,3,5]
print(l[0])"""

# Exercise 15: Create a tuple with 3 animals. Print the first animal.
t = ("cat","boat","mouse")
print(t[0])

 



