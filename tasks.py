import os
import json

from invoke import task
from pathlib import Path


def generate_links():
    if "links.json" not in os.listdir(Path("data/external/")):
        df = json.load(open(Path('data/external/lyrics.json'), 'r'))
        link = 'https://www.letras.mus.br'
        links = [f'{link}{url}traducao.html' for url in df]
        with open(Path('data/external/links.json'), 'w+') as f:
            json.dump(links, f)
    print("Links generated!")


@task
def run_crawler(c):
    if "letrasvf.json" not in os.listdir(Path("data/raw/")):
        generate_links()
        c.run(f"scrapy runspider scrapy_letras.py -o {str(Path('data/raw/letrasvf.json'))}")
    print("Done!")