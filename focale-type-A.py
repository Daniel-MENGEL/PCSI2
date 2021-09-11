#Chargement des bibliotheques
import matplotlib.pyplot as plt
import numpy as np

N=10_000
#Valeurs mesurees et incertitude type
d0min, d0max = -1, 1          # si distribution rectangulaire
d0=7.5#np.random.uniform(d0min,d0max,N)

d1=np.array([45.5,46.6,53.5,6,20,25,30,40,50,60,70,80,100,120,140,150],dtype=float)
ud1=2

d2=np.array([120,135.6,47.7,49,50.2,51.2,52.3,54.5,56.5,58.7,61.2,63.2,67.7,72.2,76.5,78.9],dtype=float)
ud2=1

invOAp=1/(d2-d1)
invOA=1/(d1-d0)

#Controle visuel
plt.figure()
plt.title('Validation de la relation de conjugaison')
plt.errorbar(invOA,invOAp,fmt='bo',label='Mesures')
plt.xlabel('$1/OA$ en m^-1')
plt.ylabel('Longueur $l$ en m')


#Determination de coefficients a et b de la droite de regression optimale
a,b=np.polyfit(invOA,invOAp,1)
plt.plot(invOAp,a*invOA+b,'r',label='Droite de régression optimale')

plt.legend()


plt.show()

