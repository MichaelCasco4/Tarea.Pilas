"""Una docente de informática en una secundaria revisa tareas impresas que sus estudiantes colocan
sobre su escritorio. Siempre revisa primero la última tarea entregada. Implementa un sistema que
permita agregar tareas (push), revisar una (pop), y mostrar cuál es la siguiente en revisar (peek),
todo usando una pila."""

from Modulos import Tarea, PilaTareas

#Creacion de menu para el usuario

def mostrar_menu():
    print("-----------MENU DE TAREAS-------------")
    print("1. Agregar una tarea")
    print("2. Revisar una tarea")
    print("3. Ver la siguiente tarea a revisar")
    print("4. Salir del menu")


def main():
    pila = PilaTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripcion de la tarea a revisar: ")
            tarea = Tarea(descripcion)
            pila.push(tarea)

        elif opcion == "2":
            pila.pop()

        elif opcion == "3":
            pila.peek()

        elif opcion == "4":
            print("Saliendo del programa, nos vemos luego...")
            break

        else:
            print("Opción inválida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()

    