import streamlit as st

st.set_page_config(page_title="Central de Aplicações", layout="centered")
st.title("🚀 Central de Aplicações Streamlit")

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
    "📥 Baixas CP Protheus": "https://baixascpprotheus-dzywhhuxvrkqdmyd29jafy.streamlit.app/",
    "📑 Cartões Escritório": "https://cart-escr-eefyjappnbdzi8vy7qcbn7m.streamlit.app/"
}

# Exibir cada card com link
for nome, url in apps.items():
    st.markdown(f"""
        <div class="app-card">
            <a href="{url}" target="_blank">{nome}</a>
        </div>
    """, unsafe_allow_html=True)
