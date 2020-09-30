#Classes and Definitions


class ChessPiece:
	def __init__(self, x, y):
		self.xaxis = x
		self.yaxis = y
	def cord(self):
		cord = [self.xaxis, self.yaxis]
		print(cord)
	def onBoard(self, x, y):
		xOnBoard = x in ['A','B','C','D','E','F','G','H'] 	
		if y not in [1,2,3,4,5,6,7,8]:
			print("You're off the board")
		

class Pawn(ChessPiece):
	if 
	def movePawn(self, x, y):
		if (x != self.xaxis) or (y > 8):
			print("Can't move there")
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
			print("Can't move there")
	
#Testing Zone
'''
pawnTest = Pawn('A', 2)
print(pawnTest.xaxis, pawnTest.yaxis)
pawnTest.cord()
pawnTest.movePawn('A',10)
pawnTest.movePawn('B',2)
pawnTest.cord()
'''

rTest = Rook('E', 1)
rTest.cord()
rTest.moveRook('E', 2)
rTest.moveRook('D', 2)
rTest.moveRook('D', 6)
rTest.moveRook('E', 6)
rTest.moveRook('A', 1)
rTest.moveRook('A', 6)

		 
