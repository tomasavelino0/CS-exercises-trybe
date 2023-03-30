class Tv:
    def __init__(self, tamanho) -> None:
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def aumentar_volume(self):
        if self.__volume < 99:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1

    def modificar_canal(self, canal):
        if canal <= 1 or canal >= 99:
            raise ValueError("Canal indisponível")

        self.__canal = canal

    def ligar_desligar(self):
        self.__ligada = not self.__ligada

    @property
    def volume(self):
        return self.__volume

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, new_canal):
        if new_canal not in range(1, 99):
            raise ValueError("o canal deve estar entre 1 e 99")
        self.__canal = new_canal

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, new_tamanho):
        self.__tamanho = new_tamanho

    @property
    def ligada(self):
        return self.__ligada


minha_tv = Tv(42)

minha_tv.aumentar_volume()
minha_tv.aumentar_volume()
minha_tv.aumentar_volume()
minha_tv.aumentar_volume()
minha_tv.aumentar_volume()

print(minha_tv.ligada)

print(minha_tv.volume)
