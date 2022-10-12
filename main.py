from neurona_final import Neurona_final
from neuronas_ocultas import Neurona_oculta

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
    
    
    for i in range(iteraciones):
        
        for j in range(len(entradas)):
            no_1=Neurona_oculta(pesos[0],entradas[j])
            no_2=Neurona_oculta(pesos[1],entradas[j])
            no_3=Neurona_oculta(pesos[2],entradas[j])
            neuronas_ocultas=[no_1,no_2,no_3]
            
            neurona_final=Neurona_final(pesos_finales,salidas[j],[1,no_1.obtener_salida(),no_2.obtener_salida(),no_3.obtener_salida()])
            error_red=neurona_final.obtener_error()
            k=0
            for neurona in neuronas_ocultas:
                error=neurona.obtener_error(pesos_finales[k+1],error_red)
                nuevos_pesos=neurona.calcular_nuevos_pesos(error,pesos_finales[k+1])
                neurona.pesos=nuevos_pesos
                print(neurona.pesos)
                k=k+1
            # ARREGLAR PESOS FINALES
            neurona_final.calcular_nuevos_pesos(error_red)
            print(neurona_final.pesos)
            print("\n")
main()