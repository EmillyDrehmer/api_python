
from flask import Flask, jsonify, request
from flask_babel import Babel, _

app = Flask(__name__)

# CONFIGURACOES DE IDIOMA
app.config['BABEL_DEFAULT_LOCALE'] = 'pt_BR'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'America/Sao_Paulo'

# PERMITE EXIBIR ACENTOS NAS RESPOSTAS JSON
app.json.ensure_ascii = False

# SELECIONA O IDIOMA
def get_locale():
    return request.accept_languages.best_match(['pt_BR', 'en']) or 'pt_BR'

# INICIALIZA O FLASK-BABEL
babel = Babel(app, locale_selector=get_locale)

# LISTA DE LIVROS
livros = [
    {
        "id": 1,
        "titulo": "É assim que acaba",
        "autor": "Colleen Hoover"
    },
    {
        "id": 2,
        "titulo": "É assim que começa",
        "autor": "Colleen Hoover"
    },
    {
        "id": 3,
        "titulo": "Até o verão terminar",
        "autor": "Colleen Hoover"
    },
    {
        "id": 4,
        "titulo": "Todas as suas imperfeições",
        "autor": "Colleen Hoover"
    },
    {
        "id": 5,
        "titulo": "Um caso perdido",
        "autor": "Colleen Hoover"
    },
    {
        "id": 6,
        "titulo": "As mil partes do meu coração",
        "autor": "Colleen Hoover"
    },
    {
        "id": 7,
        "titulo": "Novembro 9",
        "autor": "Colleen Hoover"
    },
    {
        "id": 8,
        "titulo": "Um caso perdido",
        "autor": "Colleen Hoover"
    },
    {
        "id": 9,
        "titulo": "Sem esperança",
        "autor": "Colleen Hoover"
    },
    {
        "id": 10,
        "titulo": "Verity",
        "autor": "Colleen Hoover"
    },
    {
        "id": 11,
        "titulo": "Muac",
        "autor": "Maktub"
    },
     {
        "id": 12,
        "titulo": "Maktub",
        "autor": "Paulo Coelho"
        }
]

# CONSULTAR LIVROS
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)

#CRIAR AS ROTAS /LIVROSid
@app.route("/livros/<int:id>",methods=["GET"])
#<int:> -> indica que determinada variavel é inteiro
def obter_livros_por_id(id):
    for livro in livros: 
        if livro.get("id") == id:
            return jsonify(livro)
        else:
            return jsonify ({"message":"LIVRO NÃO ENCONTRADO!"}), 404

#PUT -> primeiro, os dados enviados pelo cliente 
#serão obtidos
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):
    #permite acessar os dados json enviados no corpo da requisição(body)
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id")== id:
            livros[indice].update(livro_alterado)
            return jsonify


#CRIAÇÃO DE UM NOVO LIVRO 
@app.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

    return jsonify(livros)

#delete-excluir um livro
@app.route("/livros/<int:id>", methods= ["DELETE"])
def excluir_livro(id):
    #como é necessario remover um elemento da lista pelo seu indice, sera utilizado novamente o enumerate()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)

# INICIALIZACAO DO SERVIDOR LOCAL
if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True
    )
