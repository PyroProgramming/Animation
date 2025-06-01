#Kaeden Matches
#April 15
#Animation Project
#The Project where I learn Animations

#Imports
import pygame, sys, random

#Initialize Pygame
pygame.init()

#Declare Things
def BallMovement(brick):
    for box in BoxRects:
        dr = abs(BouncyBallRect.right - box.left)
        dl = abs(BouncyBallRect.left - box.right)
        db = abs(BouncyBallRect.bottom - box.top)
        dt = abs(BouncyBallRect.top - box.bottom)
        if min(dr, dl) < min(dt, db):
            if BouncyBallMovement[0] > 0:     
                if BouncyBallRect.colliderect(box):
                    POP.play()
                    BouncyBallMovement[0] = - BallSpeed   
            elif BouncyBallMovement[0] < 0:
                if BouncyBallRect.colliderect(box):
                    POP.play()
                    BouncyBallMovement[0] = BallSpeed
        else:
            if BouncyBallMovement[1] > 0:     
                if BouncyBallRect.colliderect(box):
                    POP.play()
                    BouncyBallMovement[1] = - BallSpeed   
            elif BouncyBallMovement[1] < 0:
                if BouncyBallRect.colliderect(box):
                    POP.play()
                    BouncyBallMovement[1] = BallSpeed
    brick.x += BouncyBallMovement[0]
    brick.y += BouncyBallMovement[1]
    pygame.draw.ellipse(display, 'green', (BouncyBallRect.x, BouncyBallRect.y, BouncyBallSize[0], BouncyBallSize[1]))


#Variables
ScreenSize = [800, 600]
play = True
Score = 0

#Sounds
POP = pygame.mixer.Sound("Sounds/pop.mp3")
WHOOSH = pygame.mixer.Sound("Sounds/whoosh.mp3")
MUSIC = pygame.mixer.Sound("Sounds\music.mp3")

#Declare Window Information
pygame.display.set_caption(f"Fun Brick Breaker Animation")
screen = pygame.display.set_mode(ScreenSize, flags = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
DisplaySize = [800, 600]
display = pygame.Surface((DisplaySize[0], DisplaySize[1]))
clock = pygame.time.Clock()

#Bouncy Balls
BouncyBallSize = [20, 20]
BouncyBallRect = pygame.Rect(random.randrange(0, display.get_width() - BouncyBallSize[0]), display.get_height() / 4 * 3, BouncyBallSize[0], BouncyBallSize[1])
BouncyBallMovement = [4, 4]
BallMove = [True, True]
BallSpeed = 4

#Paddle (AI)
Paddle = pygame.transform.scale(pygame.transform.rotate(pygame.image.load("Images\pong_paddle-removebg-preview.png"), 0), (100, 26))
Paddle.set_colorkey('white')
PaddlePos = [BouncyBallRect.x, display.get_height() - Paddle.get_height()]
PaddleRect = pygame.Rect(0, 0, Paddle.get_width(), Paddle.get_height())

#Bricks
TileSize = [100, 40]

Box1Pos = [20, 10]
Box1 = pygame.Rect(Box1Pos[0], Box1Pos[1], TileSize[0], TileSize[1])

Box2Pos = [Box1Pos[0] + TileSize[0] * 1 + 10 * 1, 10]
Box2 = pygame.Rect(Box2Pos[0], Box2Pos[1], TileSize[0], TileSize[1])

Box3Pos = [Box1Pos[0] + TileSize[0] * 2 + 10 * 2, 10]
Box3 = pygame.Rect(Box3Pos[0], Box3Pos[1], TileSize[0], TileSize[1])

Box4Pos = [Box1Pos[0] + TileSize[0] * 3 + 10 * 3, 10]
Box4 = pygame.Rect(Box4Pos[0], Box4Pos[1], TileSize[0], TileSize[1])

Box5Pos = [Box1Pos[0] + TileSize[0] * 4 + 10 * 4, 10]
Box5 = pygame.Rect(Box5Pos[0], Box5Pos[1], TileSize[0], TileSize[1])

Box6Pos = [Box1Pos[0] + TileSize[0] * 5 + 10 * 5, 10]
Box6 = pygame.Rect(Box6Pos[0], Box6Pos[1], TileSize[0], TileSize[1])

Box7Pos = [Box1Pos[0] + TileSize[0] * 6 + 10 * 6, 10]
Box7 = pygame.Rect(Box7Pos[0], Box7Pos[1], TileSize[0], TileSize[1])

#Row 2
Box8Pos = [70, 60]
Box8 = pygame.Rect(Box8Pos[0], Box8Pos[1], TileSize[0], TileSize[1])

Box9Pos = [Box8Pos[0] + TileSize[0] * 1 + 10 * 1, 60]
Box9 = pygame.Rect(Box9Pos[0], Box9Pos[1], TileSize[0], TileSize[1])

Box10Pos = [Box8Pos[0] + TileSize[0] * 2 + 10 * 2, 60]
Box10 = pygame.Rect(Box10Pos[0], Box10Pos[1], TileSize[0], TileSize[1])

Box11Pos = [Box8Pos[0] + TileSize[0] * 3 + 10 * 3, 60]
Box11 = pygame.Rect(Box11Pos[0], Box11Pos[1], TileSize[0], TileSize[1])

Box12Pos = [Box8Pos[0] + TileSize[0] * 4 + 10 * 4, 60]
Box12 = pygame.Rect(Box12Pos[0], Box12Pos[1], TileSize[0], TileSize[1])

Box13Pos = [Box8Pos[0] + TileSize[0] * 5 + 10 * 5, 60]
Box13 = pygame.Rect(Box13Pos[0], Box13Pos[1], TileSize[0], TileSize[1])

BlockList = [[Box1, Box1Pos, 13],
             [Box2, Box2Pos, 13],
             [Box3, Box3Pos, 13],
             [Box4, Box4Pos, 13],
             [Box5, Box5Pos, 13],
             [Box6, Box6Pos, 13],
             [Box7, Box7Pos, 13],
             [Box8, Box8Pos, 13],
             [Box9, Box9Pos, 13],
             [Box10, Box10Pos, 13],
             [Box11, Box11Pos, 13],
             [Box12, Box12Pos, 13],
             [Box13, Box13Pos, 13]]

#Start Program
MUSIC.play(loops = -1)
while play:
    keys = pygame.key.get_pressed()

    pygame.display.set_caption(f"Fun Brick Breaker Animation - Score: {int(Score)}")

    display.fill('black')
    
    if BouncyBallRect.x >= Paddle.get_width() / 3 and BouncyBallRect.x <= display.get_width() - Paddle.get_width() / 2:
        if keys[pygame.K_d]:
            PaddlePos[0] += 8
        if keys[pygame.K_a]:
            PaddlePos[0] -= 8

    PaddleRect = pygame.Rect(PaddlePos[0], PaddlePos[1], Paddle.get_width(), Paddle.get_height())

    BouncyBallRect = pygame.Rect(BouncyBallRect.x, BouncyBallRect.y, BouncyBallSize[0], BouncyBallSize[1])

    #Figure Out Which Boxes Are Still In
    BoxRects = []
    TotalBoxes = []
 
    BrickNumber = 0

    for Block in BlockList:
        for Box in Block:
            if BlockList[BrickNumber][2] > 0:
                BoxRects.append(BlockList[BrickNumber][0])
                TotalBoxes.append(BlockList[BrickNumber][2])
                
                if BlockList[BrickNumber][2] == 13:
                    pygame.draw.rect(display, 'blue', [BlockList[BrickNumber][1][0], BlockList[BrickNumber][1][1], TileSize[0], TileSize[1]])
                elif BlockList[BrickNumber][2] == 10:
                    pygame.draw.rect(display, 'green', [BlockList[BrickNumber][1][0], BlockList[BrickNumber][1][1], TileSize[0], TileSize[1]])
                elif BlockList[BrickNumber][2] == 7:
                    pygame.draw.rect(display, 'yellow', [BlockList[BrickNumber][1][0], BlockList[BrickNumber][1][1], TileSize[0], TileSize[1]])
                elif BlockList[BrickNumber][2] == 4:
                    pygame.draw.rect(display, 'orange', [BlockList[BrickNumber][1][0], BlockList[BrickNumber][1][1], TileSize[0], TileSize[1]])
                elif BlockList[BrickNumber][2] == 1:
                    pygame.draw.rect(display, 'red', [BlockList[BrickNumber][1][0], BlockList[BrickNumber][1][1], TileSize[0], TileSize[1]])

                if BlockList[BrickNumber][0].colliderect(BouncyBallRect):
                    BlockList[BrickNumber][2] -= 1
        
        BrickNumber += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    if BouncyBallRect.x >= display.get_width() - BouncyBallSize[0]:
        BouncyBallMovement[0] = - BallSpeed   
    if BouncyBallRect.x <= 0:
        BouncyBallMovement[0] = BallSpeed   
    if BouncyBallRect.y <= 0:
        BouncyBallMovement[1] = BallSpeed   
    if PaddleRect.colliderect(BouncyBallRect):
        BouncyBallMovement[1] = - BallSpeed   

    Ball = BallMovement(BouncyBallRect)
    
    for box in BoxRects:
            if BouncyBallRect.colliderect(box):
                Score += 1 / 3
    
    Score = round(Score)

    display.blit(Paddle, (PaddlePos[0], PaddlePos[1]))
    #pygame.draw.rect(display, 'white', PaddleRect)

    if screen.get_height() >= screen.get_width() * 0.75:
        DisplaySize[0] = screen.get_width()
        DisplaySize[1] = screen.get_width() * 0.75
    else:
        DisplaySize[0] = screen.get_height() * (8 / 6)
        DisplaySize[1] = screen.get_height()
    
    screen.fill('white')
    screen.blit(pygame.transform.scale(display, (DisplaySize[0], DisplaySize[1])), (screen.get_width() / 2 - DisplaySize[0] / 2, screen.get_height() / 2 - DisplaySize[1] / 2))

    pygame.display.update()

    if TotalBoxes == [] and BouncyBallRect.y > display.get_height() / 4 * 3:
        WHOOSH.play()
        BrickNumber = 0
        for Block in BlockList:
            BlockList[BrickNumber][2] = 13
            BrickNumber += 1

    if BouncyBallRect.y > display.get_height():
        play = False

    clock.tick(60)

pygame.quit()
sys.exit()