# -*- coding: utf-8 -*-
"""
    Image encryption - substitution
"""
# ----- Librairies ------
import keygen as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 

# ----- Reading the image -----
path_orimg = '/home/yagamiste/Desktop/Seminaire/Finger.bmp'
img = mpimg.imread(path_orimg)

plt.imshow(img,cmap='gray')
plt.show()

# ---- generating chaotic keys ----
height = img.shape[0]
width = img.shape[1]
size = height * width 

# ----- il faut que r > 3.57 et  0 < Xo < 1 ----------- 
key = kg.keygen(0.01,3.95,size)


# --- Encryption-Substitution with XOR
z=0
enimg = np.zeros(shape=[height,width,4], dtype=np.uint8)

for i in range(height):
    for j in range(width):
        # -- Pixel value is XORed with key --
        enimg[i,j]= img[i,j]^key[z]
        z+=1

plt.imshow(enimg, cmap='gray')
path_enimg = '/home/yagamiste/Desktop/Seminaire/encrypted_Finger.bmp'
plt.imsave(path_enimg, enimg)      
plt.show()

