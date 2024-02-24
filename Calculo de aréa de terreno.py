def area(larg, comp):
    area = larg * comp
    print(f'A aréa do seu terreno é {larg} X {comp} no total de aréa de {area} m²')



#Programa principal
largura = int(input('Digite a largura do seu terreno: '))
comprimento = int(input('Digite o comprimento do seu terreno: '))
area(largura, comprimento)