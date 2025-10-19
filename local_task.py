# --- Script para llamar a 2 APIs usando Hilos
import requests
import time
import threading
import os
from dotenv import load_dotenv

def api_call(url, params, total_timeout=60):
	try:
		response = requests.get(url, params=params, timeout=total_timeout)
		response.raise_for_status()
		data = response.json()
		return data
	except Exception as e:
		print(f"Error al llamar la api: {e}")
		return None
def movies_api_call(movie_name:str, limit:int):
	movie_api_recomendation_url = "https://tastedive.com/api/similar"
	if limit > 20 or limit < 0:
		raise ValueError("Limite incorrecto")
	movie_params = {
		"q": movie_name,
		"type": "movie",
		"info":0,
		"limit":limit,
		"k":movies_api_key
	}
	data = api_call(movie_api_recomendation_url, params=movie_params)
	if not data:
		print("Error al llamar a la API de peliculas")
		return
	print("---- Resultados de la llamada a la API de peliculas -----")
	print(f"Recomendaciones para: {movie_name}")
	index = 0
	for recomendation in data["similar"]["results"]:
		name = recomendation["name"]
		print(f"Recomendacion[{index}]: {name}")
		index += 1
def number_validation_api_call(phone_number:str, country_code:str):
	number_validation_url = "http://apilayer.net/api/validate"
	number_validation_params={
		"access_key":number_validation_key,
		"number":phone_number,
		"country_code":country_code,
		"format":1
	}
	data = api_call(number_validation_url, number_validation_params)
	if not data:
		print("Error al llamara a la API de validacion de teléfonos")
		return
	print("---- Resultados llamada a la API de validacion de telefonos ----")
	if not data["valid"]:
		print(f"El numero de teléfono: {phone_number} no es válido según la API")
	else:
		prefix = data["country_prefix"] or "Sin info del Prefijo"
		country_name = data["country_name"] or "Sin info del País"
		carrier = data["carrier"] or "Sin info del Operador"
		line_type = data["line_type"] or "Sin info del tipo de linea"
		print(f"El número de teléfono: {phone_number} es válido según la API, y posee la siguiente información:")
		print(f"Prefijo del pais: {prefix}")
		print(f"Nombre del pais: {country_name}")
		print(f"Operador: {carrier}")
		print(f"Tipo de linea: {line_type}")
# --- Cargar variables de entorno
load_dotenv()
movies_api_key = os.getenv("MOVIES_API_KEY")
number_validation_key = os.getenv("NUMBER_VALIDATION_API_KEY")
# --- Ejecución con Hilos
print(f"Timestamp: {time.time()}")
print("Inicializando Hilos")
start = time.time()
thread_movies_1 = threading.Thread(target=movies_api_call, args=("pride and prejudice", 5), name ="Orgullo y Prejuicio")
thread_movies_2 = threading.Thread(target=movies_api_call, args=("parasites", 5), name="El resplandor")
thread_number_1 = threading.Thread(target=number_validation_api_call, args=("3043945372", "CO"), name="Número 1")
thread_number_2 = threading.Thread(target=number_validation_api_call, args=("3164909496", "CO"), name="Número 2")
# --- Iniciar Hilos
thread_movies_1.start()
thread_movies_2.start()
thread_number_1.start()
thread_number_2.start()
# --- Esperar a que los Hilos Terminen
thread_movies_1.join()
thread_movies_2.join()
thread_number_1.join()
thread_number_2.join()
# --- Imprimir el rendimiento del programa
end = time.time()
print(f"Tiempo con Hilos: {end-start:.2f}s")

