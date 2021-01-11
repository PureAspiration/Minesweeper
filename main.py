import math
import pygame
import random
from pprint import pprint

pygame.init()
width, height = 623, 395
backgroundColor = 192, 192, 192

screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Minesweeper")

black = (0, 0, 0)


def writeText(fontDir, fontSize, text, color, alignment, locX, locY):
    font = pygame.font.Font(fontDir, fontSize)
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()

    if alignment == "center":
        textRect.center = (locX, locY)
    if alignment == "topleft":
        textRect.topleft = (locX, locY)
    if alignment == "bottomleft":
        textRect.bottomleft = (locX, locY)
    if alignment == "topright":
        textRect.topright = (locX, locY)
    if alignment == "bottomright":
        textRect.bottomright = (locX, locY)
    if alignment == "midtop":
        textRect.midtop = (locX, locY)
    if alignment == "midbottom":
        textRect.midbottom = (locX, locY)
    if alignment == "midleft":
        textRect.midleft = (locX, locY)
    if alignment == "midright":
        textRect.midright = (locX, locY)

    screen.blit(textRender, textRect)


def drawImage(imageDir, alignment, locX, locY, scaleX=None, scaleY=None, rotateAngle=None):
    image = pygame.image.load(imageDir)
    if scaleX is not None and scaleY is not None:
        image = pygame.transform.scale(image, (scaleX, scaleY))
    if rotateAngle is not None:
        image = pygame.transform.rotate(image, rotateAngle)

    imageRect = image.get_rect()

    if alignment == "center":
        imageRect.center = (locX, locY)
    if alignment == "topleft":
        imageRect.topleft = (locX, locY)
    if alignment == "bottomleft":
        imageRect.bottomleft = (locX, locY)
    if alignment == "topright":
        imageRect.topright = (locX, locY)
    if alignment == "bottomright":
        imageRect.bottomright = (locX, locY)
    if alignment == "midtop":
        imageRect.midtop = (locX, locY)
    if alignment == "midbottom":
        imageRect.midbottom = (locX, locY)
    if alignment == "midleft":
        imageRect.midleft = (locX, locY)
    if alignment == "midright":
        imageRect.midright = (locX, locY)

    screen.blit(image, imageRect)


mines = 40
tileWidth = 16
tileHeight = 16

while True:
    if mines < 1:
        mines = 1

    if mines >= tileWidth * tileHeight:
        mines = tileWidth * tileHeight - 1

    if tileWidth < 8:
        tileWidth = 8

    if tileHeight < 1:
        tileHeight = 1

    if tileWidth == 9 and tileHeight == 9 and mines == 10:
        preset = "Beginner"

    elif tileWidth == 16 and tileHeight == 16 and mines == 40:
        preset = "Intermediate"

    elif tileWidth == 30 and tileHeight == 16 and mines == 99:
        preset = "Expert"

    else:
        preset = "Custom"

    screen = pygame.display.set_mode((width, height))

    screen.fill(backgroundColor)
    drawImage("assets/background.png", "topleft", 0, 0)
    drawImage("assets/face-normal.png", "center", width / 2, 30, 22, 22)

    writeText("assets/fonts/digital-7.ttf", 35, "Mines: ", black, "midleft", 20, (height + 40) / 4)
    writeText("assets/fonts/digital-7.ttf", 35, str(mines), black, "center", 140, (height + 40) / 4)
    drawImage("assets/arrow.png", "center", 140, (height + 40) / 4 - 25, 33, 21)
    drawImage("assets/arrow.png", "center", 140, (height + 40) / 4 + 25, 33, 21, 180)

    writeText("assets/fonts/digital-7.ttf", 35, "Tiles Width: ", black, "midleft", 20, (height + 40) / 2.5)
    writeText("assets/fonts/digital-7.ttf", 35, str(tileWidth), black, "center", 220, (height + 40) / 2.5)
    drawImage("assets/arrow.png", "center", 220, (height + 40) / 2.5 - 25, 33, 21)
    drawImage("assets/arrow.png", "center", 220, (height + 40) / 2.5 + 25, 33, 21, 180)

    writeText("assets/fonts/digital-7.ttf", 35, "Tiles Height: ", black, "midleft", 20, (height + 40) / 1.8)
    writeText("assets/fonts/digital-7.ttf", 35, str(tileHeight), black, "center", 235, (height + 40) / 1.8)
    drawImage("assets/arrow.png", "center", 235, (height + 40) / 1.8 - 25, 33, 21)
    drawImage("assets/arrow.png", "center", 235, (height + 40) / 1.8 + 25, 33, 21, 180)

    writeText("assets/fonts/digital-7.ttf", 35, "Preset: ", black, "midleft", 20, (height + 40) / 1.3)
    writeText("assets/fonts/digital-7.ttf", 35, preset, black, "midleft", 140, (height + 40) / 1.3)
    drawImage("assets/arrow.png", "center", 210, (height + 40) / 1.3 - 25, 33, 21)
    drawImage("assets/arrow.png", "center", 210, (height + 40) / 1.3 + 25, 33, 21, 180)

    drawImage("assets/button.png", "center", 465, 205)
    writeText("assets/fonts/digital-7.ttf", 30, "Play", black, "center", 465, 205)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(f"{mouse[0]} {mouse[1]}")

            if 125 <= mouse[0] <= 158 and 74 <= mouse[1] <= 94:
                mines += 1

            elif 125 <= mouse[0] <= 155 and 125 <= mouse[1] <= 144:
                mines -= 1

            elif 204 <= mouse[0] <= 238 and 140 <= mouse[1] <= 161:
                tileWidth += 1

            elif 204 <= mouse[0] <= 238 and 190 <= mouse[1] <= 210:
                tileWidth -= 1

            elif 219 <= mouse[0] <= 252 and 207 <= mouse[1] <= 227:
                tileHeight += 1

            elif 219 <= mouse[0] <= 252 and 255 <= mouse[1] <= 275:
                tileHeight -= 1

            elif 193 <= mouse[0] <= 226 and 300 <= mouse[1] <= 320:
                if preset == "Intermediate":
                    mines = 10
                    tileWidth = 9
                    tileHeight = 9
                elif preset == "Expert":
                    mines = 40
                    tileWidth = 16
                    tileHeight = 16
                elif preset == "Beginner":
                    mines = 99
                    tileWidth = 30
                    tileHeight = 16
            elif 193 <= mouse[0] <= 226 and 350 <= mouse[1] <= 370:
                if preset == "Beginner":
                    mines = 40
                    tileWidth = 16
                    tileHeight = 16
                elif preset == "Intermediate":
                    mines = 99
                    tileWidth = 30
                    tileHeight = 16
                elif preset == "Expert":
                    mines = 10
                    tileWidth = 9
                    tileHeight = 9

            elif 373 <= mouse[0] <= 556 and 185 <= mouse[1] <= 225:
                print("Clicked Play")
                screen = pygame.display.set_mode((width, height))

                board = [[["", False, False] for a in range(tileHeight)]for b in range(tileWidth)]
                i = 0
                while True:
                    mineX, mineY = random.randint(0, tileWidth - 1), random.randint(0, tileHeight - 1)
                    print(f"{mineX} {mineY}")
                    if board[mineX][mineY][0] != "m":
                        board[mineX][mineY][0] = "m"
                        i += 1
                    if i == mines:
                        break
                print(board)

                while True:
                    width, height = 10 + 33 * tileWidth + 13, 62 + 33 * tileHeight + 12
                    screen = pygame.display.set_mode((width, height))

                    screen.fill(backgroundColor)

                    drawImage("assets/background/side-panel-top.png", "midtop", width / 2, 0, 10000, 10)
                    drawImage("assets/background/side-panel-bottom.png", "midtop", width / 2, 50, 10000, 12)

                    drawImage("assets/background/side-panel-left.png", "topleft", 0, 0)
                    drawImage("assets/background/side-panel-right.png", "topright", width, 0)

                    drawImage("assets/background/side-left.png", "topleft", 0, 62, 10, 10000)
                    drawImage("assets/background/side-right.png", "topright", width, 62, 13, 10000)
                    drawImage("assets/background/side-bottom.png", "midbottom", width / 2, height, 10000, 12)

                    drawImage("assets/background/corner-bottomleft.png", "bottomleft", 0, height)
                    drawImage("assets/background/corner-bottomright.png", "bottomright", width, height)

                    drawImage("assets/tile.png", "midtop", width / 2, 14)

                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            mouse = pygame.mouse.get_pos()
                            print(f"{mouse[0]} {mouse[1]}")

                            column = math.floor((mouse[0] - 10) / 33) + 1
                            print(column)

                            row = math.floor((mouse[1] - 62) / 33) + 1
                            print(row)

                        elif event.type == pygame.MOUSEBUTTONUP:
                            mouse = pygame.mouse.get_pos()
                            print(f"{mouse[0]} {mouse[1]}")
