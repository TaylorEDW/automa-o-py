import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL base do BetExplorer
base_url = "https://www.betexplorer.com/"

# Função para buscar odds de abertura
def obter_odds_abertura(temporada, liga):
    # Construa a URL específica para a temporada e liga desejadas
    url = f"{base_url}soccer/{liga}/{temporada}/"

    # Faça uma solicitação HTTP para a página
    response = requests.get("https://www.betexplorer.com/football/odds-movements/")

    if response.status_code == 200:
        # Analise o conteúdo HTML da página
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontre a tabela com as odds de abertura (ajuste a classe conforme necessário)
        odds_table = soup.find("table", class_="table-main")

        # Extraia os dados da tabela e coloque-os em um DataFrame
        df = pd.read_html(str(odds_table))[0]

        # Renomeie as colunas conforme necessário

        # Retorne o DataFrame
        return df
    else:
        print(" Não foi possível obter os dados.")
        return None

# Exemplo de uso:
temporada_desejada = "2023"
liga_desejada = "england-premier-league"

dados_odds_abertura = obter_odds_abertura(temporada_desejada, liga_desejada)

if dados_odds_abertura is not None:
    print(dados_odds_abertura)
