import streamlit as st

st.set_page_config(page_title="Central de Aplicações", layout="centered")

# Exibir o logo centralizado
st.markdown("""
    <div style="text-align: center;">
        <img src="https://cdn.brandfetch.io/espacolaser.com.br/132b29b7-ef4b-4dc1-8cd1-7c3f1f421c9e" alt="Logo Espaçolaser" width="250"/>
    </div>
""", unsafe_allow_html=True)

st.title("Central de Aplicações TESOURARIA - ESPAÇO LASER")

# Estilo dos cards
st.markdown("""
    <style>
    .app-card {
        border: 2px solid #D3D3D3;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        text-align: center;
        transition: all 0.2s ease;
        background-color: #f9f9f9;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .app-card:hover {
        border-color: #4CAF50;
        background-color: #eaffea;
        transform: scale(1.02);
    }
    .app-card a {
        text-decoration: none;
        font-size: 22px;
        color: #000000;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Links dos apps
apps = {
    "📥 Baixas Contas a Pagar Protheus": "https://baixascpprotheus-dzywhhuxvrkqdmyd29jafy.streamlit.app/",
    "📑 Cartões Adquirentes": "https://cart-escr-eefyjappnbdzi8vy7qcbn7m.streamlit.app/",
    "📑 Cartões A LISA": "https://imjbbbremlsq9m9bz22aek.streamlit.app/",
    "📋 Taxa REDE PIX": "https://taxa-rede-ctjhvxph4b7y27dldoucwc.streamlit.app/"
}

# Exibir cada card com link
for nome, url in apps.items():
    st.markdown(f"""
        <div class="app-card">
            <a href="{url}" target="_blank">{nome}</a>
        </div>
    """, unsafe_allow_html=True)
