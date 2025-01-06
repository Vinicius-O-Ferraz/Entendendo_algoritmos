from collections import deque

# Montando grafo a partir de tabelas hash.
grafo = {}
grafo['você'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['tom', 'jones']
grafo['anuj'] = []  # Nenhuma conexão, não vende manga.
grafo['peggy'] = []  # Nenhuma conexão, não vende manga.
grafo['tom'] = []  # Nenhuma conexão, não vende manga.
grafo['jones'] = []  # Nenhuma conexão, não vende manga.

# Função que verifica se a pessoa vende manga.
def p_vende_manga(p, target='anuj'):
    if p == target:
        return True
    return False

# Função que realiza a busca em largura (BFS) para encontrar quem vende manga.
def mango_seach(p, target='anuj'):
    # Inicializa a fila com as pessoas diretamente conectadas ao ponto de partida.
    s_queue = deque()
    s_queue += grafo[p]

    # Lista para verificar quem já foi visitado.
    verified = []

    # Enquanto houver pessoas na fila para explorar.
    while s_queue:
        p = s_queue.popleft()  # Retira a pessoa da frente da fila.

        # Se a pessoa ainda não foi verificada.
        if not p in verified:
            # Se a pessoa vende manga, exibe a mensagem e retorna True.
            if p_vende_manga(p, target):
                print(f"{p} vende manga")
                return True
            else:
                # Se a pessoa não vende manga, adiciona suas conexões à fila.
                s_queue += grafo[p]
                # Marca essa pessoa como verificada.
                verified.append(p)

    # Caso o algoritmo não encontre ninguém que venda manga.
    print("Não foi possível achar quem queira essas manga pôdi vei")
    return False

# Testes com diferentes pessoas.
mango_seach('você')  # Busca a partir de 'você' para encontrar quem vende manga.
mango_seach('anuj')  # Busca a partir de 'anuj', que é o alvo.
mango_seach('tom')   # Busca a partir de 'tom', que não vende manga.
mango_seach('bob', 'peggy')  # Busca a partir de 'bob' para encontrar 'peggy', que não vende manga.
