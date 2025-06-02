#Author : Fassiatou OUANRE
#This is my collection of Python training exercises for intermediate level.
#These exercises are written in simple English for beginners.
#Because my native language is French, and I am still learning English,
#But my English in this file is an improvement over my first file (BeginnerExercises).

"""After these exercises I will be able to do any project I want in python """      

                                #These exercises focus on working with characters.


#Exercise 1: Write a function that prints “Python is fun!”.

"""def fun():
    print("Python is fun!")
fun()"""

#Exercise 5: Write a function that takes a word and returns if it has more than 5 letters

"""def words(word):
    length = len(word)
    if length > 5 :
        return True
    else:
        return False
    
truth =words(word = input("Enter a word: "))
print(truth)""" # Here I use len to know the number of letter in a word

#Exercise 6: Create a dictionary with 3 names and phone numbers. Print all names.

"""contacts = {"Fassia":78458925, "OUANRE":89456312, "Brad":25469684796}
for key in contacts:
    print(key,contacts[key])"""

#Exercise 8: Write a function that takes a word and returns it in reverse

"""def words(word):
    return word[::-1]

print(words("louna"))""" 

#Exercise 9: Create a dictionary with 4 items and prices. Print all prices

pen = {"bleu_pen":"2&", "red_pen":"5&", "yelllow_pen":"8&", "green_pen":"6&"}
"""for key in pen:
    print(pen[key])""" #Fist way

"""for price in pen.values():
    print(price)""" #second way 








































































































                                #These exercises focus on working with numbers

#Exercise 2:  Write a function that takes a number and returns its triple.

"""def numbers(num):
    return  num*3
triple = numbers(3)
print(triple)"""

#Exercise 3: Write a function that takes two numbers and returns their difference.
"""def numbers(num1,num2):
    return num1 - num2
dif = numbers(2,3)
print(dif)"""

#Exercise 4:  Write a function that takes a list and returns its length.
"""def function(l):
    return len(l)

t = function([1, 3, 8, 9])
print(t)"""

#Exercise 7: Write a function that takes a number and returns if it is odd

"""def cheiknum(num):
    if num % 2 == 1:
        return True
    else:
        return False

value = cheiknum(3)
print(value)""" #Here is the first way to output the result with for loop

"""def cheiknum(num):
    return num % 2 == 1

print(cheiknum(4))""" #Here is the second way to solve this exercise
                    #If the result of my exercise should be True or False
                    #I can just write return plus the condition 


#Exercise 7: Import the math module. Print the value of pi.

"""import math
value_pi = math.pi
print(value_pi)"""

#Exercise 9: Write a function that takes a list and returns only even numbers.

"""def numbers(list_num):
    even_num = []
    for num in list_num:
        if num % 2 == 0:
            even_num.append(num)
    return even_num
        
even_numf = numbers([9, 5, 2, 1, 6, 3, 8, 74, 40, 94])
print(even_numf)"""

#Exercise 10:  Try to divide two numbers from the user. Handle division by zero with try/except.
"""while True:
    try:
        num1 = int(input("Enter a first number: "))
        num2 = int(input("Enter a second number: "))
        try :   
            div = num1/num2
            print(div)
            break
        except ZeroDivisionError:
            print("Zero is not an avaible num,enter an other num")  
    except ValueError:
        print("Enter only number ")"""

#Exercise 11: Import the random module. Print a random number between 10 and 20.

import 
