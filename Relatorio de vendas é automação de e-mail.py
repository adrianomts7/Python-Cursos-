import pandas as pd
import win32com.client as win32

# importando bases de dados
tabela_de_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_de_vendas)

# Faturamento por loja
faturamento = tabela_de_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# Quantidade de produtos vendidos por loja
quantidade = tabela_de_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)
print('-=' * 50)

#Ticket Médio dos produtos em cada loja
ticktet_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticktet_medio = ticktet_medio.rename(columns={0: 'Ticket Médio'})
print(ticktet_medio)

# Enviar um e-mail com o relatório das lojas
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.to = 'e-mail que você deseja enviar o relatorio'
mail.Subject = 'Relatorio de vendas'
mail.HTMLBody = f'''
<P>Prezados.</P>

<P>Segue o relatório das vendas de cada loja.</P>

<P>Faturamento:</P>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade de vendas</p>
{quantidade.to_html(formatters={'Quantidade': '{:.1f}'.format})}

<p>Ticket médio dos produtos em cada loja</p>
{ticktet_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<P>Qual dúvida so chamar estarei a disposição para esclarece-la</p>

<p>Att</p>

<p>A.Mateus</p>

'''

mail.Send()
print('E-mail enviado')