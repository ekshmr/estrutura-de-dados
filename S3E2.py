saltos: int = 0
nome_atleta: str = str(input("Digite o nome do atleta "))
alcance_saltos: list[float] = list()
valor_salto: float
while saltos < 5:
    valor_salto = float(input("Digite a distancia do salto "))
    alcance_saltos.append(valor_salto)
    saltos += 1
print(f"Atleta: {nome_atleta}\n")
saltos = 0
salto_atual: float
string_salto: str = ""
while saltos < 5:
    match saltos:
        case 0:
            string_salto = "Primeiro"
        case 1:
            string_salto = "Segundo"
        case 2:
            string_salto = "Terceiro"
        case 3:
            string_salto = "Quarto"
        case 4:
            string_salto = "Quinto"
        case _:
            pass
    salto_atual = alcance_saltos[saltos]
    print(f"{string_salto} salto: {salto_atual} m")
    saltos += 1

print(f"\nResultado final:\nAtleta: {nome_atleta}")
salto1_str: str = str(alcance_saltos[0])
salto2_str: str = str(alcance_saltos[1])
salto3_str: str = str(alcance_saltos[2])
salto4_str: str = str(alcance_saltos[3])
salto5_str: str = str(alcance_saltos[4])
salto1_float: float = float(alcance_saltos[0])
salto2_float: float = float(alcance_saltos[1])
salto3_float: float = float(alcance_saltos[2])
salto4_float: float = float(alcance_saltos[3])
salto5_float: float = float(alcance_saltos[4])
print(f"Saltos: {salto1_str} - {salto2_str} - {salto3_str} - {salto4_str} - {salto5_str}")
media_float = (salto1_float + salto2_float + salto3_float + salto4_float + salto5_float)
print(f"Média dos saltos: {media_float}")