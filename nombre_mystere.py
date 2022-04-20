import random

nombre_mystere = random.randint(1,10)
essai = 0


while(essai < 5):
    nombre_donne = input("Devinez le nombre mystère : ")
    if(not nombre_donne.isdigit()):
        print("Vous n'avez pas rentré un nombre !")
        exit() 
    else:
        nombre_donne = int(nombre_donne)
    if(nombre_donne < nombre_mystere):
        resultat = "Le nombre mystère est plus grand !"
        essai +=1
    elif(nombre_donne > nombre_mystere):
        resultat = "Le nombre mystère est plus petit !"
        essai +=1
    else:
        resultat = f"Bravo, vous avez trouvé le nombre mystère qui était : {nombre_mystere} en {essai+1} essai(s)"
        essai = 5
    print(resultat)

print(f"Vous avez perdu, le nombre mystère était {nombre_mystere}")


