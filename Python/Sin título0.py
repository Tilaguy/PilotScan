# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:46:17 2020

@author: Sebastian_Tilaguy
"""

import numpy as np
import matplotlib.pyplot as plt

file_path = 'C:\Users\Sebastian_Tilaguy\Documents\Data\Tila\DataEcoIntencities_'

N = 1080

I1 = []
I2 = []
I3 = []

theta = np.linspace(-135,135,N)*np.pi/180.0

for i in range(2,15):
    try:
        f = open(file_path+str(i)+'.txt', "r")
        cont = 0
        
        for j in f:
            data = j.split('\t')
            for k in range(0,3*N,3):
                I1=np.append(I1,float(data[cont+k]))
                I2=np.append(I2,float(data[cont+k+1]))
                I3=np.append(I3,float(data[cont+k+2]))
            
#            x1 = I1*np.cos(theta)
#            y1 = I1*np.sin(theta)
#            plt.plot(x1,y1,'.')
            #plt.hold(True)
            
            plt.show()
            plt.grid()
            
    except:
        pass
