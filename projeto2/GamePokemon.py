import random


class Pokemon:

    def __init__(self, especie, level=random.randint(1, 100), nome=None):
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        print(f"{self} atacou {pokemon}")


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print(f'{self} lançou um choque do trovão em {pokemon}')


class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemon):
        print(f'{self} lançou uma bola de fogo na cabeça de {pokemon}')


class PokemonAgua(Pokemon):
    tipo = "Agua"

    def atacar(self, pokemon):
        print(f'{self} lançou um jato de água em {pokemon}')


meu_pokemon = PokemonFogo("Charmander")
pokemon_amigo = PokemonEletrico("Pikachu")

meu_pokemon.atacar(pokemon_amigo)
pokemon_amigo.atacar(meu_pokemon)

