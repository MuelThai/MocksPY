import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorArboles import listaDatosArboles
from helpers.crearTablaHTML import crearTabla

def construirSiembraArbolesDataFrame():
    datosSiembraArboles= listaDatosArboles()


    SiembraArbolesDataFrame= pd.DataFrame(datosSiembraArboles,columns=["corregimiento","hectareasSembradas","nombres","fecha"])
    

    SiembraArbolesDataFrame.replace('sin',pd.NA,inplace=True)

    SiembraArbolesDataFrame.dropna(inplace=True)



    #ORDENAR LOS DATOS PARA CLASIFICARLOS

    datosOrdenadosArboles = SiembraArbolesDataFrame.groupby('corregimiento')['hectareasSembradas'].mean()
    print(datosOrdenadosArboles)

    #Grafico la informacion
    plt.figure(figsize=(20,20))
    datosOrdenadosArboles.plot(kind='bar',color='green')
    plt.title('indice de hectaria sembradas por corregimiento en medellin')
    plt.xlabel('Corregimiento')
    plt.ylabel('Hectarias')
    plt.grid(True)
    plt.savefig('./assets/img/Arboles.png',format='png',dpi=300)
    
    
construirSiembraArbolesDataFrame()