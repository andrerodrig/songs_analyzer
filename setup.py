# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['songs_analyzer', 'songs_analyzer.data']

package_data = \
{'': ['*']}

install_requires = \
['Scrapy>=2.5.1,<3.0.0', 'invoke>=1.6.0,<2.0.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'songs-analyzer',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Andre Rodrigues',
    'author_email': 'andrelmarques11@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

