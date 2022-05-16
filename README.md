# Final project for CLPS 0950

Team Chess
- Angela Li
- Tani Najman-Licht

# Our resource documents

- Object-oriented coding in python: https://realpython.com/python3-object-oriented-programming/
- pygame & numpy package/library


# Our main functions & objects

Main():

- driver for the game, updates game graphics through accessing the game state and pieces

Piece objects: 
    
- get_moves: compiles an array of all the possible moves for that piece on that turn 
- helpCheckPiece: checks if square is a valid move for piece
- withinBoardBounds: makes sure moves are contained on the board

Others: 

- movePiece: moves piece, updates new square and old square
- pieceGraphics: uploads graphics onto the board
- displayGS: displays the board and the pieces for the game
- highlightGreen/Red: highlights the square of the piece clicked on different color for different color piece

# Our main files

pieces.py:

- sets up the parents class - chessPieces
- and the subclasses - Pawn, Knight, Bishop, Rook, Queen, King
  - each representing objects of the individual types of pieces
  - includes the rules for how the pieces move
  - the method possible_moves generates a list of the moves each piece can move every turn 

gameState.py:

- creates the board and initializes the pieces on the board and their location
- has functions for special moves: en passant and pawn promotion
- updates the board after moves

chessMain.py:

- draws the current state of the game
- imports information from pieces and gameState
- allows player to click and choose piece and move it to valid coordinate
- highlights squares of selected pieces and possible moves
- removes pieces that have been captured from the board

pieceImages folder:

- all original artwork by Angela


# User instructions

1. Run chessMain or main()
2. Click on piece to move it
   1. first click to select piece
   2. second click to select square to move to (valid moves are highlighted) 
3. White and black switch off moves, beginning with white 
4. Move back and forth until one player checkmates other player
5. When king is in check, player must move out of check by blocking it or moving King
6. Checkmate is not notified - if player is in check and cannot get out of it, 
   it is checkmate and that player loses


# Our work & meeting schedule
                           
Can be seen through our extensive GitHub history, not otherwise documented due to redundancy


# Work log

We followed the schedule above and coded everything together.

4/25
- submit proposal

4/26
- make data structures for each piece
- begin compiling rules

4/28
- set up game 
- make pieces

5/1
- create board size and dimensions
- create types of pieces

5/2
- make ranks rows and columns files
- debug gameState
- start chessMain
- paste pieces on board (pieces too big)

5/3, 5/4
- create chess piece objects
- start making rules for pieces 
- allow gameState to accommodate pieces objects 
- create function to highlight square that user clicks on 
  - first click and second click attributes 
- gameState intakes pieces objects and sets up board using them

5/5
- On valid second clicks (where the second click does not == first click location), 
  pieces that can move (canMove == True) are displayed on the screen!
- chessMain takes in function moveTo in order to allow pieces to move
  through chessMain
- created potential function canMoveTo (ended up scrapping it)

5/10
- Rules for pieces in pieces.py array of possible moves for each piece 
  possible_moves reference to possible moves in chessMain

5/11
- rules for Pawns and Bishops for how to move
- rules allow certain squares to be added to possible_moves 
- bishop problem - some potential moves are off the board

5/12 
- highlight squares of pieces clicked on different colors
  depending on side 
- fixes black pawns to work (missing return possible_moves)
- fixing move rules, debugging, adding tuples together 

5/13
- debugging white pawn
- making move rules more concise 
- add rules for Kings, Rooks, Knights

5/14
- implement boundary rules so that potential moves for bishops and rooks work 
- make function for en passant and integrate it into chessMain 
  allows the en passant move to be possible

5/15 
- debugging knight, rook, king move rules 
- making rules more concise 
- fixed highlighting - highlight now disappears after click 
- clicking on piece cancels highlights 
- fix all the pieces so that they work with the moves, create queen moves
- create pawn promotion function and implement it into chessMain
- check notification when king in check 
- attempted making castling function and checkmate, but didn't quite get it to work
- submit project via email and repo link :o)