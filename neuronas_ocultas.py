import math
import numpy as np
class Neurona_oculta:
    def __init__(self,pesos,entradas):
        self.pesos=pesos
        self.entradas=entradas
        self.lr=0.2
        
    def obtener_salida(self):
        prod_escalar=np.dot(self.pesos,self.entradas)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def obtener_error(self,peso_entrada_neurona_final,error_red):
        salida_real=self.obtener_salida()
        error=salida_real*(1-salida_real)*(peso_entrada_neurona_final*error_red)
        return error
    
    def calcular_nuevos_pesos(self,error_oculto,peso_capa_oculta):
        pesos=[]
        salida_real=self.obtener_salida()
        error=salida_real*(1-salida_real)*(error_oculto*peso_capa_oculta)
        for i in range(len(self.pesos)):
            nuevo_peso=self.pesos[i]+(self.lr*self.entradas[i]*error)
            pesos.append(nuevo_peso)
        return pesos
    

    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig