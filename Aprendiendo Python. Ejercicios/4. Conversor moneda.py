#Escribe un programa que convierta cierta cantidad de libras a euros
#Escribe otro programa que convierta cierta cantidad de euros a libras

cantidad_de_libras = float(input("Añade la cantidad de libras que quieres cambiar (separa los decimales con un punto): "))
valor_de_cambio = 0.85
cantidad_en_euros = cantidad_de_libras / valor_de_cambio

print("El valor de cambio actual es de {} libras para cada €".format(valor_de_cambio))
print("Te quedan {} € después de cambiar {} libras". format(cantidad_en_euros, cantidad_de_libras))

cantidad_de_euros = float(input("Añade la cantidad de euros que quieres cambiar a libras (separa los decimales con un punto): "))
cantidad_en_libras = cantidad_de_euros * valor_de_cambio

print("Te quedan {} libras después de cambiar {} €". format(cantidad_en_libras, cantidad_de_euros))

#compruebo