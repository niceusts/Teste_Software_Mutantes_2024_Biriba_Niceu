import os
import tempfile
import pytest
from pathlib import Path
from cards.db import DB

@pytest.fixture
def db():
    # Cria um banco de dados temporário
    temp_dir = Path(tempfile.mkdtemp())
    db_instance = DB(temp_dir, 'test_db')
    yield db_instance
    db_instance.close()
    # Remove o banco de dados temporário após os testes
    for file in temp_dir.glob("*.json"):
        file.unlink()
    temp_dir.rmdir()

def test_db_create(db):
    item = {'name': 'Test Card', 'value': 123}
    card_id = db.create(item)
    assert card_id is not None

def test_db_read(db):
    item = {'name': 'Test Card', 'value': 123}
    card_id = db.create(item)
    retrieved_item = db.read(card_id)
    assert retrieved_item['name'] == 'Test Card'
    assert retrieved_item['value'] == 123

def test_db_update(db):
    item = {'name': 'Test Card', 'value': 123}
    card_id = db.create(item)
    db.update(card_id, {'value': 456})
    updated_item = db.read(card_id)
    assert updated_item['value'] == 456

def test_db_delete(db):
    item = {'name': 'Test Card', 'value': 123}
    card_id = db.create(item)
    db.delete(card_id)
    deleted_item = db.read(card_id)
    assert deleted_item is None

def test_db_count(db):
    item1 = {'name': 'Test Card 1', 'value': 123}
    item2 = {'name': 'Test Card 2', 'value': 456}
    db.create(item1)
    db.create(item2)
    count = db.count()
    assert count == 2

def test_db_delete_all(db):
    item1 = {'name': 'Test Card 1', 'value': 123}
    item2 = {'name': 'Test Card 2', 'value': 456}
    db.create(item1)
    db.create(item2)
    db.delete_all()
    count = db.count()
    assert count == 0
