
# 📘 Documentação do Projeto - IntuitiveCare | Teste Técnico

## 1. Introdução

Este projeto foi desenvolvido como parte do teste técnico da IntuitiveCare. Seu principal objetivo é permitir a busca de operadoras de planos de saúde a partir de um arquivo CSV disponibilizado, oferecendo uma interface web simples e intuitiva para visualização dos dados.

- **Público-alvo**: Avaliadores técnicos da IntuitiveCare  
- **Propósito**: Demonstrar domínio de web scraping, transformação de dados, banco de dados e integração via API

---

## 2. Requisitos

### Requisitos Funcionais
- Permitir consulta textual de operadoras (nome fantasia)
- Abrir o resultado da busca em uma nova aba em formato JSON
- Interface deve conter campo de busca e botão "Pesquisar"

### Requisitos Não Funcionais
- Código limpo e versionado no GitHub
- Interface construída com Vue.js (Vite)
- Backend com Flask, retorno JSON
- Uso de Docker para PostgreSQL
- Estrutura de pastas clara e padronizada

---

## 3. Etapa 1 – Web Scraping

Foi realizada a extração de arquivos `.zip` contendo os dados disponibilizados no site da ANS.

- Utilizou-se a biblioteca `requests` para download automático dos arquivos.
- Em seguida, os arquivos foram descompactados com `zipfile`.
- Os dados relevantes foram identificados, padronizados e salvos para uso posterior.

Notebook utilizado: `etapa1_webscraping.ipynb`

---

## 4. Etapa 2 – Transformação de Dados

Transformações aplicadas sobre os arquivos `.csv` extraídos:

- Unificação dos dados trimestrais dos anos de 2023 e 2024
- Conversão de formatos numéricos e datas
- Criação de campo `ano_trimestre`
- Salvamento do arquivo final `todos_os_saldos.csv`

Notebook utilizado: `etapa2_transformacao.ipynb`

---

## 5. Etapa 3 – Banco de Dados

Foi utilizado o PostgreSQL com Docker, via `docker-compose.yml`.

### Estrutura do banco:

- Tabela `operadoras`: Dados do relatório `Relatorio_cadop.csv`
- Tabela `demonstracoes_contabeis`: Dados dos trimestres

Scripts utilizados:

- Criação: `create_tabelas.sql`, `criar_tabelas_psycopg2.py`
- Inserção: `importar_dados.sql`, `importar_dados_psycopg2.py`
- Consultas analíticas: `analises.sql`, `consultar_top10.py`

O banco está disponível com o seguinte serviço Docker:

```yaml
services:
  postgres:
    image: postgres:13
    container_name: postgres_teste_intuitive
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: intuitive
      POSTGRES_PASSWORD: intuitive
      POSTGRES_DB: teste_intuitive
```

---

## 6. Guia de Instalação

### Pré-requisitos
- Python 3.9+
- Node.js + npm
- Docker + Docker Compose

### Backend (Flask)
```bash
cd content/api_vue/backend
python -m venv venv
venv\Scripts\activate
pip install flask flask-cors pandas unidecode
python app.py
```

### Frontend (Vue.js)
```bash
cd content/api_vue/frontend
npm install
npm run dev
```

### Banco de Dados (Docker)
```bash
cd content/banco_de_dados
docker-compose up -d
```

---

## 7. Guia do Usuário

- Acesse `http://localhost:5173`
- Digite pelo menos 3 letras no campo de busca
- Clique em "Pesquisar"
- O resultado abrirá em nova aba com retorno da API

---

## 8. Documentação da API

### Endpoint
```
GET /buscar-operadora?query={termo}
```

### Parâmetro
- `query`: string parcial com o nome da operadora (mín. 3 letras)

### Retorno
```json
[
  {
    "Nome_Fantasia": "AMIL",
    "CNPJ": "2930**********",
    "...": "..."
  }
]
```

### Exemplo
```
GET http://127.0.0.1:5000/buscar-operadora?query=amil
```

---

## 9. Organização do Projeto

| Pasta               | Conteúdo                               |
|---------------------|----------------------------------------|
| `api_vue/backend`   | Flask + API + Postman Collection       |
| `api_vue/frontend`  | Interface Vue (Vite)                   |
| `banco_de_dados/`   | CSVs, docker-compose e dados           |
| `scripts/`          | SQL e ETL auxiliares                   |
| `transformacao/`    | Notebook com ETL                       |
| `web_scraping/`     | Código de scraping                     |
| `docs/`             | Documentação do projeto                |

---

## 10. Guia de Implantação

1. Suba o banco com `docker-compose up -d`
2. Rode a API com `python app.py`
3. Inicie o frontend com `npm run dev`
4. Acesse `http://localhost:5173` no navegador

---
