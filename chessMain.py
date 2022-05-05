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
    imageDict['border'] = p.image.load("pieceImages/border.png")


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

    displayGS(screen, gs)  # displays the board and pieces
    p.display.flip()
    fps_clock = p.time.Clock()
    click_count = 0

    running = True
    while running:
        ev = p.event.get()
        for e in ev:
            first_click_coord = None

            # handle quit event
            if e.type == p.QUIT:
                running = False

            # handle mouse click
            if e.type == p.MOUSEBUTTONDOWN:  # if mouse is clicked
                click_count += 1  # advance click count
                print('this is click number: ' + str(click_count))

                # handle first click
                if click_count == 1:
                    print('first click, should highlight possible moves')
                    mouse_coord = p.mouse.get_pos()
                    board_coord = helpGetSquare(mouse_coord)
                    first_click_coord = board_coord
                    highlightSquare(screen, board_coord)
                    # TODO: currently highlights square clicked, need to highlight possible move squares instead

                # handle second click
                if click_count == 2:
                    mouse_coord = p.mouse.get_pos()
                    board_coord = helpGetSquare(mouse_coord)
                    second_click_coord = board_coord
                    if second_click_coord == first_click_coord:
                        print('changed mind, reset')
                        # TODO: in this case, just get rid of highlights and don't use up move
                    else:
                        print('second click, not in same spot, move to new coord')
                        # TODO: in this case, move the piece and use up move (toggle gs.whiteMoveNext)
                    click_count = 0



def displayGS(screen, gs):
    """
    Function that displays the board and pieces
    """
    # display the board
    for row in range(numSquares):
        if row % 2 == 0:  # even index rows
            for column in range(numSquares):
                if column % 2 == 0:  # even index cols = white
                    p.draw.rect(screen, (209, 207, 188), p.Rect(column * squareLength, row * squareLength, squareLength,
                                                                squareLength))
                else:
                    p.draw.rect(screen, (119, 145, 116), p.Rect(column * squareLength, row * squareLength, squareLength,
                                                                squareLength))
        else:  # odd index rows
            for column in range(numSquares):
                if column % 2 == 0:  # even index cols = gray
                    p.draw.rect(screen, (119, 145, 116), p.Rect(column * squareLength, row * squareLength, squareLength,
                                                                squareLength))
                else:
                    p.draw.rect(screen, (209, 207, 188), p.Rect(column * squareLength, row * squareLength, squareLength,
                                                                squareLength))

    # display the pieces
    board = getattr(gs, 'board')
    for row in board:
        for piece in row:
            if piece is not None:
                piece_coord = getattr(piece, 'coord')
                row_n = piece_coord[0]
                col_n = piece_coord[1]
                piece_name = getattr(piece, 'name')
                helpDrawPiece(screen, row_n, col_n, piece_name)  # helper fun


def helpDrawPiece(screen, row, col, piece_name):
    """
    Helper function to draw pieces at coordinates (row, col)
    :param screen: screen to draw on
    :param piece_name: name of piece type (e.g. "wP", "bB", "bQ", etc.)
    """
    screen.blit(p.transform.scale(imageDict[piece_name], (squareLength, squareLength)),
                (col * squareLength, row * squareLength))


def helpGetSquare(mouse_pos):
    """
    Helper function to translate clicked mouse position to board square coord
    :param mouse_pos: in reference to top left of screen (x, y) coordinates
    :return: (x, y) coordinates in terms of board indices
    """
    board_x = mouse_pos[0]//squareLength
    board_y = mouse_pos[1]//squareLength

    pos = (board_x, board_y)

    return pos


def highlightSquare(screen, board_pos):
    board_x = board_pos[0]
    board_y = board_pos[1]
    screen.blit(p.transform.scale(imageDict['border'], (squareLength, squareLength)),
                (board_x * squareLength, board_y * squareLength))
    p.display.flip()

main()
