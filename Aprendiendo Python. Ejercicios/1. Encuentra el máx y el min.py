#Pide al usuario que añada tres números al azar.
#El programa mostrará el número máximo y mínimo

numero_uno = int(input("Escribe un número: "))
numero_dos = int(input("Escribe otro número: "))
numero_tres = int(input("Escribe un último número: "))

numero_maximo = max(numero_uno,numero_dos, numero_tres)
numero_minimo = min(numero_uno,numero_dos, numero_tres)

#print("El número mayor es: ", numero_maximo)
#print("El número menor es: ", numero_minimo)

#Se puede mostrar el resultado de otro modo más rápido: con .format. Sustituye las llaves por los argumentos
#que le demos y en el mismo orden.

print("El número mayor es el {} y el número menor, el {}".format(numero_maximo, numero_minimo))

