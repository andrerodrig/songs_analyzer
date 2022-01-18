import os
import json
import pandas as pd

from invoke import task
from pathlib import Path
from zipfile import ZipFile

from songs_analyzer.config import get_root_path


def unzip_files(path: Path, zipname: str):
    with ZipFile(path / zipname, "r") as zip_obj:
        zip_obj.extractall(path=path)


@task
def generate_dataset(c):
    raw_data_path = get_root_path() / "data/raw/"
    data_dirname = "song_feature_data"
    if not (raw_data_path / f"{data_dirname}.csv").is_file():
        unzip_files(raw_data_path, f"{data_dirname}.zip")
        df_list = []
        for file in Path(raw_data_path / data_dirname).glob('*.json'):
            df_list.append(pd.read_json(file))
        songs_df = pd.concat(df_list)
        songs_df.to_csv(raw_data_path / f"{data_dirname}.csv", index=False)
        c.run(f"rm -rf {raw_data_path / data_dirname}")
    print("Done!")


# def generate_links():
#     if "links.json" not in os.listdir(Path("data/external/")):
#         df = json.load(open(Path('data/external/lyrics.json'), 'r'))
#         link = 'https://www.letras.mus.br'
#         links = [f'{link}{url}traducao.html' for url in df]
#         with open(Path('data/external/links.json'), 'w+') as f:
#             json.dump(links, f)
#     print("Links generated!")


# @task
# def run_crawler(c):
#     if "letrasvf.json" not in os.listdir(Path("data/raw/")):
#         generate_links()
#         c.run(f"scrapy runspider scrapy_letras.py -o {str(Path('data/raw/letrasvf.json'))}")
#     print("Done!")