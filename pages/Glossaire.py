# AUTOGENERATED! DO NOT EDIT! File to edit: ../ai_vocabulary_web_scraping.ipynb.

# %% auto 0
__all__ = []

# %% ../ai_vocabulary_web_scraping.ipynb 3
from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st

pd.options.display.max_columns = 20
pd.options.display.max_rows = 20
pd.options.display.max_colwidth = 80


# %% ../ai_vocabulary_web_scraping.ipynb 4
# Create the SQL connection to words_db as specified in your secrets file.
conn = st.connection('words_db', type='sql')

# %% ../ai_vocabulary_web_scraping.ipynb 7
base_link = "https://www.cnil.fr/fr/intelligence-artificielle/glossaire-ia?page="
pages = []
for i in range(13):
    pages.append(base_link + str(i))


# %% ../ai_vocabulary_web_scraping.ipynb 10
alphabet_list = list(map(chr, range(97, 123)))

# %% ../ai_vocabulary_web_scraping.ipynb 12
alphabet_obj = {}

for char in alphabet_list:
    alphabet_obj[char]= []

# %% ../ai_vocabulary_web_scraping.ipynb 14
from sqlalchemy import text
def word_format(word):
    obj = {}
    title = word.find("h3", class_="definition-liste-titre").a.text
    obj["title"] = title
    definition = word.find("div", class_= "definition-liste-body").text.strip()
    obj["definition"] = definition
    obj["entry"] = title[0].lower()
    link = word.find("h3", class_="definition-liste-titre").a.get("href")
    obj["link"] = link
    with conn.session as s:
        s.execute(text('CREATE TABLE IF NOT EXISTS words (entry TEXT, name, TEXT, definition TEXT, url TEXT);'))
        s.execute(
            text('INSERT INTO words (entry, name, definition, url) VALUES (:entry, :name, :definition, :url);'),
            params=dict(entry=title[0].lower(), name=title, definition=definition, url=link)
        )
        s.commit()
    
    return obj


# %% ../ai_vocabulary_web_scraping.ipynb 16
@st.cache_data
def web_scraper(alphabet):
    alphabet_obj = alphabet.copy()
    for page in pages:
        html_text = requests.get(page).text
        soup = BeautifulSoup(html_text, 'lxml')
        words = soup.find_all("div",class_="list-inner")
        for word in words:
            obj = word_format(word)
            try:
                alphabet_obj[obj["entry"]].append(obj)
            except:
                alphabet_obj[obj["entry"]] = []
                alphabet_obj[obj["entry"]].append(obj)
            
    return alphabet_obj
    

# %% ../ai_vocabulary_web_scraping.ipynb 17
alphabet_obj = web_scraper(alphabet_obj)

# %% ../ai_vocabulary_web_scraping.ipynb 22
entries = alphabet_obj.keys()


# %% ../ai_vocabulary_web_scraping.ipynb 24
st.title("GLossaire IA")
st.markdown("Les données ont été extraites du site de [CNIL](%s) à fin de créer une application qui présente les entrées de façon plus intuitive de pouvoir créer des questionnaires." % pages[0])

selected_letter = st.selectbox(
    'Par quelle lettre commence le terme que vous cherchez',
    entries)



# %% ../ai_vocabulary_web_scraping.ipynb 26
df = pd.DataFrame(alphabet_obj[selected_letter])
st.dataframe(df)

# %% ../ai_vocabulary_web_scraping.ipynb 28
def print_(e):
    return e["title"]
word_list= list(map(print_, alphabet_obj[selected_letter]))



# %% ../ai_vocabulary_web_scraping.ipynb 30
selected_entry = None
isLen =len(word_list) > 0
if isLen:
    selected_entry = st.selectbox(
        'Quel mot cherchez-vous?',
        word_list)
else:
    st.write("Il n'y a pas de mots correspondant à cette entrée.")

# %% ../ai_vocabulary_web_scraping.ipynb 32
def filter_cb(x):
    if x["title"] == selected_entry:
        return True
    else: 
        return False
                
if isLen and selected_entry is not None:
    selected_word = list(filter(filter_cb, alphabet_obj[selected_letter]))
    st.markdown(selected_word[0]["definition"])
    link = "https://www.cnil.fr/"+ selected_word[0]["link"]
    st.markdown(f"[{selected_entry}](%s)" % link)