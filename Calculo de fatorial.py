def factorial(num, show=False):
    """Passo a Passo de como calcular a fatorial de um número

    Args:
        num = O número que você vai calcular a fatorial
        
        show = o comando que você verá o passo a passo da conta, para ver o como é feito, utilizar o 'show=True' 
        caso não queira ver, só utilizar o show=False 

    Returns: O Resultado da fatorial do número digitado.
        
    """
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(c,end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f



#Programa principal
numero = int(input('Digite o número que deseja saber a fatorial: '))
factorial(numero)
print(factorial(numero, show=True))