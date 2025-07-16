import streamlit as st

# --- Configuração da Página ---
st.set_page_config(page_title="Central de Aplicações", layout="wide")


# --- DADOS DOS APLICATIVOS
APPS = [
    {
        "nome": "Baixas Contas a Pagar",
        "url": "https://baixascpprotheus-dzywhhuxvrkqdmyd29jafy.streamlit.app/",
        "categoria": "Contas a Pagar",
        "icone": "📥",
        "descricao": "Automação para baixas de pagamentos no sistema Protheus."
    },
    {
        "nome": "Lançamentos Cartões",
        "url": "https://cart-escr-eefyjappnbdzi8vy7qcbn7m.streamlit.app/",
        "categoria": "Contas a Receber",
        "icone": "📑",
        "descricao": "Valores de adquirentes de cartão agrupado para input Protheus"
    },
    {
        "nome": "Cartões A LISA",
        "url": "https://imjbbbremlsq9m9bz22aek.streamlit.app/",
        "categoria": "Contas a Receber",
        "icone": "📑",
        "descricao": "Valores do repasse Corporeos p/ A LISA ."
    },
    {
        "nome": "Taxas de PIX (REDE)",
        "url": "https://taxa-rede-ctjhvxph4b7y27dldoucwc.streamlit.app/",
        "categoria": "Tesouraria",
        "icone": "📋",
        "descricao": "Apuração e visualização das taxas de transações PIX da Rede, para lançamentos Protheus."
    },
    {
        "nome": "Incentivos SODEXO",
        "url": "https://incentivosodexo-hjqws5r5ifnnf3k52fzroc.streamlit.app/",
        "categoria": "Tesouraria",
        "icone": "📋",
        "descricao": "Apuração e formatação para lançamentos de INCENTIVO SODEXO."
    },
    {
        "nome": "Rendimentos AplicAut",
        "url": "https://aplicaut-vrhade6riqeeacy99iqtzn.streamlit.app/",
        "categoria": "Tesouraria",
        "icone": "📈",
        "descricao": "Lançamentos de IR, IOF e rendimentos de aplicações automaticas."
    },
]


# --- CSS  ---
st.markdown("""
    <style>
        /* 1. Fundo da página branco */
        .stApp {
            background: #FFFFFF; 
        }

        /* 2. Estilo do Card ajustado para o fundo branco */
        .app-card {
            background: #FFFFFF; /* Fundo do card branco sólido */
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            text-align: center;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.08); /* Sombra mais sutil */
            border: 1px solid #EAECEF; /* Borda clara para definição */
            height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .app-card:hover {
            transform: translateY(-5px); /* Efeito de elevação mais sutil */
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12); /* Sombra mais pronunciada no hover */
        }
        .app-card-title {
            text-decoration: none;
            font-size: 20px;
            color: #2c3e50; /* Cor escura para bom contraste no branco */
            font-weight: bold;
            margin-bottom: 10px;
        }
        .app-card-desc {
            font-size: 14px;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)


# --- CABEÇALHO DA PÁGINA ---
st.markdown("""
    <div style="text-align: center;">
        <img src="https://cdn.brandfetch.io/espacolaser.com.br/132b29b7-ef4b-4dc1-8cd1-7c3f1f421c9e" alt="Logo Espaçolaser" width="250"/>
    </div>
""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: left;'>Central de Aplicações TESOURARIA</h1>", unsafe_allow_html=True)


st.markdown("<p style='text-align: left; color: grey;'>Seu hub de automações financeiras.</p>", unsafe_allow_html=True)



# --- FUNCIONALIDADE DE BUSCA ---
st.markdown("---")
termo_busca = st.text_input(
    "🔍 Buscar aplicação...",
    placeholder="Digite o nome do aplicativo ou uma palavra-chave...",
    label_visibility="collapsed"
)


# --- LÓGICA DE EXIBIÇÃO EM ABAS E GRADE ---
categorias = sorted(list(set(app["categoria"] for app in APPS)))

if termo_busca:
    apps_filtrados = [
        app for app in APPS
        if termo_busca.lower() in app["nome"].lower() or termo_busca.lower() in app["descricao"].lower()
    ]
    st.subheader(f"Resultados para '{termo_busca}'")
    cols = st.columns(3)
    for i, app in enumerate(apps_filtrados):
        with cols[i % 3]:
            st.markdown(f"""
                <a href="{app['url']}" target="_blank" style="text-decoration: none;">
                    <div class="app-card">
                        <div class="app-card-title">{app['icone']} {app['nome']}</div>
                        <p class="app-card-desc">{app['descricao']}</p>
                    </div>
                </a>
            """, unsafe_allow_html=True)
    if not apps_filtrados:
        st.warning("Nenhum aplicativo encontrado.")
else:
    abas = st.tabs(categorias)
    for i, categoria in enumerate(categorias):
        with abas[i]:
            apps_na_categoria = [app for app in APPS if app["categoria"] == categoria]
            cols = st.columns(3)
            for j, app in enumerate(apps_na_categoria):
                with cols[j % 3]:
                    st.markdown(f"""
                        <a href="{app['url']}" target="_blank" style="text-decoration: none;">
                            <div class="app-card">
                                <div class="app-card-title">{app['icone']} {app['nome']}</div>
                                <p class="app-card-desc">{app['descricao']}</p>
                            </div>
                        </a>
                    """, unsafe_allow_html=True)
