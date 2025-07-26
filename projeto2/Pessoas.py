from GamePokemon import Pokemon, PokemonFogo, PokemonEletrico, PokemonAgua


class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Anônimo"

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)



class Player(Pessoa):
    tipo = "player"


class Inimigo(Pessoa):
    tipo = "inimigo"


meu_pokemon = PokemonEletrico("Pikachu")
meu_pokemon2 = PokemonFogo("Charmander")

eu = Player(nome="João", pokemons=[meu_pokemon, meu_pokemon2])

print(eu)
print(eu.mostrar_pokemons())