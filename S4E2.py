from S4C1 import Stack
import random
import string
numeros = string.digits
letras = string.ascii_uppercase
def criaCarro():
    caractere = str()
    contador = 0
    while contador < 8:
        if (contador > 0 and contador < 4) or (contador == 5):
            caractere = caractere + str(random.choice(letras))
        if (contador == 4) or (contador > 5 and contador < 8):
            caractere = caractere + str(random.choice(numeros))
        contador += 1
    return caractere
contador = int()
contador = 0
Pilha = Stack()
while contador < 10:
    contador += 1
    Pilha.push(criaCarro())
    print(f"Carro {contador}: {Pilha.peek()}")
rodando: bool = True
mensagem_usuario: str
verifica_carros: bool = True
while rodando == True:
    mensagem_usuario = input("Deseja retirar um carro? (S/n) ")
    if mensagem_usuario != "S":
        rodando = False
        verifica_carros = False

    mensagem_usuario = input("Qual carro deseja tirar? ")
    print("Será necessário tirar os carros")
    while verifica_carros == True:
        if Pilha.peek() != mensagem_usuario:
            print(Pilha.peek())
            Pilha.pop()
        if Pilha.peek() == mensagem_usuario:
            verifica_carros = False
    rodando = False
