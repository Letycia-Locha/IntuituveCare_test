# IntuitiveCare Teste Técnico

![Capa do Projeto](https://img.freepik.com/vetores-gratis/conjunto-de-executivos-planos-organicos_23-2148953628.jpg)

Este repositório contém a solução desenvolvida para o teste técnico da IntuitiveCare, abordando desde a extração e tratamento de dados até a entrega de uma API funcional e uma interface web para consulta de operadoras.

---

## 🧩 Etapas do Projeto

1. **Web Scraping**  
   Coleta automatizada dos dados do site da ANS, convertendo para arquivos utilizáveis.

2. **Transformação de Dados**  
   Limpeza, padronização e estruturação dos arquivos para uso em banco de dados.

3. **Banco de Dados (PostgreSQL + Docker)**  
   Criação e popularização de tabelas com scripts SQL e Python.

4. **API Backend (Flask)**  
   Rota `/buscar-operadora` que busca operadoras por nome e retorna os dados mais relevantes.

5. **Frontend (Vue.js)**  
   Interface leve e responsiva para permitir buscas por operadora com design customizado.

---

##  Como Executar o Projeto

### 📦 Clonar o Repositório

```bash
git clone https://github.com/Letycia-Locha/IntuituveCare_test.git
cd IntuituveCare_test
```

---

### 🐘 Subir Banco de Dados com Docker

```bash
cd content/banco_de_dados
docker-compose up -d
```

---

### ⚙️ Backend com Flask

```bash
cd ../api_vue/backend
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate no Linux/macOS
pip install flask flask-cors pandas unidecode
python app.py
```

---

### 🌐 Frontend com Vue.js

```bash
cd ../frontend
npm install
npm run dev
```

Acesse via: [http://localhost:5173](http://localhost:5173)

---

## 🔍 Testando a API via Postman

A coleção Postman está disponível em:

```
content/api_vue/backend/Postman_colection.json
```

Exemplo de rota:

```
GET http://127.0.0.1:5000/buscar-operadora?query={{termo_busca}}
```

Substitua `{{termo_busca}}` por termos como `amil`, `unimed`, etc.

---

## 🧾 Arquivo Necessário para Funcionamento da API

O seguinte arquivo CSV foi mantido no repositório:

```
content/banco_de_dados/operadoras/Relatorio_cadop.csv
```

Ele é utilizado pela API como base de dados para busca de operadoras.

---

## 📁 Download Manual dos CSVs Pesados

Os arquivos `.csv` das demonstrações contábeis **não foram versionados** devido ao tamanho.  
Você pode baixá-los manualmente via Google Drive:

🔗 [Clique aqui para baixar os arquivos CSV](https://drive.google.com/drive/folders/1EfapOpjEhFD7ePNUVc-uS-CRpKx7WoXK?usp=sharing)

Após o download, posicione os arquivos exatamente assim:

```
content/
└── banco_de_dados/
|    └── demonstracoes_contabeis/
|       ├── 2023/
|       │   ├── 1T2023.csv
|       │   ├── 2T2023.csv
|       │   ├── 3T2023.csv
|       │   └── 4T2023.csv
|       ├── 2024/
|       │   ├── 1T2024.csv
|       │   ├── 2T2024.csv
|       │   ├── 3T2024.csv
|       │   └── 4T2024.csv
|       └── todos_os_saldos.csv
└── operadoras/
        ├── Relatorio_cadop.csv
```

> ⚠️ATENÇÃO! Mantenha os nomes dos arquivos exatamente como acima para garantir o funcionamento dos scripts.

---

## ✨ Considerações Finais

Este projeto foi desenvolvido com foco na sua organização, estrutura e usabilidade. 
Os dados são manipulados de forma segura, e toda a estrutura permite fácil execução via Docker ou ambiente local.

---

Desenvolvido por [Letycia Locha](https://github.com/Letycia-Locha)
