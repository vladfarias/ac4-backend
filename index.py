from flask import Flask, request, jsonify, json
import mysql.connector


app = Flask(__name__)

# Configurações de conexão
config = {
  'user': 'root',
  'password': 'senha',
  'host': 'localhost',
  'port': '3306',
  'database': 'db_Alunos',
}
# Estabelecer a conexão
connection = mysql.connector.connect(**config)

if connection.is_connected():
    print('Conexão bem-sucedida ao banco de dados MySQL!')
else:
    print('Erro ao conectar ao banco de dados')

@app.route('/listarAlunos', methods=['GET'])
def getAlunos():
    query = f"select * from tb_aluno"
    cursor = connection.cursor() # Poderia colocar para fora
    cursorExec = cursor.execute(query)
    result = cursor.fetchall()

    # Commit da transação e fechamento da conexão
    connection.commit()
    connection.close()

    return jsonify(result)

@app.route('/cadastrar', methods=['POST'])
def saveAluno():
    data = request.get_json()

    nome = data.get('nome')
    turma = data.get('turma')
    disciplina = data.get('disciplina')

    query = f"INSERT INTO tb_aluno (nome, turma, disciplina) VALUES (%s, %s, %s)"
    values = (nome, turma, disciplina)
    cursor = connection.cursor()
    cursor.execute(query, values)

     # Commit da transação e fechamento da conexão
    connection.commit()
    connection.close()

    return jsonify({'Messagem': f'Aluno cadastrado com sucesso {nome}'})


if __name__ =='__main__':
    app.run(port=5000, debug=True)
