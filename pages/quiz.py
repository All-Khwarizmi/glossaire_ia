# AUTOGENERATED! DO NOT EDIT! File to edit: ../quiz.ipynb.

# %% auto 0
__all__ = []

# %% ../quiz.ipynb 1
import streamlit as st

# %% ../quiz.ipynb 2
st.title("Second Page")

# %% ../quiz.ipynb 3
# Create the SQL connection to pets_db as specified in your secrets file.
from sqlalchemy import text
conn = st.connection('words_db', type='sql')

# Insert some data with conn.session.
   

# Query and display the data you inserted
pet_owners = conn.query('select * from words')
st.dataframe(pet_owners)
