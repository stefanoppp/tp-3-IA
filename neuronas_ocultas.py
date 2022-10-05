import math
import numpy as np
class Neurona_oculta:
    def __init__(self,pesos,entradas,deltas):
        self.pesos=pesos
        self.entradas=entradas
        
    def obtener_salida(self):
        prod_escalar=np.dot(self.pesos,self.entradas)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig