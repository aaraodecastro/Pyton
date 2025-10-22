import streamlit as st

st.title("Convesor de Moedas")

real = st.number_input("Digite o valor em reais:")

opcao = st.selectbox(
    "Selecione uma moeda",
    ["Dolar","Euro"],
    index=None,
    placeholder="Moedas")

if opcao == "Dolar":
    st.text(f"O valor em dolares é de: {5*real}")  
elif opcao == "Euro":
    st.text(f"O valor em euros é de: {6*real}")
