#Escribe un programa que convierta grados en ºF a ºC
#La fórmula es Fahrenheit - 32 * 5/9

TempFar = int(input("Escribe la temperatura en ºF: "))
TempCel = (TempFar - 32) * 5 / 9

print("{} ºF equivalen a {}ºC".format(TempFar, TempCel))