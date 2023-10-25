while True:
    print("Digite uma das opções abaixo1 \n")
    print("[1] metros > centímetros ")
    print("[2] centímetros > metros \n")
    resposta  = int(input('opção: '))

    while resposta != 1 and resposta != 2:
            print("opção invalida! \n")
            print("[1] metros > centímetros ")
            print("[2] centímetros > metros \n")
            resposta  = int(input('opção: '))

    if resposta == 1:
        print('\n Opção escolhida: metros > centímetros \n ')
        metros = float(input("Digite o valor em metros: "))
        cent = metros * 100
        print(f"{metros}m são {cent}cm")

        resposta = str(input('Deseja continuar? [s/n]: ').upper().strip())
        while resposta != 'S' and resposta != 'N':
             print("opção invalida!")
             resposta = str(input('Deseja continuar? [s/n]: ').upper().strip())
        if resposta == 'N':
             break

    elif resposta == 2: 
        print('\n Opção escolhida: centímetros > metros \n ')
        cent = float(input("Digite o valor em cent: "))
        metros = cent/100
        print(f"{cent}cm são {metros}m")

        resposta = str(input('Deseja continuar? [s/n]: ').upper().strip())
        while resposta != 'S' and resposta != 'N':
             print("opção invalida!")
             resposta = str(input('Deseja continuar? [s/n]: ').upper().strip())
        if resposta == 'N':
             break


    
           