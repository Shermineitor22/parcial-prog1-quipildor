"""Módulo de procesamiento y estadísticas para el proyecto NotaFácil.

Contiene funciones individuales para la carga de datos, cálculos matemáticos,
estadísticas globales, ordenamiento burbuja y utilidades de texto.
"""

from validaciones import validar_nombre, validar_nota, validar_entero 


def cargar_listas(cantidad: int, nombres: list, parcial1: list, parcial2: list, promedios: list) -> None:
    """Solicita y valida de forma interactiva los nombres y las notas 

    de los dos parciales para cada alumno, calculando su promedio.

    Args:
        cantidad (int): Cantidad de alumnos a cargar.
        nombres (list): Lista donde se guardarán los nombres.
        parcial1 (list): Lista donde se guardarán las notas del primer parcial.
        parcial2 (list): Lista donde se guardarán las notas del segundo parcial.
        promedios (list): Lista donde se guardarán los promedios calculados.
    """
    for i in range(cantidad):
        print("\nRecorda que el nombre del alumno debe tener al menos 5 caracteres y contener solo letras y/o espacio.") 

        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
        while not validar_nombre(nombre):  
            print("Nombre del alumno inválido.")
            nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
        nombres[i] = nombre

        nota_parcial1 = validar_entero(f"Ingrese la nota del primer parcial de {nombre}: ")
        while not validar_nota(nota_parcial1):
            print("Nota inválida, ingrese una nota entre 0 y 10.")
            nota_parcial1 = validar_entero(f"Ingrese la nota del primer parcial de {nombre}: ")
        parcial1[i] = nota_parcial1

        nota_parcial2 = validar_entero(f"Ingrese la nota del segundo parcial de {nombre}: ")
        while not validar_nota(nota_parcial2):
            print("Nota inválida, ingrese una nota entre 0 y 10.")
            nota_parcial2 = validar_entero(f"Ingrese la nota del segundo parcial de {nombre}: ")
        parcial2[i] = nota_parcial2

        promedios[i] = (parcial1[i] + parcial2[i]) / 2

    print("\nCarga de alumnos se realizo con éxito")


def listar_alumnos(cantidad: int, nombres: list, parcial1: list, parcial2: list, promedios: list) -> None:
    """Muestra en pantalla el listado completo de alumnos junto con sus notas 

    de parciales y promedios individuales.

    Args:
        cantidad (int): Cantidad total de alumnos cargados.
        nombres (list): Lista de nombres.
        parcial1 (list): Lista de notas del primer parcial.
        parcial2 (list): Lista de notas del segundo parcial.
        promedios (list): Lista de promedios.
    """
    if cantidad == 0:
        print("\nNo hay alumnos cargados en el sistema.")
        return

    print("\n LISTADO DE ALUMNOS Y SUS NOTAS ")
    for i in range(len(nombres)):
        print(f"Alumno: {nombres[i]}")
        print(f"Nota del primer parcial: {parcial1[i]} . Nota del segundo parcial: {parcial2[i]}")
        print(f"Su promedio es: {promedios[i]}")


def promediar_curso(cantidad: int, promedios: list[float | int]) -> None:
    """Calcula y muestra el promedio general de todo el curso a partir 

    de los promedios individuales de los alumnos.

    Args:
        cantidad (int): Cantidad total de alumnos cargados en el sistema.
        promedios (list[float | int]): Lista que contiene los promedios de cada alumno.
    """
    promedio_alumnos = 0.0
    promedio_general = 0.0

    for i in range(cantidad):
        promedio_alumnos += promedios[i]

    promedio_general = promedio_alumnos / cantidad
    print(f"El promedio general del curso es de: {promedio_general}")


def obtener_mejor_y_peor_promedio(cantidad: int, nombres: list[str], promedios: list[float | int]) -> None:
    """Encuentra y muestra el o los alumnos con el mejor y peor promedio,

    gestionando empates sin utilizar métodos dinámicos.

    Args:
        cantidad (int): Cantidad total de alumnos cargados en el sistema.
        nombres (list[str]): Lista que contiene los nombres de los alumnos.
        promedios (list[float | int]): Lista que contiene los promedios de los alumnos.
    """

    mejor_promedio = promedios[0]
    peor_promedio = promedios[0]

    for i in range(1, cantidad):
        if promedios[i] > mejor_promedio:
            mejor_promedio = promedios[i]
        if promedios[i] < peor_promedio:
            peor_promedio = promedios[i]

    print("\n EXTREMOS DEL CURSO ")

    print(f"Mejor/es promedio/s ({mejor_promedio}):")
    for i in range(cantidad):
        if promedios[i] == mejor_promedio:
            print(f"Nombre: {nombres[i]} y su promedio es: {promedios[i]}")

    print(f"Peor/es promedio/s ({peor_promedio}):")
    for i in range(cantidad):
        if promedios[i] == peor_promedio:
            print(f"Nombre: {nombres[i]} y su promedio es: {promedios[i]}")


def contar_condiciones_alumnos(cantidad: int, promedios: list[float | int]) -> None:
    """Cuenta y muestra la cantidad de alumnos según su condición académica:

    Promociona (>= 6), Aprueba (>= 4 y < 6) y Desaprueba (< 4).

    Args:
        cantidad (int): Cantidad total de alumnos cargados en el sistema.
        promedios (list[float | int]): Lista que contiene los promedios de los alumnos.
    """
    promocionan = 0
    aprueban = 0
    desaprueban = 0

    for i in range(cantidad):
        if promedios[i] >= 6:
            promocionan += 1
        elif promedios[i] >= 4:
            aprueban += 1
        else:
            desaprueban += 1

    print("\n ESTADO ACADÉMICO DE LOS ALUMNOS ")
    print(f"Los Alumnos que promocionan son (promedio mayores a 6): {promocionan}")
    print(f"Los Alumnos que aprueban son (promedio entre 4 y 6): {aprueban}")
    print(f"Los Alumnos que desaprueban son (promedio menores a 4): {desaprueban}")


def imprimir_estadisticas(cantidad: int, nombres: list[str], promedios: list[float | int]) -> None:
    """Función unificadora que imprime todas las estadísticas globales del curso,

    incluyendo el promedio general, extremos e informe de condiciones.

    Args:
        cantidad (int): Cantidad total de alumnos cargados.
        nombres (list[str]): Lista de nombres de alumnos.
        promedios (list[float | int]): Lista de promedios.
    """
    if cantidad == 0:
        print("\nNo hay alumnos cargados en el sistema.")
        return

    print("\n ESTADÍSTICAS DEL CURSO ")
    promediar_curso(cantidad, promedios)
    obtener_mejor_y_peor_promedio(cantidad, nombres, promedios)
    contar_condiciones_alumnos(cantidad, promedios)


def mostrar_ranking_ordenado(cantidad: int, nombres: list[str], promedios: list[float | int]) -> None:
    """Genera y muestra un ranking ordenado de los alumnos del mejor al peor promedio

    utilizando el algoritmo de ordenamiento burbuja en listas copia paralelas.

    Args:
        cantidad (int): Cantidad total de alumnos cargados en el sistema.
        nombres (list[str]): Lista que contiene los nombres de los alumnos.
        promedios (list[float | int]): Lista que contiene los promedios de los alumnos.
    """
    if cantidad == 0:
        print("\nNo hay alumnos cargados en el sistema.")
        return

    # Declaración de variables ordenadas una debajo de la otra
    aux_nombre = ""
    aux_promedios = 0.0
    nombres_copia = [""] * cantidad
    promedios_copia = [0.0] * cantidad

    # Copia estática para no alterar el orden original de las listas del curso
    for i in range(cantidad):
        nombres_copia[i] = nombres[i]
        promedios_copia[i] = promedios[i]

    # Algoritmo de ordenamiento burbuja adaptado con la estructura del profesor
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if promedios_copia[j] < promedios_copia[j + 1]:
                aux_promedios = promedios_copia[j]
                aux_nombre = nombres_copia[j]

                promedios_copia[j] = promedios_copia[j + 1]
                promedios_copia[j + 1] = aux_promedios

                nombres_copia[j] = nombres_copia[j + 1]
                nombres_copia[j + 1] = aux_nombre

    # Impresión del ranking ordenado en pantalla
    print("\n RANKING DE ALUMNOS (MEJOR A PEOR PROMEDIO) ")
    for i in range(cantidad):
        print(f"{i + 1}. Alumno: {nombres_copia[i]} con un Promedio: {promedios_copia[i]:.2f}")



def buscar_alumno(cantidad: int, nombres: list[str], parcial1: list[int], parcial2: list[int], promedios: list[float | int]) -> None:
    """Busca un alumno por su nombre en las listas paralelas. 

    Si lo encuentra, muestra sus notas y su promedio; 
    si no, vuelve a solicitar el nombre hasta verificar que existe.

    Args:
        cantidad (int): Cantidad total de alumnos cargados en el sistema.
        nombres (list[str]): Lista que contiene los nombres de los alumnos.
        parcial1 (list[int]): Lista que contiene las notas del primer parcial.
        parcial2 (list[int]): Lista que contiene las notas del segundo parcial.
        promedios (list[float | int]): Lista que contiene los promedios de los alumnos.
    """
    encontrado = False
    nombre_a_buscar = ""

    if cantidad == 0:
        print("\nNo hay alumnos cargados en el sistema.")
        return

    while not encontrado:
        nombre_a_buscar = input("Ingrese el nombre del alumno que desea buscar: ")

        for i in range(cantidad):

            if nombre_a_buscar == nombres[i]:
                print("\n ALUMNO ENCONTRADO ")
                print(f"Alumno: {nombres[i]}")
                print(f"Su nota en el primer parcial: {parcial1[i]} y en el segundo parcial: {parcial2[i]}")
                print(f"Su promedio es: {promedios[i]:.2f}")
                encontrado = True

        if not encontrado:
            print("\nEl alumno no fue cargado al sistema, intente nuevamente.")


def procesar_nombre_usuario(lista_nombres: list[str], cantidad: int) -> None:
    """Pide al usuario un nombre de alumno, valida mediante un bucle que 

    el nombre pertenezca a la lista utilizando la cantidad, lo invierte
    carácter por carácter utilizando el método del profesor y cuenta 
    la cantidad total de vocales (mayúsculas y minúsculas).

    Args:
        lista_nombres (list[str]): Lista que contiene los nombres de los alumnos.
        cantidad (int): Número entero que indica cuántos alumnos están cargados.
    """
    if cantidad == 0:
        print("\nNo hay alumnos cargados en el sistema.")
        return

    encontrado = False
    nombre = ""
    nombre_invertido = ""
    vocales_min = "aeiou"
    vocales_mayus = "AEIOU"
    total_vocales = 0

    while not encontrado:
        nombre = input("\nIngrese el nombre del alumno para el juego: ")
        for i in range(cantidad):
            if lista_nombres[i] == nombre:
                encontrado = True
                break

        if not encontrado:
            print("Error: El alumno no se encuentra en el listado. Intente nuevamente.")

    for i in nombre:
        nombre_invertido = i + nombre_invertido

    for i in range(len(nombre)):
        caracter = nombre[i]

        for min in range(len(vocales_min)):
            if caracter == vocales_min[min]:
                total_vocales += 1
                break

        for mayus in range(len(vocales_mayus)):
            if caracter == vocales_mayus[mayus]:
                total_vocales += 1
                break

    print(f"\n JUEGO CON EL NOMBRE ")
    print(f"Nombre del alumno: {nombre}")
    print(f"Nombre invertido: {nombre_invertido}")
    print(f"Cantidad total de vocales: {total_vocales}")