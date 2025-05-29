#Author : Fassiatou OUANRE
#this is my python training exercices
#these exercices are done in simple enghish for beginner
#because my mother tongue is french and I'm learning english

"""my goal is to start with simple exercices and progress to more dificult ones. 
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

# Exercise 17 :Create a list with 4 names. Add a new name. Print the list
"""l = ["fassia","ssifa","K_FA","smoochi"]
l.append("oulfa")
print(l)"""

# Exercise 22: Ask the user for a word. Print how many letters it has.

"""word = input("Enter a word you want ")
word = word.strip()
if word.isalpha():
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


# Exercise 27 : Create a tuple with 4 cities. Print the second and third city
"""t = ("Burkina", "Togo", "Ghana", "Ivoir")
print(t[1], t[2])"""

# Exercise 28 : Ask the user for a word. Print it 4 times using a while loop.

"""word = input("Input a word you want ")
count = 1
while count<=4 :
    print(word)
    count = count +1"""






























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
print(f"the scare of {num} is {square}")""" #here I on't think I need to use loop
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
                                                        #first code the print is inside the for that mean
                                                        #each time it do a sum it print the result.
                                                        #But the second code the print is in the same
                                                        #Indentation(outside the for) that mean it do the
                                                        #sum and give after the result


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

#Exercise 29 : Ask the user for a number. Print all even numbers up to it using a for loop
"""try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Please enter a non-negative number.")
    else:
        for i in range(0, num + 1, 2):
            print(i)
except ValueError:
    print("Please enter a valid integer.")"""