contador: int = 0
nome_carro: str
qual_carro: str
catalogo: dict = {}
litros_a_cada_cem_km_str: str
litros_a_cada_cem_km: float
tipo_carro: str
alcance_em_km: float
kWh: float
kWh_a_cada_km: float
kWh_a_cada_km_str: str
bateria_em_kWh: float
bateria_em_kWh_str: str
km_a_cada_litro: float
valor_litro_gasolina: float = 6.25
valor_kWh: float = 1.304
reais_por_km_rodados: float
reais_por_km_rodados_loop: float
valor_mais_economico: float
dado: any
valor1: float
valot2: float
valor3: float
valor4: float
valor5: float
while contador < 5:
    match contador:
        case 0:
            qual_carro = "primeiro"
        case 1:
            qual_carro = "segundo"
        case 2:
            qual_carro = "terceiro"
        case 3:
            qual_carro = "quarto"
        case 4:
            qual_carro = "quinto"
    nome_carro = str(input(f"Digite o modelo do {qual_carro} carro "))
    tipo_carro = str(input("Digite o tipo do carro (Tradicional/Elétrico) "))
    if tipo_carro == "Tradicional" or tipo_carro == "tradicional":
        tipo_carro = "Tradicional"
        litros_a_cada_cem_km_str = str(input("Digite quantos litros o carro gasta a cada 100 km percorridos (L/100km) "))
        if litros_a_cada_cem_km_str.find(",") != -1:
            litros_a_cada_cem_km_str = litros_a_cada_cem_km_str.replace(",", ".")
        litros_a_cada_cem_km = float(litros_a_cada_cem_km_str)
        km_a_cada_litro = litros_a_cada_cem_km / 100
        reais_por_km_rodados = km_a_cada_litro * valor_litro_gasolina
        catalogo.update(dict({nome_carro:{"L/km":litros_a_cada_cem_km,"Tipo":tipo_carro,"R$/km":reais_por_km_rodados}}))
    if tipo_carro == "Elétrico" or tipo_carro == "elétrico" or tipo_carro == "eletrico":
        tipo_carro = "Elétrico"
        alcance_em_km = float(input("Digite quantos kilometros o carro percorre com uma carga completa (Alcance em km) "))
        bateria_em_kWh_str = str(input("Digite a especificação de kWh da bateria do carro (Bateria em kWh) "))
        if bateria_em_kWh_str.find(",") != -1:
            bateria_em_kWh_str = bateria_em_kWh_str.replace(",", ".")
        bateria_em_kWh = float(bateria_em_kWh_str)
        reducao_porcentagem = 1 - ((alcance_em_km - 100) / alcance_em_km)
        kWh_a_cada_km = (bateria_em_kWh * reducao_porcentagem) / 100
        reais_por_km_rodados = kWh_a_cada_km * valor_kWh
        
        catalogo.update(dict({nome_carro:{"kWh/km":kWh_a_cada_km,"Tipo":tipo_carro,"R$/km":reais_por_km_rodados}}))
    contador += 1
print(catalogo)
## CRÉDITOS AO ZERO ##
carro_eco = ['', 999]
for x in catalogo:
    if catalogo[x]["R$/km"] <= carro_eco[1]:
            carro_eco[0] = x
            carro_eco[1] = catalogo[x]["R$/km"]

print("Carro mais economico: ", carro_eco[0])
## FIM CRÉDITOS AO ZERO ##