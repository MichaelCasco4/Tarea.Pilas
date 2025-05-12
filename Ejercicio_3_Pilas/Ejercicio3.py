#En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes se 
#almacenan en una pila según el orden en que se procesan. Si ocurre un problema técnico, se debe 
#revertir el último registro. Implementa un sistema para registrar donantes (push), eliminar el último 
#(pop), y mostrar el donante actual en proceso.

from Modulo import PilaDonantes

def menu():
    sistema = PilaDonantes() # Se crea una instancia del sistema
    while True:
        print("\n--- Menú de Donación de Sangre ---")
        print("1. Registrar nuevo donante")
        print("2. Eliminar último donante")
        print("3. Mostrar donante actual en proceso")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")
        # Lógica según la opción elegida
        if opcion == "1":
            nombre = input("Ingrese el nombre del donante: ")
            sistema.push(nombre)
        elif opcion == "2":
            sistema.pop()
        elif opcion == "3":
            sistema.mostrar_donante_actual()
        elif opcion == "4":
            print("Terminando programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú
menu()

