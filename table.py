import pygame
from cell import Cell
from sudoku import Sudoku

from settings import WIDTH, HEIGHT, N_CELLS, CELL_SIZE

class Table:
	def __init__(self, screen):
		self.screen = screen

		# E = table length (get by multiplying number of rows and cols) minus squared value of row/col length
		puzzle = Sudoku(N_CELLS, E=(N_CELLS * N_CELLS) - (N_CELLS * 2))

		self.table = puzzle.puzzle_answers()
		self.answerable_table = puzzle.puzzle_table()

		self.table_cells = []

		self._generate_game()


	def _generate_game(self):
		for y in range(N_CELLS):
			for x in range(N_CELLS):
				self.table_cells.append(Cell(x, y, CELL_SIZE, self.answerable_table[y][x]))


	def _draw_grid(self):
		grid_color = (50, 80, 80)
		pygame.draw.rect(self.screen, grid_color, (-3, -3, WIDTH + 6, HEIGHT + 6), 6)

		i = 1
		while (i * CELL_SIZE[0]) < WIDTH:
			line_size = 2 if i % 3 > 0 else 4
			pygame.draw.line(self.screen, grid_color, ((i * CELL_SIZE[0]) - (line_size // 2), 0), ((i * CELL_SIZE[0]) - (line_size // 2), HEIGHT), line_size)
			pygame.draw.line(self.screen, grid_color, (0, (i * CELL_SIZE[0]) - (line_size // 2)), (HEIGHT, (i * CELL_SIZE[0]) - (line_size // 2)), line_size)
			i += 1


	def get_cell_from_pos(self, pos):
		for cell in self.table_cells:
			if (cell.row, cell.col) == (pos[0], pos[1]):
				return cell


	def handle_click(self, pos):
		x, y = pos[0], pos[-1]
		if x <= WIDTH and y <= HEIGHT:
			x = x // CELL_SIZE[0]
			y = y // CELL_SIZE[1]
			clicked_cell = self.get_cell_from_pos((x, y))
			print(clicked_cell.value)

		else:
			print(False)

		# if self.selected_piece is None:
		# 	if clicked_cell.occupying_piece is not None:
		# 		if clicked_cell.occupying_piece.color == self.turn:
		# 			self.selected_piece = clicked_cell.occupying_piece
		# elif self.selected_piece._move(clicked_cell):
		# 	if not self.is_jump:
		# 		self.turn = 'red' if self.turn == 'black' else 'black'
		# 	else:
		# 		if len(clicked_cell.occupying_piece.valid_jumps()) == 0:
		# 			self.turn = 'red' if self.turn == 'black' else 'black'
		# elif clicked_cell.occupying_piece is not None:
		# 	if clicked_cell.occupying_piece.color == self.turn:
		# 		self.selected_piece = clicked_cell.occupying_piece


	def update(self):
		[cell.update(self.screen) for cell in self.table_cells]

		self._draw_grid()
