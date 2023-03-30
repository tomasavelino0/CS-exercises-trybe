class Ventilador:
    def __init__(self, cor: str, marca: str, preco: float):
        self.cor = cor
        self.marca = marca
        self.preco = preco

    def __str__(self):
        return f""""
                    cor: {self.cor} 
                    marca: {self.marca}
                    preco: {self.preco}"""


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None
        self.ventilador = None

    def comprar_liquidificador(self, liquidificador):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador

    def __str__(self):
        if not self.ventilador:
            return "Essa instancia nao possui um ventilador"
        else:
            return f"essa instancia possui o ventilador: {self.ventilador}"


tomas = Pessoa("tomas", 1500)
ventilador_azul = Ventilador("branco", "frio", 130.40)

tomas.comprar_ventilador(ventilador_azul)

print(tomas)
