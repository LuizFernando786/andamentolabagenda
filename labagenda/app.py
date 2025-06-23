from flask import Flask, render_template, request, redirect
from sqlite import banco

app = Flask(__name__)

# Criar a tabela se não existir
banco.criar_tabela()

# Página inicial (listar agendamentos)
@app.route('/')
def index():
    conexao = banco.conectar()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM agendamentos')
    agendamentos = cursor.fetchall()

    conexao.close()
    return render_template('index.html', agendamentos=agendamentos)

# Rota para adicionar um agendamento
@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    data = request.form['data']
    hora = request.form['hora']
    descricao = request.form['descricao']

    conexao = banco.conectar()
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO agendamentos (nome, data, hora, descricao)
        VALUES (?, ?, ?, ?)
    ''', (nome, data, hora, descricao))

    conexao.commit()
    conexao.close()

    return redirect('/')

# Rota para deletar um agendamento
@app.route('/deletar/<int:id>')
def deletar(id):
    conexao = banco.conectar()
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM agendamentos WHERE id = ?', (id,))

    conexao.commit()
    conexao.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
