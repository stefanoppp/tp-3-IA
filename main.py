from neurona_final import Neurona_final
from neuronas_ocultas import Neurona_oculta
import matplotlib.pyplot as plt
def main():
    
    entradas=[[1,0,0],
              [1,1,1],
              [0,1,1],
              [0,0,0],
              [0,0,1]]
    
    pesos=[[0.9,0.7,0.5],
           [0.3,-0.9,-1],
           [0.8,0.35,0.1]]
    
    pesos_finales=[-0.23,-0.79,0.56,0.6]
    salidas=[1,0,0,0,1]
    
    iteraciones=int(input("Cantidad de iteraciones: "))
    
    peso_1_historial=[]
    peso_2_historial=[]
    peso_3_historial=[]
    peso_4_historial=[]
    peso_5_historial=[]
    peso_6_historial=[]
    peso_7_historial=[]
    peso_8_historial=[]
    peso_9_historial=[]
    peso_10_historial=[]
    peso_11_historial=[]
    peso_12_historial=[]
    peso_13_historial=[]
    historial_error=[]
    for i in range(iteraciones):
        
        for j in range(len(entradas)):
            no_1=Neurona_oculta(pesos[0],entradas[j])
            no_2=Neurona_oculta(pesos[1],entradas[j])
            no_3=Neurona_oculta(pesos[2],entradas[j])
            
            neuronas_ocultas=[no_1,no_2,no_3]
            no_1.pesos
            neurona_final=Neurona_final(pesos_finales,salidas[j],[1,no_1.obtener_salida(),no_2.obtener_salida(),no_3.obtener_salida()])
            error_red=neurona_final.obtener_error()
            historial_error.append(error_red)
            k=0
            conteo=0
            for neurona in neuronas_ocultas:
                error=neurona.obtener_error(pesos_finales[k+1],error_red)
                nuevos_pesos=neurona.calcular_nuevos_pesos(error,pesos_finales[k+1])
                neurona.pesos=nuevos_pesos
                if conteo==0:
                    peso_1_historial.append(neurona.pesos[0])
                    peso_2_historial.append(neurona.pesos[1])
                    peso_3_historial.append(neurona.pesos[2])
                if conteo==1:
                    peso_4_historial.append(neurona.pesos[0])
                    peso_5_historial.append(neurona.pesos[1])
                    peso_6_historial.append(neurona.pesos[2])
                if conteo==2:
                    peso_7_historial.append(neurona.pesos[0])
                    peso_8_historial.append(neurona.pesos[1])
                    peso_9_historial.append(neurona.pesos[2])
                k=k+1
                conteo+=1
            neurona_final.calcular_nuevos_pesos(error_red)
            peso_10_historial.append(neurona_final.pesos[0])
            peso_11_historial.append(neurona_final.pesos[1])
            peso_12_historial.append(neurona_final.pesos[2])
            peso_13_historial.append(neurona_final.pesos[3])
            
            
            
      
    plt.plot(peso_1_historial,'g')
    plt.plot(peso_2_historial,'r')
    plt.plot(peso_3_historial,'y')
    plt.plot(peso_4_historial,'v')
    plt.plot(peso_5_historial,'k')
    plt.plot(peso_6_historial,'b')
    plt.plot(peso_7_historial,'o')
    plt.plot(peso_8_historial,'c')
    plt.plot(peso_9_historial,'m')
    plt.plot(peso_10_historial,'k')
    plt.plot(peso_11_historial,'o')
    plt.plot(peso_12_historial,'k')
    plt.plot(peso_13_historial,'m')
    plt.show()
    plt.plot(historial_error,'k')
    plt.show()
main()