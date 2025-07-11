import streamlit as st

# --- Configuração da Página (sem alteração) ---
st.set_page_config(page_title="Central de Aplicações", layout="centered")

# Exibir o logo centralizado
st.markdown("""
    <div style="text-align: center;">
        <img src="https://cdn.brandfetch.io/espacolaser.com.br/132b29b7-ef4b-4dc1-8cd1-7c3f1f421c9e" alt="Logo Espaçolaser" width="250"/>
    </div>
""", unsafe_allow_html=True)

st.title("Central de Aplicações Financeiras")

# --- Estilo dos cards (sem alteração) ---
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


# --- 1. NOVA ESTRUTURA DE DADOS (Organizada por Categoria) ---
# Agrupei seus apps nas pastas. Você pode facilmente mover um app para outra pasta
# apenas mudando ele de lugar neste dicionário.
apps_por_categoria = {
    "Tesouraria": {
        "📋 Taxa REDE PIX": "https://taxa-rede-ctjhvxph4b7y27dldoucwc.streamlit.app/",
        "📋 Incentivo SODEXO": "https://incentivosodexo-hjqws5r5ifnnf3k52fzroc.streamlit.app/",
        "📋 Rendimentos AplicAut": "https://aplicaut-vrhade6riqeeacy99iqtzn.streamlit.app/",
    },
    "Contas a Pagar": {
        "📥 Baixas Contas a Pagar Protheus": "https://baixascpprotheus-dzywhhuxvrkqdmyd29jafy.streamlit.app/",
    },
    "Contas a Receber": {
        "📑 Cartões Adquirentes": "https://cart-escr-eefyjappnbdzi8vy7qcbn7m.streamlit.app/",
        "📑 Cartões A LISA": "https://imjbbbremlsq9m9bz22aek.streamlit.app/",
    }
}


# --- 2. LÓGICA DE EXIBIÇÃO COM ABAS (TABS) ---
# Cria as abas usando as chaves do nosso dicionário como títulos
lista_de_categorias = list(apps_por_categoria.keys())
abas = st.tabs(lista_de_categorias)

# Itera sobre as abas e os dicionários ao mesmo tempo
for i, nome_categoria in enumerate(lista_de_categorias):
    with abas[i]:
        # Pega a lista de apps para a categoria atual
        apps_na_categoria = apps_por_categoria[nome_categoria]
        
        if not apps_na_categoria:
            st.write("Nenhuma aplicação nesta categoria.")
        else:
            # Exibe cada card com link, usando a mesma lógica de antes
            for nome_app, url_app in apps_na_categoria.items():
                st.markdown(f"""
                    <div class="app-card">
                        <a href="{url_app}" target="_blank">{nome_app}</a>
                    </div>
                """, unsafe_allow_html=True)
