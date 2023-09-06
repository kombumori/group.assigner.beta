import fire
import openpyxl
import random
import pprint
from statistics import variance
import math
import pickle

def main(f, r, g, rng, m="create"):
    if(m is "restore"):
        with open('autosave.pickle', mode='br') as fi:
            selectedGroup = pickle.load(fi)
        return 
    wb = openpyxl.load_workbook(f)
    ws = wb.worksheets[0]
    values = []
    for row in ws[rng]:
        rowValues = []
        for col in row:
            rowValues.append(col.value)
        values.append(rowValues)
    groupCandidates = [createGroupCandidate(values, g) for _ in range(1000)]
    groupCandidateScores = list(map(lambda groupCandidate: variance(list(map(lambda group: sum(map(lambda row: row[4]=="女",group))/len(group),groupCandidate))),groupCandidates))
    selectedGroup = groupCandidates[groupCandidateScores.index(min(groupCandidateScores))]
    print(min(groupCandidateScores))
    for _ in range(r):
        annealing = annealingList(selectedGroup)
        selectedGroup = annealing[1]
        pprint.pprint(selectedGroup)
        with open('autosave.pickle', mode='wb') as fo:
            pickle.dump(selectedGroup, fo)
    print("### FINISHED ###")
    print(f'SCORE: {annealing[0]}')
    print("RESULT: ")
    pprint.pprint(list(map(lambda group: list(map(lambda member: int(member[0]),group)),annealing[1])))

def createGroupCandidate(values, g):
    groups = [[] for _ in range(g)]
    for row in values:
        isSet = False
        while not isSet:
            groupIndex = random.randint(0,(g-1))
            if len(groups[groupIndex]) < math.ceil(len(values)/g):
                groups[groupIndex].append(row)
                isSet = True
    return groups

def annealingList(groupCandidate):
    memberLists = list(map(lambda group: list(map(lambda member: [member[0],member[1:4]],group)),groupCandidate))
    friendsNumList = list(map(lambda members: getFriendsNum(members), memberLists))
    baseFriendScore = sum(friendsNumList)
    newFriendScore = 1
    while baseFriendScore > newFriendScore:
        memberAsex = "女"
        memberBsex = "男"
        while memberAsex is not memberBsex:
            groupAindex = random.randint(0,(len(groupCandidate)-1))
            groupBindex = random.randint(0,(len(groupCandidate)-1))
            memberAindex = random.randint(0,(len(groupCandidate[groupAindex])-1))
            memberBindex = random.randint(0,(len(groupCandidate[groupBindex])-1))
            memberA = groupCandidate[groupAindex][memberAindex]
            memberB = groupCandidate[groupBindex][memberBindex]
            memberAsex = memberA[4]
            memberBsex = memberB[4]
        groupCandidate[groupAindex][memberAindex] = memberB
        groupCandidate[groupBindex][memberBindex] = memberA
        newmemberLists = list(map(lambda group: list(map(lambda member: [member[0],member[1:4]],group)),groupCandidate))
        newfriendsNumList = list(map(lambda members: getFriendsNum(members), newmemberLists))
        newFriendScore = sum(newfriendsNumList)
    print(baseFriendScore,newFriendScore)
    return [newFriendScore,groupCandidate]

def getFriendsNum(memberInfos):
    members = list(map(lambda memberInfo: memberInfo[0],memberInfos))
    friends = list(map(lambda memberInfo: memberInfo[1],memberInfos))
    friendsNum = 0
    for friend in friends:
        friendsNum += len(set(friend)&set(members))
    return friendsNum

def writeToExcel(selectedGroup):
    return

if __name__ == "__main__":
    fire.Fire(main)
