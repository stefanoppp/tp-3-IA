from neuronas_ocultas import Neurona_oculta
def main():
    pesos_1=[0.9,0.7,0.5]
    pesos_2=[0.3,-0.9,-1]
    pesos_3=[0.8,0.35,0.1]
    pesos_4=[-0.23,-0.79,0.56]
    entradas=[1,0,0]
    delta=0
    neurona_1=Neurona_oculta(pesos_1,entradas,delta)
    neurona_2=Neurona_oculta(pesos_2,entradas,delta)
    neurona_3=Neurona_oculta(pesos_3,entradas,delta)
    
    
main()