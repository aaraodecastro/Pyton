import streamlit as st
from random import choice
from string import ascii_letters

st.title("Gerador de Senhas")

tamanho = st.select_slider(
    "Selecione o tamanho da senha",
    [5,6,7,8,])

aleatorio = ""

for i in range(tamanho):
    aleatorio += choice(ascii_letters)

st.text(f"A senha gerada foi: {aleatorio}")
print(tamanho)
