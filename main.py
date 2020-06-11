# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:19:57 2020

@author: Nielsen Castelo Damasceno Dantas
"""

import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import pandas as pd
from pandas import DataFrame

rcParams['figure.figsize'] = 15,6

filename = 'index-isolation-brazil.xlsx'
df = pd.read_excel(filename).set_index("Data")

df.head()
df.describe()
maior = df.max()

maior_ordenado = maior.sort_values(ascending=False)


plt.figure();
maior_ordenado.plot(kind='bar',)
plt.title('Rank dos estados com o valor dos maiores indice de isolamento social') 
plt.ylabel('Valores em %')


media = df.mean()
media_ordenado = media.sort_values(ascending=False)
plt.figure();
media_ordenado.plot(kind='bar',)
plt.title('Rank melhores médias do indice de isolamento social') 
plt.ylabel('Média em porcentagem')


ultimo_df = df.tail(1)
colunas = ultimo_df.columns.to_list()
valores = ultimo_df.values


valores = valores.reshape(-1,1)
ultimo_ordenado = DataFrame(index=colunas, data=valores)
ultimo_ordenado = ultimo_ordenado.sort_values([0],ascending=False)

plt.figure();
ultimo_ordenado.plot(kind='bar',legend=False)
plt.title('Rank do último dia') 
plt.ylabel('Valores em %')
