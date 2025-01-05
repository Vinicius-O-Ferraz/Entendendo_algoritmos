from collections import deque
# Montando grafo a partir de tabelas hash
grafo = {}
grafo['você'] = ['alice', 'bob','claire']
grafo['bob'] = ['anuj','peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['tom','jones']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['tom'] = []
grafo['jones'] = []

# Montando grafo a partir de tabelas hash
s_queue = deque()
s_queue += grafo['você']

def p_vende_manga(p):
    if p == 'anuj':
        return True
    return False


while s_queue:
    p = s_queue.popleft()
    if p_vende_manga(p):
        print(f"{p} vende manga")
    else:
        s_queue += grafo[p]
    
    
