# AUTOGENERATED! DO NOT EDIT! File to edit: ai_vocabulary_web_scraping.ipynb.

# %% auto 0
__all__ = []

# %% ai_vocabulary_web_scraping.ipynb 1
from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st

# %% ai_vocabulary_web_scraping.ipynb 2
base_link = "https://www.cnil.fr/fr/intelligence-artificielle/glossaire-ia?page="
pages = []
for i in range(13):
    pages.append(base_link + str(i))


# %% ai_vocabulary_web_scraping.ipynb 3
alphabet_list = list(map(chr, range(97, 123)))

# %% ai_vocabulary_web_scraping.ipynb 4
alphabet_obj = {}

for char in alphabet_list:
    alphabet_obj[char]= []

# %% ai_vocabulary_web_scraping.ipynb 5
def word_format(word):
    obj = {}
    title = word.find("h3", class_="definition-liste-titre").a.text
    obj["title"] = title
    definition = word.find("div", class_= "definition-liste-body").text.strip()
    obj["definition"] = definition
    obj["entry"] = title[0].lower()
    link = word.find("h3", class_="definition-liste-titre").a.get("href")
    obj["link"] = link
    
    
    return obj


# %% ai_vocabulary_web_scraping.ipynb 6
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


# %% ai_vocabulary_web_scraping.ipynb 8
entries = alphabet_obj.keys()


# %% ai_vocabulary_web_scraping.ipynb 9
st.title("GLossaire IA")
st.markdown("Les données ont été extraites du site de [CNIL](%s) à fin de créer une application qui présente les entrées de façon plus intuitive de pouvoir créer des questionnaires." % base_link+ str(0))

selected_letter = st.selectbox(
    'Par quelle lettre commence le terme que vous cherchez',
    entries)



# %% ai_vocabulary_web_scraping.ipynb 10
df = pd.DataFrame(alphabet_obj[selected_letter])
st.dataframe(df)

# %% ai_vocabulary_web_scraping.ipynb 11
def print_(e):
    return e["title"]
word_list= list(map(print_, alphabet_obj[selected_letter]))



# %% ai_vocabulary_web_scraping.ipynb 12
selected_entry = None
isLen =len(word_list) > 0
if isLen:
    selected_entry = st.selectbox(
        'Quel mot cherchez-vous?',
        word_list)
else:
    st.write("Il n'y a pas de mots correspondant à cette entrée.")

# %% ai_vocabulary_web_scraping.ipynb 13
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
