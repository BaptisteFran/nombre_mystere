import random

nombre_mystere = random.randint(1,50)
essai = input("Devinez le nombre mystère : ")
if(essai.isdigit()):
    print("Vous n'avez pas rentré un nombre !")
    exit() 
else:
    essai = int(essai)

# A rajouter :
# Nombre maximum d'essai avant gameover

if(essai < nombre_mystere):
    resultat = "Le nombre mystère est plus grand !"
elif(essai > nombre_mystere):
    resultat = "Le nombre mystère est plus petit !"
else:
    resultat = "Bravo, vous avez trouvé le nombre mystère qui était : " + str(nombre_mystere)


print(resultat)