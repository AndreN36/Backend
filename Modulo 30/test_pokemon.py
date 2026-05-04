import pytest
from pokemon import calcula_pontos_ataque, pokemon_evoluiu

# Fixtures (dados reutilizáveis)

@pytest.fixture
def bulbasaur():
    """
    Fixture que retorna um dicionário representando o Pokémon Bulbasaur.
    """
    return {
        "nome": "Bulbasaur",
        "forca_base": 49,
        "nivel": 10
    }


@pytest.fixture
def charmander():
    """
    Fixture que retorna um dicionário representando o Pokémon Charmander.
    """
    return {
        "nome": "Charmander",
        "forca_base": 52,
        "nivel": 15
    }

# Testes da função calcula_pontos_ataque

def test_calcula_pontos_ataque_bulbasaur(bulbasaur):
    """
    Testa se o cálculo de ataque do Bulbasaur está correto.
    """
    assert calcula_pontos_ataque(bulbasaur) == 490


def test_calcula_pontos_ataque_charmander(charmander):
    """
    Testa o cálculo de ataque do Charmander está correto.
    """
    assert calcula_pontos_ataque(charmander) == 780

# Testes da função pokemon_evoluiu

def test_pokemon_evoluiu_bulbasaur(bulbasaur):
    """
    Testa se o Bulbasaur evolui corretamente com base no nível.
    """
    # Não deve evoluir (nível insuficiente)
    assert pokemon_evoluiu(bulbasaur, 16) is False

    # Deve evoluir (nível suficiente)
    assert pokemon_evoluiu(bulbasaur, 10) is True


def test_pokemon_evoluiu_charmander(charmander):
    """
    Testa se o Charmander evolui corretamentecom base no nível.
    """
    # Não deve evoluir (nível insuficiente)
    assert pokemon_evoluiu(charmander, 20) is False

    # Deve evoluir (nível suficiente)
    assert pokemon_evoluiu(charmander, 15) is True