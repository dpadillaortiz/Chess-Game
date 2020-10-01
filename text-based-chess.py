#Classes and Definitions
letters = ['A','B','C','D','E','F','G','H'] 
nums = [1,2,3,4,5,6,7,8]

class ChessPiece:
	def __init__(self, x, y):
		if (x in letters and y in nums):
			self.xaxis = x
			self.yaxis = y
		else:
			print("The piece is off the board")
	def cord(self):
		cord = [self.xaxis, self.yaxis]
		print(cord)
			

class Pawn(ChessPiece): 
	def movePawn(self, x, y):
		if x != self.xaxis:
			print("The pawn can't move there")
		else: 
			self.yaxis = y		 
			self.cord()

class Rook(ChessPiece):
	def moveRook(self, x, y):
		# moving up/down a col
		if x == self.xaxis:
			self.yaxis = y
			self.cord()	
		# moving left/right a row 
		elif y == self.yaxis:
			self.xaxis = x
			self.cord()
		else:
			print("The rook can't move there")
	
#Testing Zone

pawnTest = Pawn('A', 2)
pawnTest.cord()
pawnTest.movePawn('A',10)
pawnTest.movePawn('B',2)
pawnTest.cord()


rTest = Rook('E', 1)
rTest.cord()
rTest.moveRook('E', 2)
rTest.moveRook('D', 2)
rTest.moveRook('D', 6)
rTest.moveRook('E', 6)
rTest.moveRook('A', 1)
rTest.moveRook('A', 6)

		 
