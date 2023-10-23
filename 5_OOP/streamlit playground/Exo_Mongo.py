import streamlit as st
from pymongo import MongoClient

st.title('Connexion à une Base de Données NoSQL (MongoDB)')

mongo = MongoClient()

db= mongo.test_db

collection = db.test_collection

# st.write(db.list_collection_names())

username = st.text_input(label='username', label_visibility='hidden', placeholder='username',)
mail = st.text_input(label='email', label_visibility='hidden', placeholder='Email address')
if st.button('add'):
    collection.insert_one({username : mail})
    st.success('Account Created!')

for account in collection.find():
    st.write(account)

mongo.close()