import math
import numpy as np
class Neurona_final:
    def __init__(self,pesos,entradas,salida):
        self.pesos=pesos
        self.entradas=entradas
        self.salida=salida
        
    def obtener_salida(self):
        prod_escalar=np.dot(self.pesos,self.entradas)
        salida_real=self.sigmoidea(prod_escalar)
        variacion=self.salida-salida_real
        delta=salida_real*(1-salida_real)*variacion
        return delta
    
    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig