calcular_horas_trabalhadas_mes: bool = bool()
resposta: str = str(input("Deseja saber quantas horas você trabalha ao mês? (S/n) "))
match resposta:
    case "S":
        calcular_horas_trabalhadas_mes = True
    case "s":
        calcular_horas_trabalhadas_mes = True
    case "N":
        calcular_horas_trabalhadas_mes = False
    case "n":
        calcular_horas_trabalhadas_mes = False
    case _:
        pass

match calcular_horas_trabalhadas_mes:
    case True:
        horas_trabalhadas_semana: float = float(input("Quantas horas você trabalha na semana? "))
        horas_trabalhadas_mes: float = horas_trabalhadas_semana * 4
    case False:
        horas_trabalhadas_mes: float = float(input("Quantas horas você trabalha por mês? "))
        horas_trabalhadas_semana: float = horas_trabalhadas_mes / 4

calcular_valor_por_hora: bool = bool()
resposta = str(input("Deseja saber o valor de horas trabalhadas ao mês? (S/n) "))
match resposta:
    case "S":
        calcular_valor_por_hora = True
    case "s":
        calcular_valor_por_hora = True
    case "N":
        calcular_valor_por_hora = True
    case "n":
        calcular_valor_por_hora = True
    case _:
        pass

valor_salario_bruto: float = float()
valor_por_hora: float = float()
match calcular_valor_por_hora:
    case True:
        valor_salario_bruto = float(input("Quanto você ganha por mês? "))
        valor_por_hora = round(valor_salario_bruto / horas_trabalhadas_mes, 2)
    case False:
        valor_por_hora = float(input("Quanto você ganha por hora? "))
        valor_salario_bruto = valor_por_hora * horas_trabalhadas_mes
    case _:
        pass

def valor_imposto_renda(valor: float) -> float:
    return valor * 0.08

def valor_inss(valor: float) -> float:
    return valor * 0.11

def valor_sindicato(valor: float) -> float:
    return valor * 0.05

imposto_renda: float = valor_inss(valor_salario_bruto)
inss: float = valor_inss(valor_salario_bruto)
sindicato: float = valor_sindicato(valor_salario_bruto)
valor_salario_total: float = (valor_salario_bruto) - (imposto_renda + inss + sindicato)

print(f"\nHoras trabalhadas na semana: {horas_trabalhadas_semana}\nHoras trabalhadas ao mês {horas_trabalhadas_mes}")
print(f"Valor Bruto do salário: {valor_salario_bruto}\nValor por hora: {valor_por_hora}")

print(f"Imposto de renda: {imposto_renda}\nINSS: {inss}\nSindicato: {sindicato}")

print(f"Valor Total do salário: {valor_salario_total}")
