valor_por_hora = float(input('Quanto você recebe por hora: '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))

def Salario(vph, ht):
    salario = valor_por_hora * horas_trabalhadas
    return salario

salario = Salario(valor_por_hora, horas_trabalhadas)
ImpostoRenda = (salario*11)/100
INSS = (salario*8)/100
sindicato = (salario*5/100)
print(f"Salário Bruto: {salario}")
print(f"IR (11%): {ImpostoRenda}")
print(f"INSS (8%): {INSS}")
print(f"Sindicato (8%): {sindicato}")
print(f"Salário líquido: {salario-INSS-ImpostoRenda-sindicato}")