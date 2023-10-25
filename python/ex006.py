valor_por_hora = float(input('Quanto você recebe por hora: '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))

def Salario(vph, ht):
    salario = valor_por_hora * horas_trabalhadas
    return salario

salario = Salario(valor_por_hora, horas_trabalhadas)
print(salario)