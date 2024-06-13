import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorVehicular import generadorVehicular
from helpers.crearTablaHTML import crearTabla

def construirVehicularDataFrame():
    datosVehicular = generadorVehicular()
    VehicularDataFrame = pd.DataFrame(datosVehicular, columns=["municipio", "tipoVehiculo", "tipoCombustible", "nombre", "fecha"])
    
    VehicularDataFrame.replace('sin', pd.NA, inplace=True)
    VehicularDataFrame.dropna(inplace=True)

    # Contar la cantidad de registros para cada tipo de combustible en cada municipio
    datosVehicular = VehicularDataFrame.groupby(['municipio', 'tipoCombustible']).size()

    # Graficar la información
    plt.figure(figsize=(20, 20))
    datosVehicular.unstack().plot(kind='bar', stacked=True, color='green')
    plt.title('Indice de tipo Vehiculo por municipio en Medellín')
    plt.xlabel('Municipio')
    plt.ylabel('Cantidad de Vehiculos')
    plt.grid(True)
    plt.savefig('./assets/img/Vehiculo.png', format='png', dpi=300)

construirVehicularDataFrame()
