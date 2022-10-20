from S4C1 import FloatStack
Pilha = FloatStack()
Pilha.push(9.9)
Pilha.push(8.8)
Pilha.push(7.7)
Pilha.push(-5.5)
Pilha.push(-10.10)
valor: float
quantidade: int
contador: int
def valoresNegativos(Pilha: FloatStack) -> int:
    quantidade = 0
    while Pilha.size() > 0:
        valor = Pilha.peek()
        _ = Pilha.pop()
        if valor < 0:
            quantidade += 1
    return quantidade
print(valoresNegativos(Pilha))