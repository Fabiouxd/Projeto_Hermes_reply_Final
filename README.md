# 🏭 Projeto de Digitalização Industrial - Hermes Reply

Este repositório contém a entrega final do **Desafio Hermes Reply**, que demonstra um pipeline de dados completo para digitalização industrial.
O projeto simula a **coleta, ingestão, armazenamento, análise e visualização de dados de sensores**, culminando em um sistema de **manutenção preditiva**.

---

## 🏗️ Arquitetura do Projeto

A arquitetura do sistema foi projetada para ser modular e reprodutível.
Ela conecta sensores simulados até a camada de decisão analítica.

📌 **Fluxo da pipeline:**

1. **Sensores Virtuais (ESP32):** dados simulados (DHT22, MPU6050, Potenciômetro).
2. **Ingestão e Armazenamento:** script Python processa as leituras e salva no banco de dados relacional (SQLite).
3. **Análise e Machine Learning:** dados armazenados alimentam um modelo de ML em Jupyter Notebook.
4. **Visualização e Alertas:** dashboard interativo exibe KPIs e gera alertas em tempo real.



---

## 📁 Estrutura do Repositório

```bash
├── db/              # Scripts SQL e o banco de dados SQLite
├── ingest/          # Scripts de simulação e ingestão de dados
├── ml/              # Notebooks e scripts de Machine Learning
├── dashboard/       # Dashboard interativo em Streamlit
├── docs/            # Diagramas e prints de execução
└── README.md        # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

* Python 3.10+
* Bibliotecas necessárias:

```bash
pip install pandas scikit-learn streamlit
```

### 2. Ingestão de Dados

Executar a ingestão para gerar o banco `sensores.db`:

```bash
cd ingest
python implementar_banco.py
```

### 3. Visualização com Dashboard

Rodar o dashboard interativo:

```bash
cd ../dashboard
streamlit run dashboard.py
```

O navegador será aberto automaticamente exibindo gráficos, KPIs e alertas.

### 4. Análise e Machine Learning

Abrir e executar o notebook:

```
ml/analise_exploratoria_hermes_reply_sprint_2.ipynb
```

Neste notebook você poderá:

* Conectar-se ao banco `sensores.db`;
* Fazer análise exploratória;
* Treinar e avaliar o modelo de Machine Learning.

---

## 🧠 Decisões Técnicas

* **Fonte de Dados:** simulação no **Wokwi** com ESP32 + DHT22 (temp/umidade) + MPU6050 (vibração).
* **Banco de Dados:** **SQLite**, escolhido pela leveza e simplicidade para prototipagem.
* **Modelo de ML:** **Regressão Logística** para classificar leituras em *Normal* ou *Anormal*.
* **Visualização:** **Streamlit** pela facilidade em criar dashboards rápidos e interativos.

---

## ✅ Resultados e Conclusão

* Pipeline ponta a ponta executada com sucesso (**coleta → ingestão → ML → dashboard/alerta**).
* Modelo de ML atingiu **99% de acurácia**, eficaz na detecção de anomalias.
* Dashboard exibe métricas em tempo real e dispara alertas funcionais.

Este MVP representa uma base sólida para **monitoramento industrial e manutenção preditiva** dentro do contexto da **Indústria 4.0**.

---

👨‍💻 **Desenvolvido por:**
Leonardo Alves Magalhães
Fábio Camargos Mendes
Marcos Vinicius dos Santos Morgado
Bernardo Zandoná Rupolo

