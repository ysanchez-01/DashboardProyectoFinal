import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde GitHub (actualiza con tu URL)
url = 'https://raw.githubusercontent.com/farreolateran/DashboardProyectoFinal/refs/heads/main/Datos_proyecto_limpio.csv'
data = pd.read_csv(url)

# Título del dashboard
st.title('Dashboard de Indicadores Financieros')

# Desplegar los primeros registros de los datos
st.header('Datos Financieros')
st.write(data.head())

# Selección de la empresa
empresa = st.selectbox('Seleccione una empresa:', data['Company_ID'].unique())

# Filtrar los datos por la empresa seleccionada
datos_empresa = data[data['Company_ID'] == empresa]

# Gráfico de barras para el Ratio de Liquidez
st.subheader('Ratio de Liquidez')
fig, ax = plt.subplots()
ax.bar(datos_empresa['Company_ID'], datos_empresa['Current_Ratio'], color='blue')
ax.set_ylabel('Ratio de Liquidez')
ax.set_title('Ratio de Liquidez por Empresa')
st.pyplot(fig)

# Gráfico de líneas para el Ratio de Deuda a Patrimonio
st.subheader('Ratio de Deuda a Patrimonio')
fig, ax = plt.subplots()
ax.plot(datos_empresa['Company_ID'], datos_empresa['Debt_to_Equity_Ratio'], marker='o', color='green')
ax.set_ylabel('Ratio de Deuda a Patrimonio')
ax.set_title('Ratio de Deuda a Patrimonio por Empresa')
st.pyplot(fig)

# Gráfico circular para la Cobertura de Gastos Financieros
st.subheader('Cobertura de Gastos Financieros')
fig, ax = plt.subplots()
ax.pie([datos_empresa['Interest_Coverage_Ratio'].values[0], 100 - datos_empresa['Interest_Coverage_Ratio'].values[0]],
       labels=['Cobertura', 'Resto'], autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
ax.set_title('Cobertura de Gastos Financieros')
st.pyplot(fig)
