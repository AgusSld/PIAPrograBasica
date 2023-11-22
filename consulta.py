import requests

# Función para obtener datos climáticos de una ciudad
def obtener_clima(ciudad):
    # Clave de acceso a la API de Weatherstack
    api_key = "Ingresa tu APIKEY"
    
    # Construir la URL de la API con la clave de acceso y la ciudad proporcionada
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={ciudad}"

    try:
        # Enviar solicitud GET a la API de Weatherstack
        response = requests.get(url)
        
        # Convertir la respuesta a formato JSON
        data = response.json()

        # Verificar si la solicitud fue exitosa (código de estado HTTP 200)
        if response.status_code == 200:
            # Verificar si las claves 'current' y 'temperature' están presentes en la respuesta
            if "current" in data and "temperature" in data["current"]:
                # Extraer datos relevantes de la respuesta JSON
                temperatura = data["current"]["temperature"]
                sensacion_termica = data["current"]["feelslike"]
                porcentaje_precipitacion = data["current"]["precip"]
                humedad = data["current"]["humidity"]
                velocidad_viento = data["current"]["wind_speed"]

                # Imprimir la información del clima en la consola
                print("La temperatura en", ciudad, "es", temperatura, "°C.")
                print("Sensación térmica:", sensacion_termica, "°C")
                print("Porcentaje de precipitación:", porcentaje_precipitacion, "%")
                print("Humedad:", humedad, "%")
                print("Velocidad del viento:", velocidad_viento, "km/h")

                # Devolver un diccionario con los datos climáticos
                return {
                    "temperatura": temperatura,
                    "sensacion_termica": sensacion_termica,
                    "porcentaje_precipitacion": porcentaje_precipitacion,
                    "humedad": humedad,
                    "velocidad_viento": velocidad_viento
                }
            else:
                # Manejar el caso en que la respuesta no contiene la información esperada
                print(f"Error al obtener el pronóstico para {ciudad}: La respuesta de la API no contiene la información esperada.")
                print(f"Respuesta completa de la API: {data}")  # Agregar esta línea para obtener más información
                return None
        else:
            # Manejar el caso en que la respuesta no es exitosa
            print(f"Error al obtener el pronóstico para {ciudad}: La respuesta de la API no contiene la información esperada.")
            print(f"Respuesta completa de la API: {str(data)[:200]}")  # Imprimir los primeros 200 caracteres de la respuesta
            return None
    except Exception as e:
        # Manejar excepciones durante la solicitud a la API
        print(f"Error al obtener el pronóstico para {ciudad}: {str(e)}")
        return None
