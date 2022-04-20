import random

nombre_mystere = random.randint(1,50)
essai = input("Devinez le nombre mystère : ")

# A rajouter :
# Nombre maximum d'essai avant gameover

if(int(essai) < nombre_mystere):
    resultat = "Le nombre mystère est plus grand !"
elif(int(essai) > nombre_mystere):
    resultat = "Le nombre mystère est plus petit !"
else:
    resultat = "Bravo, vous avez trouvé le nombre mystère qui était : " + str(nombre_mystere)


print(resultat)