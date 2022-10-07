def converte_horas(horario: str) -> str:
    string_horario: str = horario
    lista_horario: list = string_horario.split(":")
    horas_string: str = lista_horario[0]
    minutos_string: str = lista_horario[1]
    horas_float: float = float(horas_string)
    minutos_float: float = float(minutos_string)
    float_horario: float = round(float(((horas_float * 60) + minutos_float) / 60), 2)
    if float_horario > 12:
        float_horario -= 12
        notacao: str = "P.M."
    else:
        notacao: str = "A/M."
    ## ((horas_float * 60) + minutos_float) / 60
    string_horario = str(float_horario)
    lista_horario = string_horario.split(".")
    horas_float: float = float(lista_horario[0])
    minutos_float: float = float(lista_horario[1])
    horas_string = str(int(float_horario))
    minutos_string = str(round((float_horario * 60) % 60))
    horario = f"{horas_string}:{minutos_string} {notacao}\n"
    return horario

converteu: bool = False
rodando: bool = True
continuar: str = "S"
while rodando == True:    
    horario: str = str(input("Digite o horário no formato horas:minutos"))
    converteu = True
    if converteu == True:
        continuar: str = str(input("Quer converter outro horário? (S/n) "))
        if continuar == "n":
            rodando = False    
    print(converte_horas(horario))
    