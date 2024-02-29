
# importando a base de dados
tabela_de_venda = pd.read_excel('Vendas.xlsx')

#visualizar base de dados
pd.set_option('display.max_columns', None)

#Faturamento da loja
Faturamento = tabela_de_venda[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(Faturamento)
print('-' * 50)

#Quantidade de produtos vendidos por loja
Quantidade = tabela_de_venda[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(Quantidade)
print('-' * 50)


#ticket Médio de produto em cada loja
ticket_medio = (Faturamento['Valor Final'] / Quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

#Enviar e-mail com relatorio
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'adrianomts07@gmail.com'
mail.subject = 'Relatorio de vendas por loja'
mail.HTMLBody = f''' 
<p>Prezados,</p>

<p>Texto do Parágrafo</p>

<p>Segue o Relatorio de vendas de cada loja.</p>

<p>Faturamento:</p>
{Faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade de produtos vendidos:</p>
{Quantidade.to_html}

<p>Ticket Médio dos produtos em cada loja:</p>
{ticket_medio.to_html(formatters={'Ticket Medio': 'R${:,.2f}'.format})}

<p>Qualquer duvida só chamar que estou a disposição para tira-la</p>

<p>Att..</p>
<p>Adriano.</p>
'''

mail.Send()
print('E-mail enviado com sucesso')