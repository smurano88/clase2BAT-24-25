"""
#Programa que calcula la división entre dos números
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

while divisor == 0 :
    divisor = int(input("Divisor (no 0): "))
print("El resultado de la división es", dividendo / divisor)

"""
#Programa....
suma = 0
n = float(input("Dame un número: "))

while (n != 0) :
    suma = suma + n
    n = float(input("Dame otro número: "))
print ("La suma es", suma)