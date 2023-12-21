import pygame
from cell import Cell
from sudoku import Sudoku

from settings import WIDTH, HEIGHT, N_CELLS, CELL_SIZE

class Table:
	def __init__(self, screen):
		self.screen = screen

		puzzle = Sudoku(N_CELLS, (N_CELLS * N_CELLS) // 2)

		self.table = puzzle.puzzle_answers()
		self.answerable_table = puzzle.puzzle_table()

		self.table_cells = []

		self._generate_game()


	def _generate_game(self):
		for y in range(N_CELLS):
			for x in range(N_CELLS):
				self.table_cells.append(Cell(x, y, CELL_SIZE))


	def update(self):
		[cell.update(self.screen) for cell in self.table_cells]
