def Main():
    print('Conversor de temperaturas: ')
    print('Opções: \n[1] celsius > farenheit \n[2] farenheit > celsius')
    resposta = Controle()
    print(resposta)
    Conversor(resposta)
    Continuar()

def Controle():
    r = input("Digite a opção de conversão: ")
    while r not in '12':
            print("Opção inválida.")
            r = input("Digite a opção de conversão: ")
    if r == '1':
        return 1
    elif r == '2': 
        return 2
    

def Conversor(Controle):
    if Controle == 1:
        print("Opção escolhida: [1] celsius > farenheit")
        Tc = float(input("Digite a temperatura em Celsius: "))
        Tf = (Tc*1.8)+32
        print(f"A temperatura {Tc:.1f}ºC equivale {Tf:.1f}ºF")
    elif Controle == 2: 
        print("Opção escolhida: [2] farenheit > celsius ")
        Tf = float(input("Digite a temperatura em farenheit: "))
        Tc = (Tf-32)/1.8
        print(f"A temperatura {Tf:.1f}ºF equivale {Tc:.1f}ºC")

def Continuar():
    resposta = input("Deseja Continuar?: [s/n]").strip().upper()
    while resposta not in 'SN':
            print("Opção inválida")
            resposta = input("Deseja Continuar?: [s/n]").strip().upper()
    if resposta == 'S':
        Main()
    elif resposta == 'N':
        return

        

Main()