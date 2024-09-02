# tests/api/test_card.py
import pytest
from dataclasses import dataclass, field
from cards.api import Card  # Substitua por seu caminho real

def test_card_initialization():
    # Testa a criação de um Card com valores padrão
    card = Card()

    # Verifica que os atributos padrão estão corretamente definidos
    assert card.summary is None
    assert card.owner is None
    assert card.state == "todo"
    assert card.id is None

def test_card_custom_values():
    # Testa a criação de um Card com valores personalizados
    card = Card(summary="Test Summary", owner="Test Owner", state="done", id=1)

    # Verifica que os atributos foram definidos corretamente
    assert card.summary == "Test Summary"
    assert card.owner == "Test Owner"
    assert card.state == "done"
    assert card.id == 1

def test_card_state_annotation():
    # Testa a criação de um Card com o estado padrão
    card = Card()
    assert card.state == "todo"

    # Testa a criação de um Card com um estado personalizado
    card_custom_state = Card(state="in_progress")
    assert card_custom_state.state == "in_progress"

    # Testa a criação de um Card com None como estado
    card_none_state = Card(state=None)
    assert card_none_state.state is None
