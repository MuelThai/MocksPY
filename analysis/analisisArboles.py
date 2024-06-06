import pandas as pd
from data.generators.generadorArboles import listaDatosArboles
def construirSiembraArbolesDataFrame():
    datosSiembraArboles= listaDatosArboles()
    SiembraArbolesDataFrame= pd.DataFrame(datosSiembraArboles,columns=["corregimiento","hectareasSembradas","nombres","fecha"])
    print(SiembraArbolesDataFrame)
    
    
construirSiembraArbolesDataFrame()