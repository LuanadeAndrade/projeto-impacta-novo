# from flask import Flask, jsonify, request, make_response, render_template


# class users:
#     def init(self, email, nome, senha):
#         self.email = email
#         self.nome = nome
#         self.senha= senha

# user1 = users('fvvariz@gmail', 'Fabricio', 'Fa@20012003')
# user2 = users('fvvariz@gmail', 'Fabricio', 'Fa@20012003')
# lista = [user1, user2]

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('template.html', titulo='Jogos', users=lista)

# @app.route('/novo')
# def novo():
#     return render_template('add.html', titulo='Usuario')

# @app.route('/criar', methods=['POST',])
# def criar():
#     email = request.form['email']
#     nome = request.form['nome']
#     senha = request.form['senha']
#     user = users(email, nome, senha)
#     lista.append(user)
#     return render_template('template.html', titulo='Jogos', users=lista)


# app.run(port=5000, host='localhost', debug=True)