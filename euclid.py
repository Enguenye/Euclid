#!/usr/bin/env sage



def Euclidean (a,b):
    numiteraciones=0
    while a:
        b, a = a, b%a
        numiteraciones+=1
    return b



def ExtEuclidean(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    numiteraciones = 0
    while a:
        (q, a), b = (b // a, b % a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
        numiteraciones += 1
    return b, x0, y0

def ExtEuclideanModif(a, b):
    print("Iniciales: a:" + str(a) + " b: " + str(b))
    inia=a
    inib=b
    numiteraciones = 0
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a:
        (q, a), b = (b // a, b % a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
        numiteraciones += 1
    print("El numero de iteraciones de la función es de: " + str(numiteraciones))
    print(str(b)+"="+str(inia)+"*" + str(x0) +"+" +str(inib)+"*"+str(y0))
    return b,x0,y0

def Inverse(y,p):
    (b,z,x)=ExtEuclidean(y,p)
    if(z<0):
        z=z+p
    return z

