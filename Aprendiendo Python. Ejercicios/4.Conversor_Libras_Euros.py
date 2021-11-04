Cantidad_Libras = float(input("Introduce la cantidad de libras que quieres cambiar: "))
Valor_de_Cambio = 0.85
print("Valor de cambio: 1 € = {} libras".format(Valor_de_Cambio))

Cantidad_Euros = Cantidad_Libras / Valor_de_Cambio
# Si fuera de euros a libras, habría que multiplicar la cantidad de euros por el valor de cambio.
# Podríamos preguntar el valor de cambio

print("Tu dinero en libras equivale a {} €".format(Cantidad_Euros))
