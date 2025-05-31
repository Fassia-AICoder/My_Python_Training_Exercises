#Author : Fassiatou OUANRE
#this is my python training exercises
#these exercises are done in simple enghish for beginner
#because my mother tongue is french and I'm learning english

"""my goal is to start with simple exercises and progress to more dificult ones. 
 as I want to develop strong python skills. This will help me to undertand
 and create advanced AI programs"""



                                        # Exercises with letters


# Exercise 1 : Print "Learn Python" on the screen 

"""print("Learn Python")"""

# Exercise 2 : Ask the user for their name. Print “Hello, [name]!”.

"""name = input("what's your name? ")
print(f"hello, {name}!")"""

# Exercise 9 : Create a list with 3 fruits. Print the list.

"""l = ["mangoes","oranges","banana"]
print(l)"""

# Exercise 10 : Create a tuple with 4 colors. Print the tuple.

"""t = ("black","yellow","red","white")
print(t)"""

# Exercise 13 : Ask the user for a word. Print each letter on a new line using a for loop
"""word = input("input a sentence ")
for element in word:
    print(element)"""

# Exercise 15 : Create a tuple with 3 animals. Print the first animal.
"""t = ("cat","boat","mouse")
print(t[0])"""


# Exercise 17 :Create a list with 4 names. Add a new name. Print the list
"""l = ["fassia","ssifa","K_FA","smoochi"]
l.append("oulfa")
print(l)"""

# Exercise 22: Ask the user for a word. Print how many letters it has.

"""word = input("Enter a word you want ")
if  word.strip() and word.isalpha():
    count = 0
    for element in word: 
        count = count + 1
    print(count)
else:
    print("Please!!! Enter a another word without space and numbers")""" #here I can just count only word without sentence but 
                                                                    #if I delete the condition if I can count all charecter I put.
                                                                   
"""sentence = input("Enter a sentence: ")
letter_count = 0
for char in sentence:
    if char.isalpha():
        letter_count = letter_count + 1
print(letter_count) """                                                                 
                    # Here I can count the number of letters in a sentence excluding other character
                    

# Exercise 23 : Create a set with 3 numbers. Print the set.
"""s = {"A", "B", 4}
print(s)""" #Here If you make a set with {1, 2, 2, 3}, it becomes {1, 2, 3} (the extra 2 is removed).
            #It Doesn’t care about the order of item, for exemple {1, 2, 3} might print as {2, 1, 3} or {3, 1, 2}
            #You can’t change items in a set like you can with a list (e.g., my_list[0] = 10). Instead, you add or remove items.

# Exercise 27 : Create a tuple with 4 cities. Print the second and third city
"""t = ("Burkina", "Togo", "Ghana", "Ivoir")
print(t[1], t[2])"""

# Exercise 28 : Ask the user for a word. Print it 4 times using a while loop.

"""word = input("Input a word you want ")
count = 1
while count<=4 :
    print(word)
    count = count +1"""

# Exercise 31 : Create a set with 4 fruits. Add one fruit,remove one fruit and Print the set.
"""s = {"mango", "banana","orange", "strawberie"}
s.add("tomato")
s.discard("orange")
print(s)"""    #Here I can use add() to put one item in the set.
            #Use remove() to take an item out (raises an error if the item isn’t there).
            #Use discard() to remove an item safely (no error if it’s not there).

#Exercise 33 : Create a list with 3 colors. Replace the first color with “red”. Print the list

"""l = ["black","yellow","red","white"]
l[0]="red"
print(l)"""

#Exercise 37 : Ask the user for a word. Print the last letter using a for loop.
"""word = input("Give me a letter you want: ")
for letter in word :
    letter = word[-1]
print(letter)"""

#Exercise 37 : Create a list with 4 animals. Print the list in reverse order.
"""l = ["cat", "dog", "chicken", "goat"]
print(l[::-1])""" #first way to resolve this exercise.
                #The syntax list[start:end:step] with step = -1 reverses the list.
                #No start or end means the entire list ([:]), and -1 step reverses it.~

"""l = ["cat", "dog", "chicken", "goat"]
l.reverse()
print(l)""" #the second way with using reverse method 

#Exercise 43 : Ask the user for a word. Check if it starts with “s” using if.
"""word = input("Input a word you want: ")
first_letter = word[0]
if first_letter == "s":
    print(f"{word} starts with s")
else:
    print(f"{word} don't starts with s")"""

#Exercise 34 : Create a tuple with 3 fruits. Print how many fruits are in the tuple

"""fruits = ("banana", "orange", "apple")
l= len(fruits)
print(l)"""


















                                         # Exercises with numbers



# Exercise 3 : Ask the user for a number. Print the number tripled

"""numb = input("give me a number: ")
numb_int = int(numb)
numb_result = numb_int*3
print(f"the number is : {numb_result}")"""

# Exercise 4 : Ask the user for two numbers. Print their sum

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


# Exercise 5 : Ask the user for a number. Print if it is even or odd.

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
 

# Exercise 6 : Print numbers from 1 to 6 using a for loop.

"""for n in range(1,7) : 
    print(n)"""

# Exercise 7 : Print numbers from 5 to 1 using a while loop

"""num = 5
while num >= 1 : 
    print(num)
    num = num -1"""

# Exercise 8 : Ask the user for a number. Print if it is positive or negative

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


# Exercise 11 : Ask the user for a number. Print its square using a for loop.
"""num = input("enter a number ")
num = int(num)
square = pow(num,2)
print(f"the scare of {num} is {square}")""" #here I don't think I need to use loop
                                        #to resolve this exercise


# Exercise 12 : Print all odd numbers from 1 to 9 using a for loop
"""for n in range(1,10): 
    remainder = n % 2
    if remainder == 1: 
        print(n, end="")""" #here I use end = "" to print the results in the same line


# Exercise 14 : Create a list with 5 numbers. Print the last number.
"""l = [1,2,3,5]
print(l[0])"""

# Exercise 15 : Create a tuple with 3 animals. Print the first animal.
"""t = ("cat","boat","mouse")
print(t[0])"""

# Exercise 16 : Ask the user for a number. Print numbers from 1 to that number using a while loop

"""num = int(input("enter a numb "))
firstnum = 1
while firstnum <= num :
    print(firstnum)
    firstnum = firstnum + 1"""
  
 
# Exercise 18 : Ask the user for a number. If it is more than 50, print “Big”. Else, print “Small”
"""numb = int(input("Enter a number "))
if numb > 50 : 
    print("this number is big")
else : 
    print("this number is small")"""

# Exercise 19 : Print numbers from 1 to 8. Stop at 4 using break.
"""for i in range(1,9) : 
    print(i)
    if i == 4 :
        break"""

# Exercise 20 :Print numbers from 1 to 8. Skip 6 using continue.
"""for i in range(1,9) : 
    if i == 6 :
        continue
    print(i)"""

# Exercise 21 : Create a list with 5 numbers. Print their sum using a for loop
"""l = [9,56,99,145,7963]
s = sum(l)
print(s)""" #Here I did the sum of the list without using for
            #(it's the normal way to do the sum of list)

"""l = [9, 56, 99, 145, 7963]      l = [9, 56, 99, 145, 7963] 
s = 0                           s = 0                       
for element in l:               for element in l:           
    s = s + element                 s = s + element          
    print(s)                    print(s)          """        
                                                        #this two code give 2 different ouput because in the
                                                        #first code the print is inside the for, that mean
                                                        #each time it do a sum it print the result.
                                                        #But the second code the print is in the same
                                                        #Indentation(outside the for) that mean it do the
                                                        #sum and give after the total result


# Exercise 24: Ask the user for a number. Print its multiplication table (1 to 10) using a for loop.
"""try:
    num = int(input("Enter a number "))
    for i in range(1,11):
        mult = num*i
        print(f"{i} * {num} = {mult}")
except ValueError :
    print("Enter only an integer")"""

# Exercise 25:  Create a list with 5 numbers. Print the smallest number.
"""l = [5, 0, -1, 7, -69]
smallest = min(l)
print(f"the smallest number is: {smallest}")"""


# Exercise 26: Ask the user for a number. Print if it is divisible by 5 using if.

"""num = int(input("Enter a number "))
div = num % 5
if div == 0 :
     print(f"{num} is divisible by 5")
else:
     print(f"{num} is not divisible by 5")"""


 # Exercise 29 : Create a list with 5 numbers. Remove the first number. Print the list.
     
"""l = [5, 0, -1, 7, -69]
del l[0]
print(l)"""

#Exercise 30 : Ask the user for a number. Print all even numbers up to it using a for loop
"""try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Please enter a non-negative number.")
    else:
        for i in range(0, num + 1, 2):
            print(i)
except ValueError:
    print("Please enter a valid integer.")"""

#Exercise 32 : Ask the user for a number. If it is between 1 and 10, print “Valid”. Else, print “Invalid”
"""while True:
    try:
        num = int(input("Enter a number between 1 and 10: "))
        if 1<=num<=10 :
            print(f"{num} is valid")
        else:
            print(f"{num} is invalid")
        break
    except ValueError:
        print("please!!! Enter a number between 1 and 10")"""

#Exercise 34 : Print numbers from 1 to 15. Skip multiples of 3 using continue
"""for i in range(1,15):
    if i % 3 == 0:
        continue
    print(i)"""

#Exercise 35 : Ask the user for a number. Print its factorial using a while loop.


"""try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Please enter a non-negative number (factorial is not defined for negative numbers).")
    else:
        factorial = 1
        counter = 1
        while counter <= num:
            factorial *= counter
            counter += 1
        print(factorial)
except ValueError:
    print("Please enter a valid integer.")"""

#Exercise 36 : Create a tuple with 5 numbers. Print the product of all numbers

"""t = (1, 8, 2, 6, 3)
p = 1 
for element in t:
     p = p * element
print(p) """           #first way to do this exercise

"""t = (1, 8, 2, 6, 3)
p = 1 
index = 0
while index < len(t):
    p = p * t[index]
    index = index + 1
print(p)"""                #second way to do this exercise

#Exercise 38 : Create a list with 5 numbers. Print only numbers less than 20

"""l = [22, 5, 6, 9, 54, 25, 20, 1, 0, 6, 3, 10, 15 ,12, 18, 19]
for num in l : 
    if num < 20 :
        print(num)"""

#Exercise 41 :  Ask the user for three numbers. Print their average using a for loop

"""num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))
sum = num1 + num2 + num3 
div = sum / 3
print(div)""" # First way to do this exercise , here I repeat 3 time the input 

"""try:
    numbers = []
    for i in range(3):
        num = float(input("Enter your first number:"))
        numbers.append(num) 
    sum = 0 
    for numb in numbers :
        sum = sum + numb
    div = sum /3
    print(div)
except ValueError:
    print("Try again")"""

#Exercise 44 : Print numbers from 1 to 12. Stop if the number is 9 using break.
"""for i in range(1,12):
    if i == 9:
        break
    print(i)"""

#Exercise 49 :Create a set with 4 numbers. Check if 10 is in the set.
"""numbers = {4, 5, 6, 8, 10}
print(10 in numbers)"""