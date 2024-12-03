import pandas as pd
import sqlite3

# Defina o caminho para o arquivo Excel
arquivo_excel = "C:/Users/Pedro/Downloads/pratica/data/DADOS 01.xlsx"

# Conecta-se ao banco de dados
nome_do_banco_de_dados = "BancodeDados.db"
conexao = sqlite3.connect(nome_do_banco_de_dados)

# Carregar o arquivo excel
xls = pd.ExcelFile(arquivo_excel)

# nome da tabela no banco de dados onde todos os dados serão armazenados
tabela_unica = "curriculos"

# Iterar sobre cada planilha no arquivo Excel
for nome_da_planilha in xls.sheet_names:
    # Ler a planilha atual
    df = pd.read_excel(arquivo_excel, sheet_name=nome_da_planilha)

    # Adicionar uma coluna para identificar o cargo (nome da planilha)
    df['cargo'] = nome_da_planilha

    # Inserir os dados na tabela única, adicionando a coluna 'cargo'
    df.to_sql(tabela_unica, conexao, if_exists="append", index=False)
    print(f"Dados da planilha '{nome_da_planilha}' foram transferidos para a tabela '{tabela_unica}'.")

# Fechar a conexão com o banco de dados
conexao.close()

print("Todos os dados foram transferidos com sucesso para a tabela única!")
