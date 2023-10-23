import streamlit as st
import sqlite3

st.title('Connexion à une Base de Données SQL (SQLite)')

con = sqlite3.connect('my_sql_db.db')
cursor = con.cursor()

table_create = '''CREATE TABLE IF NOT EXISTS utilisateurs (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nom,
email

);'''

cursor.execute(table_create)
con.commit()

username = st.text_input(label='username', label_visibility='hidden', placeholder='username')
mail = st.text_input(label='email', label_visibility='hidden', placeholder='Email address')
if st.button('add'):
    cursor.execute(f'INSERT INTO utilisateurs (nom, email) VALUES ("{username}" , "{mail}");')
    st.success('Account Created!')
    con.commit()

if st.button('montre moi'):
    output = cursor.execute('SELECT * FROM utilisateurs')
    output = output.fetchall()
    st.write(output)

con.close()