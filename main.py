from Candidate import Candidate
import Converter
from Voter import *
import VotingSystems

values = Converter.excelToJson('Votes.xlsx')
candidates = Converter.excelToJson('Votes.xlsx',sheet='Candidates')

candidateArray = []
for i in candidates:
    candidateArray.append(Candidate(i))

voterArray = []
for i in values:
    voterArray.append(Voter(i))

VotingSystems.plularity(voterArray, candidateArray)
VotingSystems.borda(voterArray, candidateArray)


print("name \tplurality \tborda")
for i in candidateArray:
    print(f"{i.name} \t{i.pluralityVotes} \t\t{i.bordaVotes}")

condorcte = VotingSystems.isThereCondorcteCandidate(candidateArray)
if(condorcte):
    print(f"Name of the Condorcte candidate is: {condorcte.name}")
else:
    print("There is no Condorcte candidate")
