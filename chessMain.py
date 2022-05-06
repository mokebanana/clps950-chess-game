import pygame as p
import matplotlib as plt
from PIL import Image
import numpy as np

# global variables for board dimensions and piece graphics
import gameState
import pieces

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
    board = getattr(gs, 'board')

    displayGS(screen, gs)  # displays the board and pieces
    p.display.flip()
    fps_clock = p.time.Clock()
    click_count = 0
    current_piece = None
    first_click_coord = None

    running = True
    while running:
        ev = p.event.get()
        for e in ev:

            # handle quit event
            if e.type == p.QUIT:
                running = False

            # handle mouse click
            if e.type == p.MOUSEBUTTONDOWN:  # if mouse is clicked
                click_count += 1  # advance click count
                print('this is click number: ' + str(click_count))

                # handle first click
                if click_count == 1:
                    mouse_coord = p.mouse.get_pos()
                    board_coord = helpGetSquare(mouse_coord)
                    first_click_coord = board_coord  # save where the first click was to check against second click
                    print('     first click at coord ' + str(first_click_coord))

                    # is there a piece at that board_coord
                    current_piece = board[board_coord[1]][board_coord[0]]
                    if current_piece is not None:  # there is a piece at that coord
                        print('     there is a piece at first click, the piece is ' + getattr(current_piece, 'name'))
                        color_can_move = gs.whiteMoveNext != getattr(current_piece, 'color')
                        if color_can_move:
                            print('     this piece is able to move')

                            # what are its options to move?
                            highlightSquare(screen, board_coord)
                            # highlightMove(current_piece, canMoveTo)
                            # TODO: currently highlights square clicked, need to highlight possible move squares instead
                            pass  # TODO: pass in diff rules for diff pieces

                        else:
                            print('     this piece is unable to move')
                            click_count = 0
                    else:
                        click_count = 0  # if there's no piece at the square first clicked, reset click_count

                # handle second click
                if click_count == 2:
                    mouse_coord = p.mouse.get_pos()
                    board_coord = helpGetSquare(mouse_coord)
                    second_click_coord = board_coord
                    print('     second click at coord' + str(second_click_coord))
                    if second_click_coord == first_click_coord:
                        print('     same spot! canceled')
                        click_count = 0
                    else:
                        print('     second click, not in same spot, move to new coord')
                        # TODO: in this case, move the piece and use up move (toggle gs.whiteMoveNext) (helpDrawPiece)
                        gs.whiteMoveNext = not gs.whiteMoveNext  # toggle whiteMoveNext -> not doing anything rn
                        gs.movePiece(current_piece, second_click_coord)
                        print(*gs.board)

                        # draw selected piece at new position
                        helpDrawPiece(screen, board_coord[1], board_coord[0], getattr(current_piece, 'name'))  # todo

                        # remove old piece graphics
                        helpRemovePiece(screen, first_click_coord[1], first_click_coord[0])

                        # update graphics
                        p.display.flip()

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
    board_x = mouse_pos[0] // squareLength
    board_y = mouse_pos[1] // squareLength

    pos = (board_x, board_y)

    return pos


def highlightSquare(screen, board_pos):
    board_x = board_pos[0]
    board_y = board_pos[1]
    screen.blit(p.transform.scale(imageDict['border'], (squareLength, squareLength)),
                (board_x * squareLength, board_y * squareLength))
    p.display.flip()
# def highlightMove(current_piece, canMoveTo)
    #

def helpRemovePiece(screen, board_x, board_y):
    # I read in pygame you can't remove, you can just draw on top in background color

    xy_sum = board_x + board_y
    if xy_sum % 2 == 0:
        p.draw.rect(screen, (209, 207, 188), p.Rect(board_y * squareLength, board_x * squareLength, squareLength,
                                                    squareLength))
    else:
        p.draw.rect(screen, (119, 145, 116), p.Rect(board_y * squareLength, board_x * squareLength, squareLength,
                                                    squareLength))


main()
