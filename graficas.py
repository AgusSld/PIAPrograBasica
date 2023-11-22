import matplotlib.pyplot as plt
import numpy as np
import os

def graficar_estadisticas(datos_por_parametro):
    # Colores para las barras en las gráficas
    colores = ['#FF9999', '#66B2FF', '#99FF99']

    # Crear la carpeta 'Graficas' si no existe
    carpeta_graficas = 'Graficas'
    if not os.path.exists(carpeta_graficas):
        os.makedirs(carpeta_graficas)

    # Iterar sobre los parámetros y sus datos en el diccionario
    for parametro, datos in datos_por_parametro.items():
        if datos:
            # Crear una figura para la gráfica con un tamaño específico
            plt.figure(figsize=(10, 6))
            
            # Crear barras para el promedio, máximo y mínimo
            bars = plt.bar(['Promedio', 'Máximo', 'Mínimo'], [np.mean(datos), np.max(datos), np.min(datos)], color=colores)

            # Agregar etiquetas con los valores en la parte superior de las barras
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval:.2f}', ha='center', va='bottom', fontsize=10, color='black')

            # Configurar título y etiquetas del eje x e y
            plt.title(f'Estadísticas para {parametro}', fontsize=18, fontweight='bold', color='#333333')
            plt.xlabel('Parámetro', fontsize=14, fontweight='bold', color='#333333')
            plt.ylabel('Valor', fontsize=14, fontweight='bold', color='#333333')
            
            # Configurar el formato y alineación de las etiquetas del eje x
            plt.xticks(rotation=45, ha='right', fontsize=12, color='#555555')
            
            # Configurar el formato de las etiquetas del eje y
            plt.yticks(fontsize=12, color='#555555')
            
            # Agregar una línea de cuadrícula horizontal punteada
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            
            # Agregar una línea horizontal en 0 (línea base)
            plt.axhline(0, color='black', linewidth=0.5)
            
            # Agregar una línea horizontal en la media de los datos con un formato específico
            plt.axhline(np.mean(datos), color='red', linestyle='--', linewidth=2, label='Media')
            
            # Agregar una leyenda en la esquina superior derecha
            plt.legend(fontsize=12, loc='upper right')

            # Ajustar el diseño de la gráfica para evitar superposiciones
            plt.tight_layout()

            # Guardar la gráfica en la carpeta 'Graficas' con un nombre específico
            nombre_grafica = f'grafica_{parametro.lower()}.png'
            ruta_grafica = os.path.join(carpeta_graficas, nombre_grafica)
            plt.savefig(ruta_grafica)

            # Imprimir la ruta de la gráfica guardada
            print(f'Gráfica guardada en: {ruta_grafica}')
            
            # Mostrar la gráfica en la ventana
            plt.show()
            
            # Cerrar la figura para liberar recursos
            plt.close()
        else:
            # Imprimir un mensaje si no hay datos numéricos para el parámetro
            print(f"No hay datos numéricos para {parametro} en el archivo.")
