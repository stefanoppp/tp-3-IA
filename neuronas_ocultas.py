import math
import numpy as np
class Neurona_oculta:
    def __init__(self,pesos,entradas,delta):
        self.pesos=pesos
        self.entradas=entradas
        self.delta=delta
        
    def obtener_salida(self):
        prod_escalar=np.dot(self.pesos,self.entradas)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def actualizar_pesos(self,delta):
        salida_real=self.obtener_salida()
        delta_oculto=salida_real*(1-salida_real)*delta
        for i in range(len(self.pesos)):
            self.pesos[i]=self.pesos[i]+self.entradas[i]*delta_oculto
        return self.pesos
    
    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig