import streamlit as st 
import groq as Groq
from groq import Groq
CLAVE_API='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'

def crear_usuario_groq():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(api_key=clave_secreta)

    
st.set_page_config(page_title="Prueba de IA", page_icon="6️⃣", layout="centered")
st.title("Prueba de charla con mi propia ia")
nombre = st.text_input("¿Cuál es tu nombre?")

# Botón para mostrar el saludo
if st.button("Saludar"):
    st.write(f"¡Hola, {nombre}! gracias por venir a Talento Tech.")


MODELOS = [
    'llama3-8b-8192', 
    'llama3-70b-8192', 
    'mixtral-8x7b-32768'
    ]

def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
      model=modelo,
      messages=[{"role": "user", "content": mensajeDeEntrada}],
      stream=True
)

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

def configurar_pagina():
 
    # Agregamos un título principal a nuestra página
    st.title("Chat")
    st.sidebar.title("Configuración de la IA") # Creamos un sidebar con un título.
    elegirModelo =  st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    return elegirModelo

modelo = configurar_pagina()
mensaje= st.chat_input("Escribí tu mensaje")


clienteUsuario= crear_usuario_groq()

inicializar_estado()

# Tomamos el mensaje del usuario por el input.
mensaje = st.chat_input("Escribí tu mensaje:")

# Verificamos que el mensaje no esté vacío antes de configurar el modelo
if mensaje:
    configurar_modelo(clienteUsuario, MODELOS[1], mensaje)
    print(mensaje) # Mostramos el mensaje en la terminal para ver cómo se muestra

