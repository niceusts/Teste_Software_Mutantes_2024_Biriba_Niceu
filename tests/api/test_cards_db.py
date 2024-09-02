# tests/api/test_cards_db.py

import tempfile
import pytest
from pathlib import Path
from cards.api import CardsDB  # Substitua por seu caminho real

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

def test_cards_db_initialization(temp_db_path):
    # Testa a inicialização da CardsDB para garantir que o nome do banco de dados está correto
    cards_db = CardsDB(temp_db_path)

    # Nome correto do arquivo do banco de dados
    expected_db_file = temp_db_path / ".cards_db.json"

    # Verifica se o arquivo do banco de dados foi criado com o nome esperado
    assert expected_db_file.exists()
