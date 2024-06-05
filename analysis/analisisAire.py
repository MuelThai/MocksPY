import pandas as pd 

from data.generators.generadorAire import generarDatosCalidadAire
from helpers.crearTablaHTML import crearTabla

def construirAireDataFrame():
    datosAires=generarDatosCalidadAire()


    aireDataFrame = pd.DataFrame(datosAires,columns=['nombre', 'comuna', 'ica', 'fecha', 'correo' ])

    crearTabla(aireDataFrame,"datosAire")

    print(aireDataFrame)

construirAireDataFrame()
