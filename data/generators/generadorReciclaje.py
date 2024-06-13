import random

def generadorReciclaje():

    listaReciclaje=[]
    for i in range(200):
        barrio=random.choice(["Prados", "La inmaculada", "trapiche", "la doctora", "holanda"])
        tipoReciclaje=random.choice(["carton","plastico","vidrios","metales"])
        tiempoSemana=random.randint(1,4)
        nombre=random.choice(["melisa agudelo","cristian narvaez","jhon agustin","claudia mora"])


        encuesta=[barrio,tipoReciclaje,tiempoSemana,nombre]

        listaReciclaje.append(encuesta)
    
    return listaReciclaje

print(generadorReciclaje())




















#Reciclaje
""" barrio
tiporeciclaje
tiempo
nombre
fecha
 """
