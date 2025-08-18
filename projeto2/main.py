from GamePokemon import *
from Pessoas import *


def escolher_pokemon_inicial(player):

    print(f"Olá {player}, você poderá escolher agora o pokemon que irá lhe acompanhar nessa jornada!")

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    Squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possui 3 escolhas:")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", Squirtle)

    while(True):
        escolha = input("Escolha o seu pokemon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(Squirtle)
            break
        else:
            print("Escolha inválida!")

player = Player("Guilherme")
#print(player)
#player.mostrar_pokemons()
escolher_pokemon_inicial(player)
player.mostrar_pokemons()
