#Classes and Definitions
letters = ['A','B','C','D','E','F','G','H'] 
numbers = [1,2,3,4,5,6,7,8]

class ChessPiece:
   def __init__(self, x, y):
      self.xaxis = x
      self.yaxis = y
      print([self.xaxis,self.yaxis])
	
   def cord(self):
      print([self.xaxis, self.yaxis])
	
   def onBoard(self, x, y):
      if (x in letters) and (y in numbers):
         return True
      else:
         print([x,y],"is not valid")

class Movement(ChessPiece):
   def latMov(self, x, y): 
      if x != self.xaxis and y != self.yaxis:
         return False
      else:
         self.yaxis = y
         self.xaxis = x
         self.cord()

   #Diagonal movement
   #needs more specific conditions; as long as the it's false, it'll move the piece to the desired location
   def diagMov(self, x, y):
      if x == self.xaxis or y == self.yaxis:
         return False 
      else:         
         self.xaxis = x
         self.yaxis = y
         self.cord()
   
#Rook class is completed but here's a double error for an "off-board" piece 
class Rook(Movement):	
   def moveRook(self, x, y):
      if self.onBoard(x,y) == True:
         if self.latMov(x,y) == False:
            print("Rook cannot move to",[x,y])

#Bishop class is not completed
class Bishop(Movement):
   def moveBishop(self, x, y):
      if self.onBoard(x,y) == True:   
         self.diagMov(x,y)
      else: 
         print("Bishop cannot move to",[x,y]) 

class Queen(Movement): 
   def moveQueen(self, x, y):   
      if self.onBoard(x,y) == True: 
         if x == self.xaxis:
            self.yaxis = y
            self.cord() 
         elif y == self.yaxis:
            self.xaxis = x
            self.cord()
         elif x == self.xaxis or y == self.yaxis:
            return False 
         else:         
            self.xaxis = x
            self.yaxis = y
            self.cord()        
      else:
         print("Queen cannot move to",[x,y]) 

class Pawn(ChessPiece): 
   def movePawn(self, x, y):
      if (x != self.xaxis) or (self.onBoard(x,y) == False):
         print("The pawn can't move there")
      else: 
         self.yaxis = y		 
         self.cord()

def rookTest():
   print("------Rook-----")
   rTest = Rook('E', 1) 
   rTest.moveRook('E', 2)
   rTest.moveRook('F', 1) 
   rTest.moveRook('D', 2)
   rTest.moveRook('D', 6)
   rTest.moveRook('2', 6)
   rTest.moveRook('H', 6) 
   rTest.moveRook('F', 8) 
   rTest.moveRook('A', 3) 
   rTest.moveRook('A', 8)
   rTest.moveRook('C', 1) 
   rTest.moveRook('H', 1) 

rookTest()

def bishopTest():
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

#bishopTest()

def queenTest():
   print("------Queen-----")
   qTest = Queen('E', 1) 
   qTest.moveQueen('E', 2)   
   qTest.moveQueen('F', 1) 
   qTest.moveQueen('D', 2) 
   qTest.moveQueen('D', 6)
   qTest.moveQueen('2', 6)
   qTest.moveQueen('H', 6) 
   qTest.moveQueen('F', 8) 
   qTest.moveQueen('A', 3) 
   qTest.moveQueen('A', 8)
   qTest.moveQueen('C', 1)
   

#queenTest()







