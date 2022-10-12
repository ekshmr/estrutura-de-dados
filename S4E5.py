from S4C1 import FloatStack
PilhaPositiva = FloatStack()
PilhaNegativa = FloatStack()
lista: list[float] = []
contador: int = 0
valor_usuario: float
lista_condicoes: list[float] = [0]
while contador < 8:
    valor_usuario = float(input("Digite um número positivo ou negativo "))
    lista += [valor_usuario]
    contador += 1
def organizaLista(lista: list[float], PilhaPositiva: FloatStack, PilhaNegativa: FloatStack) -> tuple[FloatStack, FloatStack]:
    for valor in lista:
        if valor > 0:
            PilhaPositiva.push(valor)
        if valor < 0:
            PilhaNegativa.push(valor)
        if valor == 0:
            _ = PilhaPositiva.pop()
            _ = PilhaNegativa.pop()
    return PilhaPositiva, PilhaNegativa
print(organizaLista(lista, PilhaPositiva, PilhaNegativa))