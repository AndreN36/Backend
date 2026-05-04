import asyncio
import random
import time


# Listas de Pokémons por região
pokemons_kanto = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Eevee"]
pokemons_johto = ["Chikorita", "Cyndaquil", "Totodile", "Mareep", "Togepi"]
pokemons_hoenn = ["Treecko", "Torchic", "Mudkip", "Ralts", "Trapinch"]


async def busca_pokemon_kanto():
    """
    Simula a busca de um Pokémon na região de Kanto.
    Aguarda um tempo aleatório entre 1 e 5 segundos
    e retorna um Pokémon aleatório da região.
    """
    tempo_aleatorio = random.uniform(1, 5)
    print(f"[Kanto] Iniciando busca... Tempo estimado: {tempo_aleatorio:.2f}s")
    await asyncio.sleep(tempo_aleatorio)
    pokemon = random.choice(pokemons_kanto)
    return f"Kanto: {pokemon}"


async def busca_pokemon_johto():
    """
    Simula a busca de um Pokémon na região de Johto.
    Aguarda um tempo aleatório entre 1 e 5 segundos
    e retorna um Pokémon aleatório da região.
    """
    tempo_aleatorio = random.uniform(1, 5)
    print(f"[Johto] Iniciando busca... Tempo estimado: {tempo_aleatorio:.2f}s")
    await asyncio.sleep(tempo_aleatorio)
    pokemon = random.choice(pokemons_johto)
    return f"Johto: {pokemon}"


async def busca_pokemon_hoenn():
    """
    Simula a busca de um Pokémon na região de Hoenn.
    Aguarda um tempo aleatório entre 1 e 5 segundos
    e retorna um Pokémon aleatório da região.
    """
    tempo_aleatorio = random.uniform(1, 5)
    print(f"[Hoenn] Iniciando busca... Tempo estimado: {tempo_aleatorio:.2f}s")
    await asyncio.sleep(tempo_aleatorio)
    pokemon = random.choice(pokemons_hoenn)
    return f"Hoenn: {pokemon}"


async def main():
    """
    Executa as buscas simultaneamente usando asyncio.gather(),
    mede o tempo total de execução e exibe os resultados.
    """
    print("=== Simulador de Busca Assíncrona de Pokémons ===\n")

    inicio = time.perf_counter()

    resultados = await asyncio.gather(
        busca_pokemon_kanto(),
        busca_pokemon_johto(),
        busca_pokemon_hoenn()
    )

    fim = time.perf_counter()
    tempo_total = fim - inicio

    print("\n=== Resultados das Buscas ===")
    for resultado in resultados:
        print(f"- Pokémon encontrado em {resultado}")

    print(f"\nTempo total de execução: {tempo_total:.2f} segundos")


if __name__ == "__main__":
    asyncio.run(main())