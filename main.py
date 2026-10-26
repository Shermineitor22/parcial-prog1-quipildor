from validaciones import validar_entero
from procesamiento import (
    inicializar_y_cargar_curso,
    listar_alumnos,
    buscar_alumno,
    procesar_nombre_usuario,
    mostrar_ranking_ordenado,
    imprimir_estadisticas,
)


def main() -> None:
    """Función principal que gestiona el menú interactivo del sistema escolar."""
    cantidad = 0
    nombres = [""]
    parcial1 = [0]
    parcial2 = [0]
    promedios = [0.0]
    salir = False

    # Bucle principal del sistema
    while not salir:
        print("\n===== NOTAFÁCIL =====")
        print("1. Cargar alumnos")
        print("2. Mostrar listado")
        print("3. Mostrar estadísticas")
        print("4. Ver ranking (ordenado)")
        print("5. Buscar alumno")
        print("6. Juegos con un nombre")
        print("0. Salir")

        opcion = validar_entero("Seleccione una opción: ")

        match opcion:
            case 1:
                # Paso 1: Validar cantidad de alumnos e inicializar listas paralelas
                cantidad, nombres, parcial1, parcial2, promedios = inicializar_y_cargar_curso()

            case 2:
                # Mostrar listado completo de alumnos y notas
                resultado_listado = listar_alumnos(cantidad, nombres, parcial1, parcial2, promedios)
                print(resultado_listado)

            case 3:
                # Calcular e imprimir reporte de estadísticas globales
                resultado_estadisticas = imprimir_estadisticas(cantidad, nombres, promedios)
                print(resultado_estadisticas)

            case 4:
                # Mostrar el ranking ordenado mediante listas copia estáticas
                resultado_ranking = mostrar_ranking_ordenado(cantidad, nombres, promedios)
                print(resultado_ranking)

            case 5:
                # Búsqueda de alumno por nombre y notas
                resultado_busqueda = buscar_alumno(cantidad, nombres, parcial1, parcial2, promedios)
                print(resultado_busqueda)

            case 6:
                # Juego de nombres y contador de vocales 
                resultado_juego = procesar_nombre_usuario(nombres, cantidad)
                print(resultado_juego)

            case 0:
                print("\nSaliendo del sistema... ¡Hasta luego!")
                salir = True

            case _:
                print("\nOpción inválida. Por favor, seleccione una opción correcta.")


# Punto de entrada estándar del programa
if __name__ == "__main__":
    main()