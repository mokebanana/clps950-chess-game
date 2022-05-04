import pygame as p
import matplotlib as plt
from PIL import Image
import numpy as np

# global variables for board dimensions and piece graphics
import gameState

boardLength = 500
numSquares = 8
squareLength = boardLength // numSquares
imageDict = {}  # keys: piece name, val: corresponding image of piece


def pieceGraphics():
    """
    Function to load piece graphics into imageDict at the beginning
    """
    pieceTypes = ['B', 'K', 'N', 'P', 'Q', 'R']
    for piece in pieceTypes:
        imageDict['w' + piece] = p.image.load("pieceImages/w" + piece + ".png")
        imageDict['b' + piece] = p.image.load("pieceImages/b" + piece + ".png")


def main():
    """
    Main Function
    """

    p.init()  # initialize pygame

    screen = p.display.set_mode((boardLength, boardLength))
    screen.fill("white")
    pieceGraphics()
    # access GameState
    gs = gameState.GameState()

    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        displayGS(screen, gs)
        p.display.flip()


def displayGS(screen, gs):
    """
    Function that displays the board and pieces
    """
    # display the board
    for row in range(numSquares):
        if row % 2 == 0:  # even index rows
            for column in range(numSquares):
                if column % 2 == 0:  # even index cols = white
                    p.draw.rect(screen, "white", p.Rect(column * squareLength, row * squareLength, squareLength,
                                                        squareLength))
                else:
                    p.draw.rect(screen, "gray", p.Rect(column * squareLength, row * squareLength, squareLength,
                                                       squareLength))
        else:  # odd index rows
            for column in range(numSquares):
                if column % 2 == 0:  # even index cols = gray
                    p.draw.rect(screen, "gray", p.Rect(column * squareLength, row * squareLength, squareLength,
                                                       squareLength))
                else:
                    p.draw.rect(screen, "white", p.Rect(column * squareLength, row * squareLength, squareLength,
                                                        squareLength))

    # display the pieces
    board = gs.board
    for row in range(numSquares):
        for column in range(numSquares):
            pieceName = board[row][column]
            if pieceName != "--":  # not empty square
                screen.blit(p.transform.scale(imageDict[pieceName], (squareLength, squareLength)),
                            (column * squareLength, row * squareLength))





main()
