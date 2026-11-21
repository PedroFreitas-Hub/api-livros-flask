from flask import Flask, jsonify

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Lista com os três livros cadastrados
livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    {"id": 3, "titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977}
]

# Rota /livros que aceita apenas o método GET
@app.route('/livros', methods=['GET'])
def obter_livros():
    # Retorna a lista convertida para o formato JSON
    return jsonify({"livros": livros})

# Inicia o servidor local em modo de depuração
if __name__ == '__main__':
    app.run(debug=True)