def valida_pessoa(nome: str, idade: int, salario: float, sexo: str, estado_civil: str) -> bool:
    valido: bool = True
    if len(nome) < 3:
        valido = False
    if idade < 0 and idade > 150:
        valido = False
    if salario < 1:
        valido = False
    if sexo == "f" or sexo == "m":
        string: str = "sexo valido"
    else:
        valido = False
    if estado_civil != ("s" or "c" or "v" or "d"):
        valido = False
    return valido
nome: str = str(input("Digite seu nome "))
idade: int = int(input("Digite sua idade "))
salario: float = float(input("Digite seu salário "))
sexo: str = str(input("Digite seu sexo (f ou m) "))
estado_civil: str = str(input("Digite seu estado civil (s ou c ou v ou d) "))
print(valida_pessoa(nome, idade, salario, sexo, estado_civil))