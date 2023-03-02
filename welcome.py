import streamlit as st
def bienvenida(nombre):
    mymensaje = f'fbienvenido/a {nombre}'
    return mymensaje
myname = st.text_input('nombre :')
if (myname):
   mensaje = bienvenida(myname)
