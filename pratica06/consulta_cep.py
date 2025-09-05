"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP 
fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro,
 bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests

def consulta_cep(cep):
    try:
        consulta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if consulta.status_code == 200:
            dados = consulta.json()
            return f"""
            CEP: {cep}
            Logradouro: {dados["logradouro"]}
            Bairro: {dados["bairro"]}
            Cidade: {dados["localidade"]}
            Estado: {dados["uf"]}
            """
        else:
            return "CEP não encontrado."
    except requests.RequestException as e:
        return f"Erro na consulta: {e}"

def main():
    cep = input("Digite um CEP para consulta (apenas números): ")
    print("\nConsultando CEP...\n")
    resultado = consulta_cep(cep)
    print(resultado)

# Executa o programa
main()