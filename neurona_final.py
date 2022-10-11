import math
import numpy as np
class Neurona_final:
    def __init__(self,pesos,salida,entradas):
        self.pesos=pesos
        self.entradas=entradas
        self.salida=salida
        self.lr=0.2

    def obtener_pesos(self):
        return self.pesos
    
    def obtener_salida(self):
        prod_escalar=np.dot(self.pesos,self.entradas)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def obtener_error(self):
        salida_obtenida=self.obtener_salida()
        error=salida_obtenida*(1-salida_obtenida)*(self.salida-salida_obtenida)
        return error
        
    def calcular_nuevos_pesos(self):
        pesos=[]
        error=self.obtener_error()
        for i in range(len(self.pesos)):
            nuevo_peso=self.pesos[i]+(self.lr*self.entradas[i]*error)
            pesos.append(nuevo_peso)
        return pesos
    # los valores de la ulitma neurona para calcular pesos de capa oculta, se 
    # actualizan en la 2da vuelta
    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig