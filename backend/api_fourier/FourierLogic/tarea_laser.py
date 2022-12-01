import numpy as np
import scipy


h = 1.054571817* (10**(-34)) ##Constante de Planck 
v = 5 * 10**(14) ##Este es mi nu
Dv=100 * (10**6)   ##Este es mi delta nu
g = Dv/ (2*np.pi *((Dv/2)**2) ) ##Funcion en linea
c = 3 * (10**8) ##Velocidad de la luz
A_21 = 10**5 ##Coeficiente de emision espontanea
tau_21 = 1/A_21
lmd = c/v
tau_20 = 50 * (10**(-6)) ##Tau 20 50picosegundos
tau_10 = 10 * (10**(-9)) ##Tau 20 10 nanosegundos
P = 1.8 * (10**22)  ##Bombeo uniforme y constante
s = (A_21*g * ((lmd)**2)) /(8*np.pi)    ##Sigma 

tau_2 = ( (1/tau_20) +A_21)**(-1)

print(f"Lambda: {lmd} en metros")
print(f"La funcion forma de linea tiene un valor de {g}")
print(f"La seccion eficaz es {s}")


##¿Ahora el calculo de la intensidad de saturacion?

I_s = (h*v)/(s*tau_20) * ((1+(tau_10/tau_20)-((tau_10*tau_20)/tau_21))**(-1))  ##Revisar si se debe usar tau2 o tau20
print(f"La intensidad de saturacion es: {I_s}" )
##Bueno hasta este punto tengo los calculos hasta el punto d, continuo con el punto e

R_1 = 0.99
R_2 = 0.8

gamma= s *P*tau_2*(1-tau_10/tau_21)
l_g = 0.75 ## la longitud de la cavidad

G = gamma*l_g

print(f"la eficiencia gamma es: {gamma}")
print(f"la ganancia: {G}")

g_lazo_cerrado= R_1*R_2 * np.exp(2*G)

round_trip = 2* l_g / c
tau_photon = round_trip / (1-R_1*R_2)
print(f"El round trip encontrado es: {round_trip}")
print(f"El tiempo de vida del foton es: {tau_photon}")

##Factor de calidad y finesa