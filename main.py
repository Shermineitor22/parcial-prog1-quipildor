from validaciones import crear_lista, validar_alumnos, validar_entero
from procesamiento import (
    cargar_listas,
    listar_alumnos,
    buscar_alumno,
    procesar_nombre_usuario,
    mostrar_ranking_ordenado,
    imprimir_estadisticas,
)


def main() -> None:
    """Función principal que gestiona el menú interactivo del sistema escolar."""
    cantidad = 0
    opcion = -1
    nombres = [""]
    parcial1 = [0]
    parcial2 = [0]
    promedios = [0.0]

    # Bucle principal del sistema
    while opcion != 0:
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
                cantidad = validar_alumnos()

                nombres = crear_lista(cantidad, "")
                parcial1 = crear_lista(cantidad, 0)
                parcial2 = crear_lista(cantidad, 0)
                promedios = crear_lista(cantidad, 0.0)

                # Paso 2: Cargar y procesar notas
                cargar_listas(cantidad, nombres, parcial1, parcial2, promedios)

            case 2:
                # Mostrar listado completo de alumnos y notas
                listar_alumnos(cantidad, nombres, parcial1, parcial2, promedios)

            case 3:
                # Calcular e imprimir reporte de estadísticas globales
                imprimir_estadisticas(cantidad, nombres, promedios)

            case 4:
                # Mostrar el ranking ordenado mediante listas copia estáticas
                mostrar_ranking_ordenado(cantidad, nombres, promedios)

            case 5:
                # Búsqueda interactiva de alumno por nombre y notas
                buscar_alumno(cantidad, nombres, parcial1, parcial2, promedios)

            case 6:
                # Juego de nombres y contador de vocales 
                procesar_nombre_usuario(nombres, cantidad)

            case 0:
                print("\nSaliendo del sistema... ¡Hasta luego!")

            case _:
                print("\nOpción inválida. Por favor, seleccione una opción correcta.")


# Punto de entrada estándar del programa
# if __name__ == "__main__":

main()