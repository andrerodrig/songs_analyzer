import os
import json

from invoke import task


def generate_links():
    if "links.json" not in os.listdir("data/external/"):
        df = json.load(open('data/external/lyrics.json', 'r'))
        link = 'https://www.letras.mus.br'
        links = [f'{link}{url}traducao.html' for url in df]
        with open('data/external/links.json', 'w+') as f:
            json.dump(links, f)
    print("Links generated!")


@task
def run_crawler(c):
    if "letrasvf.json" not in os.listdir("data/raw/"):
        generate_links()
        c.run("scrapy runspider scrapy_letras.py -o data/raw/letrasvf.json")
    print("Done!")