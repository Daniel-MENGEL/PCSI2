#Chargement des bibliotheques
import numpy as np

#mesures effectuees
il=42 #degres
uil=4

#Conversion en rad
il=il*np.pi/180
uil=uil*np.pi/180

#Simulation MC
N=10_000
il=il+uil*np.random.randn(N) #N tirages autour de i_l, loi normale

n=1/np.sin(il)
print("Meilleur estimateur : ",n.mean())
print("Incertitude type : ",n.std())