CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf INTEGER NOT NULL,
    email TEXT NOT NULL,
    telefone INTEGER NOT NULL,
    senha TEXT NOT NULL)
"""

INSERIR_CLIENTE = """
INSERT INTO cliente (nome, cpf, email, telefone, senha)
VALUES (?,?,?,?,?)
"""

OBTER_TODOS = """
    SELECT
    id, nome, cpf, email, telefone, senha
    FROM cliente
"""