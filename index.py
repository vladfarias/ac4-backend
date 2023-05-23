from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import mysql.connector
import uuid

app = Flask(__name__)

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Configurações de conexão
config = {
  'user': db_user,
  'password': db_password,
  'host': db_host,
  'port': db_port,
  'database': db_name,
}
# Estabelecer a conexão
connection = mysql.connector.connect(**config)

if connection.is_connected():
    print('Conexão bem-sucedida ao banco de dados MySQL!')
else:
    print('Erro ao conectar ao banco de dados')

@app.route('/listarAlunos', methods=['GET'])
def get_alunos():
    query = f"select * from tb_aluno"
    cursor = connection.cursor() 
    cursor.execute(query)
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return jsonify(result)

@app.route('/cadastrar', methods=['POST'])
def save_aluno():
    data = request.get_json()

    nome = data.get('nome')
    turma = data.get('turma')
    disciplina = data.get('disciplina')
    id = str(uuid.uuid4())

    query = f"INSERT INTO tb_aluno (nome, turma, disciplina, ID) VALUES (%s, %s, %s, %s)"
    values = (nome, turma, disciplina, id)
    cursor = connection.cursor()
    cursor.execute(query, values)

    connection.commit()
    connection.close()

    return jsonify({'Messagem': f'Aluno cadastrado com sucesso {nome}'})

@app.route('/aluno/<id>', methods=['GET'])
def get_aluno_by_Id(id):
    query = f"SELECT * FROM tb_aluno WHERE ID = %s"
    values = (id,)
    cursor = connection.cursor()
    cursor.execute(query, values)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'message': 'Aluno não encontrado!'})
    
    aluno = {
        'id': result[3],
        'nome': result[0],
        'disciplina': result[2],
        'turma': result[1]
    }

    return jsonify(aluno)

if __name__ =='__main__':
    app.run(port=5000, debug=True)
