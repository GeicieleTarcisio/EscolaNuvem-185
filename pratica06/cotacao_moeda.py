"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao
 Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD,
EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, 
além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação.
"""
import requests

def cotacao_moeda(codigo_moeda):
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{codigo_moeda}BRL"
        if chave not in dados:
            return "❌ Código de moeda inválido ou não encontrado."

        moeda = dados[chave]
        return f"""
        Moeda: {moeda['code']} para {moeda['codein']}
        Nome: {moeda['name']}
        Alta: {moeda['high']}
        Baixa: {moeda['low']}
        Variação: {moeda['varBid']}
        Porcentagem de variação: {moeda['pctChange']}%
        """
    except requests.RequestException as e:
        return f"Erro na requisição: {e}"

def main():
    codigo = input("Digite o código da moeda para a cotação (ex: USD, EUR, GBP): ").upper().strip()
    print("\nObtendo cotação...\n")
    resultado = cotacao_moeda(codigo)
    print(resultado)

# Executa o programa
main()