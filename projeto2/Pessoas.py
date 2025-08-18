import random
from GamePokemon import *


NOMES = ["João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego",
         "Patricia", "Marcelo", "Gustavo", "Gerônimo", "Gary"
         ]


POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarpy"),
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"Pokemons de {self}")
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f"{self} não possui pokemons")

        return None # Quando não coloco nenhum return no final é o mesmo que colocar return None no final.


class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon) # Vai add o pokemon a lista vazia
        print(f"{self} capturou {pokemon}")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons) # super() a classe pai e pode chamar os objetos contidos nele.