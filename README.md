# Python REST OpenAI ETL - Explorando IA Generativa em um Pipeline de ETL

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange.svg)
![Status](https://img.shields.io/badge/Status-%20finalizado-green.svg)

## 📋 Descrição do Projeto

Este projeto é uma **implementação prática de um pipeline ETL (Extract, Transform, Load)** que integra uma **API pública de dados**, **inteligência artificial generativa (OpenAI)** e uma **API REST própria em Python (Flask)**.

O objetivo é demonstrar como enriquecer dados brutos com IA, seguindo a proposta do desafio **"Santander Dev Week 2023"** da [Digital Innovation One (DIO)](https://www.dio.me), mas aplicado a um novo domínio: **usuários de uma plataforma educacional de tecnologia**.

### 🎯 Fluxo do Pipeline ETL

```
┌─────────────────────────────────────────────────────────────────┐
│                    PIPELINE ETL COM IA                          │
└─────────────────────────────────────────────────────────────────┘

1️⃣ EXTRACT (Extração)
   └─→ JSONPlaceholder API
       └─→ GET https://jsonplaceholder.typicode.com/users
           └─→ Retorna: 10 usuários com dados básicos (id, name, email, address)

2️⃣ TRANSFORM (Transformação com IA)
   └─→ OpenAI ChatGPT API (gpt-4o-mini)
       └─→ Para cada usuário:
           ├─→ Gera: profile_summary (resumo do perfil)
           └─→ Gera: learning_path (trilha de estudos recomendada)

3️⃣ LOAD (Carregamento)
   └─→ Salva em CSV (data/users_transformed.csv)
   └─→ Expõe em API REST (Flask)
       └─→ GET http://127.0.0.1:5000/users
           └─→ Retorna: JSON com todos os usuários enriquecidos
```

---

## 🏗️ Arquitetura do Projeto

```
python-rest-openai-etl-users/
│
├── data/
│   └── users_transformed.csv          # Saída do pipeline (usuários enriquecidos)
│
├── etl/
│   ├── __init__.py
│   ├── extract.py                     # Extrai dados da API JSONPlaceholder
│   ├── transform.py                   # Transforma com OpenAI
│   └── load.py                        # Carrega em CSV
│
├── api/
│   ├── __init__.py
│   └── app.py                         # Servidor Flask (API REST)
│
├── .env                               # Variáveis de ambiente (NÃO versionar)
├── .env.example                       # Template do .env
├── .gitignore
├── requirements.txt                   # Dependências Python
├── main_etl.py                        # Orquestrador do pipeline
└── README.md                          # Este arquivo
```

---

## 🚀 Como Usar (Passo a Passo)

### Pré-requisitos

- **Python 3.8+**
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)
- **Chave de API da OpenAI** (obtenha em [platform.openai.com](https://platform.openai.com/api/keys))

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/GustavoMimoso/python-rest-openai-etl-users.git
cd python-rest-openai-etl-users
```

### 2️⃣ Criar Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sk-proj-sua_chave_aqui
OPENAI_MODEL=gpt-4o-mini
```

**⚠️ Importante:** Nunca comite `.env` para o GitHub! Já está no `.gitignore`.

### 5️⃣ Executar o Pipeline ETL

```bash
python main_etl.py
```

**Saída esperada:**

```
Extraindo usuários da API externa...
Transformando usuários com OpenAI...
Carregando dados transformados para CSV...
Pipeline ETL com API externa concluída com sucesso!
```

Verifique se o arquivo `data/users_transformed.csv` foi criado com sucesso.

### 6️⃣ Iniciar o Servidor Flask (API REST)

```bash
python api/app.py
```

**Saída esperada:**

```
 * Running on http://127.0.0.1:5000
```

### 7️⃣ Testar a API

#### Via cURL:

```bash
curl http://127.0.0.1:5000/users
```

#### Via Python:

```python
import requests

response = requests.get('http://127.0.0.1:5000/users')
print(response.json())
```

#### Via Insomnia/Postman:

1. Importe a URL: `http://127.0.0.1:5000/users`
2. Método: `GET`
3. Envie a requisição

**Resposta esperada (JSON):**

```json
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "email": "Sincere@april.biz",
    "username": "Bret",
    "address": {...},
    "profile_summary": "Leanne Graham é um usuário comprometido com...",
    "learning_path": "Backend com Python e Flask"
  },
  ...
]
```

---

## 📚 Conceitos Explorados

| Conceito | Descrição |
|----------|-----------|
| **ETL Pipeline** | Extração, Transformação e Carregamento de dados em 3 fases distintas |
| **APIs Externas** | Consumo de dados via REST (JSONPlaceholder) |
| **IA Generativa** | Integração com ChatGPT (OpenAI) para enriquecimento de dados |
| **Python Modular** | Organização em módulos independentes (extract, transform, load) |
| **REST API** | Criação de endpoint GET em Flask para expor dados |
| **Variáveis de Ambiente** | Segurança de credenciais via `.env` e `python-dotenv` |
| **Processamento de DataFrames** | Uso de `pandas` para manipulação de dados |
| **Integração Full Stack** | API externa → Processamento → Armazenamento → Endpoint REST |

---

## 🔑 Tecnologias Utilizadas

```
┌─────────────────────────────────────────────────────────┐
│          STACK TECNOLÓGICO DO PROJETO                   │
├─────────────────────────────────────────────────────────┤
│ Linguagem:       Python 3.8+                            │
│ Orquestração:    main_etl.py (script sequencial)       │
│ Extração:        requests + JSONPlaceholder API         │
│ Transformação:   OpenAI API (GPT-4o-mini)               │
│ Processamento:   pandas (DataFrame)                     │
│ Armazenamento:   CSV (data/)                            │
│ API REST:        Flask 2.0+                             │
│ Configuração:    python-dotenv                          │
│ Versionamento:   Git + GitHub                           │
└─────────────────────────────────────────────────────────┘
```

---

## 📦 Dependências

Todas as dependências estão listadas em `requirements.txt`:

```txt
openai>=1.30.0        # Cliente oficial da OpenAI
pandas                # Manipulação de DataFrames
python-dotenv         # Gerenciamento de variáveis de ambiente
flask                 # Framework web para API REST
requests              # Cliente HTTP para APIs
```

Para instalar:

```bash
pip install -r requirements.txt
```

---

## 🔄 Fluxo Detalhado de Execução

### 1. Fase de Extração (`etl/extract.py`)

```python
def extract_users_from_api() -> pd.DataFrame:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()  # Lista de dicionários
    df = pd.DataFrame(users)  # Converte para DataFrame
    return df
```

**Dados brutos obtidos:**
- `id`, `name`, `username`, `email`, `address` (city, street, etc.)
- 10 usuários de exemplo

### 2. Fase de Transformação (`etl/transform.py`)

Para cada usuário, o **ChatGPT é chamado** com o seguinte prompt:

```
Gere informações para o seguinte usuário:
Nome: {name}
Username: {username}
Email: {email}
Cidade: {city}

Regras:
- profile_summary: no máximo 2 parágrafos curtos.
- learning_path: sugestão objetiva de trilha.
```

**Saída de exemplo:**

```json
{
  "profile_summary": "Ana é uma profissional dinamarquesa interessada em desenvolvimento de software...",
  "learning_path": "Frontend React + TypeScript + Tailwind CSS"
}
```

### 3. Fase de Carregamento (`etl/load.py`)

Os dados transformados são salvos em:

```csv
id,name,email,username,profile_summary,learning_path
1,Leanne Graham,Sincere@april.biz,Bret,"Leanne é...",Backend Python
2,Ervin Howell,Shanna@melissa.tv,Antonette,"Ervin é...",Full Stack MERN
...
```

### 4. Exposição via API Flask (`api/app.py`)

```python
@app.route("/users", methods=["GET"])
def get_users():
    df = pd.read_csv("data/users_transformed.csv")
    return jsonify(df.to_dict(orient="records"))
```

Endpoint: `GET http://127.0.0.1:5000/users`

---

## 💡 Casos de Uso Práticos

### ✅ Casos Suportados

1. **Enriquecimento de Leads**
   - Entrada: Lista de contatos
   - IA: Gera resumo de interesse e trilha recomendada
   - Saída: Dados enriquecidos para CRM

2. **Classificação de Usuários**
   - Entrada: Perfis de usuários
   - IA: Identifica competências e recomendações
   - Saída: Segmentação automática

3. **Geração de Conteúdo Personalizado**
   - Entrada: Metadados de usuários
   - IA: Gera descrições, e-mails, mensagens
   - Saída: Conteúdo pronto para comunicação

---

## 🛠️ Modificações e Extensões

### Trocar a API de Origem

Edite `etl/extract.py`:

```python
# De JSONPlaceholder para outra API
NEW_API_URL = "https://api.exemplo.com/usuarios"

def extract_users_from_api() -> pd.DataFrame:
    response = requests.get(NEW_API_URL)
    return pd.DataFrame(response.json())
```

### Ajustar o Prompt da IA

Edite `etl/transform.py`:

```python
SYSTEM_PROMPT = """
Você é um especialista em [seu_domínio].
[Suas regras e instruções específicas]
"""
```

### Adicionar Novos Campos

Estenda `etl/transform.py`:

```python
return {
    "profile_summary": data.get("profile_summary"),
    "learning_path": data.get("learning_path"),
    "novo_campo": data.get("novo_campo")  # ← Novo
}
```

---

## ⚠️ Limitações e Considerações

| Aspecto | Descrição |
|---------|-----------|
| **Custo de API** | Cada chamada ao ChatGPT incorre em custo (menor com gpt-4o-mini) |
| **Rate Limit** | OpenAI tem limites de requisições (429 se exceder) |
| **Timeout** | Requisições longas podem expirar (defina timeout em requests) |
| **Dados Fake** | JSONPlaceholder fornece dados de exemplo, não reais |
| **Escalabilidade** | Para >1000 usuários, considere processamento em lote com delay |
| **Persistência** | CSV é simples; para produção, use banco de dados (PostgreSQL, MongoDB) |

---

## 🔐 Segurança

✅ **Boas Práticas Implementadas:**

- ✔️ Chave OpenAI em `.env` (nunca em código)
- ✔️ `.gitignore` configurado (não versionamos `.env`)
- ✔️ Validação de respostas JSON estruturadas
- ✔️ Tratamento de exceções em requisições HTTP

⚠️ **Melhorias Futuras:**

- [ ] Adicionar autenticação na API REST
- [ ] Implementar rate limiting
- [ ] Usar banco de dados em vez de CSV
- [ ] Adicionar testes unitários
- [ ] Logging estruturado com `logging` module

---

## 📖 Recursos Adicionais

### Documentação Oficial

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Pandas Documentation](https://pandas.pydata.org/docs)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com)

### Projeto Original (Santander Dev Week 2023)

- [GitHub - DIO Santander Dev Week 2023](https://github.com/digitalinnovationone/santander-dev-week-2023-api)
- [Notebook - SantanderDevWeek2023.ipynb](https://colab.research.google.com/github/digitalinnovationone/dio-lab-open-source/blob/main/SantanderDevWeek2023.ipynb)

### Referências de Aprendizado

- [DIO - Bootcamp Ciência de Dados](https://www.dio.me)
- [Python Official Docs](https://docs.python.org/3)
- [REST API Best Practices](https://restfulapi.net)

---

## 🤝 Como Contribuir

1. Faça um **fork** deste repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um **Pull Request**

---

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença **MIT**. Sinta-se livre para usar, modificar e distribuir.

---

## 👨‍💻 Autor

**Gustavo Mimoso**

- GitHub: [@GustavoMimoso](https://github.com/GustavoMimoso)
- Projeto: [python-rest-openai-etl-users](https://github.com/GustavoMimoso/python-rest-openai-etl-users)

---

## 🎓 Aprendizados e Insights

Este projeto foi desenvolvido como exercício prático do desafio da **Digital Innovation One (DIO)** e demonstra:

✅ Integração de múltiplas APIs (origem + OpenAI)
✅ Pipeline ETL profissional em Python
✅ Uso de IA generativa para enriquecimento de dados
✅ Exposição de dados via REST API
✅ Boas práticas de organização e segurança
✅ Potencial para evolução em projetos reais

---

## 📞 Dúvidas ou Sugestões?

Abra uma **issue** no repositório ou entre em contato!

---

**Última atualização:** Dezembro de 2025 | **Status:** Pronto para uso 🚀


