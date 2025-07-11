import streamlit as st

# --- Configuração da Página ---
st.set_page_config(page_title="Central de Aplicações", layout="wide")


# --- DADOS DOS APLICATIVOS (Estrutura Melhorada) ---
APPS = [
    {
        "nome": "Baixas Contas a Pagar",
        "url": "https://baixascpprotheus-dzywhhuxvrkqdmyd29jafy.streamlit.app/",
        "categoria": "Contas a Pagar",
        "icone": "📥",
        "descricao": "Automação para baixas de pagamentos no sistema Protheus."
    },
    {
        "nome": "Conciliação de Cartões",
        "url": "https://cart-escr-eefyjappnbdzi8vy7qcbn7m.streamlit.app/",
        "categoria": "Contas a Receber",
        "icone": "📑",
        "descricao": "Relatórios e conciliação de valores de adquirentes de cartão."
    },
    {
        "nome": "Cartões A LISA",
        "url": "https://imjbbbremlsq9m9bz22aek.streamlit.app/",
        "categoria": "Contas a Receber",
        "icone": "📑",
        "descricao": "Análise detalhada e escrituração dos cartões da A LISA."
    },
    {
        "nome": "Taxas de PIX (REDE)",
        "url": "https://taxa-rede-ctjhvxph4b7y27dldoucwc.streamlit.app/",
        "categoria": "Tesouraria",
        "icone": "📋",
        "descricao": "Apuração e visualização das taxas de transações PIX da Rede."
    },
    {
        "nome": "Incentivos SODEXO",
        "url": "https://incentivosodexo-hjqws5r5ifnnf3k52fzroc.streamlit.app/",
        "categoria": "Tesouraria",
        "icone": "📋",
        "descricao": "Controle e gestão dos pagamentos de incentivos Sodexo."
    },
    {
        "nome": "Rendimentos AplicAut",
        "url": "https://aplicaut-vrhade6riqeeacy99iqtzn.streamlit.app/",
        "categoria": "Tesouraria",
        "icone": "📈",
        "descricao": "Acompanhamento dos rendimentos de aplicações automáticas."
    },
]


# --- CSS COM A SUA PALETA DE CORES ---
st.markdown("""
    <style>
        /* 1. Fundo com a sua imagem corporativa */
        .stApp {
            background: url("https://assets.ellabs.net/images/background-espacolaser.png");
            background-size: cover; /* Garante que a imagem cubra todo o fundo */
        }
        
        /* 2. Título principal com a cor azul corporativa */
        .main-title {
            color: #003fc3;
            text-align: center;
            font-weight: bold;
        }

        /* 3. Estilo do Card, mantendo um design limpo mas adaptado */
        .app-card {
            background: #FFFFFF; /* Fundo branco sólido para melhor legibilidade sobre a imagem */
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            text-align: center;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 15px 0 rgba(0, 63, 195, 0.2); /* Sombra com tom azulado */
            border: 1px solid #E0E0E0;
            height: 180px; 
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .app-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 25px 0 rgba(0, 63, 195, 0.3);
            border-color: #003fc3; /* Borda azul ao passar o mouse */
        }
        .app-card-title {
            text-decoration: none;
            font-size: 20px;
            color: #003fc3; /* 4. Título do card com a cor azul */
            font-weight: bold;
            margin-bottom: 10px;
        }
        .app-card-desc {
            font-size: 14px;
            color: #333; /* Cor de texto padrão para boa leitura */
        }
        
        /* 5. Estilo para as abas (Tabs) para combinar */
        .stTabs [data-baseweb="tab-list"] {
        	gap: 24px;
        }
        .stTabs [data-baseweb="tab"] {
        	height: 50px;
            background-color: #f0f2f6;
            border-radius: 8px;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #e0e6f2;
        }
        .stTabs [aria-selected="true"] {
            background-color: #003fc3;
            color: white;
        }
        
    </style>
""", unsafe_allow_html=True)


# --- CABEÇALHO DA PÁGINA ---
st.markdown("""
    <div style="text-align: center;">
        <img src="https://cdn.brandfetch.io/espacolaser.com.br/132b29b7-ef4b-4dc1-8cd1-7c3f1f421c9e" alt="Logo Espaçolaser" width="250"/>
    </div>
""", unsafe_allow_html=True)

# Aplica a classe .main-title ao título
st.markdown('<h1 class="main-title">Central de Aplicações Financeiras</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Seu hub de automações financeiras.</p>", unsafe_allow_html=True)


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
