import numpy as np
import matplotlib.pyplot as plt
import random as rd
im1=plt.imread('8_groix_thirdArrowProcessing.bmp')
im2=np.copy(im1)
im3=plt.imread('3_groix_thirdProcessing.bmp')
im4=np.copy(im3)

deplacement=[(0,0),(-4,1),(-4,2),(-4,3),(-4,4),(-3,4),(-2,4),(-1,4),(0,4),(1,4),(2,4),(3,4),(4,4),(4,3),(4,2),(4,1),(4,0),(4,-1),(4,-2),(4,-3),(4,-4),(3,-4),(2,-4),(1,-4),(0,-4),(-1,-4),(-2,-4),(-3,-4),(-4,-4),(-4,-3),(-4,-2),(-4,-1)]

tableau=np.zeros((im2.shape[0],im2.shape[1]),dtype=int)

for k in range(im2.shape[0]):
    for l in range(im2.shape[1]):
        if list(im2[k,l,:])!=[185,122,8]:
            tableau[k][l]=int(im2[k,l,1]/7)

for k in range(im4.shape[0]):
    for l in range(im4.shape[1]):
        if list(im4[k,l,:])==[0,0,255]:
            im4[k,l,1]=255

for k in range(20):
    nb_repet=5000
    compteur=0
    print(20-k)
    if k<0:
        print("At which coordinates do you want to place your first particle?")
        print("(x in [0,",im4.shape[0],"] and y in [0,",im4.shape[1],'])')
        x=int(input("Coordinates in x: "))
        y=int(input("Coordinates in y: "))
    if k==0:
        y=798
        x=130
    elif k==1:
        y=1247
        x=400
    else:
        x=rd.randrange(0,im4.shape[0]-1)
        y=rd.randrange(0,im4.shape[1]-1)
    while compteur < nb_repet:
        if tableau[x][y]==0:
            im4[x,y,0]=0
            im4[x,y,0]=0
            im4[x,y,0]=0
            compteur=nb_repet
        else:
            x,y=x+deplacement[tableau[x][y]][0],y+deplacement[tableau[x][y]][1]
            im4[x,y,0]=255
            im4[x,y,1]=0
            im4[x,y,2]=0
            compteur=compteur+1

plt.imsave('Result.bmp',im4)
  
