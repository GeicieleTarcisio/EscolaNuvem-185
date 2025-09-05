"""
4- Crie uma função que calcule a idade de uma pessoa em dias,
baseada no ano de nascimento.
"""
from datetime import date

def idade_em_dias(ano_nascimento: int) -> int:

    # Obtém o ano atual
    ano_atual = date.today().year

    # Calcula a idade em anos
    idade_anos = ano_atual - ano_nascimento

    # Aproxima a idade em dias (desconsiderando anos bissextos)
    idade_dias = idade_anos * 365

    return idade_dias


# --- Exemplo de uso ---
ano = int(input("Digite o ano em que você nasceu: "))
dias = idade_em_dias(ano)
print(f"Você tem aproximadamente {dias} dias de vida.")