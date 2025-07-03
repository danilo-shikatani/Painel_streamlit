import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Central de Aplicativos", layout="wide")
st.title("🚀 Central de Aplicações Streamlit")

# Links dos seus apps
apps = {
    "📥 Baixas CP Protheus": "https://baixascpprotheus-dzywhhuxvrkqdmyd29jafy.streamlit.app/",
    "📑 Cartões Escritório": "https://cart-escr-eefyjappnbdzi8vy7qcbn7m.streamlit.app/"
}

st.markdown("## Escolha um aplicativo para abrir:")

# Layout em colunas com botões
col1, col2 = st.columns(2)

with col1:
    if st.button("📥 Baixas CP Protheus"):
        st.markdown(f"[Abrir em nova aba]({apps['📥 Baixas CP Protheus']})", unsafe_allow_html=True)
        components.iframe(apps["📥 Baixas CP Protheus"], height=800)

with col2:
    if st.button("📑 Cartões Escritório"):
        st.markdown(f"[Abrir em nova aba]({apps['📑 Cartões Escritório']})", unsafe_allow_html=True)
        components.iframe(apps["📑 Cartões Escritório"], height=800)
