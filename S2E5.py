numeros: list[int] = []
continuar: bool = True
mensagem: str
valor: int
while continuar == True:
    mensagem = input("Deseja inserir um número? (S/n)")
    if mensagem == "n":
        continuar = False
    else:
        valor = int(input("Digite um valor qualquer: "))
        numeros.append(valor)

def soma_valores(lista: list[int]) -> int:
    soma: int = 0
    for valor in lista:
        soma += valor
    return soma

print(soma_valores(numeros))