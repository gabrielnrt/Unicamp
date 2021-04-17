# -*- coding: utf-8 -*-
from math import pow, sqrt

def K1(massa,energia,planck):
    retorno = sqrt(2*massa*energia)
    retorno = retorno/planck
    return retorno

def K2(massa,energia,potencial,planck):
    diferenca = energia - potencial
    valor = K1(massa,diferenca,planck)
    return valor

def massa_do_eletron(velocidade_da_luz):
    Mev = pow(10,6)
    C = velocidade_da_luz
    
    VALOR = 0.5*Mev
    VALOR = VALOR/pow(C,2)
    return VALOR

def Transmissao(k1,k2):
    final = (4*k1*k2)/pow(k1+k2,2)
    return final

def Reflexao(k1,k2):
    reflexao = pow(k1-k2,2)/pow(k1+k2,2)
    return reflexao

# ESSES VALORES SÃO CONSTANTES
E = 10
V = 9

# SEM USAR UNIDADES NATURAIS
print("Usando os valores no S.I.")
c = 299792458
hcortado = 6.582*pow(10,-16)
m = massa_do_eletron(c)
k1 = K1(m,E,hcortado)
k2 = K2(m,E,V,hcortado)

T = Transmissao(k1,k2)
R = Reflexao(k1,k2)

print("A probabilidade de transmissão é",T)
print("A probabilidade de reflexão é", R)
print("De fato, vemos que T + R = ",T+R)

# USANDO UNIDADES NATURAIS
print()
print("Usando unidades naturais, note que:")
m = massa_do_eletron(1)
k1 = K1(m,E,1)
k2 = K2(m,E,V,1)

T = Transmissao(k1,k2)
R = Reflexao(k1,k2)

print("A probabilidade de transmissão é",T)
print("A probabilidade de reflexão é", R)
print("De fato, vemos que T + R = ",T+R)
