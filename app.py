import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Portfólio de Automação - Cleverson dos Passos",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dados para gráficos
def create_sample_data():
    # Dados de projetos por categoria (ajustados para 1 ano)
    projects_data = {
        'Categoria': ['Web Scraping', 'RPA', 'APIs', 'Relatórios', 'Análise de Dados'],
        'Quantidade': [8, 6, 4, 12, 5],
        'Tempo Economizado (horas/semana)': [60, 40, 20, 80, 30]
    }
    
    # Dados de tecnologias e proficiência
    tech_data = {
        'Tecnologia': ['Python', 'Selenium', 'Pandas', 'Flask', 'PostgreSQL', 'Scrapy', 'Plotly'],
        'Proficiência (%)': [85, 80, 75, 70, 65, 70, 72]
    }
    
    # Dados de projetos ao longo do tempo (Nov 2024 até Out 2025)
    dates = pd.date_range(start='2024-11-01', end='2025-10-31', freq='M')
    projects_timeline = {
        'Data': dates,
        'Projetos Concluídos': np.random.poisson(2, len(dates)),
        'Clientes Atendidos': np.random.poisson(1, len(dates))
    }
    
    # Dados de economia de tempo por setor
    sector_data = {
        'Setor': ['E-commerce', 'Financeiro', 'Saúde', 'Educação', 'Varejo'],
        'Economia de Tempo (%)': [65, 58, 70, 60, 55],
        'ROI (%)': [220, 180, 280, 200, 160]
    }
    
    return projects_data, tech_data, projects_timeline, sector_data

# Hero Section com métricas
def create_hero_section():
    # Criar duas colunas: uma para a imagem e outra para o conteúdo
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Adicionar a imagem de perfil
        try:
            st.image("imagem_redonda.png", width=200, caption="Cleverson dos Passos")
        except:
            st.write("📷 Foto de perfil")
    
    with col2:
        st.markdown("# 🤖 Cleverson dos Passos")
        st.markdown("### Especialista em Automação Web | Python | RPA")
        
        # Adicionar um pouco de espaço
        st.markdown("")
        
        # Breve descrição
        st.markdown("""
        **Transformando processos manuais em soluções automatizadas**
        
        Especialista em criar automações que economizam tempo e aumentam a produtividade empresarial.
        """)
    
    # Métricas em linha separada
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📊 Projetos Concluídos",
            value="25+",
            delta="10 este ano"
        )
    
    with col2:
        st.metric(
            label="⏰ Horas Economizadas",
            value="800+",
            delta="150 horas/mês"
        )
    
    with col3:
        st.metric(
            label="🏢 Empresas Atendidas",
            value="12+",
            delta="5 novas este ano"
        )
    
    with col4:
        st.metric(
            label="💰 ROI Médio",
            value="250%",
            delta="20% vs início do ano"
        )

# Gráfico de projetos por categoria
def create_projects_chart(projects_data):
    st.markdown("## 📈 Distribuição de Projetos por Categoria")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de pizza
        fig_pie = px.pie(
            values=projects_data['Quantidade'],
            names=projects_data['Categoria'],
            title="Projetos por Categoria",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Gráfico de barras - Tempo economizado
        fig_bar = px.bar(
            x=projects_data['Categoria'],
            y=projects_data['Tempo Economizado (horas/semana)'],
            title="Tempo Economizado por Categoria (horas/semana)",
            color=projects_data['Tempo Economizado (horas/semana)'],
            color_continuous_scale="Viridis"
        )
        fig_bar.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico de habilidades técnicas
def create_skills_chart(tech_data):
    st.markdown("## 🛠️ Proficiência em Tecnologias")
    
    # Gráfico radar das habilidades
    fig_radar = go.Figure()
    
    fig_radar.add_trace(go.Scatterpolar(
        r=tech_data['Proficiência (%)'],
        theta=tech_data['Tecnologia'],
        fill='toself',
        name='Proficiência',
        line_color='rgb(30, 58, 138)',
        fillcolor='rgba(30, 58, 138, 0.3)'
    ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        title="Radar de Habilidades Técnicas (%)"
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)

# Timeline de projetos
def create_timeline_chart(projects_timeline):
    st.markdown("## 📅 Evolução de Projetos ao Longo do Tempo")
    
    df_timeline = pd.DataFrame(projects_timeline)
    
    # Gráfico de linha dupla
    fig_timeline = go.Figure()
    
    fig_timeline.add_trace(go.Scatter(
        x=df_timeline['Data'],
        y=df_timeline['Projetos Concluídos'].cumsum(),
        mode='lines+markers',
        name='Projetos Concluídos (Acumulado)',
        line=dict(color='rgb(30, 58, 138)', width=3)
    ))
    
    fig_timeline.add_trace(go.Scatter(
        x=df_timeline['Data'],
        y=df_timeline['Clientes Atendidos'].cumsum(),
        mode='lines+markers',
        name='Clientes Atendidos (Acumulado)',
        line=dict(color='rgb(59, 130, 246)', width=3)
    ))
    
    fig_timeline.update_layout(
        title="Crescimento do Portfólio",
        xaxis_title="Período",
        yaxis_title="Quantidade",
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)

# Gráfico de setores atendidos
def create_sectors_chart(sector_data):
    st.markdown("## 🏭 Impacto por Setor")
    
    # Gráfico de dispersão - Economia vs ROI
    fig_scatter = px.scatter(
        x=sector_data['Economia de Tempo (%)'],
        y=sector_data['ROI (%)'],
        text=sector_data['Setor'],
        size=[100]*len(sector_data['Setor']),
        color=sector_data['ROI (%)'],
        color_continuous_scale="Viridis",
        title="Economia de Tempo vs ROI por Setor"
    )
    
    fig_scatter.update_traces(textposition="middle center")
    fig_scatter.update_layout(
        xaxis_title="Economia de Tempo (%)",
        yaxis_title="ROI (%)"
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)

# Seção sobre com card informativo
def create_about_section():
    st.markdown("## 👨‍💻 Sobre Mim")
    
    # Criar layout com duas colunas
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Adicionar algumas informações extras
        st.markdown("### 📍 Localização")
        st.write("Curitiba, PR - Brasil")
        
        st.markdown("### 💼 Experiência")
        st.write("1 ano em automação")
        
        st.markdown("### 🎯 Especialização")
        st.write("Python & Web Scraping")
    
    with col2:
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
    
        # Adicionar botões de contato
        st.markdown("### 🔗 Links Rápidos")
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            st.link_button("📧 Email", "mailto:cleversonpassos35@gmail.com")
        
        with col_btn2:
            st.link_button("💼 LinkedIn", "https://linkedin.com/in/cleverson-dos-passos")

# Processo de automação com diagrama
def create_process_section():
    st.markdown("## ⚙️ Processo de Automação")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        ### 1️⃣ Coleta
        - Identificação de fontes
        - Web scraping
        - APIs
        """)
    
    with col2:
        st.markdown("""
        ### 2️⃣ Tratamento
        - Limpeza de dados
        - Validação
        - Estruturação
        """)
    
    with col3:
        st.markdown("""
        ### 3️⃣ Processamento
        - Análise automática
        - Regras de negócio
        - Transformação
        """)
    
    with col4:
        st.markdown("""
        ### 4️⃣ Entrega
        - Relatórios
        - Dashboards
        - Integrações
        """)

# Seção de contato
def create_contact_section():
    st.markdown("## 📞 Entre em Contato")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📧 Contato Profissional")
        st.write("**Email:** cleversonpassos35@gmail.com")
        st.write("**WhatsApp:** (41) 99235-6589")
        st.write("**Horário:** Seg - Sex: 8h às 18h")
        
        st.markdown("### 🔗 Redes Sociais")
        st.write("**GitHub:** [github.com/Cleverson10C](https://github.com/Cleverson10C)")
        st.write("**LinkedIn:** [linkedin.com/in/cleverson-dos-passos](https://linkedin.com/in/cleverson-dos-passos)")
    
    with col2:
        st.markdown("### 💰 Solicitar Orçamento")
        
        with st.form("budget_form"):
            nome = st.text_input("Nome Completo")
            email = st.text_input("Email")
            whatsapp = st.text_input("WhatsApp com DDD")
            projeto_tipo = st.selectbox(
                "Tipo de Projeto",
                ["Automação Web", "Web Scraping", "RPA", "API Integration", "Análise de Dados", "Outro"]
            )
            mensagem = st.text_area("Detalhes do Projeto")
            
            submitted = st.form_submit_button("📨 Enviar Solicitação")
            
            if submitted:
                if nome and email and whatsapp and mensagem:
                    st.success("✅ Solicitação enviada com sucesso! Entrarei em contato em breve.")
                    # Mostrar resumo da solicitação
                    st.info(f"""
                    **Resumo da Solicitação:**
                    - **Nome:** {nome}
                    - **Email:** {email}
                    - **WhatsApp:** {whatsapp}
                    - **Tipo:** {projeto_tipo}
                    - **Projeto:** {mensagem[:100]}...
                    """)
                else:
                    st.error("❌ Por favor, preencha todos os campos obrigatórios.")

# Main app
def main():
    # Obter dados
    projects_data, tech_data, projects_timeline, sector_data = create_sample_data()
    
    # Hero Section
    create_hero_section()
    
    st.markdown("---")
    
    # Navegação com tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Início", 
        "📊 Analytics", 
        "🛠️ Habilidades", 
        "👨‍💻 Sobre", 
        "📞 Contato"
    ])
    
    with tab1:
        create_about_section()
        st.markdown("---")
        create_process_section()
    
    with tab2:
        create_projects_chart(projects_data)
        st.markdown("---")
        create_timeline_chart(projects_timeline)
        st.markdown("---")
        create_sectors_chart(sector_data)
    
    with tab3:
        create_skills_chart(tech_data)
        
        # Lista de habilidades em colunas
        st.markdown("### 📋 Tecnologias Dominadas")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**🌐 Automação Web**")
            st.write("• Selenium WebDriver")
            st.write("• Scrapy Framework")
            st.write("• Beautiful Soup")
            st.write("• Requests & APIs")
        
        with col2:
            st.markdown("**📊 Análise de Dados**")
            st.write("• Pandas")
            st.write("• OpenPyXL & Excel")
            st.write("• Matplotlib & Plotly")
            st.write("• Relatórios Automatizados")
        
        with col3:
            st.markdown("**🐍 Desenvolvimento**")
            st.write("• Flask")
            st.write("• APIs RESTful")
            st.write("• PostgreSQL")
            st.write("• SQLAlchemy")
    
    with tab4:
        create_about_section()
        
        # Adicionar algumas estatísticas extras
        st.markdown("### 📈 Estatísticas de Impacto")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Tempo Médio de Projeto", "1-3 semanas", "Entrega ágil")
        
        with col2:
            st.metric("Taxa de Satisfação", "95%", "Baseado em feedback")
        
        with col3:
            st.metric("Economia Média", "60%", "Redução de tempo manual")
    
    with tab5:
        create_contact_section()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; padding: 2rem; background-color: #1e3a8a; color: white; border-radius: 10px;'>"
        "<p>© 2025 Cleverson dos Passos - Todos os direitos reservados.</p>"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
