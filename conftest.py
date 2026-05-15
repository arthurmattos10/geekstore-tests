import os
import pytest
import sqlite3

TEST_DB = "test.db"


@pytest.fixture(scope="function")
def test_db():

    # Usa banco de testes
    os.environ["DB_PATH"] = TEST_DB

    # Remove banco anterior se existir
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    # Cria banco temporário
    conn = sqlite3.connect(TEST_DB)

    conn.execute("""
        CREATE TABLE produtos (
            nome TEXT PRIMARY KEY,
            preco REAL,
            estoque INTEGER
        )
    """)

    # Dados fictícios
    conn.execute("""
        INSERT INTO produtos (nome, preco, estoque)
        VALUES ('teclado', 200.0, 10)
    """)

    conn.execute("""
        INSERT INTO produtos (nome, preco, estoque)
        VALUES ('mouse', 100.0, 5)
    """)

    conn.execute("""
        INSERT INTO produtos (nome, preco, estoque)
        VALUES ('monitor', 1500.0, 0)
    """)

    conn.commit()

    yield conn

    # Teardown
    conn.close()

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)