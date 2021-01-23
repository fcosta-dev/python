from random import randint

class Die():
    """Uma classe que representa um único dado."""

    def __init__(self, num_sides=6): #quando uma instancia de nosso dado for criada o numero de lados sempre será 6.
        """Supõe que seja um dado de seis lados."""
        self.num_sides = num_sides

    def roll(self): #metodo roll usa a função randint para devolver um numero aleatorio entre 1 e o número de lados(6)
        """Devolve um valor aleatório entre 1 e o número de lados."""
        return randint(1, self.num_sides)
