import streamlit as st
import requests

st.title('test avec flask')
server ='http://localhost:5000'

def requete():
    output = requests.get(f'{server}/data')
    data = output.json()
    return data

if st.button('get!'):
    data = requete()
    st.write('YEy :')
    st.json(data)