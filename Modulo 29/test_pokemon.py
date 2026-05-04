from pokemon import calcula_pontos_ataque, pokemon_evolui


def test_calcula_pontos_ataque_nivel_1():
    pokemon = {"forca_base": 10, "nivel": 1}
    assert calcula_pontos_ataque(pokemon) == 10


def test_calcula_pontos_ataque_nivel_0():
    pokemon = {"forca_base": 5, "nivel": 0}
    assert calcula_pontos_ataque(pokemon) == 0


def test_calcula_pontos_ataque_nivel_5():
    pokemon = {"forca_base": 20, "nivel": 5}
    assert calcula_pontos_ataque(pokemon) == 100


def test_pokemon_evolui_abaixo_do_nivel():
    pokemon = {"nivel": 15}
    assert pokemon_evolui(pokemon, 20) is False


def test_pokemon_evolui_no_nivel_exato():
    pokemon = {"nivel": 20}
    assert pokemon_evolui(pokemon, 20) is True


def test_pokemon_evolui_acima_do_nivel():
    pokemon = {"nivel": 25}
    assert pokemon_evolui(pokemon, 20) is True