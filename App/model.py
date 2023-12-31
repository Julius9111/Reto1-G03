﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from datetime import datetime as dt
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(adt):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {
        'results': None,
        'goalscorers': None,
        'shootouts': None
    }
    data_structs['results'] = lt.newList(datastructure=adt, cmpfunction=cmp_partidos_by_fecha_y_pais)
    data_structs['goalscorers'] = lt.newList(datastructure=adt)
    data_structs['shootouts'] = lt.newList(datastructure=adt)
    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data, file):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs[file], data)
    return data_structs


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, file, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    return lt.getElement(data_structs[file], id)


def data_size(data_structs, file):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs[file])

def get_first_last_three_datastructs(data_structs, file):
    filtered = lt.newList("ARRAY_LIST")
    for i in range(1, 4):
        lt.addLast(filtered, get_data(data_structs, file, i))
    size = data_size(data_structs, file)
    for i in range((size - 2), size + 1):
        lt.addLast(filtered, get_data(data_structs, file, i))

    return filtered

def get_first_last_three_list(list):
    filtered = lt.newList("ARRAY_LIST")
    for i in range(1, 4):
        lt.addLast(filtered, lt.getElement(list, i))
    for i in range(-2, 1):
        lt.addLast(filtered, lt.getElement(list, i))

    return filtered


def req_1(data_structs, team_name, condition):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    t_name = team_name.lower()
    results = data_structs["results"]
    filtered_list = lt.newList("ARRAY_LIST")

    for result in lt.iterator(results):
        if condition == "local":
            if t_name == result["home_team"].lower():
                lt.addLast(filtered_list, result)

        elif condition == "visitante":
            if t_name == result["away_team"].lower():
                lt.addLast(filtered_list, result)
        elif condition == "neutro":
            if (t_name == result["away_team"].lower()) or (t_name == result["home_team"].lower()):
                lt.addLast(filtered_list, result)
    
    return filtered_list



def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def cmp_partidos_by_fecha_y_pais(result1, result2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2,
    en caso de que sean iguales tenga el nombre de la ciudad en que se disputó el partido,
    de lo contrario devuelva falso (False).
    Args:
    result1: información del primer registro de resultados FIFA que incluye 
    “date” y el “country” 
    result2: información del segundo registro de resultados FIFA que incluye 
    “date” y el “country” 
    """
    #TODO: Crear función comparadora para ordenar
    formato_fecha = "%Y-%m-%d"

    fecha1 = result1['date']
    fecha2 = result2['date']

    fecha1 = dt.strptime(fecha1, formato_fecha)
    fecha2 = dt.strptime(fecha2, formato_fecha)

    if fecha1 > fecha2:
        return True
    elif fecha1 < fecha2:
        return False
    else:
        hscore1 = int(result1['home_score'])
        hscore2 = int(result2['home_score'])

        if hscore1 > hscore2:
            return True
        elif hscore1 < hscore2:
            return False
        else:
            ascore1 = int(result1['away_score'])
            ascore2 = int(result2['away_score'])
            if ascore1 > ascore2:
                return True
            else: 
                return False

def cmp_goalscorers(scorer1, scorer2):
    formato_fecha = "%Y-%m-%d"

    fecha1 = scorer1['date']
    fecha2 = scorer2['date']

    fecha1 = dt.strptime(fecha1, formato_fecha)
    fecha2 = dt.strptime(fecha2, formato_fecha)

    if fecha1 > fecha2:
        return True
    elif fecha1 < fecha2:
        return False
    else:
        min1 = (scorer1['minute'])
        min2 = (scorer2['minute'])

        if min1 > min2:
            return True
        elif min1 < min2:
            return False
        else:
            player1 = scorer1['scorer'].lower()
            player2 = scorer2['scorer'].lower()
            if player1 > player2:
                return True
            else:
                return False

def cmp_shootouts(shoot1, shoot2):
    formato_fecha = "%Y-%m-%d"

    fecha1 = shoot1["date"]
    fecha2 = shoot2["date"]

    fecha1 = dt.strptime(fecha1, formato_fecha)
    fecha2 = dt.strptime(fecha2, formato_fecha)

    if fecha1 > fecha2:
        return True
    elif fecha1 < fecha2:
        return False
        
    else: 
        nombre_1_local = shoot1["home_team"].lower()
        nombre_2_local = shoot2["home_team"].lower()

        if nombre_1_local > nombre_2_local:
            return True
        elif nombre_1_local < nombre_1_local:
            return False
        
        else:
            nombre_1_visitante = shoot1["away_team"].lower()
            nombre_2_visitante = shoot2["away_team"].lower()

            if nombre_1_visitante > nombre_2_visitante:
                return True
            elif nombre_1_visitante < nombre_1_visitante:
                return False
        
def sort(data_structs, algorithm):

    if algorithm == 'shell':
        sa.sort(data_structs['results'], cmp_partidos_by_fecha_y_pais)
        #sa.sort(data_structs['goalscorers'], cmp_goalscorers)
        #sa.sort(data_structs['shootouts'], cmp_shootouts)

    elif algorithm == 'insertion':
        ins.sort(data_structs['results'], cmp_partidos_by_fecha_y_pais)
        #ins.sort(data_structs['goalscorers'], cmp_goalscorers)
        #ins.sort(data_structs['shootouts'], cmp_shootouts)
    
    elif algorithm == 'selection':
        se.sort(data_structs['results'], cmp_partidos_by_fecha_y_pais)
        #se.sort(data_structs['goalscorers'], cmp_goalscorers)
        #se.sort(data_structs['shootouts'], cmp_shootouts)
    
    elif algorithm == 'merge':
        merg.sort(data_structs['results'], cmp_partidos_by_fecha_y_pais)
        #merg.sort(data_structs['goalscorers'], cmp_goalscorers)
        #merg.sort(data_structs['shootouts'], cmp_shootouts)
    
    elif algorithm == 'quick':
        quk.sort(data_structs['results'], cmp_partidos_by_fecha_y_pais)
        #quk.sort(data_structs['goalscorers'], cmp_goalscorers)
        #quk.sort(data_structs['shootouts'], cmp_shootouts)
    
    else:
        return None
