


def findCandidateObject(candidate, candidateArray):
    for i in candidateArray:
        if candidate == i.name:
            return i

def plularity(voterArray, candidateArray):
    for voter in voterArray:
        candidateObject = findCandidateObject(voter.choices[0], candidateArray)
        candidateObject.pluralityVotes += 1
    
    candidateWithMostVotes = candidateArray[0]
    for i in candidateArray:
        if i.pluralityVotes > candidateWithMostVotes.pluralityVotes:
            candidateWithMostVotes = i
    candidateWithMostVotes.pluralityVoteWinner = True

    

def borda(voterArray, candidateArray):
    for voter in voterArray:
        for index, vote in enumerate(voter.choices):
            candidateObject = findCandidateObject(vote, candidateArray)
            candidateObject.bordaVotes += len(voter.choices) - index

    candidateWithMostVotes = candidateArray[0]
    for i in candidateArray:
        if i.bordaVotes > candidateWithMostVotes.bordaVotes:
            candidateWithMostVotes = i
    candidateWithMostVotes.bordaVoteWinner = True

def isThereCondorcteCandidate(candidateArray):
    for i in candidateArray:
        if i.bordaVoteWinner and i.pluralityVoteWinner:
            i.condorcteCriterium = True
            return i
    return False
    

    