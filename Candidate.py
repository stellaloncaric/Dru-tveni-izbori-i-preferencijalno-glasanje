

class Candidate:
    name = ''
    pluralityVotes = 0
    pluralityVoteWinner = False
    bordaVotes = 0
    bordaVoteWinner = False
    condorcteCriterium = False

    def __init__(self, candidate):
        self.name = candidate.get('Name')
    