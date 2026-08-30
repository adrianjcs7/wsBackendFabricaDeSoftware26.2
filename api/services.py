import requests


def buscar_produtos_externos():
    url = "https://dummyjson.com/products"

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            return resposta.json()

        return {
            "erro": "API externa retornou um erro",
            "status_code": resposta.status_code
        }

    except requests.exceptions.RequestException as erro:
        return {
            "erro": "Não foi possível acessar a API externa",
            "detalhes": str(erro)
        }