#Chargement des bibliotheques
import numpy as np
import matplotlib.pyplot as plt

#Mesures effectuees
i1=np.array([0.0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90],dtype=float) #deg
i2=np.array([0.0,3.5,7,10,13,16,19,22.5,25.5,28,30.5,33,35,37,39,40,41,41,42],dtype=float) #deg

#Conversion degres => radian
def d2r(angle):
    return angle*np.pi/180

#Verification graphique
sini1=np.sin(d2r(i1))
sini2=np.sin(d2r(i2))
plt.plot(sini1,sini2,'bo',label="Points experimentaux")
plt.xlabel("$\sin i_1$")
plt.ylabel("$\sin i_2$")
a,b=np.polyfit(sini1,sini2,1)
plt.plot(sini1,a*sini1,'r',label="Regression lineaire")
plt.title("Verification de la loi de la refraction")
plt.legend(loc='best')
plt.show()

#Methode statistique
sini1=np.delete(sini1,0) #pour eviter la divison par zero
sini2=np.delete(sini2,0)
n=sini1/sini2
print("Meilleur estimateur : ",n.mean())
print("Incertitude type : ",n.std())

plt.figure() #nouvelle fenetre graphique pour l'histogramme
plt.title("Histogramme $n$")
plt.hist(n,bins='auto')

#Recours a une simulation de Monte-Carlo
Nsim=10_000 #Nombre de simulations
a=np.zeros((Nsim,1),dtype=float) #tableau vide (pentes)

N=len(sini1) #Nombre de points de mesure
for k in range(Nsim): # tirages
    tsini1=sini1+d2r(1)*np.random.randn(N) #si loi normale
    tsini2=sini2+d2r(3)*np.random.randn(N) #si loi normale
    a[k]=np.sum(tsini1*tsini2)/sum(tsini2*tsini2) #pente pour ce tirage

print("Pente de la droite : ",a.mean()," +- ",a.std())
