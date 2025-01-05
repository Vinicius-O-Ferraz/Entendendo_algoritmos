voted = {}

def vote_verification(name):
    if voted.get(name):
        print("Fuck off motherfucker!")
        return

    voted[name] = True
    print("Vote now mate!")
    return

vote_verification('paulinho')
vote_verification('amélia')
vote_verification('kid bengala')
vote_verification('paulinho')
