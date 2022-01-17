

def getChoicesList(voter):
    array = []
    array.append(voter.get('1st'))    
    array.append(voter.get('2nd'))    
    array.append(voter.get('3rd'))    
    return array

class Voter:
    name = ''
    choices = []

    def __init__(self, voter):
        self.name = voter.get('name')
        self.choices = getChoicesList(voter)