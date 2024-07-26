# -*- coding: utf-8 -*-
"""
Fonction pour générer la clé en utilisant la "logistic map" pour un 
processus de cryptage
"""
def keygen(x,r,size):
    # -- création du vecteur qui contiendra les clés -- 
    key=[]

    # -- Génération des clé avec la carte logistique --
    for i in range(size):
        
        x = r * x * (1-x) # Xn+1 = r Xn (1-Xn)
        key.append(int((x * pow(10,16))%256)) # key = (x*10¹⁶)%256

    return key

