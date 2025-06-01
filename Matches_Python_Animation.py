#Kaeden Matches
#April 15
#Animation Project
#The Project where I learn Animations

#Imports
import pygame, sys, random

#Initialize Pygame
pygame.init()

#Declare Things
def BallMovement(ball, movement, size, speed, color):
    for box in BoxRects:
        dr = abs(ball.right - box.left)
        dl = abs(ball.left - box.right)
        db = abs(ball.bottom - box.top)
        dt = abs(ball.top - box.bottom)
        if min(dr, dl) < min(dt, db):
            if movement[0] > 0:     
                if ball.colliderect(box):
                    POP.play()
                    movement[0] = - speed[0]
            elif movement[0] < 0:
                if ball.colliderect(box):
                    POP.play()
                    movement[0] = speed[0]
        else:
            if movement[1] > 0:     
                if ball.colliderect(box):
                    POP.play()
                    movement[1] = - speed[1]   
            elif movement[1] < 0:
                if ball.colliderect(box):
                    POP.play()
                    movement[1] = speed[1]
    ball.x += movement[0]
    ball.y += movement[1]
    pygame.draw.ellipse(display, color, (ball.x, ball.y, size[0], size[1]))

#Variables
ScreenSize = [800, 600]
play = True
Score = 0
FirstColor1 = 255
FirstColor2 = 1
FirstColor3 = 1
RGBColor = (FirstColor1, FirstColor2, FirstColor3)
SecondColor1 = 1
SecondColor2 = 1
SecondColor3 = 255
RGBColor2 = (SecondColor1, SecondColor2, SecondColor3)

#Sounds
POP = pygame.mixer.Sound("Sounds/pop.mp3")
WHOOSH = pygame.mixer.Sound("Sounds/whoosh.mp3")
MUSIC = pygame.mixer.Sound("Sounds\music.mp3")

#Declare Window Information
pygame.display.set_caption(f"Block Breaker Game")
screen = pygame.display.set_mode(ScreenSize, flags = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
DisplaySize = [800, 600]
display = pygame.Surface((DisplaySize[0], DisplaySize[1]))
clock = pygame.time.Clock()

#Fonts
FunFont = pygame.font.Font("Fonts\FunFont.ttf", 50)
ScoreDisplay = FunFont.render(f"Score", 0, 'white')

#Paddle (AI)
Paddle = pygame.transform.scale(pygame.transform.rotate(pygame.image.load("Images\pong_paddle-removebg-preview.png"), 0), (100, 26))
Paddle.set_colorkey('white')
Paddle.fill((150, 255, 150, 200), special_flags = pygame.BLEND_MULT)
PaddlePos = [display.get_width() / 2 - Paddle.get_width() / 2, display.get_height() - Paddle.get_height()]
PaddleRect = pygame.Rect(0, 0, Paddle.get_width(), Paddle.get_height())

Paddle2 = pygame.transform.scale(pygame.transform.rotate(pygame.image.load("Images\pong_paddle-removebg-preview.png"), 0), (100, 26))
Paddle2.set_colorkey('white')
Paddle2.fill((150, 150, 255, 200), special_flags = pygame.BLEND_MULT)
Paddle2Pos = [display.get_width() / 2 - Paddle2.get_width() / 2, display.get_height() - Paddle.get_height() - 10 - Paddle2.get_height()]
PaddleRect2 = pygame.Rect(0, 0, Paddle2.get_width(), Paddle2.get_height())

#Bouncy Balls
MinSpeed = 4
MaxSpeed = 5

BouncyBallSize = [20, 20]
BouncyBallRect = pygame.Rect(random.randrange(0, display.get_width() - BouncyBallSize[0]), random.randrange(300, 550), BouncyBallSize[0], BouncyBallSize[1])
BallSpeed = [random.randrange(MinSpeed, MaxSpeed), random.randrange(MinSpeed, MaxSpeed)]
BouncyBallMovement = [BallSpeed[0], BallSpeed[1]]
BallMove = [True, True]

BouncyBall2Size = [20, 20]
BouncyBall2Rect = pygame.Rect(random.randrange(0, display.get_width() - BouncyBall2Size[0]), random.randrange(300, 550), BouncyBall2Size[0], BouncyBall2Size[1])
Ball2Speed = [random.randrange(MinSpeed, MaxSpeed), random.randrange(MinSpeed, MaxSpeed)]
BouncyBall2Movement = [Ball2Speed[0], Ball2Speed[1]]
Ball2Move = [True, True]

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
    pygame.display.set_caption(f"Block Breaker Game - Score: {int(Score)}")

    display.fill('black')

    if FirstColor1 == 255 and FirstColor2 <= 254 and FirstColor3 == 1:
        FirstColor2 += 1
    if FirstColor1 >= 2 and FirstColor2 == 255 and FirstColor3 == 1:
        FirstColor1 -= 1
    if FirstColor1 == 1 and FirstColor2 == 255 and FirstColor3 <= 254:
        FirstColor3 += 1
    if FirstColor1 == 1 and FirstColor2 >= 2 and FirstColor3 == 255:
        FirstColor2 -= 1
    if FirstColor1 <= 254 and FirstColor2 == 1 and FirstColor3 == 255:
        FirstColor1 += 1
    if FirstColor1 == 255 and FirstColor2 == 1 and FirstColor3 >= 2:
        FirstColor3 -= 1

    RGBColor = (FirstColor1, FirstColor2, FirstColor3)

    if SecondColor1 == 255 and SecondColor2 <= 254 and SecondColor3 == 1:
        SecondColor2 += 1
    if SecondColor1 >= 2 and SecondColor2 == 255 and SecondColor3 == 1:
        SecondColor1 -= 1
    if SecondColor1 == 1 and SecondColor2 == 255 and SecondColor3 <= 254:
        SecondColor3 += 1
    if SecondColor1 == 1 and SecondColor2 >= 2 and SecondColor3 == 255:
        SecondColor2 -= 1
    if SecondColor1 <= 254 and SecondColor2 == 1 and SecondColor3 == 255:
        SecondColor1 += 1
    if SecondColor1 == 255 and SecondColor2 == 1 and SecondColor3 >= 2:
        SecondColor3 -= 1

    RGBColor2 = (SecondColor1, SecondColor2, SecondColor3)

    Ball1 = abs(display.get_height() - BouncyBallRect.y)
    Ball2 = abs(display.get_height() - BouncyBall2Rect.y)

    if BouncyBallRect.x >= Paddle.get_width() / 3 and BouncyBallRect.x <= display.get_width() - Paddle.get_width() / 2:
        PaddlePos[0] = BouncyBallRect.x + BouncyBallSize[0] / 2 - Paddle.get_width() / 2
    
    if BouncyBall2Rect.x >= Paddle2.get_width() / 3 and BouncyBall2Rect.x <= display.get_width() - Paddle2.get_width() / 2:
        Paddle2Pos[0] = BouncyBall2Rect.x + BouncyBall2Size[0] / 2 - Paddle2.get_width() / 2

    PaddleRect = pygame.Rect(PaddlePos[0], PaddlePos[1], Paddle.get_width(), Paddle.get_height())
    Paddle2Rect = pygame.Rect(Paddle2Pos[0], Paddle2Pos[1], Paddle2.get_width(), Paddle2.get_height())

    BouncyBallRect = pygame.Rect(BouncyBallRect.x, BouncyBallRect.y, BouncyBallSize[0], BouncyBallSize[1])
    BouncyBall2Rect = pygame.Rect(BouncyBall2Rect.x, BouncyBall2Rect.y, BouncyBall2Size[0], BouncyBall2Size[1])

    BouncyBalls = [BouncyBallRect, BouncyBall2Rect]
    
    #Figure Out Which Boxes Are Still In
    BoxRects = []
    TotalBoxes = []
    BouncyBallNumber = 1

    for BouncyBall in BouncyBalls:
        BrickNumber = 0
        for Block in BlockList:
            for Box in Block:
                if BlockList[BrickNumber][2] > 0:
                    if BouncyBallNumber == 1:
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

                    if BlockList[BrickNumber][0].colliderect(BouncyBall):
                        BlockList[BrickNumber][2] -= 1

            BrickNumber += 1
        BouncyBallNumber += 1

    BoxRects.append(PaddleRect)
    BoxRects.append(Paddle2Rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    if BouncyBallRect.x >= display.get_width() - BouncyBallSize[0]:
        BouncyBallMovement[0] = - BallSpeed[0]
    if BouncyBallRect.x <= 0:
        BouncyBallMovement[0] = BallSpeed[0]
    if BouncyBallRect.y <= 0:
        BouncyBallMovement[1] = BallSpeed[1]
    
    if BouncyBall2Rect.x >= display.get_width() - BouncyBall2Size[0]:
        BouncyBall2Movement[0] = - Ball2Speed[0]
    if BouncyBall2Rect.x <= 0:
        BouncyBall2Movement[0] = Ball2Speed[0]
    if BouncyBall2Rect.y <= 0:
        BouncyBall2Movement[1] = Ball2Speed[1]

    Ball = BallMovement(BouncyBallRect, BouncyBallMovement, BouncyBallSize, BallSpeed, RGBColor)
    Ball2 = BallMovement(BouncyBall2Rect, BouncyBall2Movement, BouncyBall2Size, Ball2Speed, RGBColor2)
    
    for BouncyBall in BouncyBalls:
        for box in BoxRects:
            if BouncyBall.colliderect(box):
                Score += 1 / 3
    
    Score = round(Score)

    display.blit(Paddle, (PaddlePos[0], PaddlePos[1]))
    display.blit(Paddle2, (Paddle2Pos[0], Paddle2Pos[1]))

    #pygame.draw.rect(display, 'white', PaddleRect)

    if screen.get_height() >= screen.get_width() * 0.75:
        DisplaySize[0] = screen.get_width()
        DisplaySize[1] = screen.get_width() * 0.75
    else:
        DisplaySize[0] = screen.get_height() * (8 / 6)
        DisplaySize[1] = screen.get_height()
    
    ScoreDisplay = FunFont.render(f"Score: {Score}", 0, 'white')
    display.blit(ScoreDisplay, (display.get_width() / 2 - ScoreDisplay.get_width() / 2, display.get_height() / 2 - ScoreDisplay.get_height() / 2))
    
    screen.fill('white')
    screen.blit(pygame.transform.scale(display, (DisplaySize[0], DisplaySize[1])), (screen.get_width() / 2 - DisplaySize[0] / 2, screen.get_height() / 2 - DisplaySize[1] / 2))

    pygame.display.update()

    if TotalBoxes == [] and (BouncyBallRect.y and BouncyBall2Rect.y > display.get_height() / 4 * 3):
        WHOOSH.play()
        BrickNumber = 0
        for Block in BlockList:
            BlockList[BrickNumber][2] = 13
            BrickNumber += 1

    clock.tick(60)

pygame.quit()
sys.exit()