from S4C1 import Stack
from typing import Type
Pilha = Stack()
Pilha.push(1.1)
Pilha.push(2.2)
Pilha.push(3.3)
def menorMaiorValor(Pilha: Stack) -> list[Type[float]]:
    Pilha = Pilha
    # print(Pilha.pop())
    tamanho: int = int(Pilha.size())
    lista: list[Type[float]] = list()
    contador: int = int(1)
    while contador < tamanho:
        lista = [Pilha.pop()]
        
        contador += 1
    return lista
# print(Pilha.pop())
print(menorMaiorValor(Pilha))