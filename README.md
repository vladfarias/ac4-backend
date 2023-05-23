# Exemplo de payload

```json
{
    "nome": "João",
    "turma": "A",
    "disciplina": "Matemática",
}
```
# Script do banco de dados (MYSQL)

```sql
CREATE TABLE tb_aluno (
nome VARCHAR(20)
, turma VARCHAR(20)
, disciplina VARCHAR(20)
)
ALTER TABLE tb_aluno ADD ID VARCHAR(50);
ALTER TABLE tb_aluno ADD CONSTRAINT PK_ID PRIMARY KEY (ID);
