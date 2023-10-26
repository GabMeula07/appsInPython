n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro número: '))

if n1 > n2 :
    print(f"O maior número digitado foi {n1}")
elif n2 > n1:
    print(f'O maior número digitado foi {n2}')
else: 
    print("Os números digitados são iguais")