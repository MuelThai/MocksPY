import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorReciclaje import generadorReciclaje
from helpers.crearTablaHTML import crearTabla

def construirReciclajeDataFrame():
    datosReciclajes = generadorReciclaje()
    ReciclajeDataFrame = pd.DataFrame(datosReciclajes, columns=["barrio", "tipoReciclaje", "tiempoSemana", "nombre"])
    
    ReciclajeDataFrame.replace('sin', pd.NA, inplace=True)
    ReciclajeDataFrame.dropna(inplace=True)

    # Contar la cantidad de registros para cada tipo de reciclaje en cada barrio
    datosOrdenadosReciclaje = ReciclajeDataFrame.groupby(['barrio', 'tipoReciclaje']).size()

    # Graficar la información
    plt.figure(figsize=(20, 20))
    datosOrdenadosReciclaje.unstack().plot(kind='bar', stacked=True, color='green')
    plt.title('Indice de Reciclajes por barrio en Medellín')
    plt.xlabel('Barrio')
    plt.ylabel('Reciclaje')
    plt.grid(True)
    plt.savefig('./assets/img/Reciclaje.png', format='png', dpi=300)

construirReciclajeDataFrame()
