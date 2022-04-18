
# plus tard, ajout de random(1, 1000)
nombre_mystere = 7

essai = input("Devinez le nombre mystère : ")

if(int(essai) < nombre_mystere):
    print("Le nombre mystère est plus grand !")
elif(int(essai) > nombre_mystere):
    print("Le nombre mystère est plus petit !")
else:
    print("Bravo, vous avez trouver le nombre mystère qui était : " + str(nombre_mystere))