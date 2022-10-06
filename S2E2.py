import os
def limpar() -> int:
    os.system('cls')

limpar()

candidato_a: float = 0
candidato_b: float = 0
candidato_c: float = 0
candidato_d: float = 0
votos_nulo: float = 0
votos_branco: float = 0

quantidade_votos: int = int(input("Quantas pessoas irão votar? "))
limpar()
while quantidade_votos > 0:
    quantidade_votos -= 1
    escolha: str = str(input("\nURNA\n\n(1) Candidato A\n(2) Candidato B\n(3) Candidato C\n(4) Candidato D\n(5) Voto Nulo\n(6) Voto em Branco\n\n"))
    match escolha:
        case "1":
            escolha = "Candidato A"
            candidato_a += 1
        case "2":
            escolha = "Candidato B"
            candidato_b += 1
        case "3":
            escolha = "Candidato C"
            candidato_c += 1
        case "4":
            escolha = "Candidato D"
            candidato_d += 1
        case "5":
            escolha = "Voto Nulo"
            votos_nulo += 1
        case "6":
            escolha = "Voto Branco"
            votos_branco += 1
    limpar()

total_votos: float = round(candidato_a + candidato_b + candidato_c + candidato_d + votos_nulo + votos_branco, 0)

# print(f"\nQUANTIDADE DE VOTOS\n\nTotal: {total_votos}\nCandidato A: {candidato_a}\nCandidato B {candidato_b}\nCandidato C: {candidato_c}\nCandidato D: {candidato_d}\nVotos em Nulo: {votos_nulo}\nVotos em Branco: {votos_branco}")

def porcentagem(valor: float, total: float) -> float:
    return round((valor / total) * 100)

candidato_a_: float = porcentagem(candidato_a, total_votos)
candidato_b_: float = porcentagem(candidato_b, total_votos)
candidato_c_: float = porcentagem(candidato_c, total_votos)
candidato_d_: float = porcentagem(candidato_d, total_votos)
votos_nulo_: float = porcentagem(votos_nulo, total_votos)
votos_branco_: float = porcentagem(votos_branco, total_votos)

print(f"\nCandidato A: {candidato_a_}%\nCandidato B: {candidato_b_}%\nCandidato C: {candidato_c_}%\nCandidato D: {candidato_d_}%\n\nVotos Nulo: {votos_nulo_}%\nVotos Branco: {votos_branco_}%")