

# 📧 Classificador de Emails com IA

Aplicação web que utiliza **Inteligência Artificial (Google Gemini)** para classificar emails como **Produtivos** ou **Improdutivos**, além de gerar uma **resposta sugerida profissional** automaticamente.

O sistema foi desenvolvido com **Python no backend** e **HTML/CSS/JS no frontend**, permitindo que qualquer usuário cole um email e receba uma análise instantânea.

---

## 🚀 Funcionalidades

* Classificação automática de emails
* Geração de resposta sugerida com IA
* Interface simples e intuitiva
* Botão para copiar a resposta
* Tratamento de erros (cota da API, falha de conexão, etc.)

---

## 🧠 Tecnologias Utilizadas

### Backend

* Python 3
* FastAPI
* Google Gemini API (`google-genai`)
* Uvicorn
* python-dotenv

### Frontend

* HTML5
* CSS3
* JavaScript (Fetch API)

---

## 📂 Estrutura do Projeto

```
email-ai-classifier/
│
├── app/
│   ├── main.py        # API FastAPI
│   ├── ia.py          # Lógica com Gemini
│   ├── nlp.py         # Pipeline de normalização textual
│
├── templates/
│   └── index.html     # Interface web
│
├── static/
│   └── style.css      # Estilo da página
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔑 Configuração da API

1. Crie uma chave no Google AI Studio
   👉 [https://ai.google.dev/](https://ai.google.dev/)

2. Crie um arquivo `.env` na raiz.

3. Cole a linha abaixo com sua chave de API.

```env
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

---

## ▶️ Como Executar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/BetannySilva/email-ai-classifier.git
cd email-ai-classifier
```

2. Crie o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o servidor:

```bash
uvicorn app.main:app --reload
```

5. Acesse no navegador:

```
http://127.0.0.1:8000
```

---

## 🌐 Versão Online

A aplicação também pode ser hospedada em plataformas como **Render**.

---

## 🧪 Exemplo de Email para Teste

```text
Assunto: Problema com cobrança

Olá, bom dia.

Recebi uma cobrança indevida no meu boleto deste mês e gostaria de verificar o que ocorreu.
Poderiam me ajudar, por favor?

Atenciosamente,
Carlos Silva
```

---

## 📌 Observações

* A versão gratuita da API Gemini possui **limite diário de requisições**
* Em caso de erro 429, aguarde e tente novamente mais tarde

---

## 👨‍💻 Autora

**Betanny Alexandra da Silva Cruz**

Projeto com foco em IA aplicada à automação de atendimento.

---
