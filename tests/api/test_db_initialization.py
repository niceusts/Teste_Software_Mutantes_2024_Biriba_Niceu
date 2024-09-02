import tempfile
import pytest
from pathlib import Path
from cards.db import DB

@pytest.fixture
def temp_db_path():
    # Cria um diretório temporário para o banco de dados
    temp_dir = tempfile.mkdtemp()
    temp_path = Path(temp_dir)
    yield temp_path
    # Remove o diretório temporário após os testes
    for file in temp_path.glob('*'):
        file.unlink()
    temp_path.rmdir()

@pytest.fixture
def db(temp_db_path):
    db_instance = DB(temp_db_path, 'test_db')
    yield db_instance
    db_instance.close()

def test_db_initialization(temp_db_path, db):
    # Verifique se o banco de dados foi criado corretamente
    assert db._db is not None  # Certifique-se de que o banco de dados está inicializado

    # Verifique se o arquivo foi criado no diretório
    assert any(file.suffix == '.json' for file in temp_db_path.glob('*'))
