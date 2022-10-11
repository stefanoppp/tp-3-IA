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
    pesos_neurona_oculta=[-0.23,-0.79,0.56,0.6]
    salidas=[1,0,0,0,1]
    
    neurona_1=Neurona_oculta(pesos[0],entradas[0])
    neurona_2=Neurona_oculta(pesos[1],entradas[0])
    neurona_3=Neurona_oculta(pesos[2],entradas[0])
    capa_oculta=[neurona_1,neurona_2,neurona_3]
    neurona_final=Neurona_final(pesos_neurona_oculta,salidas[0],[1,neurona_1.obtener_salida(),
                                                                    neurona_2.obtener_salida(),
                                                                    neurona_3.obtener_salida()])
    iteraciones=int(input("Cantidad de iteraciones: "))

    for i in range(iteraciones):

        error_red=neurona_final.obtener_error()

        i=0
        # NEURONAS OCULTAS
        for neurona in capa_oculta:
            nuevos_pesos_ocultos=[]
            error_oculto=neurona.obtener_error(neurona_final.pesos[i+1],error_red)
            
            for peso in neurona.pesos:
                peso=peso+(neurona.lr*neurona.entradas[i]*error_oculto)
                nuevos_pesos_ocultos.append(peso)
            print(nuevos_pesos_ocultos)
            neurona.pesos=nuevos_pesos_ocultos
        
        nuevos_pesos_finales=neurona_final.calcular_nuevos_pesos()
        neurona_final.pesos=nuevos_pesos_finales
        print(nuevos_pesos_finales)   
        print("\n")
main()