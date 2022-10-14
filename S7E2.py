from S7C1 import IntegerQueue
Fila = IntegerQueue() # Cria intância da classe Integer Queue
Fila.enqueue(1) # Coloca 1 na primeira posição da fila
Fila.enqueue(2) # Coloca 2 na segunda posição da fila
Fila.enqueue(3) # Coloca 3 na terceira posição da fila
Fila.enqueue(Fila.dequeue()) # Coloca 1 de volta pro começo da fila
Fila.enqueue(Fila.dequeue()) # Coloca 2 de volta pro começo da fila
print(Fila.dequeue()) # Imprime o primeiro valor na fila