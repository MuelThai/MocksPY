import random

def generadorDatosRuido () :

    lisDatosRuido = []
    for i in range (200):
        comuna=random.choice(["Fátima, Rosales, Belén, Las Playas, La Mota, El Rincón, Altavista, La Palma, El Nogal, Cerro Nutibara"])
        dBdiurnos=random.randint(0,140)
        dbnocturnos=random.randint(0,140)
        fecha=random.choice(['2024-04-15','2024-04-16','2024-04-17'])

        misDatos=[comuna,dBdiurnos,dbnocturnos,fecha]

        lisDatosRuido.append(misDatos)

    return lisDatosRuido

print(generadorDatosRuido()) 
    





#Ruido Ambiental
#""" comuna
#direccion
#decibeliosdiurnos
#decibeliosnocturnos
#fecha """