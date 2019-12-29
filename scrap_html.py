import requests
import lxml.html as lh
import pandas as pd

url='http://pokemondb.net/pokedex/all'

page = requests.get(url)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')

[len(T) for T in tr_elements[:12]]
