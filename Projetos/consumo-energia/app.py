print("=== Calculadora de Consumo Elétrico ===\n")

total_consumo = 0
total_custo = 0

while True:
    aparelho = input("Nome do aparelho: ")

    try:
        potencia = float(input("Potência (W): "))
        horas_dia = float(input("Horas por dia: "))

        if potencia < 0 or horas_dia < 0:
            print("Valores negativos.\n")
            continue

        if potencia == 0 or horas_dia == 0:
            confirmacao = input(
                "Um dos valores é 0, o consumo será zero. Deseja prosseguir? (s/n): "
            ).lower()
            if confirmacao != 'sim':
                print("Digite os valores novamente.\n")
                continue

    except ValueError:
        print("Tente novamente.\n")
        continue

    consumo = (potencia * horas_dia * 30) / 1000
    custo = consumo * 0.75

    total_consumo += consumo
    total_custo += custo

    print("\n--- Resultado ---")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo: {consumo:.2f} kWh/mês")
    print(f"Custo: R$ {custo:.2f}\n")

    continuar = input("Deseja adicionar outro aparelho? (sim/nao): ").lower()
    if continuar != 'sim':
        break

print("\n=== TOTAL AO MÊS ===")
print(f"Consumo total: {total_consumo:.2f} kWh/mês")
print(f"Custo total: R$ {total_custo:.2f}")
