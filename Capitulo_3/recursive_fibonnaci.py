from time import time_ns  # Biblioteca para medir tempo em nanosegundos
import matplotlib.pyplot as plt  # Biblioteca para visualização de gráficos

def rec_fib(n):
    """
    Calcula o n-ésimo número de Fibonacci usando uma abordagem recursiva.

    Args:
        n (int): Posição do número de Fibonacci desejado (n >= 0).

    Returns:
        int: O n-ésimo número de Fibonacci.
    """
    if n < 2:
        return 1  # Caso base: Fibonacci(0) e Fibonacci(1) = 1
    else:
        # Calcula o número de Fibonacci como a soma dos dois anteriores
        return rec_fib(n-1) + rec_fib(n-2)

# Lista para armazenar os tempos de execução
intervals = []

# Intervalo de índices para calcular os números de Fibonacci
indices = range(2, 40)

# Medir o tempo de execução para cada índice no intervalo
for i in indices:
    start = time_ns()  # Tempo inicial
    rec_fib(i)  # Calcula o número de Fibonacci para o índice i
    end = time_ns()  # Tempo final
    intervals.append(end - start)  # Armazena o tempo decorrido

# Exibe os tempos de execução medidos
print("Tempos de execução (nanosegundos):", intervals)

# Plota o gráfico dos tempos de execução
plt.plot(indices, intervals)
plt.title("Crescimento do Tempo de Execução - Fibonacci Recursivo")
plt.xlabel("Índice (n)")
plt.ylabel("Tempo (nanosegundos)")
plt.grid()
plt.show()
