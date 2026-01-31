

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

A aplicação também está hospedada na plataforma **Render**:
https://email-ai-classifier-q5u5.onrender.com/

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

### 📄 Justificativa para o uso de entrada em texto

A aplicação foi projetada para trabalhar exclusivamente com texto inserido manualmente pelo usuário, em vez de exigir o envio de arquivos (como PDFs ou imagens).

Essa decisão foi tomada por três motivos principais:

* **Facilidade de uso:**
O usuário pode simplesmente copiar e colar o conteúdo do email (assunto, remetente e corpo) no campo de texto, sem a necessidade de gerar ou converter arquivos.

* **Agilidade na análise:**
O processamento direto do texto elimina etapas intermediárias, tornando a resposta mais rápida e reduzindo falhas relacionadas a leitura de arquivos.

*  **Hospedagem mais simples e leve:**
Ao não lidar com upload de arquivos nem armazenamento em banco de dados, a aplicação consome menos recursos do servidor, facilitando a hospedagem em plataformas gratuitas e de baixo custo.

Assim, a escolha por trabalhar apenas com texto garante uma experiência mais prática para o usuário e maior eficiência técnica para o sistema.

---

## 👨‍💻 Autora

**Betanny Alexandra da Silva Cruz**

Projeto com foco em IA aplicada à automação de atendimento.

---
