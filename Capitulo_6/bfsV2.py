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

def p_vende_manga(p):
    if p == 'anuj':
        return True
    return False

def mango_seach(p):
    s_queue = deque()
    s_queue += grafo[p]
    verified = []
    while s_queue:
        p = s_queue.popleft()
        if not p in verified:
            if p_vende_manga(p):
                print(f"{p} vende manga")
                return True
            else:
                s_queue += grafo[p]
                verified.append(p)
    print("Não foi possível achar quem queira essas manga pôdi vei")
    return False

mango_seach('você')
mango_seach('anuj')
mango_seach('tom')