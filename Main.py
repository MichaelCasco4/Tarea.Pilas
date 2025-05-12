
from pila import Pila

def menu():
    print("\nSimulación carga y descarga de sacos")
    print("1. Apilar saco")
    print("2. Descargar saco")
    print("3. Ver tope")
    print("4. Salir")

def main():
    pila = Pila()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            saco = input("Ingrese el nombre del saco a apilar: ")
            pila.apilar(saco)
            print(f"Saco '{saco}' apilado.")

        elif opcion == "2":
            saco = pila.descargar()
            if saco:
                print(f"Saco '{saco}' descargado.")
            else:
                print("La pila está vacía. No hay sacos para descargar.")

        elif opcion == "3":
            saco = pila.ver_tope()
            if saco:
                print(f"Saco en el tope: '{saco}'")
            else:
                print("La pila está vacía.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
