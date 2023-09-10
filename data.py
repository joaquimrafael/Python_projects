import numpy as np
import pandas as pd
import seaborn as sns

df_glp = pd.read_csv("https://raw.githubusercontent.com/scalabrinig/datasets_oficina/master/datasets/precos_glp.csv", sep=";", decimal=",")

df_glp.head(7)
df_glp.tail(8)
df_glp.index
df_glp.columns
df_glp.shape

df_glp['Valor de Venda'].mean()
df_glp['Valor de Venda'].median()
df_glp['Valor de Venda'].mode()[0]
df_glp['Valor de Venda'].var()
df_glp['Valor de Venda'].std()
df_glp['Valor de Venda'].min()
df_glp['Valor de Venda'].max()
df_glp['Valor de Venda'].quantile(0.25)
df_glp['Valor de Venda'].quantile(0.75)
df_glp['Valor de Venda'].quantile(0.5)

df_glp['Valor de Venda'].describe()
print('Média: ', df_glp['Valor de Venda'].mean())

df_glp = df_glp.rename(columns={"Regiao - Sigla":"regiao",
                      "Estado - Sigla":"uf",
                      "Municipio":"municipio",
                      "Revenda":"revenda",
                      "CNPJ da Revenda":"cnpj",
                      "Nome da Rua":"rua",
                      "Numero Rua":"nro_rua",
                      "Complemento":"complemento",
                      "Bairro":"bairro",
                      "Cep":"cep",
                      "Produto":"produto",
                      "Data da Coleta":"dt_coleta",
                      "Valor de Venda":"valor_venda",
                      "Valor de Compra":"valor_compra",
                      "Unidade de Medida":"unidade_medida",
                      "Bandeira":"bandeira",})

sns.boxplot(x=df_glp["valor_venda"])
sns.distplot(df_glp["valor_venda"])


df_glp.isnull()
df_glp.isnull().sum()

df_glp.dropna(axis='columns', how='all', inplace=True)

df_glp = df_glp.dropna(subset=['bairro'])

df_glp = df_glp.fillna(value={'complemento':'-'})

q1 = df_glp["valor_venda"].quantile(0.25)
q3 = df_glp["valor_venda"].quantile(0.75)
iqr = q3 - q1
lim_inf = q1 - 1.5 * iqr
lim_sup = q3 + 1.5 * iqr

df_iqr = df_glp[(df_glp['valor_venda'] > lim_inf) & (df_glp['valor_venda'] < lim_sup)]

sns.boxplot(x=df_iqr["valor_venda"])

df_glp = df_iqr.copy()


df_glp.duplicated().sum()

df_glp.duplicated(subset=['cnpj']).sum()

df_glp = df_glp.sort_values(by='dt_coleta', ascending=False)

df_glp = df_glp.drop_duplicates(subset=['cnpj'], keep='first')

df_glp.nunique()

df_glp = df_glp.drop(columns=['produto','unidade_medida'])

sel = df_glp.loc[0, 'revenda']
seli = df_glp.iloc[0,3]

df_glp_ultra_m100 = df_glp.query("bandeira == 'ULTRAGAZ' and valor_venda < 100")

df_graf = df_glp.groupby('bandeira')['valor_venda'].mean().reset_index
df_graf = df_graf.sort_values(by='valor_venda')
sns.barplot(x='valor_venda', y='bandeira', data=df_graf)
