import json, math
import memberCard as mc

# Calculate the time for the longest member
def calcMaxMemberTime(songDataPath):
    with open(songDataPath, "r") as f:
        songData = json.load(f)
        maxMemberTime = 0
        for member in songData["members"]:
            memberTime = 0
            for timestamp in member["timestamps"]:
                timeRange = timestamp.split("-")
                memberTime += float(timeRange[1]) - float(timeRange[0])
            if memberTime > maxMemberTime:
                maxMemberTime = memberTime
    return maxMemberTime

# Calculate the number of frames based on song length and FPS
def calcNumFrames(songDataPath):
    with open(songDataPath, "r") as f:
        songData = json.load(f)
        return math.ceil(float(songData['songLength']) * float(songData['fps']))

# 
def getActiveMemberFrames(songDataPath):
    with open(songDataPath, "r") as f:
        songData = json.load(f)
        nFrames = round(float(songData['songLength']) * float(songData['fps']))
        activeMemberFrames = {}
        for i in range(nFrames):
            for member in songData["members"]:
                for timestamp in member["timestamps"]:
                    timeRange = timestamp.split("-")
                    if float(timeRange[0]) <= float(i / float(songData['fps'])) <= float(timeRange[1]):
                        if member['name'] in activeMemberFrames:
                            activeMemberFrames[member['name']].append(i)
                        else:
                            activeMemberFrames[member['name']] = [i]
    return activeMemberFrames

def makeMemberCardObjects(cardSize):
    with open("INPUT_FOLDER\songData\songData.json", "r") as f:
        timestamps = json.load(f)
        memberCards = []
        for member in timestamps["members"]:
            memberCard = mc.MemberCard(member["name"], cardSize)
            memberCards.append(memberCard)
    return memberCards

def getMemberComulativeTime(activeMemberFrames, nFrames, fps):
    memberComulativeTime = {}
    for member in activeMemberFrames:
        memberComulativeTime[member] = []
        for frame in range(nFrames):
            if frame in activeMemberFrames[member]:
                memberComulativeTime[member].append(memberComulativeTime[member][frame - 1] + 1 / fps)
            else:
                if frame == 0:
                    memberComulativeTime[member].append(0)
                else:
                    memberComulativeTime[member].append(memberComulativeTime[member][frame - 1])
    print(memberComulativeTime)
    return memberComulativeTime

def readFPS(songDataPath):
    with open(songDataPath, "r") as f:
        songData = json.load(f)
        return float(songData['fps'])

# Calculate the number of members
def readNumberOfMembers(songDataPath):
    with open(songDataPath, "r") as f:
        songData = json.load(f)
    return len(songData['members'])