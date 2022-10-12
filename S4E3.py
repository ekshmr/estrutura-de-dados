from S4C1 import Stack()
Pilha = Stack()
Pilha2 = Stack()
contador: int = 10
inserir_valor: str
numero_usuario: float
inserir_valor = input("Deseja adicionar um numero na pilha 1? ")
while contador > 0 and inserir_valor != "n":    
    if inserir_valor != "n":
        numero_usuario = float(input("Digite o que deseja inserir na pilha 1 "))
        Pilha.push(numero_usuario)
    if inserir_valor != "n":
        numero_usuario = float(input("Digite o que deseja inserir na pilha 2 "))
        Pilha2.push(numero_usuario)
    contador -= 1
def pilhasIguais(Pilha1, Pilha2, contado) -> bool:
    sao_iguais: bool
    while contado > 0:
        if Pilha1.peek() == Pilha2.peek():
            sao_iguais = True
        else:
            sao_iguais = False
        contado -= 1
    print(sao_iguais)
    return sao_iguais
print(pilhasIguais(Pilha, Pilha2, 10))