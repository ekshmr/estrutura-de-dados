'''
2) Construa um programa em PYTHON utilizando uma pilha que resolva o 
seguinte problema:
Armazene as placas dos carros que estão estacionados numa rua sem saída 
estreita. Dado uma placa verifique se o carro está estacionado na rua. Caso 
esteja, informe a sequência de carros que deverá ser retirada para que o carro 
em questão consiga sair.
'''

import random

class Pilha:
    def __init__(self):
        self.itens: list = []

    def vazia(self):
        return self.itens == []

    def inserir(self, item: int):
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
id_carro: int
contador: int
placa_generica: int = "AAA0A00"
placa_carro: int
caractere: str

while cabe_carro == True:
    if quantidade_carros <= 6:
        cabe_carro = False
    # AAA0A00
    for caractere in placa_generica:
        contador += 1
        placa_carro[id_carro][contador]
