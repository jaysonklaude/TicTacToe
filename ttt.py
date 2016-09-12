import os

class TicTacToe():
    def __init__(self):
        self.players = {1:'X', 2:'O'}
        self.positions = {1:"0 0", 2:"0 1", 3:"0 2", 4:"1 0", 5:"1 1", 6:"1 2", 7:"2 0", 8:"2 1", 9:"2 2"}
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        #0-active game; 1,2-victory; 3-cat's.//
        #Second position to describe how game was won.
        self.winner = [0,0]
        self.numberOfMoves = 0

    def setSpace(self, i, j, k):
        self.board[i][j] = k

    def won(self, k):
        if self.winner[0] != 0:
            return
        if self.board[0][0] in ["X", "O"]:
            if len({self.board[i][0] for i in xrange(3)}) == 1:
                self.winner = [k + 1, "first coloumn"]
                return
            elif len(set(self.board[0])) == 1:
                self.winner = [k + 1, "first row"]
                return
        if self.board[2][2] in ["X", "O"]:
            if len({self.board[i][2] for i in xrange(3)}) == 1:
                self.winner = [k + 1, "third coloumn"]
                return
            elif len(set(self.board[2])) == 1:
                self.winner = [k + 1, "third row"]
                return
        if self.board[1][1] in ["X", "O"]:
            if len({self.board[i][1] for i in xrange(3)}) == 1:
                self.winner = [k + 1, "second coloumn"]
                return
            elif len(set(self.board[1])) == 1:
                self.winner = [k + 1, "second row"]
                return
            elif len({self.board[i][i] for i in xrange(3)}) == 1:
                self.winner = [k + 1, "main diagonal"]
                return
            elif len({self.board[i][2-i] for i in xrange(3)}) == 1:
                self.winner = [k + 1, "reverse diagonal"]
                return
        if self.numberOfMoves == 9:
            self.winner = [3]
            return

    def makeMove(self, k):
        while True:
            try:
                print self.returnBoard()
                [i, j] = map(int, self.positions[int(raw_input(
                    "Player " + str(k+1) + ", choose a column and a row (in order) with a space between them:"))].strip().split(' '))
                if not self.board[i][j] in ["X", "O"]:
                    self.setSpace(i, j, self.players[k+1])
                    self.numberOfMoves += 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print "Someone has already claimed that spot!\n"
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print "You did something wrong!\n"

    def returnBoard1(self):
        return str(self.board[0]) + "\n" + str(self.board[1]) + "\n" + str(self.board[2])

    def returnBoard(self):
        return ("   |   |   \n" +
                " " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + " \n" +
                "___|___|___\n   |   |   \n" +
                " " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + " \n" +
                "___|___|___\n   |   |   \n" +
                " " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + " \n" +
                "   |   |   ")

    def gameOver(self):
        print self.returnBoard()
        if self.winner[0] == 1 or self.winner[0] == 2:
            print "Player " + str(self.winner[0]) + " has won the game by making three in a row in the " + self.winner[1] + "!"
        elif self.winner[0] == 3:
            print "Cat's game! Nobody wins!" 

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    k = 1
    y = TicTacToe()
    while y.winner[0] == 0:
        k = (k + 1) % 2
        y.makeMove(k)
        y.won(k)
    y.gameOver()

if __name__ == "__main__":
    main()
