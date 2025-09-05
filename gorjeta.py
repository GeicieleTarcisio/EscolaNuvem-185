"""
Crie uma função que calcule o valor da gorjeta baseado no total da conta e na.
porcentagem desejada.
- Parametros:
valor_conta (float): O valor total da conta
 porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna: 
float: O valor da gorjeta calculada
"""
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

# Versão interativa 
try:
    valor = float(input("Digite o valor total da conta: R$ "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (%) "))
    gorjeta = calcular_gorjeta(valor, porcentagem)
    total = valor + gorjeta
    print(f"A gorjeta a ser deixada é: R$ {gorjeta}")
    print(f" Total a pagar (conta + gorjeta) é: {total}")
except ValueError:
    print(f"Entrada inválida! Digite apenas números.")