"""Módulo de validaciones para el proyecto NotaFácil.

Contiene funciones robustas para validar la cantidad de alumnos,
los nombres, las notas y la creación estática de listas paralelas.
"""


def validar_entero(mensaje: str) -> int:
    """Solicita y valida por teclado que el valor ingresado sea un número entero,

    verificando carácter por carácter.

    Args:
        mensaje (str): El texto que se muestra en pantalla al solicitar el dato.

    Returns:
        int: El número entero validado correctamente.
    """
    valido = False
    cantidad = ""

    while not valido:
        cantidad = input(mensaje)    
        if len(cantidad) == 0:
            print("Error, no ingresó nada. Intente de nuevo.")
            continue  

        valido = True
        for i in range(len(cantidad)):
            caracter = cantidad[i]
            if not ("0" <= caracter <= "9"):
                valido = False
                print("Error: debe ingresar un carácter entero válido del 0 al 9.")
                break  

    return int(cantidad)


def validar_alumnos() -> int:
    """Solicita la cantidad de alumnos y valida que se encuentre

    dentro del rango permitido (1 a 30).

    Returns:
        int: La cantidad de alumnos validada correctamente dentro del rango.
    """
    valido = False
    cantidad = 0

    while not valido:
        cantidad = validar_entero("Ingrese la cantidad de alumnos (1 - 30): ")
        if 1 <= cantidad <= 30:
            valido = True
        else:
            print("Cantidad de alumnos ingresados inválida. Debe ser entre 1 y 30.")

    return cantidad


def crear_lista(cantidad: int, valor_inicial: int | float | str) -> list:
    """Crea una lista repitiendo un valor inicial una cantidad específica de veces,

    utilizando replicación estática (sin métodos dinámicos como append).

    Args:
        cantidad (int): Cantidad de elementos (alumnos) a crear.
        valor_inicial (int | float | str): El valor con el que se rellenará la lista.

    Returns:
        list: Una lista nueva con la cantidad de elementos especificada 
        y rellena con el valor inicial.
    """
    lista = [valor_inicial] * cantidad
    
    return lista


def validar_nombre(nombre: str) -> bool:
    """Valida que un nombre tenga al menos 5 caracteres y contenga

    únicamente letras (mayúsculas o minúsculas) y espacios.

    Args:
        nombre (str): La cadena de texto que representa el nombre a validar.

    Returns:
        bool: True si el nombre cumple con todas las condiciones, 
        False en caso contrario.
    """
    if len(nombre) < 5:
        return False

    for i in range(len(nombre)):
        caracter = nombre[i]
        es_minuscula = "a" <= caracter <= "z"
        es_mayuscula = "A" <= caracter <= "Z"
        tiene_espacio = caracter == " "

        if not (es_minuscula or es_mayuscula or tiene_espacio):
            return False

    return True


def validar_nota(nota: int | float) -> bool:
    """Valida que una nota esté dentro del rango permitido (0 a 10).

    Args:
        nota (int | float): La nota del alumno a validar.

    Returns:
        bool: True si la nota está entre 0 y 10 (inclusive), 
        False en caso contrario.
    """
    if nota < 0 or nota > 10:
        return False
        
    return True