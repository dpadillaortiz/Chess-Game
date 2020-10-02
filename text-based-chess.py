#Classes and Definitions
letters = ['A','B','C','D','E','F','G','H'] 
numbers = [1,2,3,4,5,6,7,8]

class ChessPiece:
	def __init__(self, x, y):
		self.xaxis = x
		self.yaxis = y
		print([self.xaxis,self.yaxis])
	def cord(self):
		cord = [self.xaxis, self.yaxis]
		print(cord)
	def onBoard(self, x, y):
		if (x not in letters) or (y not in numbers):	
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
	#def onPiece(self, x, y):
		# how do i check if a piece is on the board
class Pawn(ChessPiece): 
	def movePawn(self, x, y):
		if (x != self.xaxis) or (self.onBoard(x,y) == False):
			print("The pawn can't move there")
		else: 
			self.yaxis = y		 
			self.cord()

class Rook(ChessPiece):	
	def moveRook(self, x, y):
		if self.onBoard(x,y) == False:	
			print("Rook cannot move to [",x,",",y,"]")	
		else:
			self.move(x, y)

class Bishop(ChessPiece):
   def moveBishop(self, x, y):
      if self.onBoard(x,y) == False:
         print("Bishop cannot move to [",x,",",y,"]")
      else:
         if x == self.xaxis or y == self.yaxis:
            print("Bishop cannot move to [",x,",",y,"]")
         else:
            self.xaxis = x
            self.yaxis = y
            self.cord()	
'''
class Bishop(ChessPiece):
	def moveBishop(self, x, y):
		if self.onBoard(x,y) == False:
			print("Bishop cannot move to [",x,",",y,"]")
		else:
			for i in range(len(letters)):
				if self.xaxis == letters[i]:
					selfVar = i + 1
				if x == letters[i]:
					argVar = i + 1	
			if (argVar == selfVar + 1) or (argVar == selfVar - 1):
				self.xaxis = x
				self.yaxis = y
				self.cord()
			else:
				print("Bishop cannot move to [",x,",",y,"]") 
	
'''

#--------------------------------------
#Testing Zone

print("---Rook Tests---")
bTest = Bishop('E', 1)
bTest.moveBishop('E', 2)
bTest.moveBishop('F', 1)
bTest.moveBishop('D', 2)
bTest.moveBishop('D', 6)
bTest.moveBishop('2', 6)
bTest.moveBishop('H', 6)

