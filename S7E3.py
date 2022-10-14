from S7C1 import FloatQueue
Fila = FloatQueue()
contador: int = 8
dicionario: dict[str,float]
while contador > 0:
    Fila.enqueue(float(input("Digite um número ")))
    contador -= 1
minimo: int
maximo: int
valor: float = float()
def dadosFila(Fila: FloatQueue) -> dict[str,float]:
    lista: list[float] = []
    media_aritmetica: float = float()
    condicao: FloatQueue = Fila
    while condicao.isEmpty() != True:
        valor = Fila.dequeue()
        lista.append(valor)
        media_aritmetica += valor
        _ = condicao.dequeue()
    minimo = min(lista)
    maximo = max(lista)
    media_aritmetica /= float(len(lista))
    dicionario = {"Maior valor da lista":maximo,"Menor valor da lista":minimo,"Média aritmética":media_aritmetica}
    return dicionario
print(dadosFila(Fila))