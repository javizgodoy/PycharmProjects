#numero_ganador = int(3)
#numero_escogido = int(input("Elige un número del 1 al 10: "))

#Se puede hacer de otra forma:
#la librería Random es útil para generar números aleatorios

import random

# la funcion randint da números aleatorios y pide dos parámetros, el intervalo de números que elegir:

numero_ganador = random.randint(1, 10)
numero_escogido = int(input("Elige un número del 1 al 10: "))

while numero_escogido != numero_ganador:
    print("Oh, el número ganador era {}. Prueba otra vez".format(numero_ganador))
    numero_ganador = random.randint(1, 10)
    numero_escogido = int(input("Elige un número del 1 al 10: "))

if numero_escogido == numero_ganador:
    print("¡Enhorabuena, has acertado! Menuda suerte ¡Ni te la crees! ")






