# Colores ANSI para la terminal
VERDE = "\033[32m"   # Color verde
ROJO = "\033[31m"    # Color rojo
AMARILLO = "\033[33m" # Color amarillo
RESET = "\033[0m"    # Resetear color
# Número de líneas en blanco que deseas imprimir
numero_de_lineas = 5

# Imprimir líneas en blanco a principio
for _ in range(numero_de_lineas):
    print()

def dibujar_arbol(nivel):

    #Estrella central
    print(' ' * (nivel-1)+AMARILLO+'*'+RESET)
    # Dibuja el árbol
    for i in range(nivel):
        espacios = ' ' * (nivel - i - 1)  # Espacios para centrar el árbol
        hojas = '*' * (2 * i + 1)         # Hojas del árbol
        print(espacios+VERDE+ hojas+RESET)

    # Dibuja el tronco
    tronco_espacios = ' ' * (nivel - 6)
    tronco = '*' * (nivel//2)
    for i in range (nivel//5) :
        print(tronco_espacios+ROJO + tronco+RESET)


# Llamar a la función
dibujar_arbol(20)

# Imprimir líneas en blanco al fin 
for _ in range(numero_de_lineas):
    print()