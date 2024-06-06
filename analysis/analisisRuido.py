import pandas as pd
from data.generators.generadorRuido import generadorDatosRuido

def construirContaminacionRuidoDataFrame():
    datosRuido= generadorDatosRuido()
    vehicularDataFrame= pd.DataFrame(datosRuido,columns=["comuna","BDduirnos","BDnocturnos","fecha"])
    print(vehicularDataFrame)
    
    
construirContaminacionRuidoDataFrame()