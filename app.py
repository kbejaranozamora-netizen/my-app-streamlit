import streamlit as st

#st.title("Hola, IA 👋")
#nombre = st.text_input("¿Cómo te llamas?")
#if nombre:
 #   st.write(f"¡Hola, {nombre}! Esta es mi primera app en internet.")

st.title("Convertidor a Mayúsculas")

# Caja de texto para que el usuario escriba
texto_usuario = st.text_input("Escribe tu texto aquí:", "")

# Procesar el texto y mostrarlo en mayúsculas
texto_procesado = texto_usuario.upper()

# Mostrar el resultado en otra caja o área de texto
st.text_area("Texto procesado (Mayúsculas):", value=texto_procesado, height=100)
