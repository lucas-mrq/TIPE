import numpy as np
import matplotlib.pyplot as plt
im1=plt.imread('3_groix_thirdProcessing.bmp')
im20=np.copy(im1)

c=[[0,255,255],[185,122,8],[0,0,255]]

im10=np.copy(im20)

fleches=[]
compteur=0

def distance(coord1,coord2):
    return(((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2)**0.5)

def tourniquet(coord1,coord2):
    x=coord1[0]-coord2[0]
    y=coord1[1]-coord2[1]
    H=(x**2+y**2)**0.5
    A=np.abs(x)
    if H==0:
        H=H+1
    angle=np.arccos(A/H)
    if x>0 and y>0:
        angle=(1-angle)+np.pi/2
    if x>0 and y<0:
        angle=angle+np.pi
    if x<0 and y<0:
        angle=(1-angle)+3*np.pi/2
    return(int(np.ceil((angle/(2*np.pi))*32)+1))

im2=np.zeros((im10.shape[0]+80, im10.shape[1]+80, 3),dtype=np.uint8)

im2[40:-40,40:-40]=im10

plt.imsave('4_groix_vectors.bmp',im2)

for k in range(im2.shape[0]):
    for l in range(im2.shape[1]):
        if list(im2[k,l,:])==[0,0,255]:
            coord=[]
            for m in range(50):
                for n in range(50):
                    if list(im2[k+m-25,l+n-25,:])==[0,0,255]:
                        im2[k+m-25,l+n-25,0]=255
                        im2[k+m-25,l+n-25,1]=255
                        im2[k+m-25,l+n-25,2]=255
                        coord.append([k+m-25,l+n-25])
            fleches.append(coord)
            compteur=compteur+1

print("Step 6")

bary=[]

for k in range(len(fleches)):
    y=0
    x=0
    nb=0
    for i in range(len(fleches[k])):
        x=x+fleches[k][i][0]
        y=y+fleches[k][i][1]
        nb=nb+1
    bary.append([int(x/len(fleches[k])),int(y/len(fleches[k]))])

for k in range(len(bary)):
    im2[bary[k][0],bary[k][1],0]=255
    im2[bary[k][0],bary[k][1],1]=0
    im2[bary[k][0],bary[k][1],2]=255

coordmax_mo=[]
coordmax_pl=[]

print("Step 7")

plt.imsave('5_groix_arrow_barycenter.bmp',im2)

im1=plt.imread('4_groix_vectors.bmp')
im2=np.copy(im1)

for k in range(len(bary)):
    coordmax=bary[k]
    for l in range(bary[k][0]-20,bary[k][0]+20):
        for m in range(bary[k][1]-20,bary[k][1]+20):
            if list(im2[l,m,:])==[0,0,255]:
                if distance(coordmax,bary[k])<distance([l,m],bary[k]):
                    coordmax=[l,m]
    coordmax_pl.append(coordmax)
    
for k in range(len(bary)):
    coordmin=bary[k]
    for l in range(bary[k][0]-20,bary[k][0]+20):
        for m in range(bary[k][1]-20,bary[k][1]+20):
            if list(im2[l,m,:])==[0,0,255]:
                if distance(coordmin,coordmax_pl[k])<distance([l,m],coordmax_pl[k]):
                    coordmin=[l,m]
    coordmax_mo.append(coordmin)

vecteur=[]

for k in range(len(coordmax_pl)):
    im2[coordmax_pl[k][0],coordmax_pl[k][1],0]=255
    im2[coordmax_pl[k][0],coordmax_pl[k][1],1]=0
    im2[coordmax_pl[k][0],coordmax_pl[k][1],2]=0
    im2[coordmax_mo[k][0],coordmax_mo[k][1],0]=255
    im2[coordmax_mo[k][0],coordmax_mo[k][1],1]=0
    im2[coordmax_mo[k][0],coordmax_mo[k][1],2]=0
    print(coordmax_pl[k],coordmax_mo[k])
    vecteur.append(tourniquet(coordmax_mo[k],coordmax_pl[k]))

print("Step 8")

plt.imsave('6_groix_firstArrowProcessing.bmp',im2)

for k in range(im2.shape[0]):
    for l in range(im2.shape[1]):
        if list(im2[k,l,:])==[0,0,0] or list(im2[k,l,:])==[0,0,255]:
            im2[k,l,0]=0
            im2[k,l,1]=255
            im2[k,l,2]=255
    
plt.imsave('7_groix_secondArrowProcessing.bmp',im2)

for k in range(im2.shape[0]):
    print(im2.shape[0]-k)
    for l in range(im2.shape[1]):
        if list(im2[k,l,:])!=[185,122,8]:
            minimum=distance([0,0],[im2.shape[0],im2.shape[1]])
            numero=0
            for j in range(len(bary)):
                if distance(bary[j],[k,l])<minimum:
                    minimum=distance(bary[j],[k,l])
                    numero=j
            im2[k,l,0]=0
            im2[k,l,1]=7*vecteur[numero]
            im2[k,l,2]=0

print("End !")

im10=im2[40:-40,40:-40]
plt.imsave('8_groix_thirdArrowProcessing.bmp',im10)

