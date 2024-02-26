from time import sleep
def contador(i, f, p):
    while i <= f:
        print(f'{i}')
        sleep(1)
        i += p
    while i >= f:
        print(f'\n{i}')
        sleep(1)
        i -= p
    print('=== Fim do programa ===')

inicio = int(input('Digite o inicio da contagem: '))
fim = int(input('Digite até onde a contagem vai: '))
passo = int(input('Digite de quantos números deve pular até o fim: '))
contador(inicio, fim, passo)