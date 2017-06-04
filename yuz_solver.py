import sys
import time
import random


print("begin", time.time())
begin = time.time()
dimX = 10
dimY = 10
counter = 0
highestDepth = 0
# sys.setrecursionlimit(1500)

class Game(object):
	def __init__(self, board = None, currentPosition = None, moveNumber = 1, depth = 0):
		if board is not None:
			self.board = board
		else:
			self.board = [[0 for x in range(dimX)] for y in range(dimY)]
		
		self.currentPosition = currentPosition
		self.moveNumber = moveNumber
		self.depth = depth

	def printBoard(self):
		for i in self.board:
			for p in range(self.depth):
				sys.stdout.write('  ')
			for x in i:
				sys.stdout.write('%3d' % x)
			print
		print

	def isEmpty(self):
		for i in self.board:
			for o in i:
				if(o != 0):
					return False
		return True

	def getAllSquares(self):
		moves = [(1,7)]
		for i in range(dimX):
			for x in range(dimY):
				moves.append((i,x))

		return moves


	def isPossible(self):
		if((dimX * dimY - 1 == self.depth)):
			return True

		for x in range(dimX):
			for y in range(dimY):
				if((self.board[x][y] is 0) and len(self.getAvailableMoves((x,y))) is 0):
					# print((x,y))
					return False
		return True


	def getAvailableMoves(self, position = None):

		if(position is None):
			return self.getAllSquares()

		# curX = self.currentPosition[0]
		# curY = self.currentPosition[1]
		availableMoves = []
		curX = position[0]
		curY = position[1]

		if(curX-3 >= 0 and self.board[curX-3][curY] == 0):
			availableMoves.append((curX-3,curY))
		if(curX+3 < dimX and self.board[curX+3][curY] == 0):
			availableMoves.append((curX+3,curY))
		if(curY-3 >= 0 and self.board[curX][curY-3] == 0):
			availableMoves.append((curX,curY-3))
		if(curY+3 < dimY and self.board[curX][curY+3] == 0):
			availableMoves.append((curX,curY+3))
		if(curX+2 < dimX and curY+2 < dimY and self.board[curX+2][curY+2] == 0):
			availableMoves.append((curX+2,curY+2))
		if(curX+2 < dimX and curY-2 >= 0 and self.board[curX+2][curY-2] == 0):
			availableMoves.append((curX+2,curY-2))
		if(curX-2 >= 0 and curY-2 >= 0 and self.board[curX-2][curY-2] == 0):
			availableMoves.append((curX-2,curY-2))
		if(curX-2 >= 0 and curY+2 < dimY and self.board[curX-2][curY+2] == 0):
			availableMoves.append((curX-2,curY+2))

		# random.shuffle(availableMoves)
		return availableMoves
		

	def getGameWithMove(self, move):
		newBoard = self.board
		newBoard[move[0]][move[1]] = self.moveNumber
		newGame = Game(newBoard, move, self.moveNumber + 1, self.depth + 1)
		# print(newGame.currentPosition)
		# print(newGame.getAvailableMoves())
		# print(self.moveNumber)
		# newGame.printBoard()
		global highestDepth
		if(self.depth > highestDepth):
			newGame.printBoard()
			highestDepth = self.depth
			print(self.depth)
		global counter
		counter += 1
		if(counter % 10000 == 0):
			print(counter)
		return newGame
	
	def didWin(self):
		if(self.depth == dimX*dimY):
			return True
		return False


def solve(game):
	if(game.didWin()):
		print("YOU WON!!!!")
		print(time.time()-begin)
		print(counter)
		game.printBoard()
		raise Exception('You won!')
	elif(game.isPossible()):
		moves = game.getAvailableMoves(game.currentPosition)

		for move in moves:
			solve(game.getGameWithMove(move))
			game.board[move[0]][move[1]] = 0



game = Game()
solve(game)


#(4,1)
#(6,2)
#(7,4)
#(6,6)
#(2,2)
#()