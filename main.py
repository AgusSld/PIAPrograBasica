# Importar funciones y módulos necesarios
from consulta import obtener_clima
from excel_utils import crear_libro, guardar_estadisticas, guardar_libro, calcular_estadisticas
from graficas import graficar_estadisticas
import datetime
import os

# Crear carpetas para almacenar archivos si no existen
carpeta_consultas = 'Consultas'
if not os.path.exists(carpeta_consultas):
    os.makedirs(carpeta_consultas)

carpeta_reporte = 'Reporte'
if not os.path.exists(carpeta_reporte):
    os.makedirs(carpeta_reporte)

# Función para guardar datos climáticos en un archivo
def guardar_datos(ciudad, datos):
    nombre_archivo = os.path.join('Consultas', 'datos_clima.txt')

    try:
        # Obtener la hora actual en el formato deseado
        hora_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Abrir el archivo en modo 'a' (append) para agregar datos al final
        with open(nombre_archivo, "a") as archivo:
            archivo.write("Ciudad: " + ciudad + "\n")
            archivo.write("Hora de consulta:" + hora_actual + "\n")
            archivo.write("Temperatura: {}°C\n".format(datos["temperatura"]))
            archivo.write("Sensación térmica: {}°C\n".format(datos["sensacion_termica"]))
            archivo.write("Porcentaje de precipitación: {}%\n".format(datos["porcentaje_precipitacion"]))
            archivo.write("Humedad: {}%\n".format(datos["humedad"]))
            archivo.write("Velocidad del viento: {} km/h\n".format(datos["velocidad_viento"]))
            archivo.write("\n")  

        print("Datos guardados en", nombre_archivo)
    except Exception as e:
        print("Error al guardar los datos:", str(e))

# Función para ver datos guardados en un archivo
def ver_datos_guardados():
    nombre_archivo = os.path.join('Consultas', 'datos_clima.txt')

    try:
        # Abrir el archivo en modo 'r' (read) para leer su contenido
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print("Datos almacenados en el archivo:\n")
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe o está vacío.")
    except Exception as e:
        print("Error al leer los datos:", str(e))

# Función para guardar consultas numéricas en un archivo
def guardar_consulta_numerica(ciudad, datos):
    nombre_archivo = os.path.join('Consultas', 'consultas_numericas.txt')

    try:
        # Abrir el archivo en modo 'a' (append) para agregar datos al final
        with open(nombre_archivo, "a") as archivo:
            archivo.write("Consulta para {}: \n".format(ciudad))
            archivo.write("Temperatura: {}\n".format(datos["temperatura"]))
            archivo.write("Sensación térmica: {}\n".format(datos["sensacion_termica"]))
            archivo.write("Porcentaje de precipitación: {}\n".format(datos["porcentaje_precipitacion"]))
            archivo.write("Humedad: {}\n".format(datos["humedad"]))
            archivo.write("Velocidad del viento: {}\n".format(datos["velocidad_viento"]))
            archivo.write("\n")

        print("Consulta para {} guardada en {}".format(ciudad, nombre_archivo))
    except Exception as e:
        print("Error al guardar la consulta para {}: {}".format(ciudad, str(e)))

# Función principal que ejecuta el menú
def menu():
    while True:
        print("\nMenú:")
        print("1. Ver pronóstico")
        print("2. Ver consultas almacenadas")
        print("3. Análisis estadístico")
        print("4. Graficar los datos estadísticos")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Obtener la ciudad del usuario
            ciudad = input("Ingresa la ciudad para ver el pronóstico: ")
            try:
                # Obtener datos climáticos
                datos_clima = obtener_clima(ciudad)
                if datos_clima is not None:
                    guardar = input("¿Quieres guardar estos datos? (si/no): ")
                    if guardar.lower() == "si":
                        # Guardar datos y consulta numérica
                        guardar_datos(ciudad, datos_clima)
                        guardar_consulta_numerica(ciudad, datos_clima)

                else:
                    print("No se pudo obtener el pronóstico para la ciudad", ciudad)
            except Exception as e:
                print("Error al obtener el pronóstico para {}: {}".format(ciudad, str(e)))

        elif opcion == "2":
            # Ver datos almacenados
            ver_datos_guardados()
             
        elif opcion == "3":
            # Realizar análisis estadístico
            datos_por_parametro = calcular_estadisticas()
            libro_excel = crear_libro()
            guardar_estadisticas(libro_excel, datos_por_parametro)
            guardar_libro(libro_excel)

        elif opcion == "4":
            # Graficar los datos estadísticos
            graficar_estadisticas(datos_por_parametro)

        elif opcion == "0":
            # Salir del programa
            print("Se terminó el programa")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    # Ejecutar el menú cuando el script es ejecutado directamente
    menu()