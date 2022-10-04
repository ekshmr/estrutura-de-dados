calcular_horas_trabalhadas_mes: bool
resposta: str = str(input("Deseja saber quantas horas você trabalha ao mês? (S/n)"))
match resposta:
    case "S":
        calcular_horas_trabalhadas_mes = True
    case "s":
        calcular_horas_trabalhadas_mes = True
    case "N":
        calcular_horas_trabalhadas_mes = False
    case "s":
        calcular_horas_trabalhadas_mes = False

match calcular_horas_trabalhadas_mes:
    case True:
        horas_trabalhadas_semana: float = float(input("Quantas horas você trabalha na semana? "))
        horas_trabalhadas_mes: float = horas_trabalhadas_semana * 4
    case False:
        horas_trabalhadas_mes: float = float(input("Quantas horas você trabalha por mês? "))

calcular_valor_por_hora: bool
resposta = str(input("Deseja saber o valor de horas trabalhadas ao mês? (S/n)"))
match resposta:
    case "S":
        calcular_valor_por_hora = True
    case "s":
        calcular_valor_por_hora = True
    case "N":
        calcular_valor_por_hora = True
    case "n":
        calcular_valor_por_hora = True

match calcular_valor_por_hora:
    case True:
        valor_salario: float = float(input("Quanto você ganha por mês? "))
        valor_por_hora: float = valor_salario / horas_trabalhadas_mes
    case False:
        valor_por_hora: float = float(input("Quanto você ganha por hora? "))
        valor_salario: float = valor_por_hora * horas_trabalhadas_mes



print(f"{valor_por_hora}\n{horas_trabalhadas_mes}")