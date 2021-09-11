#Chargement des bibliotheques
import numpy as np

#mesures effectuees
i1 , ui1 = 50.0*np.pi/180 , 1*np.pi/180 #rad
i2 , ui2 = 30.5*np.pi/180 , 1*np.pi/180

#Simulation MC
N=10_000
i1=i1+ui1*np.random.randn(N) #N tirages autour de i_1, loi normale
i2=i2+ui2*np.random.randn(N)

n=np.sin(i1)/np.sin(i2)
print("Meilleur estimateur : ",n.mean())
print("Incertitude type : ",n.std())

# Comparaison avec la valeur precedente
n0 , un0=1.5072992699978365, 0.12049103789915017
En=abs(n.mean()-n0)/np.sqrt(n.std()+un0)
print("Ecart normalise avec la valeur precedente :",En)