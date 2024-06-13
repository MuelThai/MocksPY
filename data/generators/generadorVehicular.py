import random

def generadorVehicular():

    listaVehicular=[]
    for i in range(200):
        municipio=random.choice(["Sabaneta", "Envigado", "Poblado", "Bello", "Girardota", "La Estrella"])
        tipoVehiculo=random.choice(["Moto", "Automovil","NPR","Bus","Tractomula"])
        tipoCombustible=random.choice(["ACPM", "Corriente","Premiun","Electrico","Gas"])
        nombre=random.choice(["ana vega", "juan cruz", "gilberto montoya", "cecilia miranda", "paola vera"])
        fecha=random.choice(['2024-03-15','2024-04-16','2024-05-17'])

        encuesta=[municipio,tipoVehiculo,tipoCombustible,nombre,fecha]

        listaVehicular.append(encuesta)

    return listaVehicular

print(generadorVehicular())











    # Contaminacion Vehicular
""" municipio
tipovehiculo
tipocombustible
nombre
fecha """
        