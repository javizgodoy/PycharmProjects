#pide al usuario que acierte el número que has escogido del 1 al 10
#objetivo: practicar "if"

#la función "randint" de random realiza esa función. Hay que pasarle dos parámetros, el intervalo
#Ahora el numero ganador es aleatorio

#if num_escogido == num_ganador:
 #   print("¡Enhorabuena! Has acertado")
#else:
 #   print("Oh, no es ese número. Prueba otra vez")

#Quiero que el programa no se termine hasta que el usuario acierte.
#He leído que "While" puede conseguir eso. Pruebo

import random

num_escogido = int(input("Escribe un número del 1 al 10: "))
num_ganador = random.randint(1, 10)

while num_escogido != num_ganador:
    print("Oh, el número ganador era el {}. Prueba otra vez".format(num_ganador))
    num_escogido = int(input("Escribe otro número del 1 al 10: "))
    num_ganador = random.randint(1, 10)

if num_escogido == num_ganador:
    print("¡Enhorabuena! Has acertado")

#nop, es un bucle infinito.
#Creo que así le propongo un final
#Tengo que volverle a preguntar al usuario otro número
#nop, voy a sacar el acierto del bucle
#bien!
#Hay un modo de que el número ganador varíe de manera aleatoria con cada intento. Voy a probarlo
#a ver ahora
#ais
#toma!