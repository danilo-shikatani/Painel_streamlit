import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Central de Aplicativos", layout="centered")
st.title("🚀 Central de Aplicações Tesouraria")
st.markdown("### Escolha um aplicativo para abrir abaixo:")

# Dicionário com os nomes e URLs dos apps
apps = {
    "📥 Baixas CP Protheus": "https://baixascpprotheus-dzywhhuxvrkqdmyd29jafy.streamlit.app/",
    "📑 Cartões Escritório": "https://cart-escr-eefyjappnbdzi8vy7qcbn7m.streamlit.app/"
}

# Botões um embaixo do outro
for nome, url in apps.items():
    if st.button(nome):
        st.markdown(f"[🔗 Abrir {nome} em nova aba]({url})", unsafe_allow_html=True)
        components.iframe(url, height=1000)
        st.markdown("---")
