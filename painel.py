import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Central de Aplicativos", layout="centered")
st.title("🧭 Central de Aplicações TESOURARIA")
st.markdown("Selecione o aplicativo que deseja abrir abaixo:")

# Dicionário com nomes e links dos apps
apps = {
    "📥 Baixas Contas a Pagar Protheus": "https://baixascpprotheus-dzywhhuxvrkqdmyd29jafy.streamlit.app/",
    "📑 Cartões Adquirentes": "https://cart-escr-eefyjappnbdzi8vy7qcbn7m.streamlit.app/"
}

# Mostrar os botões em sequência (um abaixo do outro)
for nome, url in apps.items():
    st.markdown(f"### {nome}")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if st.button(f"🔗 Abrir {nome}"):
            st.markdown(f"[Abrir em nova aba]({url})", unsafe_allow_html=True)
            st.success(f"{nome} carregado abaixo 👇")

    with col2:
        # Mostra o iframe somente se o botão foi clicado
        if st.session_state.get(nome):
            components.iframe(url, height=800)
        else:
            st.empty()

    # Atualiza estado para mostrar iframe
    if f"🔗 Abrir {nome}" in st.session_state and st.session_state[f"🔗 Abrir {nome}"]:
        st.session_state[nome] = True

    st.markdown("---")
