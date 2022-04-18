import random

nombre_mystere = random.randint(1,1000)
essai = input("Devinez le nombre mystère : ")

if(int(essai) < nombre_mystere):
    resultat = "Le nombre mystère est plus grand !"
elif(int(essai) > nombre_mystere):
    resultat = "Le nombre mystère est plus petit !"
else:
    resultat = "Bravo, vous avez trouver le nombre mystère qui était : " + str(nombre_mystere)

print(resultat)