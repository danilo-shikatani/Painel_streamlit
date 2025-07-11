import streamlit as st

# --- Configuração da Página ---
st.set_page_config(page_title="Central de Aplicações", layout="wide")


# --- DADOS DOS APLICATIVOS (Estrutura Melhorada) ---
# Mudei para uma lista de dicionários. Fica mais fácil adicionar novas informações
# como ícone e descrição para cada app.
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


# --- CSS (Estilo Modernizado) ---
st.markdown("""
    <style>
        /* Fundo com gradiente suave */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        /* Card com efeito de vidro (glassmorphism) */
        .app-card {
            background: rgba(255, 255, 255, 0.6);
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 25px;
            text-align: center;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            height: 180px; /* Altura fixa para alinhar os cards na grade */
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .app-card:hover {
            transform: translateY(-10px) scale(1.03);
            box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.3);
        }
        .app-card-title {
            text-decoration: none;
            font-size: 20px;
            color: #1E2A78; /* Cor mais forte para o título */
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

st.title("Central de Aplicações TESOURARIA")
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

# Filtra os aplicativos com base na busca
if termo_busca:
    apps_filtrados = [
        app for app in APPS
        if termo_busca.lower() in app["nome"].lower() or termo_busca.lower() in app["descricao"].lower()
    ]
    # Se houver busca, mostra tudo em uma única grade
    st.subheader(f"Resultados para '{termo_busca}'")
    cols = st.columns(3) # Cria 3 colunas para a grade
    for i, app in enumerate(apps_filtrados):
        with cols[i % 3]: # Loop entre as 3 colunas
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
    # Se não houver busca, mostra as abas
    abas = st.tabs(categorias)
    for i, categoria in enumerate(categorias):
        with abas[i]:
            apps_na_categoria = [app for app in APPS if app["categoria"] == categoria]
            cols = st.columns(3) # Cria 3 colunas para a grade dentro de cada aba
            for j, app in enumerate(apps_na_categoria):
                with cols[j % 3]: # Loop entre as 3 colunas
                    st.markdown(f"""
                        <a href="{app['url']}" target="_blank" style="text-decoration: none;">
                            <div class="app-card">
                                <div class="app-card-title">{app['icone']} {app['nome']}</div>
                                <p class="app-card-desc">{app['descricao']}</p>
                            </div>
                        </a>
                    """, unsafe_allow_html=True)
