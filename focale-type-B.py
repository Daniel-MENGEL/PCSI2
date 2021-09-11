#Chargement des bibliotheques
import numpy as np

#Mesures effectuees
d0min, d0max = ?, ?          # si distribution rectangulaire
d1m , ud1 = ? , ?            # si distribution normale
d2m , ud2 = ? , ?            # si distribution normale

#Utilisation de la methode de Monte Carlo, incertitude type B
N=10_000
d0=np.random.uniform(ud0min,ud0max,N) # si rectangulaire
d1=d1m+ud1*np.random.randn(N)       # si normale
d2=d2m+ud2*np.random.randn(N)       # si normale

f_p=(d0-d1)*(d2-d1)/((d0-d1)-(d2-d1)) # calcul de f'
print(f_p.mean()) # valeur moyenne, le meilleur estimateur
print(f_p.std())  # ecart type, l'incertitude type

#Comparaison a la valeur attendue
f_th=1/3

E_n=abs(f_th-f_p.mean())/f_p.std()
print(E_n)
