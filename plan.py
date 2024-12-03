import pandas as pd

arquivo_excel = "C:/Users/Pedro/Downloads/pratica/data/DADOS 01.xlsx"

# Lista todas as planilhas no arquivo
xls = pd.ExcelFile(arquivo_excel)
print("Planilhas disponíveis:", xls.sheet_names)
