import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorRuido import generadorDatosRuido
from helpers.crearTablaHTML import crearTabla

def construirContaminacionRuidoDataFrame():
    datosRuido= generadorDatosRuido()
    
    
    RuidoDataFrame= pd.DataFrame(datosRuido,columns=["comuna","BDduirnos","BDnocturnos","fecha"])
    
    RuidoDataFrame.replace('sin',pd.NA,inplace=True)

    RuidoDataFrame.dropna(inplace=True)



    #ORDENAR LOS DATOS PARA CLASIFICARLOS

    datosOrdenadosRuido = RuidoDataFrame.groupby('comuna')['BDduirnos'].mean()
    print(datosOrdenadosRuido)

    #Grafico la informacion
    plt.figure(figsize=(20,20))
    datosOrdenadosRuido.plot(kind='bar',color='green')
    plt.title('Indice de DBdiurnos por comuna en medellin')
    plt.xlabel('Barrio')
    plt.ylabel('Reciclaje')
    plt.grid(True)
    plt.savefig('./assets/img/Ruido.png',format='png',dpi=300)
    
    
construirContaminacionRuidoDataFrame()