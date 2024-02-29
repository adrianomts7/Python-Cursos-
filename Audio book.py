import pyttsx3

#iniciando o motor da sintase de fala
engine = pyttsx3.init()

#Texto que quer que seja lido em forma de audio book
texto = str(input('O que deseja que seja lido em forma de audio book: '))

#configuração da voz e da velocidade da leitura
velocidade_da_fala = float = input('Qual a velocidade que você quer ouvir o audio:')
engine.setProperty("rate",velocidade_da_fala) 

#gerando o audiobook
engine.say(texto)

#Aguarde ate a conclusão da leitura:
engine.runAndWait()

#encerre o motor da sintese de fala
engine.stop()