from S4C1 import IntegerStack
contador = 10
Pilha = IntegerStack()
while contador > 0:
    valor = int(input("Digite um valor "))
    Pilha.push(valor)
    contador -= 1
    ##print(contador)
while contador < 11:
    if Pilha.isEmpty() == False:
        print(Pilha.peek())
        _ = Pilha.pop()
    contador += 1
##print(Pilha.peek())