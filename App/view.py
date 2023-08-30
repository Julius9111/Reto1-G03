﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
   
    control = controller.new_controller()
    return control






def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    results, goalscorers, shootouts = controller.load_data(control)
    print("Primeros y ultimos 3 resultados: \n")

    file1 = 'results'
    r1 = controller.get_data(control,file1, 1)
    r2 = controller.get_data(control,file1, 2)
    r3 = controller.get_data(control,file1, 3)
    lr1 = controller.get_data(control,file1, (results))
    lr2 = controller.get_data(control,file1, (results - 1))
    lr3 = controller.get_data(control,file1, (results - 2))
    table_results =[r1, r2, r3, lr3, lr2, lr1]
    print(tabulate(table_results, headers="keys", tablefmt="fancy"), "\n")


    print("Primeros y ultimos 3 anotadores: \n")
    file2 = "goalscorers"

    g1 = controller.get_data(control, file2, 1)
    g2 = controller.get_data(control, file2, 2)
    g3 = controller.get_data(control, file2, 3)
    lg1 = controller.get_data(control, file2, (goalscorers))
    lg2 = controller.get_data(control, file2, (goalscorers -1))
    lg3 = controller.get_data(control, file2, (goalscorers - 2))
    table_goalscorers = [g1, g2, g3, lg3, lg2, lg1]
    print(tabulate(table_goalscorers, headers="keys", tablefmt="fancy"), "\n")

    print("Primeros y ultimos 3 goles:\n")
    file3 = "shootouts"

    s1 = controller.get_data(control, file3, 1)
    s2 = controller.get_data(control, file3, 2)
    s3 = controller.get_data(control, file3, 3)
    ls1 = controller.get_data(control, file3, (shootouts))
    ls2 = controller.get_data(control, file3, (shootouts -1))
    ls3 = controller.get_data(control, file3, (shootouts - 2))
    table_shootouts = [s1, s2, s3, ls3, ls2, ls1]
    print(tabulate(table_shootouts, headers="keys", tablefmt="fancy"), "\n")

    
    return results, goalscorers, shootouts


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            rsize, gsize, ssize = load_data(control)
            print('Total de encuentros cargados: ' + str(rsize))
            print('Total de anotaciones cargadas: ' + str(gsize))
            print('Total de goles marcados desde el punto penal cargados: ' + str(ssize))
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
