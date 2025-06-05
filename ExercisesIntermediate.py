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

#Exercise 9: Write a function that takes a word and returns it in reverse

"""def words(word):
    return word[::-1]

print(words("louna"))""" 

#Exercise 10: Create a dictionary with 4 items and prices. Print all prices

"""pen = {"bleu_pen":"2&", "red_pen":"5&", "yelllow_pen":"8&", "green_pen":"6&"}
for key in pen:
    print(pen[key])""" #Fist way

"""for price in pen.values():
    print(price)""" #second way 

#Exercise 16: Write a function that takes a word and returns how many consonants it has

"""def count_consonants(word):
    # List of vowels
    vowels = "aeiou"
    # Start with a count of 0
    count = 0
    # Loop through each letter in the word, make it lowercase
    for letter in word.lower():
        # Check if the letter is a letter and not a vowel
        if letter.isalpha() and letter not in vowels:
            # Add 1 to count if it is a consonant
            count = count + 1
    # Return the total number of consonants
    return count

print(count_consonants("hello"))""" # loop through = iterate over and are both = sont tout les deux 

#Exercise 17: Create a dictionary with 3 students and scores. Add a new student. Print the dictionary.

"""students = {"student1":19, "student2":12, "student3":15}
students["student4"] = "16"
print(students)"""

#Exercise 18:  Import the datetime module. Print the current year

"""import datetime
current_year = datetime.datetime.now().year
print(current_year)""" # datetime allows to find the combination of a date and a time
                        # now permit to find the current datetime and .year permit to know the curent year only
 
#Exercise 20:  Create a dictionary with 4 countries and capitals. Print the country with capital“Paris”.

"""countries = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome", "Spain": "Madrid"}
for key, value in countries.items():
    if value == "Paris":
        print(key)"""
#Exercise 21:  Import the time module. Pause the program for 2 seconds

"""import time 
print("say something....")
time.sleep(2)
print("The end of my program")""" #The sleep() function takes a number of seconds to wait

#Exercise 22: Write a function that takes a word and returns it with the last letter capitalized

"""def words(word):
    return word[:-1] + word[-1].upper()
    
print(words( input("Enter something : ")))"""

#Exercise 23:  Create a class called Cat with a name attribute. Create one Cat and print its name

"""class Cat:
    def __init__(self,name):
        self.name = name

cat_1 = Cat("luna")
print(cat_1.name)"""

#Exercise 26: Create a class called Book with title and author attributes. Create one Book and print its title

"""class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

book_1 = Book("Humans","Fassia")
print(book_1.author)
print(book_1.title)"""

#Exercise 27: Import the os module. Check if a file “test.txt” exists

"""import os

file_exists = os.path.exists("test.txt")
print(file_exists)"""

#Exercise 28: Create a class called Vehicle with a method to print its type. Create one Vehicle and call the method

"""class Vehicle:
    def __init__(self,color,type):
        self.color = color
        self.type = type

    def types(self):
        return f"this car is a/an {self.type}"

vehicle_1 = Vehicle("red","toyoota")
print(vehicle_1.color)
print(vehicle_1.types())"""

#Exercise 29:Create a class called Triangle with base and height attributes. Add a method to calculate area

"""class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        result = self.base * self.height * 0.5     
        return result

triangle_1 = Triangle(5,6)
print(triangle_1.area())"""




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


#Exercise 8: Import the math module. Print the value of pi.

"""import math
value_pi = math.pi
print(value_pi)"""

#Exercise 11: Write a function that takes a list and returns only even numbers.

"""def numbers(list_num):
    even_num = []
    for num in list_num:
        if num % 2 == 0:
            even_num.append(num)
    return even_num
        
even_numf = numbers([9, 5, 2, 1, 6, 3, 8, 74, 40, 94])
print(even_numf)"""

#Exercise 12:  Try to divide two numbers from the user. Handle division by zero with try/except.
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

#Exercise 13: Import the random module. Print a random number between 10 and 20.

"""import random
numbers = random.randint(10,20)
print(numbers)"""

#Exercise 14: Write a function that takes a number and returns its square root using the math module

"""def numb_square(n):
    import math
    return math.isqrt(n)

print(numb_square(int(input("Enter a number: "))))"""

#Exercise 15: Create a set with 5 numbers. Find the difference with another set of 3 numbers

"""s1 = {85, 74, 52, 4, 12}
s2 = {12, 85, 45}
s3 = s1 - s2
print(s3) """ # Here I can also use the funtion s1.difference(s2) to solve this problem
                #s1 - s2: The - operator finds the difference, returning a new set 
                # with numbers that are in s1 but not in s2 and also numbers are in 
                # s2 but not in s1

#Exercise 19: Write a function that takes a list and returns it sorted in descending order

"""def numbers(list):
    return sorted(list,reverse = True)
print(numbers([9, 5, 2, 1, 6, 3, 8, 74, 40, 94]))"""
#here sorted() allows me to have a new sort out list and reverse permits me to have the
#  descending order with True an ascending order with False 

#Exercise 24: Write a function that takes a list and returns a new list with all numbers doubled.

"""def double(l):
    nl = []
    for element in l :
        mult = element *2
        nl.append(mult)
    return nl
    
print(double([9, 5, 2, 1, 6, 3, 8, 74, 40, 94]))"""

#Exercise 25: Write a function that takes a list and returns a new list with all numbers duplicated.

"""def duplicate(l):
    nl = []
    for element in l:
        nl.append(element)
        nl.append(element)
    return nl

print(duplicate([9, 5, 2, 1, 6, 3, 8, 74, 40, 94]))"""