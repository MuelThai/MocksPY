import pandas as pd 
import matplotlib.pyplot as plt

from data.generators.generadorAire import generarDatosCalidadAire
from helpers.crearTablaHTML import crearTabla

def construirAireDataFrame():
    datosAires=generarDatosCalidadAire()


    aireDataFrame = pd.DataFrame(datosAires,columns=['nombre', 'comuna', 'ica', 'fecha', 'correo' ])

    #crearTabla(aireDataFrame,"datosAire")



    #Limpiando el dataframe
    #reemplazando valores
    aireDataFrame.replace('sin',pd.NA,inplace=True)
    #elimino registros que no cumplen el criterio
    aireDataFrame.dropna(inplace=True)

    


    #filtrar Datos 
    #filtrar es aplicar condiciones logicas
    #que permiten analizar la informacion del DF
    filtroCalidadAireBueno = aireDataFrame.query('(ica>=10)and(ica<40)')
    filtroCalidadAireAceptable = aireDataFrame.query('(ica>=40)and(ica<50)')
    filtroCalidadAireMala = aireDataFrame.query('(ica>=50)and(ica<100)')

    #ORDENAR LOS DATOS PARA CLASIFICARLOS

    datosOrdenadosAire = aireDataFrame.groupby('comuna')['ica'].mean()
    print(datosOrdenadosAire)

    #Grafico la informacion
    plt.figure(figsize=(20,20))
    datosOrdenadosAire.plot(kind='bar',color='green')
    plt.title('indice de contaminacion por comuna en medellin')
    plt.xlabel('Comuna')
    plt.ylabel('ICA')
    plt.grid(True)
    plt.savefig('./assets/img/calidadaire.png',format='png',dpi=300)

construirAireDataFrame()
