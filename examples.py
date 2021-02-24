from euclid import *

#Hallar el mcm(a,b)
print(Euclidean(12,5))
print(Euclidean(16,2))
print(Euclidean(75,81))

#Hallar los coeficientes de Bezout de (a,b)

(d,x,y)=ExtEuclidean(12,5)
print(str(d)+"=12*"+str(x)+"+5*"+str(y))
(d,x,y)=ExtEuclidean(75,81)
print(str(d)+"=75*"+str(x)+"+81*"+str(y))

#Hallar el inverso multiplicativo de a mod p

print(Inverse(4,5))
print(Inverse(7,11))