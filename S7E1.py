from S7C1 import IntegerQueue
contador: int = 1
valor_usuario: int
Fila = IntegerQueue()
while contador > 0:
    valor_usuario = int(input("Digite um valor inteiro "))
    if valor_usuario > 0:
        Fila.enqueue(valor_usuario)
    else:
        contador -= 1
contador = 8
while contador > 0:
    _ = Fila.dequeue()
    print(_)