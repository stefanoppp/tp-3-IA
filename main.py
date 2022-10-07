from neurona_final import Neurona_final
from neuronas_ocultas import Neurona_oculta

def main():
    
    entradas=[[1,0,0],[1,1,1],[0,1,1],[0,0,0],[0,0,1]]
    
    salidas=[1,0,0,0,1]
    
    delta=1
    
    neurona_1=Neurona_oculta([0.9,0.7,0.5],entradas[0],delta)
    neurona_2=Neurona_oculta([0.3,-0.9,-1],entradas[0],delta)
    neurona_3=Neurona_oculta([0.8,0.35,0.1],entradas[0],delta)
    
    neurona_final=Neurona_final([-0.23,-0.79,0.56,0.6],salidas[0],[1,
                                                            neurona_1.obtener_salida(),
                                                            neurona_2.obtener_salida(),
                                                            neurona_3.obtener_salida()])
    delta=neurona_final.obtener_delta()
    
    pesos_1=neurona_1.actualizar_pesos(delta)
    pesos_2=neurona_2.actualizar_pesos(delta)
    pesos_3=neurona_3.actualizar_pesos(delta)
    
main()