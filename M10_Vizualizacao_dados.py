import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')

print(df.head().to_string())

print(df.info())

#Todo Tratar os dados

print('Valores duplicados: ', df.duplicated().sum())

print('Valores nulos: ', df.isnull().sum())

print("Valores dos Descontos: ", df['Desconto'].value_counts())
df.fillna(value={'Desconto': 'Sem Desconto'}, inplace=True) #Substitui os valores nulos por 'Sem Desconto'
print("Valores dos Descontos: ", df['Desconto'].value_counts()) #Mesmo nao usando eu queria tratar os valores nulos

#Pegando os valores que me interessam
df = df[['Qtd_Vendidos','Qtd_Vendidos_Cod', 'Preço_MinMax', 'Nota_MinMax', 'Marca_Cod', 'Temporada_Cod', 'Marca_Freq', 'Material_Cod', 'N_Avaliações_MinMax', 'Gênero', 'Temporada', 'Nota', "N_Avaliações", "Marca"]]
print(df.head().to_string())
df = df.dropna()

print("Valores da temporada: ", df['Temporada'].value_counts()) #Ve a quantidade de cada coisa na coluna
print("Quantidade de vendidos: ", df['Qtd_Vendidos'].value_counts())
print("Quantidade de vendidos por temporada:")
df = df[df['Temporada'] != '2021'] #Tirei o 2021 para dar replace nas temporadas que eu quero
df['Temporada'] = df['Temporada'].astype(str).str.strip()
mapeamento = {
    'primavera/verão': 'pv',
    'primavera-verão': 'pv',
    'outono/inverno': 'oi',
    'outono-inverno': 'oi',
    'primavera-verão outono-inverno': 'pvoi',
    'primavera-verão - outono-inverno': 'pvoi',
    'primavera/verão/outono/inverno': 'pvoi',
    'primavera/verão outono/inverno': 'pvoi'
}

df['Temporada'] = df['Temporada'].replace(mapeamento)
print("Valores da temporada: ", df['Temporada'].value_counts())

df['Qtd_Vendidos'] = df['Qtd_Vendidos'].astype(str).str.strip()
quantidade = {
    '+100': 100,
    '+1000': 1000,
    '+50': 50,
    '+25': 25,
    '+5': 5,
    '+10mil': 10000,
    '+50mil': 50000,
    '1': 1,
    '3': 3,
    '4': 4,
    '2': 2
}
df['Qtd_Vendidos_Num'] = df['Qtd_Vendidos'].map(quantidade)

df_agrupado = df.groupby('Temporada')['Qtd_Vendidos_Num'].sum().reset_index()

print("Tabela das somas das quantidades:")
print(df_agrupado)
print(df.info())

print("Notas: ", df['Nota_MinMax'].value_counts())
print("Gênero: ", df["Gênero"].value_counts())
df['Gênero'] = df['Gênero'].astype(str).str.strip()

genero = {
    'Feminino': 'Feminino',
    'Masculino': 'Masculino',
    'Bebês': 'Infantil',
    'Meninos': 'Infantil',
    'Meninas': 'Infantil',
    'menino': 'Infantil',
    'Sem gênero': 'Sem Gênero',
    'Sem Gênero': 'Sem Gênero',
    'Sem gênero infantil': 'Infantil',
    'Unissex': 'Sem Gênero'
}
df['Gênero'] = df['Gênero'].replace(genero)

categorias = ['Feminino', 'Masculino', 'Infantil', 'Sem Gênero']

df.loc[~df['Gênero'].isin(categorias), 'Gênero'] = 'Outros'

# 5. Confere o resultado final limpinho
print("Gêneros mudados: ", df['Gênero'].value_counts())

#Todo fazer os 5 graficos diferentes (Calor, Pizza, Disperção, Barra, Densidade

#Primeiro Grafico (Barras)

plt.figure(figsize=(10, 6)) #Define o tamanho da figura na tela=
plt.bar(df_agrupado['Temporada'], df_agrupado['Qtd_Vendidos_Num'], color='blue')
plt.title('Total de Produtos Vendidos por Temporada', fontsize=14, fontweight='bold')
plt.xlabel('Temporada')
plt.ylabel('Quantidade Total Vendida')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

#Segundo Grafico (Pizza)

plt.figure(figsize=(10, 6))
plt.pie(df_agrupado['Qtd_Vendidos_Num'], labels=df_agrupado['Temporada'], autopct='%1.1f%%', startangle=90)
plt.title('Total de Produtos Vendidos por Temporada', fontsize=14, fontweight='bold')
plt.show()

#Terceiro Grafico (Disperção)

plt.figure(figsize=(10, 6))
plt.scatter(df['Nota_MinMax'], df['N_Avaliações'], color='red')
plt.xlabel('Nota')
plt.ylabel('Numero de avaliações')
plt.title('Valiaçoes nos produtos', fontsize=14, fontweight='bold')
plt.show()

#Quarto Grafico (Calor)

tb = pd.crosstab(df['Gênero'], df['Temporada'])
plt.figure(figsize=(10, 6))
sns.heatmap(tb, annot=True, fmt=".2f", cmap='coolwarm')
plt.show()

#Quinto Grafico (Densidade)

plt.figure(figsize=(10, 6))
sns.kdeplot(df['Nota_MinMax'], fill=True, color='#863e9c')
plt.title('Densidade de Notas')
plt.xlabel('Nota')
plt.show()