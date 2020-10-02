#Classes and Definitions
letters = ['A','B','C','D','E','F','G','H'] 
nums = [1,2,3,4,5,6,7,8]

class ChessPiece:
	def __init__(self, x, y):
		self.xaxis = x
		self.yaxis = y
		print([self.xaxis,self.yaxis])
	def cord(self):
		cord = [self.xaxis, self.yaxis]
		print(cord)
	def onBoard(self, x, y):
		if (self.xaxis not in letters) or (self.yaxis not in nums):
			return False
	def move(self, x, y):
		#pieceOnBoard = self.onBoard(x,y)
		#if pieceOnBoard == ("not in letters" or "not in numbers"):
		# moving up/down a col
		if x == self.xaxis:
			self.yaxis = y
			self.cord()	
		# moving left/right a row 
		elif y == self.yaxis:
			self.xaxis = x
			self.cord()	
	
class Pawn(ChessPiece): 
	def movePawn(self, x, y):
		if (x != self.xaxis) or (self.onBoard(x,y) == False):
			print("The pawn can't move there")
		else: 
			self.yaxis = y		 
			self.cord()
#i think i'm going to do something similar to what i did with Pawn
class Rook(ChessPiece):	
	def moveRook(self, x, y):
		if self.onBoard(x,y) == False:	
			print("Rook cannot move to [",x,",",y,"]")	
		else:
			self.move(x, y)




#--------------------------------------
#Testing Zone

print("---Pawn Tests---")
pawnTest = Pawn('A', 2)
pawnTest.movePawn('B',2)
pawnTest.movePawn('A',5)

print("---Rook Tests---")
rTest = Rook('E', 1)
rTest.moveRook('E', 2)
rTest.moveRook('D', 2)
rTest.moveRook('D', 6)
rTest.moveRook('2', 6)
rTest.moveRook('A', 6)


"""
rTest = Rook('E', 1)
rTest.cord()
rTest.moveRook('E', 2)
rTest.moveRook('D', 2)
rTest.moveRook('D', 6)
#rTest.moveRook('2', 6)
#rTest.moveRook('X', 6)
#rTest.moveRook('D', 11)
rTest.moveRook('E', 6)
rTest.moveRook('A', 1)
rTest.moveRook('A', 6)
rTest.moveRook('D', 8)


qTest = Queen('A', 4)
qTest.cord()
qTest.moveRook('E', 2)
qTest.moveRook('D', 2)
qTest.moveRook('D', 6)
qTest.moveRook('E', 20)
qTest.moveRook('A', 1)
qTest.moveRook('A', 6)
"""
