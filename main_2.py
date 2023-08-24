import sqlite3
from db.db_utils import *


conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS Estudantes
""")

cria_tabela(conn)

Estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022),
]
registro(conn, Estudantes)
conn.commit()

cursor.execute("SELECT * FROM Estudantes WHERE AnodeIngresso BETWEEN 2019 AND 2020")
print(cursor.fetchall())

atualiza(conn, "Estudantes", "AnodeIngresso", "Nome", 2023, "Maria Oliveira")
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())

deleta(conn, "Estudantes", "ID", 2)
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())

atualiza(conn, "Estudantes", "AnodeIngresso", "Curso", 3018, "Computação")
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())

conn.close()