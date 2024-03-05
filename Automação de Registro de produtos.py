# importar a base de dados
import pyautogui
import time
import pandas 

pyautogui.PAUSE = 1

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Abrir o Navegador(chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=832, y=622)

# Entrando no site 
pyautogui.write(link)
pyautogui.press("enter")

# Fazer uma pausa de 3 segundos
time.sleep(3)

# Fazer o login
pyautogui.click(x=911, y=469)
pyautogui.write("Coloca o seu e-mail")
pyautogui.click(x=729, y=592)
pyautogui.write("coloca a senha que voê desejar")
pyautogui.click(x=922, y=675)
time.sleep(3)

#Importando a base de dados
tabela = pandas.read_csv("produtos.csv")

# Cadastrar o Produto
for linha in tabela.index:

    #Clicar no 1 campo
    pyautogui.click(x=754, y=269)

    # Cadastrar codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #tipo do produto
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    # categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preço do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #observação
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write()
    pyautogui.press("tab")

    # Para enviar 
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    
    #Repetir o processo até acabar os produtos