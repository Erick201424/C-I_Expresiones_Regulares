import streamlit as st
from tkinter import *
import pandas as pd

st.title('Alberto Vázquez Miranda - 201425')
st.title('Erick Díaz Hernández - 201424')
df = pd.read_excel("contactos_2023.xlsx")

nombre = st.text_input("Buscar por nombre")

df['Nombre Contacto'] = df['Nombre Contacto'].str.upper()

filtered_df = df[df['Nombre Contacto'].str.contains(nombre.upper(), regex=True, na=False)]

st.write(filtered_df)

