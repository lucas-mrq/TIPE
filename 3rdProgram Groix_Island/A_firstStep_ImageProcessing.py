import numpy as np
import matplotlib.pyplot as plt
im1=plt.imread('0_groix_initialPicture.jpg')
im20=np.copy(im1)

c=[[0,255,255],[185,122,8],[0,0,255]]

for k in range(im1.shape[0]):
    for l in range(im1.shape[1]):
        moy=(int(im1[k,l,0])+int(im1[k,l,1])+int(im1[k,l,1]))/3
        
        if int(im1[k,l,2])>190 and int(im1[k,l,1])>190 and int(im1[k,l,0])>190:
            im20[k,l,0]=0
            im20[k,l,1]=255
            im20[k,l,2]=255
            
        elif int(im1[k,l,0])>moy and int(im1[k,l,1])<190 and int(im1[k,l,2])<190:
            im20[k,l,0]=185
            im20[k,l,1]=122
            im20[k,l,2]=8
        else:
            im20[k,l,0]=0
            im20[k,l,1]=0
            im20[k,l,2]=255
            
print("Step 1")

def filtration1(im20,i):
    for k in range(1,im20.shape[0]-1):
        if (im20.shape[0]-1-k)%100 == 0 :
            print((im20.shape[0]-1-k)//100)
        im3=np.copy(im20)
        for l in range(1,im20.shape[1]-1):
            compteur=0
            if list(im3[k,l,:])!=c[i] and list(im3[k,l,:]) in c:
                if c[i]==list(im20[k+1,l+1,:]):
                    compteur=compteur+1
                if c[i]==list(im20[k+1,l,:]):
                    compteur=compteur+1
                if c[i]==list(im20[k+1,l-1,:]):
                    compteur=compteur+1
                if c[i]==list(im20[k,l+1,:]):
                    compteur=compteur+1
                if c[i]==list(im20[k+1,l-1,:]):
                    compteur=compteur+1
                if c[i]==list(im20[k-1,l-1,:]):
                    compteur=compteur+1
                if c[i]==list(im20[k-1,l,:]):
                    compteur=compteur+1
                if c[i]==list(im20[k-1,l+1,:]):
                    compteur=compteur+1
                if compteur>5:
                    im20[k,l,0]=c[i][0]
                    im20[k,l,1]=c[i][1]
                    im20[k,l,2]=c[i][2]
            elif ([im3[k,l,0],im3[k,l,1],im3[k,l,2]]) not in c:
                im20[k,l,0]=0
                im20[k,l,1]=255
                im20[k,l,2]=255
                    
    return(im20)

plt.imsave('1_groix_firstProcessing.bmp',im20)

for k in range(3):
    print("Step",k+2)
    im20=np.copy(filtration1(im20,k))

print("Step 4")
    
plt.imsave('2_groix_secondProcessing.bmp',im20)

im2=np.zeros((im20.shape[0]+80, im20.shape[1]+80, 3),dtype=np.uint8)

im2[40:-40,40:-40]=im20

for k in range(40,im2.shape[0]-1-40):
    print(im2.shape[0]-1-40-k)
    for l in range(40,im2.shape[1]-1-40):
        if list(im2[k,l,:])==[185,122,8]:
            compteur=0
            for n in range(k-10,k+10):
                for m in range(l-10,l+10):
                    if n!=k and m!=l:
                        if list(im2[n,m,:])==[185,122,8]:
                            compteur=compteur+1
            if compteur<40:
                im2[k,l,0]=0
                im2[k,l,1]=0
                im2[k,l,2]=255

for k in range(40,im2.shape[0]-1-40):
    print(im2.shape[0]-1-40-k)
    for l in range(40,im2.shape[1]-1-40):
        if list(im2[k,l,:])==[0,0,255]:
            compteur=0
            for n in range(k-10,k+10):
                for m in range(l-10,l+10):
                    if n!=k and m!=l:
                        if list(im2[n,m,:])==[0,0,255]:
                            compteur=compteur+1
            if compteur<40:
                im2[k,l,0]=0
                im2[k,l,1]=255
                im2[k,l,2]=255
                
im20=im2[40:-40,40:-40]
                
print("Step 5")

plt.imsave('3_groix_couleurs_traitee2.bmp',im20)


