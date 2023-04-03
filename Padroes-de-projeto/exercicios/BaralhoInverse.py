from collections.abc import Iterator
import Baralho


class iteradorReverso(Iterator):
    def __init__(self, cartas):
        self._cartas = cartas
        self._pos = -1

    def __next__(self):
        try:
            carta = self._cartas[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos -= 1
            return carta


class BaralhoInverso(Baralho.Baralho):
    def _iter_(self):
        return iteradorReverso(self._cartas)


baralho = BaralhoInverso()
print(baralho[0])
