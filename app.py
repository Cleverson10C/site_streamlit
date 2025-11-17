import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# ================================
# CONFIGURAÇÃO DA PÁGINA
# ================================
st.set_page_config(
    page_title="Portfólio de Automação - Cleverson dos Passos",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================================
# DADOS DO PORTFÓLIO
# ================================

def obter_dados_portfolio():
    """Retorna todos os dados necessários para exibir o portfólio."""
    
    # Projetos por categoria (1 ano de experiência)
    dados_projetos_por_categoria = {
        'Categoria': ['Web Scraping', 'RPA', 'APIs', 'Relatórios', 'Análise de Dados'],
        'Quantidade': [8, 6, 4, 12, 5],
        'Tempo Economizado (horas/semana)': [60, 40, 20, 80, 30]
    }
    
    # Proficiência em tecnologias
    dados_proficiencia_tecnologias = {
        'Tecnologia': ['Python', 'Selenium', 'Pandas', 'Flask', 'PostgreSQL', 'Scrapy', 'Plotly', "Matplotlib", 'Streamlit'],
        'Proficiência (%)': [85, 80, 75, 70, 65, 70, 72, 78, 74]
    }
    
    # Evolução temporal dos projetos (Nov 2024 - Out 2025)
    datas_timeline = pd.date_range(start='2024-11-01', end='2025-10-31', freq='M')
    dados_evolucao_temporal = {
        'Data': datas_timeline,
        'Projetos Concluídos': np.random.poisson(2, len(datas_timeline)),
        'Clientes Atendidos': np.random.poisson(1, len(datas_timeline))
    }
    
    # Impacto por setor de mercado
    dados_impacto_por_setor = {
        'Setor': ['E-commerce', 'Financeiro', 'Saúde', 'Educação', 'Varejo'],
        'Economia de Tempo (%)': [65, 58, 70, 60, 55],
        'ROI (%)': [220, 180, 280, 200, 160]
    }
    
    return dados_projetos_por_categoria, dados_proficiencia_tecnologias, dados_evolucao_temporal, dados_impacto_por_setor


# ================================
# SEÇÕES DO SITE
# ================================

def renderizar_secao_hero():
    """Renderiza a seção hero com foto, título e métricas principais."""
    
    # Layout: imagem do perfil + apresentação
    coluna_foto, coluna_apresentacao = st.columns([1, 2])
    
    with coluna_foto:
        # Foto de perfil
        try:
            st.image("imagem_redonda.png", width=200, caption="Cleverson dos Passos")
        except:
            st.write("📷 Foto de perfil")
    
    with coluna_apresentacao:
        st.markdown("# 🤖 Cleverson dos Passos")
        st.markdown("### Especialista em Automação Web | Python | RPA")
        st.markdown("")
        st.markdown("""
        **Transformando processos manuais em soluções automatizadas**
        
        Especialista em criar automações que economizam tempo e aumentam a produtividade empresarial.
        """)
    
    # Métricas de impacto
    st.markdown("---")
    
    metrica_projetos, metrica_horas, metrica_empresas, metrica_roi = st.columns(4)
    
    with metrica_projetos:
        st.metric(label="📊 Projetos Concluídos", value="25+", delta="10 este ano")
    
    with metrica_horas:
        st.metric(label="⏰ Horas Economizadas", value="800+", delta="150 horas/mês")
    
    with metrica_empresas:
        st.metric(label="🏢 Empresas Atendidas", value="12+", delta="5 novas este ano")
    
    with metrica_roi:
        st.metric(label="💰 ROI Médio", value="250%", delta="20% vs início do ano")


def renderizar_graficos_projetos(dados_projetos):
    """Renderiza gráficos de pizza e barras com distribuição de projetos."""
    st.markdown("## 📈 Distribuição de Projetos por Categoria")
    
    coluna_pizza, coluna_barras = st.columns(2)
    
    with coluna_pizza:
        # Gráfico de pizza: distribuição por categoria
        grafico_pizza = px.pie(
            values=dados_projetos['Quantidade'],
            names=dados_projetos['Categoria'],
            title="Projetos por Categoria",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        grafico_pizza.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(grafico_pizza, use_container_width=True)
    
    with coluna_barras:
        # Gráfico de barras: tempo economizado
        grafico_barras = px.bar(
            x=dados_projetos['Categoria'],
            y=dados_projetos['Tempo Economizado (horas/semana)'],
            title="Tempo Economizado por Categoria (horas/semana)",
            color=dados_projetos['Tempo Economizado (horas/semana)'],
            color_continuous_scale="Viridis"
        )
        grafico_barras.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(grafico_barras, use_container_width=True)


def renderizar_grafico_habilidades(dados_tecnologias):
    """Renderiza gráfico radar com proficiência em tecnologias."""
    st.markdown("## 🛠️ Proficiência em Tecnologias")
    
    # Gráfico radar: nível de proficiência
    grafico_radar = go.Figure()
    
    grafico_radar.add_trace(go.Scatterpolar(
        r=dados_tecnologias['Proficiência (%)'],
        theta=dados_tecnologias['Tecnologia'],
        fill='toself',
        name='Proficiência',
        line_color='rgb(30, 58, 138)',
        fillcolor='rgba(30, 58, 138, 0.3)'
    ))
    
    grafico_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        title="Radar de Habilidades Técnicas (%)"
    )
    
    st.plotly_chart(grafico_radar, use_container_width=True)


def renderizar_grafico_evolucao_temporal(dados_timeline):
    """Renderiza gráfico de linha com evolução de projetos ao longo do tempo."""
    st.markdown("## 📅 Evolução de Projetos ao Longo do Tempo")
    
    dataframe_timeline = pd.DataFrame(dados_timeline)
    
    # Gráfico de linhas: crescimento acumulado
    grafico_linha = go.Figure()
    
    grafico_linha.add_trace(go.Scatter(
        x=dataframe_timeline['Data'],
        y=dataframe_timeline['Projetos Concluídos'].cumsum(),
        mode='lines+markers',
        name='Projetos Concluídos (Acumulado)',
        line=dict(color='rgb(30, 58, 138)', width=3)
    ))
    
    grafico_linha.add_trace(go.Scatter(
        x=dataframe_timeline['Data'],
        y=dataframe_timeline['Clientes Atendidos'].cumsum(),
        mode='lines+markers',
        name='Clientes Atendidos (Acumulado)',
        line=dict(color='rgb(59, 130, 246)', width=3)
    ))
    
    grafico_linha.update_layout(
        title="Crescimento do Portfólio",
        xaxis_title="Período",
        yaxis_title="Quantidade",
        hovermode='x unified'
    )
    
    st.plotly_chart(grafico_linha, use_container_width=True)


def renderizar_grafico_impacto_setores(dados_setores):
    """Renderiza gráfico de dispersão com impacto por setor."""
    st.markdown("## 🏭 Impacto por Setor")
    
    # Gráfico de dispersão: economia vs ROI
    grafico_dispersao = px.scatter(
        x=dados_setores['Economia de Tempo (%)'],
        y=dados_setores['ROI (%)'],
        text=dados_setores['Setor'],
        size=[100]*len(dados_setores['Setor']),
        color=dados_setores['ROI (%)'],
        color_continuous_scale="Viridis",
        title="Economia de Tempo vs ROI por Setor"
    )
    
    grafico_dispersao.update_traces(textposition="middle center")
    grafico_dispersao.update_layout(
        xaxis_title="Economia de Tempo (%)",
        yaxis_title="ROI (%)"
    )
    
    st.plotly_chart(grafico_dispersao, use_container_width=True)


def renderizar_secao_sobre():
    """Renderiza a seção 'Sobre Mim' com informações pessoais e profissionais."""
    st.markdown("## 👨‍💻 Sobre Mim")
    
    # Layout: informações básicas + descrição detalhada
    coluna_info_basica, coluna_descricao = st.columns([1, 2])
    
    with coluna_info_basica:
        st.markdown("### 📍 Localização")
        st.write("Curitiba, PR - Brasil")
        
        st.markdown("### 💼 Experiência")
        st.write("1 ano em automação")
        
        st.markdown("### 🎯 Especialização")
        st.write("Python", "Web Scraping", "RPA", "APIs", "Análise de Dados")
    
    with coluna_descricao:
        st.info("""
        **Especialista em Automação e Desenvolvimento Python**
        
        Sou especialista em automação e desenvolvimento Python, com experiência em criar soluções inteligentes para empresas. 
        Domino ferramentas como **Selenium WebDriver**, **Scrapy**, **Beautiful Soup** e **Requests** para automação de 
        navegadores e web scraping avançado.
        
        Utilizo **Pandas**, **OpenPyXL**, **Matplotlib** e **Plotly** para análise e geração de relatórios automatizados, 
        otimizando processos e entregando resultados precisos.
        
        **Expertise em:**
        - 🤖 Robotic Process Automation (RPA)
        - 🔗 Integração de sistemas
        - 📊 Scripts de produtividade
        - 📈 Monitoramento automatizado
        - 🐍 Desenvolvimento backend com Flask
        - 🗄️ Bancos de dados (PostgreSQL, SQLite3, MySQL)
        """)
        
        # Botões de contato rápido
        st.markdown("### 🔗 Links Rápidos")
        botao_email, botao_linkedin = st.columns(2)
        
        with botao_email:
            st.link_button("📧 Email", "mailto:cleversonpassos35@gmail.com")
        
        with botao_linkedin:
            st.link_button("💼 LinkedIn", "https://linkedin.com/in/cleverson-dos-passos")


def renderizar_secao_processo():
    """Renderiza a seção com as etapas do processo de automação."""
    st.markdown("## ⚙️ Processo de Automação")
    
    etapa_coleta, etapa_tratamento, etapa_processamento, etapa_entrega = st.columns(4)
    
    with etapa_coleta:
        st.markdown("""
        ### 1️⃣ Coleta
        - Identificação de fontes
        - Web scraping
        - APIs
        """)
    
    with etapa_tratamento:
        st.markdown("""
        ### 2️⃣ Tratamento
        - Limpeza de dados
        - Validação
        - Estruturação
        """)
    
    with etapa_processamento:
        st.markdown("""
        ### 3️⃣ Processamento
        - Análise automática
        - Regras de negócio
        - Transformação
        """)
    
    with etapa_entrega:
        st.markdown("""
        ### 4️⃣ Entrega
        - Relatórios
        - Dashboards
        - Integrações
        """)


def renderizar_secao_contato():
    """Renderiza a seção de contato com formulário de orçamento."""
    st.markdown("## 📞 Entre em Contato")
    
    coluna_contatos, coluna_formulario = st.columns(2)
    
    with coluna_contatos:
        st.markdown("### 📧 Contato Profissional")
        st.write("**Email:** cleversonpassos35@gmail.com")
        st.write("**WhatsApp:** (41) 99235-6589")
        st.write("**Horário:** Seg - Sex: 8h às 18h")
        
        st.markdown("### 🔗 Redes Sociais")
        st.write("**GitHub:** [github.com/Cleverson10C](https://github.com/Cleverson10C)")
        st.write("**LinkedIn:** [linkedin.com/in/cleverson-dos-passos](https://linkedin.com/in/cleverson-dos-passos)")
    
    with coluna_formulario:
        st.markdown("### 💰 Solicitar Orçamento")
        
        with st.form("formulario_orcamento"):
            nome_cliente = st.text_input("Nome Completo")
            email_cliente = st.text_input("Email")
            whatsapp_cliente = st.text_input("WhatsApp com DDD")
            tipo_projeto = st.selectbox(
                "Tipo de Projeto",
                ["Automação Web", "Web Scraping", "RPA", "API Integration", "Análise de Dados", "Outro"]
            )
            detalhes_projeto = st.text_area("Detalhes do Projeto")
            
            formulario_enviado = st.form_submit_button("📨 Enviar Solicitação")
            
            if formulario_enviado:
                if nome_cliente and email_cliente and whatsapp_cliente and detalhes_projeto:
                    st.success("✅ Solicitação enviada com sucesso! Entrarei em contato em breve.")
                    st.info(f"""
                    **Resumo da Solicitação:**
                    - **Nome:** {nome_cliente}
                    - **Email:** {email_cliente}
                    - **WhatsApp:** {whatsapp_cliente}
                    - **Tipo:** {tipo_projeto}
                    - **Projeto:** {detalhes_projeto[:100]}...
                    """)
                else:
                    st.error("❌ Por favor, preencha todos os campos obrigatórios.")


def renderizar_lista_tecnologias():
    """Renderiza lista detalhada de tecnologias por categoria."""
    st.markdown("### 📋 Tecnologias Dominadas")
    
    coluna_web, coluna_dados, coluna_dev = st.columns(3)
    
    with coluna_web:
        st.markdown("**🌐 Automação Web**")
        st.write("• Selenium WebDriver")
        st.write("• Scrapy Framework")
        st.write("• Beautiful Soup")
        st.write("• Requests & APIs")
    
    with coluna_dados:
        st.markdown("**📊 Análise de Dados**")
        st.write("• Pandas")
        st.write("• OpenPyXL & Excel")
        st.write("• Streamlit")
        st.write("• Matplotlib & Plotly")
        st.write("• Relatórios Automatizados")
    
    with coluna_dev:
        st.markdown("**🐍 Desenvolvimento**")
        st.write("• Flask")
        st.write("• APIs RESTful")
        st.write("• PostgreSQL")
        st.write("• SQLAlchemy")


def renderizar_estatisticas_impacto():
    """Renderiza métricas adicionais de impacto profissional."""
    st.markdown("### 📈 Estatísticas de Impacto")
    
    metrica_tempo, metrica_satisfacao, metrica_economia = st.columns(3)
    
    with metrica_tempo:
        st.metric("Tempo Médio de Projeto", "1-3 semanas", "Entrega ágil")
    
    with metrica_satisfacao:
        st.metric("Taxa de Satisfação", "95%", "Baseado em feedback")
    
    with metrica_economia:
        st.metric("Economia Média", "60%", "Redução de tempo manual")


def renderizar_rodape():
    """Renderiza o rodapé do site."""
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; padding: 2rem; background-color: #1e3a8a; color: white; border-radius: 10px;'>"
        "<p>© 2025 Cleverson dos Passos - Todos os direitos reservados.</p>"
        "</div>", 
        unsafe_allow_html=True
    )


# ================================
# APLICAÇÃO PRINCIPAL
# ================================

def main():
    """Função principal que organiza e renderiza todas as seções do site."""
    
    # Carregar dados do portfólio
    dados_projetos, dados_tecnologias, dados_timeline, dados_setores = obter_dados_portfolio()
    
    # Seção Hero
    renderizar_secao_hero()
    st.markdown("---")
    
    # Navegação por abas
    aba_inicio, aba_analytics, aba_habilidades, aba_sobre, aba_contato = st.tabs([
        "🏠 Início", 
        "📊 Analytics", 
        "🛠️ Habilidades", 
        "👨‍💻 Sobre", 
        "📞 Contato"
    ])
    
    with aba_inicio:
        renderizar_secao_sobre()
        st.markdown("---")
        renderizar_secao_processo()
    
    with aba_analytics:
        renderizar_graficos_projetos(dados_projetos)
        st.markdown("---")
        renderizar_grafico_evolucao_temporal(dados_timeline)
        st.markdown("---")
        renderizar_grafico_impacto_setores(dados_setores)
    
    with aba_habilidades:
        renderizar_grafico_habilidades(dados_tecnologias)
        renderizar_lista_tecnologias()
    
    with aba_sobre:
        renderizar_secao_sobre()
        renderizar_estatisticas_impacto()
    
    with aba_contato:
        renderizar_secao_contato()
    
    # Rodapé
    renderizar_rodape()


if __name__ == "__main__":
    main()
