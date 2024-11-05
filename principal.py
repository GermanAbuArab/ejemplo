import requests
from funciones import imprimir_hola
import funciones

if __name__ == '__main__':

    # aca sucede todo

    titulo =("Harry potter")
    url = "https://openlibrary.org/search.json?q="+titulo.replace(" ","+")
    response=requests.get(url)

    if response.status_code == 200:
        data = response.json()
        documentos= data["docs"]
        if len(documentos)>0:
            print(documentos[1].get("author_name"))
        else:
            print("No se encontro el libro")

    if response.status_code == 400:
        print("Fallo la llamada a la API")



    # Hacer un loop que use la dado un input del usuario
    # 1 si el usuario ingresa "exit"
    # 2 si el usuario ingresa otra cosa usar la funcion creada en llamada_api para imprimir el titulo de lo buscado


if __name__ == '__main__':
    while True:
        user_input = input("Ingrese un título de libro para buscar o 'exit' para salir: ")
        if user_input.lower() == "exit":
            print("Saliendo del programa.")
            break
        else:
            llamada_api(user_input)
            imprimir_hola()






















