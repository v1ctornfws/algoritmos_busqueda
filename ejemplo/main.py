import streamlit as st

st.title("Sumador de 2 números")

num1 = st.number_input("Número 1", value=0.0, format="%.0f")
num2 = st.number_input("Número 2", value=0.0, format="%.0f")

if st.button("Sumar"):
    resultado = num1 + num2
    st.success(f"Resultado: {resultado}")
else:
    st.write("Introduce dos números y pulsa 'Sumar'.")
