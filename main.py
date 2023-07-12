### Line-Distribution-Visualizer ###
### Under GNU GPL v3.0 License ###

import pygame as pg
import preprocessor as pp
import time

# Preprocess the song data
songDataPath = "INPUT_FOLDER/songData/songData.json"
maxMemberTime = pp.calcMaxMemberTime(songDataPath)
nFrames = pp.calcNumFrames(songDataPath)
fps = pp.readFPS(songDataPath)
numberOfMembers = pp.readNumberOfMembers(songDataPath)

# Calculate number of frames and active member frames
activeMemberFrames = pp.getActiveMemberFrames(songDataPath) # Returns a dictionary with member names as keys and a list of active frames as values
memberComulativeTime = pp.getMemberComulativeTime(activeMemberFrames, nFrames, fps) # Returns a dictionary with member names as keys and a list of comulative time as values

# Initialize pygame
pg.init()
pg.display.set_caption("Line Distribution Visualizer")
windowSize = [1920, 1080]
#windowSize = [1920*2, 1080*2]
window = pg.display.set_mode(windowSize, pg.SRCALPHA)

# Make a list of member cards
memberCards = pp.makeMemberCardObjects((windowSize[0],windowSize[1]/numberOfMembers)) # Returns a list of memberCard objects
# Sort the member cards based on their first appearance
for memberCard in memberCards:
    memberCard.firstAppearanceFrame = activeMemberFrames[memberCard.name][0]
memberCards.sort(key=lambda x: x.firstAppearanceFrame)
print(memberCards)

for frame in range(nFrames):
    # Make window with 0 aplha
    window = pg.Surface((windowSize[0], windowSize[1]), pg.SRCALPHA)

    # Generate the member cards
    for memberCard in memberCards:
        memberCard.generateCardSurface(memberComulativeTime[memberCard.name][frame], maxMemberTime)

    # Sort the member cards by memberComulativeTime
    memberCards.sort(key=lambda x: x.memberTime, reverse=True)
    memberCardPos = {}
    for i, memberCard in enumerate(memberCards):
        memberCardPos[memberCard.name] = memberCard.cardHeight * i

    # Draw the member cards
    for memberCard in memberCards:
        memberCard.drawCard(window, memberCardPos[memberCard.name])

    # Update the display
    pg.display.update()
    pg.image.save(window, 'OUTPUT_FOLDER/frames/frame_' + str(frame) + '.png')

    # Wait for 1 / fps seconds
    #time.sleep(1 / fps)
    #print("Frame out of {nFrame}: " + str(frame))

# Quit pygame
pg.quit()