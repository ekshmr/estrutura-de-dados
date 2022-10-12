from S4C1 import FloatStack
Pilha = FloatStack()
Pilha2 = FloatStack()
contador: int = 3
inserir_valor: str
numero_usuario: float
inserir_valor = input("Deseja adicionar um numero na pilha 1? ")
while contador > 0 and inserir_valor != "n":    
    if inserir_valor != "n":
        numero_usuario = float(input("Digite o que deseja inserir na pilha 1 "))
        Pilha.push(numero_usuario)
        print(Pilha)
    if inserir_valor != "n":
        numero_usuario = float(input("Digite o que deseja inserir na pilha 2 "))
        Pilha2.push(numero_usuario)
    contador -= 1
def pilhasIguais(Pilha1 : FloatStack, Pilha2 : FloatStack, contado : int) -> bool:
    sao_iguais: bool = False
    while contado > 0:
        if Pilha1.peek() == Pilha2.peek():
            sao_iguais = True
        else:
            sao_iguais = False
        contado -= 1
    return sao_iguais   
print(pilhasIguais(Pilha, Pilha2, 10))