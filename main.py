from scrapy import SELLER
from dataclasses import asdict
import pandas as pd
import logging
from datetime import date
from datetime import date
from dataclasses import asdict
import pandas as pd
import logging
from time import sleep
import os

log_directory = "logs"
log_file = f"{log_directory}/{date.today().strftime('%d-%m-%Y')}.log"

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(
    format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    filename=log_file,
    filemode='a',
    encoding='utf-8',
)

def save(products):
    nome_arquivo = f"data/{products[-1].date.strftime('%Y%m%d%H%M%S')}.csv"
    lista_de_dicionarios = [asdict(instancia) for instancia in products]
    df = pd.DataFrame(lista_de_dicionarios)
    df = df.drop_duplicates(subset=[col for col in df.columns if col != 'date'])
    df.to_csv(nome_arquivo, index=False)
    logging.info(f'{len(df)} produtos salvos no arquivo {nome_arquivo}')

def main():
    logging.info('[START]')
    products = []
    for nome, scraper in SELLER.items():
        for i in range(3):
            try:
                products += scraper().get_entrys()
                break
            except Exception as e:
                logging.error(e)
                logging.warning(f'Aconteceu algum erro. Iniciando tentativa {i+2}')
                sleep(10)            

    save(products)
    logging.info('[END]')


if __name__ == "__main__":
    main()