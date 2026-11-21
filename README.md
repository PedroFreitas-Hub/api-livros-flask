# API de Livros com Python e Flask

## Objetivo da API
Disponibilizar o catálogo de livros de uma livraria através de uma rota HTTP GET, retornando os dados de três livros cadastrados em formato JSON.

## Instalação das dependências
1. Crie e ative o ambiente virtual:
   - **Windows (CMD/PowerShell):**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Git Bash / Linux / macOS:**
     ```bash
     python -m venv venv
     source venv/Scripts/activate
     ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução da aplicação
Com o ambiente virtual ativado, execute:
```bash
python app.py
```

## Rota disponibilizada
- **GET** `http://127.0.0.1:5000/livros` — Retorna a lista com os três livros em JSON.
