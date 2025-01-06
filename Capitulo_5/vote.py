# Dicionário que funciona como uma hash table para registrar os votos.
voted = {}

def vote_verification(name):
    # Verifica se o nome já está na hash table.
    if voted.get(name):
        print("You cannot vote now, please leave immediately!")  # Mensagem caso o usuário já tenha votado.
        return

    # Adiciona o nome à hash table, marcando que o usuário já votou.
    voted[name] = True
    print("Vote now mate!")  # Mensagem caso o usuário ainda não tenha votado.
    return

# Testando a função com diferentes nomes.
vote_verification('paulinho')  # Output: Vote now mate!
vote_verification('amélia')    # Output: Vote now mate!
vote_verification('kid bengala')  # Output: Vote now mate!
vote_verification('paulinho')  # Output: You cannot vote now, please leave immediately
