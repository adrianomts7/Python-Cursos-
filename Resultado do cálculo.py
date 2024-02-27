from Calculos import metade, aumentar, diminuir

preço = float(input('Digite o Preço R$ '))
porcentagem_a_mais = float(input('Quantos % deseja aumentar o preço: '))
multiplicar = int(input('Quantas vezes deseja multiplicar o prreço: '))
print(f'A Metade de {preço} é {metade(preço)}')
print(f'Você multiplicou {multiplicar} X {preço} = {preço * multiplicar}')
print(f'O Aumento foi de {porcentagem_a_mais}% , dando no total de {aumentar(preço, porcentagem_a_mais)} ')

