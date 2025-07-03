import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Central de Aplicações", layout="wide")
st.title("🧭 Central de Aplicativos Streamlit")

# Lista de apps disponíveis
apps = {
    "📥 Baixas CP Protheus": "https://baixascpprotheus-dzywhhuxvrkqdmyd29jafy.streamlit.app/",
    "📑 Cartões Escritório": "https://cart-escr-eefyjappnbdzi8vy7qcbn7m.streamlit.app/"
}

# Seletor
app_selecionado = st.selectbox("Selecione o app que deseja abrir:", list(apps.keys()))

# Ações
if st.button("🔗 Abrir em nova aba"):
    url = apps[app_selecionado]
    st.markdown(f"[Clique aqui para abrir {app_selecionado}]({url})", unsafe_allow_html=True)

if st.button("📥 Abrir integrado aqui na tela"):
    url = apps[app_selecionado]
    st.success(f"Carregando: {app_selecionado}")
    components.iframe(url, height=800, scrolling=True)
