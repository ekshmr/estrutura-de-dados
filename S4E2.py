class Pilha:
    def __init__(self):
        self.itens: list[str] = []

    def vazia(self):
        return self.itens == []

    def inserir(self, item: str):
        self.itens.append(item)

    def remover(self):
        return self.itens.pop()

    def olhar(self):
        return self.itens[len(self.itens)-1]

    def tamanho(self):
        return len(self.itens)

cabe_carro: bool = True
quantidade_carros: int = 0
alfabeto_maiusculas: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
id_carro: int = int()
contador: int = int()
placa_generica: str = "AAA0A00"
placa_carro: list[int] = list()
caractere: str

while cabe_carro == True:
    if quantidade_carros <= 6:
        cabe_carro = False
    # AAA0A00
    for caractere in placa_generica:
        contador += 1
        placa_carro[id_carro]
