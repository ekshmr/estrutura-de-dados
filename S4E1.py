class Pilha:
    def __init__(self):
        self.itens: list[int] = []
    
    def vazia(self):
        return self.itens == []

    def enviar(self, item: int):
        self.itens.append(item)
    
    def pegar(self):
        return self.itens.pop()

    def ver(self):
        return self.itens[len(self.itens)-1]

    def size(self):
        return len(self.itens)

numero_base: int = 0
numero_usuario: int = 1
pilha = Pilha()
itens: list[int] = pilha.itens
while (numero_base <= 10) and (numero_usuario >= 1):
    numero_usuario = int(input("Digite um valor inteiro: "))    
    pilha.enviar(numero_usuario)
    print(itens)

deletar_itens: str = "N"
while deletar_itens != ("S" or "N"):
    deletar_itens = input("\nDeseja deletar os itens da pilha? (S/N) ")
    match deletar_itens:
        case "N":
            print("Saindo...")
        case "S":
            print("Deletando...")
        case _:
            pass
