# programa de calculo de consumo eletrico
# entrada

aparelho = (input("Digite o nome do aparelho: "))
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário do aparelho em horas: "))

# processamento

consumo_mensal = (potencia * horas_dia * 30) / 1000
valor_estimado = consumo_mensal * 0.75

# saida

print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal}kWh/mês")
print(f"Custo estimado (R$ 0,75 por kWh): R$ {valor_estimado:.2f}")