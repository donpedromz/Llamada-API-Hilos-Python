# Llamada API Hilos Python

## Descripción

Este proyecto demuestra el uso de **hilos (threads)** en Python para realizar múltiples llamadas a APIs externas de manera concurrente, optimizando el tiempo de ejecución del programa.

El script realiza llamadas paralelas a dos tipos de APIs:
- **API de recomendaciones de películas** (TasteDive): Obtiene recomendaciones de películas similares basadas en un título dado
- **API de validación de números telefónicos** (APILayer): Valida números telefónicos y obtiene información sobre el país, operador y tipo de línea

## Características

- ✅ Ejecución concurrente de múltiples llamadas API usando hilos de Python
- ✅ Manejo de errores y timeouts en las llamadas HTTP
- ✅ Configuración segura mediante variables de entorno
- ✅ Medición del tiempo de ejecución para evaluar el rendimiento

## Requisitos Previos

- Python 3.6 o superior
- Claves API de:
  - [TasteDive API](https://tastedive.com/read/api) (para recomendaciones de películas)
  - [APILayer Numverify](http://apilayer.net/api) (para validación de números telefónicos)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/donpedromz/Llamada-API-Hilos-Python.git
cd Llamada-API-Hilos-Python
```

2. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
```

3. Activar el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instalar las dependencias necesarias:
```bash
pip install requests python-dotenv
```

## Configuración

1. Crear un archivo `.env` en la raíz del proyecto:
```bash
touch .env
```

2. Agregar tus claves API al archivo `.env`:
```
MOVIES_API_KEY=tu_clave_tastedive_aqui
NUMBER_VALIDATION_API_KEY=tu_clave_apilayer_aqui
```

⚠️ **Importante**: Nunca compartas tus claves API públicamente. El archivo `.env` está incluido en `.gitignore` para evitar que se suba al repositorio.

## Uso

Ejecutar el script principal:
```bash
python local_task.py
```

### Salida Esperada

El programa ejecutará cuatro llamadas API de manera concurrente:
1. Recomendaciones de películas para "pride and prejudice"
2. Recomendaciones de películas para "parasites"
3. Validación del número telefónico colombiano: 3043945372
4. Validación del número telefónico colombiano: 3164909496

Al finalizar, mostrará el tiempo total de ejecución con hilos.

## Estructura del Código

### Funciones Principales

- `api_call(url, params, total_timeout=60)`: Función genérica para realizar llamadas HTTP GET a cualquier API
- `movies_api_call(movie_name, limit)`: Llama a la API de TasteDive para obtener recomendaciones de películas
- `number_validation_api_call(phone_number, country_code)`: Llama a la API de validación de números telefónicos

### Implementación de Hilos

El script utiliza el módulo `threading` de Python para ejecutar las llamadas API de manera concurrente:
```python
thread_movies_1 = threading.Thread(target=movies_api_call, args=("pride and prejudice", 5))
thread_movies_1.start()
thread_movies_1.join()  # Espera a que el hilo termine
```

## Dependencias

- `requests`: Para realizar llamadas HTTP a las APIs
- `python-dotenv`: Para cargar variables de entorno desde el archivo `.env`
- `threading`: Módulo estándar de Python para manejo de hilos (incluido)

## Ventajas del Uso de Hilos

En este proyecto, el uso de hilos permite que las llamadas API se ejecuten de manera concurrente en lugar de secuencial, lo que resulta en:

- ⚡ Reducción significativa del tiempo total de ejecución
- 🔄 Mejor aprovechamiento de los tiempos de espera de I/O
- 📊 Mayor eficiencia cuando se trabaja con múltiples APIs

## Notas Técnicas

- El límite de recomendaciones de películas debe estar entre 0 y 20
- Las llamadas API tienen un timeout predeterminado de 60 segundos
- El código incluye manejo básico de errores para capturar excepciones durante las llamadas

## Autor

Juan Pablo Olave Muñoz
Luisa Maria Arango Lopez

## Licencia

Este proyecto está disponible para uso educativo y demostrativo.
