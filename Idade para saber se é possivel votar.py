def voto(ano,msg):
    from datetime import date
    ano = date.today().year
    idade = ano - nascimento
    if idade < 16:
        return f'Olá {nome} tem {idade} anos não tem idade suficiente para votar, espere a idade minima que é 16 anos'
    elif 16 <= idade < 18 or idade > 65:
        return f'Olá {nome} você tem {idade} anos é nessa idade o seu voto é opcional'
    else:
        return f'Olá {nome} você tem {idade} anos a partir dessa idade o seu voto é obrigatorio'
    

#programa principal
nome = str(input('Digite seu nome: '))
nascimento = int(input('Digite o seu ano de nascimento: '))
voto(nascimento, nome)
print(voto(nascimento, nome))