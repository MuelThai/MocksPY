import random

def listaDatosArboles():

    datosSiembraArboles=[]
    for i in range (200):
        corregimiento=random.randint(1,14)
        hectareasSemabradas=random.randint(1,5)
        nombres=random.choice(['carlos capeto',"daniel caballero","tomas vargas","ana montes","luisa carmona"])
        fecha=random.choice(["12-04-23","12-04-24","12-04-25"])


        encuesta=[corregimiento,hectareasSemabradas,nombres,fecha]

        datosSiembraArboles.append(encuesta)

    return datosSiembraArboles










# Siembra de arboles
""" corregimiento
hectareassembradas
nombres
fecha
correo """