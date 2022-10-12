from S4C1 import FloatStack
Pilha = FloatStack()
Pilha.push(1.1)
Pilha.push(2.2)
Pilha.push(3.3)
def menorMaiorValor(Pilha: FloatStack) -> list[float]:
    Pilha = Pilha
    tamanho: int = int(Pilha.tamanho())
    numeros: list[float] = list()
    contador: int = int(1)
    while contador < tamanho:
        numeros += [Pilha.pop()]
        contador += 1
    tamanho = len(numeros)
    maior_e_menor: list[float] = [min(numeros), max(numeros)]
    return maior_e_menor
print(menorMaiorValor(Pilha))