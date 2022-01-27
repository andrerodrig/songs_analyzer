from pathlib import Path
import json

from invoke import task
import pandas as pd
from argostranslate import package, translate


# tradutor
package.install_from_path('models/translate-pt_en-1_0.argosmodel')
installed_languages = translate.get_installed_languages()
pt2en = installed_languages[1].get_translation(to=installed_languages[0])


@task
def data(c):
    folder = Path("data/raw/playlists/new")
    data_path = Path("data/processed/data.csv")
    json_data = []
    for file in folder.iterdir():
        with open(file) as json_file:
            json_data.extend(json.load(json_file))
        parts = list(file.parts)
        parts[parts.index("new")] = "old"
        file.rename(Path('/'.join(parts)))
    if not json_data:
        print("No playlists to add.")
        return 0
    df_new = (
        pd
        .DataFrame(json_data)
        .drop_duplicates(subset=["uri"])
        .reset_index(drop=True)
    )
    # translating
    # print(df_new.genrers)
    df_new = df_new.assign(
        genrers=df_new.genrers.apply(lambda x: ' '.join(eval(str(x)) if x else '')),
        name=df_new.name.apply(lambda x: pt2en.translate(str(x).lower())),
        artist=df_new.artist.apply(lambda x: str(x).lower()),
    )
    print(f"Adding {len(df_new)} songs")
    
    df_old = pd.read_csv(Path(data_path))
    concatenate_df = (
        pd
        .concat([df_old, df_new])
        .drop_duplicates(subset=["uri"])
        .reset_index(drop=True)
    )
    concatenate_df.to_csv(data_path, index=False)
    
    print(f"Dataset generated at {data_path}")


# @task
# def generate_dataset(c):
#     raw_data_path = get_root_path() / "data/raw/"
#     data_dirname = "song_feature_data"
#     if not (raw_data_path / f"{data_dirname}.csv").is_file():
#         unzip_files(raw_data_path, f"{data_dirname}.zip")
#         df_list = []
#         for file in Path(raw_data_path / data_dirname).glob('*.json'):
#             df_list.append(pd.read_json(file))
#         songs_df = pd.concat(df_list)
#         songs_df.to_csv(raw_data_path / f"{data_dirname}.csv", index=False)
#         c.run(f"rm -rf {raw_data_path / data_dirname}")
#     print("Done!")


# # def generate_links():
# #     if "links.json" not in os.listdir(Path("data/external/")):
# #         df = json.load(open(Path('data/external/lyrics.json'), 'r'))
# #         link = 'https://www.letras.mus.br'
# #         links = [f'{link}{url}traducao.html' for url in df]
# #         with open(Path('data/external/links.json'), 'w+') as f:
# #             json.dump(links, f)
# #     print("Links generated!")


# # @task
# # def run_crawler(c):
# #     if "letrasvf.json" not in os.listdir(Path("data/raw/")):
# #         generate_links()
# #         c.run(f"scrapy runspider scrapy_letras.py -o {str(Path('data/raw/letrasvf.json'))}")
# #     print("Done!")