import requests
from Funciones import imprimir_hola
import Funciones

if __name__ == '__main__':

    # aca sucede todo
    print("HOLA")

    imprimir_hola()
    print(Funciones.dividir_entre_2(5))


    # url = "https://openlibrary.org/search.json?q=the+lord+of+the+rings"
    # response=requests.get(url)
    #
    # if response.status_code == 200:
    #     print()
    #     data = response.json()
    #     documentos= data["docs"]
    #     print(documentos[1]["author_name"])


