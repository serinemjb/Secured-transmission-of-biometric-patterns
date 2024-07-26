# -*- coding: utf-8 -*-
"""
    Image encryption - substitution
"""
# ----- Librairies ------
import keygen as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 

# -- Reading the crypted image --
path_enimg = '/home/yagamiste/Desktop/Seminaire/encrypted_Finger.bmp'
enimg = plt.imread(path_enimg)  
plt.imshow(enimg,cmap='gray')
plt.show()


height = enimg.shape[0]
width = enimg.shape[1]
size = height * width

# --- Generation of the key ---
key = kg.keygen(0.01,3.95,size)


# --- Decryption ---
z=0 
decimg = np.zeros(shape=[height,width,3], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        # -- Pixel value is XORed with key --
        decimg[i,j]= enimg[i,j]^key[z]
        z+=1

plt.imshow(decimg,cmap='gray')
plt.show()
path_decimg = '/home/yagamiste/Desktop/Seminaire/decrypted_Finger.bmp'
plt.imsave(path_decimg,decimg)
