# main.py

import chessboard as Chessboard
import chesspiece as Chesspiece


chessNotation = {
    "N": Chesspiece.Knight(),
    "Q": Chesspiece.Queen()
}

knight = chessNotation["N"]
print(knight.name)
print(knight.knights)

knight.moveTo("C2")
print(knight.knights)
knight.moveTo("D3")
print(knight.knights)
knight.moveTo("D8")