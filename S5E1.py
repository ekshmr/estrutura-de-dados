from S4C1 import StringStack
import os
def limparTela() -> None:
    _ = os.system("cls")
sair: bool = False
url: str = str()
qual_opcao: str = str()
Pilha = StringStack()
pagina_aberta: bool = False
while sair == False:
    limparTela()
    if Pilha.isEmpty() != True:
        pagina_aberta = True
        print(Pilha.peek())
    else:
        pagina_aberta = False
    if pagina_aberta:
        string = "1 - Sair\n2 - Abrir uma página\n"
    else:
        string = "1 - Sair\n2 - Abrir uma página\n3 - Voltar\n"
    qual_opcao = str(input(string))
    match qual_opcao:
        case "1":
            sair = True
        case "2":
            url = str(input("Digite a URL da página que deseja abrir "))
            Pilha.push(url)
        case "3":
            if pagina_aberta != False:
                _ = Pilha.pop()
        case _:
            pass