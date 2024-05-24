import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
    host=st.secrets['db_host'],
    port=st.secrets['db_port'],
    username=st.secrets['db_username'],
    password=st.secrets['db_password'],
    database=st.secrets['db_name']
)
cursor = conn.cursor()

nome = st.text_input('Digite o nome')
cadastrar = st.button('Cadastrar')

if cadastrar:

    sql = 'INSERT INTO pjp(nome) values (%s);'
    dados = (nome,)
    cursor.execute(sql,dados)
    conn.commit()
    cursor.close()
    conn.close()
