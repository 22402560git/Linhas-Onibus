import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Cálculo de demanda e distribuição de frota para as linhas")
st.header("Viação DSO")

nome = st.text_input("Digite seu nome:")
if nome:
    st.write("Olá,", nome)

linha = st.selectbox("Escolha as linhas:", ["8001A", "822", "9402", "9414"])

if linha:
    st.write("Linha selecionada:", linha) 

linhas = st.multiselect("Escolha as linhas:", ["8001A", "822", "9402", "9414"]) 
st.write(linhas)

if st.button("Calcular"):
    st.write("Calculando...")


