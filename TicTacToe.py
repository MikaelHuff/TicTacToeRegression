import TTTLinearRegression.GamePlayer as gp
import numpy as np


class tictactoe:

    def __init__(self, visible, p1Type, p2Type):
        self.board = np.zeros(9)
        self.turn = 0
        self.winner = 0
        self.visible = visible
        self.players = [int(p1Type), int(p2Type)]

    # Checks if a move is legal, returns true when spot n equals 0
    def isLegal(self, n):
        return not bool(self.board[n])

    # Makes a move on the board, increases turn count by 1 or to 10 if game over
    def makeMove(self, player, move):
        self.board[move] = player
        self.turn += 1
        if self.checkGameOver():
            self.turn = 10

    # Checks if board is full or a player has won
    def checkGameOver(self):
        # Check vertical win
        for i in range(3):
            inRow = self.board[i] + self.board[i + 3] + self.board[i + 6]
            if abs(inRow) == 3:
                self.winner = np.sign(inRow)
                return True

        # Check horizontal win
        for i in range(3):
            inRow = self.board[3 * i] + self.board[3 * i + 1] + self.board[3 * i + 2]
            if abs(inRow) == 3:
                self.winner = np.sign(inRow)
                return True

        # Check diagonal win
        inRow = self.board[0] + self.board[4] + self.board[8]
        if abs(inRow) == 3:
            self.winner = np.sign(inRow)
            return True
        inRow = self.board[2] + self.board[4] + self.board[6]
        if abs(inRow) == 3:
            self.winner = np.sign(inRow)
            return True

        # Check full board
        if self.turn == 9:
            return True

    # Prints out the board
    def showBoard(self):
        for i in range(len(self.board)):
            if i % 3 == 0:
                print("\n")
            print( "X" if self.board[i] == 1 else "O" if self.board[i] == -1 else "●", "  ", end ='')

    # Checks to see if we want player to be human, random choice, or ai
    def getMove(self, player):
        game = gp.GamePlayer(len(self.board))
        playerind = int((player + 1)/2)
        if self.players[playerind] == 0:
            return int(input("\nShow your moves\n")) - 1
        if self.players[playerind] == 1:
            return np.random.randint(9)
        if self.players[playerind] == 2:
            return game.bestMove(self.board, player, self.isLegal)


    # Runs game by making a move, checking leaglity, alternating player, and showing board
    def runGame(self, starter):
        player = starter*2-3
        while self.turn < 10:
            move = self.getMove(player)
            if self.isLegal(move):
                self.makeMove(player, move)
                player = player * -1
                if self.visible:
                    self.showBoard()
            elif self.visible:
                print("\nNot Legal\n")
        if self.visible:
            print ("\n\n",self.winner)


#ttt = tictactoe(1, 0, 1)
#ttt.runGame(1)
