"""
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
O programa deve exibir o nome, email e país do usuário gerado.
"""
import requests

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()["results"][0]
        nome = dados["name"]["first"]
        email = dados['email']
        pais = dados['location']['country']
        return f"\n Nome:{nome}\nEmail: {email}\nPais: {pais}"
    except requests.RequestsException as e:
        return f"erro ao obter usuário aleatório: {e}"
    
print("Gerando um usuário aleatorio")
usuario = obter_usuario_aleatorio()
print(usuario)