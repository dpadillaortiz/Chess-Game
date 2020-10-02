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
		if (x not in letters):
			return False
		else:
			return True
	def move(self, x, y):
		if self.onBoard(x,y) == True:
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

class Rook(ChessPiece):	
	def move_Rook(self, x, y):
		if self.onBoard(x,y) != False:	
			print("Rook cannot move to [",x,",",y,"]")	
		else:
			self.move(x, y)

	def moveRook(self, x, y):
		self.move(x, y)



#--------------------------------------
#Testing Zone

print("---Rook Tests---")
rTest = Rook('E', 1)
rTest.moveRook('E', 2)
rTest.moveRook('D', 2)
rTest.moveRook('D', 6)
rTest.moveRook('2', 6)
rTest.moveRook('A', 6)



