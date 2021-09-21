import sys as sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
import random

valeur=int()
tableau=[]

taille=501

def tableau_1 (taille):
    f1 = open ('database_vecteur.txt','w')
    f2 = open ('database_vitesse.txt','w')
    for k in range(taille):
        liste=[]
        for l in range(taille):
            if k==0 and l != taille-1 :
                f1.write ("9 ")
                valeur=9
            elif l==0:
                f1.write ("1 ")
                valeur=1
            elif l==taille-1 and k != taille-1:
                f1.write ("17"+"\n")
                valeur=17
            elif k==taille-1 and l != taille-1:
                f1.write ("25 ")
                valeur=25
            elif k==taille-1 and l==taille-1 :
                f1.write ("25"+"\n")
                valeur=25
            else:
                nb1=tableau[k-1][l]
                nb2=liste[l-1]
                nb1,nb2=min(nb1,nb2),max(nb1,nb2)
                if nb1>2:
                    nb1=nb1-3
                else:
                    nb1=(nb1+31)-3
                if nb2<29:
                    nb2=nb2+3
                else:
                    nb2=nb2+3-31
                nb1,nb2=min(nb1,nb2),max(nb1,nb2)
                ajout=random.randint(nb1,nb2)
                f1.write (str(ajout)+" ")
                valeur=ajout
            liste.append(valeur)

        tableau.append(liste)
            
    for k in range(taille):
        for l in range(taille):
            if k==0 or k==taille-1 or l==0 or l==taille-1:
                f2.write("0 ")
            else:
                f2.write(str(random.randint(1,8))+" ")
        f2.write("\n")

    f1.close()
    f2.close()

def tableau_2 (taille):
    f1 = open ('database_vecteur.txt','w')
    f2 = open ('database_vitesse.txt','w')
    print("Génération des courants")
    for ligne in range(taille):
        indic1,indic2=False,False
        liste=[]
        for colonne in range(taille):
            if (ligne==0 and colonne != taille-1) or ((ligne < (taille//2)) and (colonne==taille//2 or colonne==(taille//2)+1)) :
                f1.write ("8 ")
                valeur=8
            elif colonne==0 or ((colonne < (taille//2)) and (ligne==taille//2 or ligne==(taille//2)+1)):
                f1.write ("0 ")
                valeur=0
            elif colonne==taille-1 and ligne != taille-1:
                f1.write ("16"+"\n")
                valeur=16
            elif (colonne > (taille//2)+1) and (ligne==taille//2 or ligne==(taille//2)+1):
                f1.write ("16 ")
                valeur=16
            elif (ligne==taille-1 and colonne != taille-1) or ((ligne > (taille//2)+1) and (colonne==taille//2 or colonne==(taille//2)+1)):
                f1.write ("24 ")
                valeur=24
            elif ligne==taille-1 and colonne==taille-1 :
                f1.write ("24"+"\n")
                valeur=24
            elif colonne==ligne and ligne<=(taille//2):
                f1.write ("4 ")
                valeur=4
                indic1=True
            elif colonne==ligne and ligne>(taille//2):
                f1.write ("20 ")
                valeur=20
                indic2=True
            elif ligne==(taille-colonne) and ligne<(taille//2):
                f1.write ("12 ")
                valeur=12
                indic2=True
            elif ligne==(taille-colonne) and ligne>(taille//2):
                f1.write ("28 ")
                valeur=28
                indic1=True
                
            # Zone 9h - 12h
            elif ligne < taille//2 and colonne < taille//2:
                if indic1==True:
                    ajout=random.randint(5,9)
                    f1.write (str(ajout)+" ")
                    valeur=ajout
                else:
                    ajout=random.randint(1,5)
                    f1.write (str(ajout)+" ")
                    valeur=ajout
            
            # Zone 6h - 9h
            elif ligne > taille//2 and colonne < taille//2:
                if indic1==True:
                    ajout=random.randint(25,29)
                    f1.write (str(ajout)+" ")
                    valeur=ajout
                else:
                    ajout=random.randint(29,33)
                    if ajout>31:
                        ajout=ajout-32
                    f1.write (str(ajout)+" ")
                    valeur=ajout
                    
            # Zone 3h - 6h
            elif ligne > taille//2 and colonne > taille//2:
                if indic2==True:
                    ajout=random.randint(17,21)
                    f1.write (str(ajout)+" ")
                    valeur=ajout
                else:
                    ajout=random.randint(21,25)
                    f1.write (str(ajout)+" ")
                    valeur=ajout

            # Zone 12h - 3h
            elif ligne < taille//2 and colonne > taille//2:
                if indic2==True:
                    ajout=random.randint(13,17)
                    f1.write (str(ajout)+" ")
                    valeur=ajout
                else:
                    ajout=random.randint(9,13)
                    f1.write (str(ajout)+" ")
                    valeur=ajout
                    
            liste.append(valeur)

        tableau.append(liste)
    print("")
    print("Génération des vitesses des courants")
    print("")

    for k in range(taille):
        for l in range(taille):
            f2.write(str(random.randint(1,8))+" ")
        f2.write("\n")

    f1.close()
    f2.close()

tableau_2(taille)

image=plt.imread('map.bmp')
im2=np.copy(image)

def prt (s):
    """ Writes and flushes without delay a text in the console"""
    sys.stdout.write(s)
    sys.stdout.flush()

def mouvement (tableau,h2,i2,liste,tableau_vit):
    deplacement=[(-4,0),(-4,1),(-4,2),(-4,3),(-4,4),(-3,4),(-2,4),(-1,4),(0,4),(1,4),(2,4),(3,4),(4,4),(4,3),(4,2),(4,1),(4,0),(4,-1),(4,-2),(4,-3),(4,-4),(3,-4),(2,-4),(1,-4),(0,-4),(-1,-4),(-2,-4),(-3,-4),(-4,-4),(-4,-3),(-4,-2),(-4,-1)]
    mvmt=deplacement[int(tableau[h2//9][i2//9])]
    vit=float(tableau_vit[h2//9][i2//9])
    h2=floor(h2+mvmt[0]*vit)
    i2=floor(i2+mvmt[1]*vit)

    return(h2,i2)

def lancement (hauteur,largeur,im2,tableau,liste,tableau_vit,limite,nb_couleur):
    banque_couleur=[[255, 255, 255],[255, 0, 0],[0, 255, 0],[0, 0, 255],[0, 255, 255],[255, 0, 255],[255, 255, 0],[127, 127, 127],[127, 0, 0],[0, 127, 0],[0, 0, 127],[0, 127, 127],[127, 0, 127],[127, 127, 0],[255,0,127],[0,255,127]]
    couleur=banque_couleur[nb_couleur]
    compteur=0
    liste_coord=[[hauteur,largeur]]
    for k in range(1):
        valeur1=k-4
        for l in range(1):
            valeur2=l-4
            im2[hauteur+valeur1,largeur+valeur2]=np.array([couleur[0],couleur[1],couleur[2],135])
    while hauteur!=0 and largeur!=0 and hauteur!=limite and i2 !=limite and compteur < 30000 :
        hauteur,largeur=mouvement(tableau,hauteur,largeur,liste,tableau_vit)
        if hauteur<0:
            hauteur=0
        elif hauteur>limite:
            hauteur=limite
        elif largeur<0:
            largeur=0
        elif largeur>limite:
            largeur=limite
        im2[hauteur,largeur]=np.array([couleur[0],couleur[1],couleur[2],135])
        compteur=compteur+1
        liste_coord.append([hauteur,largeur])
        if liste_coord[compteur]==liste_coord[compteur-1]:
            hauteur=hauteur+random.randint(-2,2)
            largeur=largeur+random.randint(-2,2)

def homogen (oldmap):
    newmap = list(oldmap)
##    for k in range(taille-2):
##        for l in range(taille-2):
##            hauteur=k+1
##            largeur=l+1
##            if hauteur!=(taille//2)-1 and hauteur!=(taille//2) and hauteur!=(taille//2)+1 and hauteur!=(taille//2)+2 and largeur!=(taille//2)-1 and largeur!=(taille//2) and largeur!=(taille//2)+1 and largeur!=(taille//2)+2:
##                newmap[hauteur][largeur]=str(int((int(oldmap[hauteur][largeur])*4+int(oldmap[hauteur-1][largeur-1])+int(oldmap[hauteur-1][largeur+1])+int(oldmap[hauteur+1][largeur-1])+int(oldmap[hauteur+1][largeur+1]))/8))
    return(newmap)            
    
f1 = open ('database_vitesse.txt','r')
f2 = open ('database_vecteur.txt','r')

liste=f2.readlines()
vitesse=f1.readlines()

tableau=[]
tableau_vit=[]

for k in range (len(liste)):
    a=liste[k].split()
    tableau.append(a)

for k in range (len(vitesse)):
    a=vitesse[k].split()
    tableau_vit.append(a)

limite=(taille*9)-1

print("Le plateau est de dimention ",taille," par ",taille)
nb_repet=int(input("Combien voulez vous lancer de particules ? (14 maximum) "))
print("")

tabl_homo=homogen(tableau)

for k in range(nb_repet):
    print("Ou voulez vous placer votre micro particule numéro ",k+1," ? ")
    h=int(input("hauteur: "))
    i=int(input("longueur: "))
#    h=random.randint(50,450)
#    i=random.randint(50,450)
    h2=h*9+4
    i2=i*9+4
    lancement(h2,i2,im2,tabl_homo,liste,tableau_vit,limite,k)
    print("Particule placée !")
    print("")

plt.imsave('test.bmp',im2)
