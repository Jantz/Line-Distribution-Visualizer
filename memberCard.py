import pygame as pg
class MemberCard:
    def __init__(self, name, width, height):
        # Set the name of the member
        self.name = name

        # Load the card visual parameters
        self.cardWidth = width
        self.cardHeight = height

        # Load the profile picture
        self.profilePicPath = "images/profilePics/" + name + ".png"
        self.profilePic = pg.image.load(self.profilePicPath).convert_alpha()
        # Scale the profile picture
        self.profilePic = pg.transform.scale(self.profilePic, (round(height / 1.5), round(height / 1.5)))
        # Defines the spacing between cards (Must be >= 2)
        self.profilePicRadius = height / 3
        # Profile picture top left position
        self.profilePicPos = [self.cardHeight / 6, self.cardHeight / 6]

        # Render the name of the member
        self.nameFont = pg.font.Font("fonts\Kreadon-D.otf", round(self.cardHeight / 6))
        self.nameSurface = self.nameFont.render(self.name, True, (0, 0, 0))
        # Name text top left position
        self.nameTextPos = [self.cardHeight, self.cardHeight / 4]

        # Set the time bar parameters
        self.memberTime = 2
        self.memberTimeProgress = 0
        self.memberTimeBarWidth = 0
        self.memberTimeBarHeight = round(self.cardHeight / 6)
        self.timeBarPos = [self.cardHeight, self.cardHeight * 7 / 12]
        self.memberTimeBarMaxWidth = self.cardWidth - (self.cardHeight * 7 / 6) #(1 cardHeight from left and 1/6 cardHeight from right)

    def generateCardSurface(self, memberTime, maxMemberTime):
        # Generate transparent card surface
        self.cardSurface = pg.Surface((self.cardWidth, self.cardHeight), pg.SRCALPHA)

        # Render the time bar
        self.memberTime = memberTime
        self.memberTimeProgress = memberTime / maxMemberTime
        self.memberTimeBarWidth = round(self.memberTimeBarMaxWidth * self.memberTimeProgress)
        # Draw the time bar as a rectangle
        pg.draw.rect(self.cardSurface, (0, 0, 0), (self.timeBarPos[0], self.timeBarPos[1], self.memberTimeBarWidth, self.memberTimeBarHeight))

        # Blit the profile picture (centered)
        self.cardSurface.blit(self.profilePic, self.profilePicPos)
        # Draw the name of the member
        self.cardSurface.blit(self.nameSurface, self.nameTextPos)
        
        # Draw a debug rectangle around the card with red color
        pg.draw.rect(self.cardSurface, (255, 0, 0), (0, 0, self.cardWidth, self.cardHeight), 1)

        return self.cardSurface