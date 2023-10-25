pesoPeixe = float(input("Digite o peso do peixe: "))
excesso = pesoPeixe-50
multa = excesso*4

if pesoPeixe <= 50:
    print("O peso do peixe não está sujeito a multa")
else: 
    print(f"O peso excedeu: {excesso} \nA multa a ser paga será de: R${multa:.2f}")