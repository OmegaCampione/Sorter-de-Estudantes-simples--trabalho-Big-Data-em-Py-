import pandas as pd

# lê o CSV
df = pd.read_csv('alunos.csv')

# Exibe as 5 primeiras linhas
print("As 5 primeiras linhas do arquivo:")
print(df.head())

# Seleciona apenas as colunas de nome e nota
nome_nota = df[['Nome', 'Nota']]
print("\nColunas nome e nota:")
print(nome_nota)

# Filtra alunos de Engenharia com nota maior que 8
engenharia_8 = df[(df['Curso'] == 'Engenharia') & (df['Nota'] > 8)]
print("\nAlunos de Engenharia com nota maior que 8:")
print(engenharia_8)

# Calcula a média das notas por curso
media_notas = df.groupby('Curso')['Nota'].mean().reset_index()
print("\nMédia das notas por curso:")
print(media_notas)

# Salva o resultado da média em um arquivo CSV
media_notas.to_csv('media_notas.csv', index=False)
print("\nArquivo 'media_notas.csv' salvo com sucesso.")
