import pandas as pd 

from data.generators.generadorAire import generarDatosCalidadAire

def construirAireDataFrame():
    datosAires=generarDatosCalidadAire()


    aireDataFrame = pd.DataFrame(datosAires,columns=['nombre', ])

    print(aireDataFrame)

construirAireDataFrame()
