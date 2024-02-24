def tabuada(num):
    for c in range(1,11):
        print(f'A tabuda de {num}: {num} X {c} = {num * c}')

#Programa Principal
numero = int(input('Digite o número que deseja saber a Tabuada: '))
tabuada(numero)