#calculer le max entre deux nombres 

"""a=float(input("entrer un prmier réèl "))
f=float(input("entrer un deuxième réèl "))
if a<f :
    print("le max est: ", f)
else :
    print("le max est :", a)"""

#Verifier si un nombre est positif ou négatif 

"""b=float(input("entrer un nombre: "))
if b>=0 :
    print("le nombre est positif")
else :
    print("le nombre est négatif")"""

# programme qui lit la valeur de la température

"""t = int(input("entrer la valeur de la température: "))
if t<0 :
    print("glace")
elif t>0 and t<100:
    print("liquide")
else :
    print("vapeur")"""

# saisir un entier et recupérer le jour correspondant 

"""a = int(input("input a number between 1 and 7: "))
if a==1:
    print("monday")
elif a==2 : 
    print("tuesday")
elif a==3 : 
    print("wenesday")
elif a==4 : 
    print("thursday")
elif a==5 : 
    print("friday")
elif a==6 : 
    print("saturday")
else: 
    print("sunday")"""

# calcul de la somme des 20 premier entier positif grace
# au boucle imbriqué 
"""s=0
for i in range(1,21) :
    s=s+i
print("la somme est :", s)"""

# réaliser un rectangle avec des étoiles grace au boucles
# inbriqué 
# ici lorsqu'on utilise  print("*") seulement il les place
# à la longueur donc on doit ajouté end pour qu'il les place
# par ligne pour avoir le rectangle
"""l = int(input("veuillez entrer un nombre de ligne : "))
c = int(input("veuillez entrer un nombre de colonne : "))
for i in range(1,l+1):
    for j in range(1,c+1):
        print("* ", end=" ")
    print()"""

# écrire un programme qui demande un nombre compris entre 10 et 20
# en utulisant le boucle tant que 
"""n = int(input("veuillez entrer un nombre: "))
while n<10 : 
    print("le nombre est petit")
    n = int(input("veuillez entrer un autre nombre: "))
while n>20 :
    print("le nombre est grand")
    n = int(input("veuillez entrer un nombre: "))
print("le nombre est compris entre 10 et 20")"""

# saisir un nombre supérieur à 1 et calcul la somme des entiers jusqu'a ce nombre

"""n = int(input("entrer un nombre supérieur à 1: "))
while n<1 :
    n = int(input("entrer un nombre supérieur à 1: "))
s=0
for i in range(1,n+1):
    s=s+i
print("la somme est: ",s)"""

# en utulisant les modules standart de python , écrire les programmes suivant :

# 1-écrire un programme qui calcule la factorielle d'un nombre

"""import math
n = int(input("entrer un nombre: "))
a= math.factorial(n)
print(a)"""

# écrire un programme qui affiche un nombre impaire aléatoire entre 1 et 101

"""import random
a= random.randint(1,101)
if a%2==0 :
    a= random.randint(1,101)
print(a)"""

# écrire un programme pour calculer le mode et l'écart type d'une série estatistique

"""import statistics
l = [1,4,5,1,2,5,2,6,3,2,1,4,3,9,5,4,2,1,8,7,6,9,2,2,2]
md = statistics.mode(l)
ecart = statistics.stdev(l)
print(md)
print(ecart)"""

# écrire un programme qui affiche la date d'aujordh'ui

"""from datetime import date
t = date.today()
print(t)"""

# écrire un progamme qui permet d'ouvrir le site web google.com

"""import webbrowser
url= "https://www.google.com"
webbrowser.open_new_tab(url)"""

# écrire un programme qui convertis les bitcoin en euro 
# il faut installer une bibliothèque et itulisé cette module

"""from forex_python.bitcoin import BtcConverter
bitcoin = BtcConverter()
print(bitcoi.get_latest_price('EUR'))
print(bitcoi.get_latest_price('USD'))"""


# écrir un programme qui vous permets de créer une liste nommées
# lettres, dont les éléments sont les lettres française . Ensuite
# en utulisant les éléménts de la liste le programme affichera votre nom 
# et prenom. 

l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','y','z']
print(l[5],l[0],l[18],l[18],l[8],l[0])