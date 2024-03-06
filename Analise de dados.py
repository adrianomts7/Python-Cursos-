import pandas as pd
tabela = pd.read_csv("cancelamentos.csv")

tabela = tabela.drop(columns="CustomerID") 
print(tabela) 

print(tabela.info()) 
tabela = tabela.dropna() 
print(tabela.info())

print(tabela['cancelou'].value_counts()) 
print(tabela['cancelou'].value_counts(normalize=True)) 

import plotly.express as px

for coluna in tabela.columns: 
    grafico = px.histogram(tabela, x=coluna,color="cancelou") 
    grafico.show()
    

tabela = tabela[tabela["duracao_contrato"] != "Monthly"]  
tabela = tabela[tabela["ligacoes_callcenter"] <= 5] 
tabela = tabela[tabela["dias_atraso"]>= 20] 

print(tabela["cancelou"].value_counts(normalize=True))