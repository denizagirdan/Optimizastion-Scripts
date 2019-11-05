# Optimizastion-Scripts

# -*- coding: utf-8 -*-

import numpy

def newton_raphson(iteration, initial):    
    
    x=initial
    
    f=numpy.zeros((iteration+1,1))
    f[0]=((3*x - 2)**2)*((2*x - 3)**2)
    
    print("Iter","X","dif_f(X)","Gradient",sep="\t\t")
    
    for i in list(range(0,iteration)):
        x= x - (72*x**3 -234*x**2 + 241*x -78)/ (216*x**2 - 468*x + 241)
        
        f[i+1]= (3*x - 2)**2*(2*x - 3)**2
        
        dif_f = (f[i+1] - f[i])
                
        gradient = 72*x**3 -234*x**2 + 241*x -78
        
        print(i,round(x,5),round(dif_f[0],5),round(gradient,5),sep='\t\t')

        if abs(gradient) < 0.001:
            break

    
    
    
