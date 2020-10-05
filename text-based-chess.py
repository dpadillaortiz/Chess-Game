#Classes and Definitions
letters = ['A','B','C','D','E','F','G','H'] 
numbers = [1,2,3,4,5,6,7,8]

class ChessPiece:
	def __init__(self, x, y):
		self.xaxis = x
		self.yaxis = y
		print([self.xaxis,self.yaxis])
	def name(self, name):
		pieceName = name
	def cord(self):
		cord = [self.xaxis, self.yaxis]
		print(cord)
	def onBoard(self, x, y):
		if (x not in letters) or (y not in numbers):
			print("Location does not exist")	
			return False
		else:
			return True
	piece = self.name(n)

class Movement(ChessPiece):
   def moveUDLR(self, x, y):
      if self.onBoard(x,y) == True:
         if x == self.xaxis:
            self.yaxis = y
            self.cord()
            return True
         elif y == self.yaxis:
            self.xaxis = x
            self.cord()
            return True

   def moveDiag(self, x, y):
      if self.onBoard(x,y) == True:
         if x == self.xaxis or y == self.yaxis:
            print(ChessPiece.piece,"cannot move there")
         else:
            self.xaxis = x
            self.yaxis = y
            self.cord()

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

class Queen(Movement): 
   def moveQueen(self, x, y):
      self.moveUDLR(x,y)
     
                  

class Bishop(Movement):
   ChessPiece.name("Bishop")
   def moveBishop(self, x, y):
      self.moveDiag(x,y)
     
#--------------------------------------
#Testing Zone
print("------Queen-----")
qTest = Queen("D",4)
qTest.moveQueen("D",1)
qTest.moveQueen("F",7)


print("------Bishop-----")
bTest = Bishop('E', 1)
bTest.moveBishop('E', 2)
bTest.moveBishop('F', 1)
bTest.moveBishop('D', 2)
bTest.moveBishop('D', 6)
bTest.moveBishop('2', 6)
bTest.moveBishop('H', 6)
bTest.moveBishop('F', 8)
bTest.moveBishop('A', 3)
bTest.moveBishop('A', 8)
bTest.moveBishop('C', 1)











