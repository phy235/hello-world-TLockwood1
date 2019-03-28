# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:53:41 2019

@author: 150193878
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants

q=1.6e-19 #ColoumbI
kb=constants.k
def beta(T): return q/(kb*T)  #Coloumbs/Joule
V_oc=0.5 #Volts
I_L=-2

def Current(V,T):
    I=I_0*(np.exp(q*V/(kb*T))-1)-I_L
    return I
    
def Power(I,V,T):
    if np.isclose(V_oc-(1/beta(T))*np.log(1+beta(T)*V),V,atol=1e-4):
        return V*I

for T in (300,400):#Kelvin
    IV=[]
    I_0=I_L/(np.exp((q*V_oc)/(kb*T)))
    for V in np.linspace(0,V_oc,10000):
            IV.append(Power(Current(V,T),V,T))
            
    #Filter out the Nones and print max
    print('T={0} Kelvin\nI_0={2:.4}\nMaxPower={1:1.4f} Watts\n'.format(T,max([i for i in IV if i]),I_0))#Filter out the Nones and print max


#Assuming at 400Kelvin the short circuit current and open circuit voltage unchanged

    
    
#%%