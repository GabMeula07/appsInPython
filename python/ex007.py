ladoQuadrado = float(input("Digite o tamanho do quadrado: "))

def Metro(lado):
    area = lado * lado 
    aDobro = area * 2 
    print(f'a área do quadrado é {area} e seu dobro é {aDobro}')

Metro(ladoQuadrado)