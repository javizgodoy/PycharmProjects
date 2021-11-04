numero1 = int(input("Elige un número: "))
numero2 = int(input("Elige otro número: "))
numero3 = int(input("Elige último número: "))

#print(numero1, numero2, numero3)
#numero_max = max(numero1,numero2,numero3)
#numero_min = min(numero1,numero2,numero3)
#print("tu número máximo es ", numero_max)
#print("tu número min es ", numero_min)

#Se puede concatenar un string con un int a través de corchetes + .format(sustituto de corchetes)

print("El número mayor es {}".format(max(numero1, numero2,numero3)))
print("El número menor es {}".format(min(numero1, numero2,numero3)))

#el proceso empieza con el máximo de los tres números, luego lo formatea en los corchetes y luego se imprime el texto
#con el resultado del formateo. Se lee de derecha a izquiera, como el árabe