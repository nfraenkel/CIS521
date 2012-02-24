'''
Created on Feb 23, 2012

@author: Boyang Zhang
'''

import sudoku
f = open('solutions.txt', 'w')
s = sudoku.SudokuBoard("sudoku-board1.txt")
s.ac3(f)
s = sudoku.SudokuBoard("sudoku-board2.txt")
s.ac3(f)
s = sudoku.SudokuBoard("sudoku-board3.txt")
s.ac3(f)
s = sudoku.SudokuBoard("sudoku-board4.txt")
s.ac3(f)
s = sudoku.SudokuBoard("sudoku-board5.txt")
s.ac3(f)
print "end"
