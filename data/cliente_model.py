from dataclasses import dataclass

@dataclass
class Cliente:
    id: int
    nome: str
    cpf: int
    email: str
    telefone: int
    senha: str

