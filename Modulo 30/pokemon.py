def calcula_pontos_ataque(pokemon: dict) -> int:
    """Calcula o poder de ataque baseado na força base e nível do Pokémon."""
    return pokemon["forca_base"] * pokemon["nivel"]


def pokemon_evoluiu(pokemon: dict, nivel_evolucao: int) -> bool:
    """Retorna True se o Pokémon pode evoluir."""
    return pokemon["nivel"] >= nivel_evolucao