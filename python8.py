'''
8.1 Crea un array con los número 10, 20, 30, 40 y 50 y luego muestra los que hay
en las posiciones impares (primero, tercero y quinto: 10, 30 y 50)
Dev: SM
Diciembre 24/25
PRySI II - IES La Nía

'''

#Declaro el array datos
datos = []

#Pido los datos al user
for i in range (0,5):
    datos.append(int(input("Dame un dato: ")))

datos[0] = 500

#Recorro y muestro los datos del array
for i in range (0,5):
    print(datos[i])
