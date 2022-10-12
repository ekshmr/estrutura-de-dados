from S4C1 import FloatStack
Pilha = FloatStack()
Pilha.push(1.1)
Pilha.push(2.2)
Pilha.push(3.3)
def menorMaiorValor(Pilha: FloatStack) -> list[float]:
    Pilha = Pilha
    # print(Pilha.pop())
    tamanho: int = int(Pilha.tamanho())
    numeros: list[float] = list()
    contador: int = int(1)
    while contador < tamanho:
        numeros += [Pilha.pop()]
        contador += 1
    tamanho = len(numeros)
    contador= 0
    proximo_valor: float
    maior_valor: float
    while contador < tamanho:
        proximo_valor = numeros[contador + 1]
        if (numeros[contador] > proximo_valor): 
            maior_valor = numeros[contador]
            if ()
    return numeros
# print(Pilha.pop())
print(menorMaiorValor(Pilha))