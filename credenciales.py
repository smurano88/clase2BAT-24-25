#Función que pinta el menú en pantalla
def menu():   
    print("")
    print("==================") 
    print("       MENÚ ") 
    print("==================") 
    print(" 1. Lo que sea 1") 
    print(" 2. Lo que sea 2")
    print(" 3. Lo que sea 3") 
    print(" 4. Salir") 
    print("")  

#Pintamos menús
menu()
#Pedimos opción al usuario
opcion = input("Elige opción: ")  

while opcion != '4': 

    #Opción 1 - Saludo según idioma elegido 

    if opcion == '1': 
        print("-----------------------")
        print(">>>Lo que sea opción 1")
        print("-----------------------")
    
    #Opción 2: Mostrar número de estrellas según elección usuario
    elif opcion == '2': 
        
        print("-----------------------")
        print(">>>Lo que sea opción 2")
        print("-----------------------")

    #Opción 3: Escalera de estrellas según número elegido
    elif opcion == '3':     
        
        print("-----------------------")
        print(">>>Lo que sea opción 3")
        print("-----------------------")

    else: 
        
        print("")
        print("^^^^^ Opción incorrecta ^^^^^") 

    #Volvemos a mostrar menú y pedimos nueva opción hasta que el user pulse 4
    print("")    
    menu()
    opcion = input("Elige otra opción: ") 

#Hemos pulsado 4 y acaba el programa
print("")    
print("--- Fin del programa ---")
print("")