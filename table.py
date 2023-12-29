import pygame
from cell import Cell
from sudoku import Sudoku

from settings import WIDTH, HEIGHT, N_CELLS, CELL_SIZE

class Table:
	def __init__(self, screen):
		self.screen = screen

		# E = table length (get by multiplying number of rows and cols) minus squared value of row/col length
		puzzle = Sudoku(N_CELLS, (N_CELLS * N_CELLS) // 2) # E=(N_CELLS * N_CELLS) - (N_CELLS * 2))

		self.table = puzzle.puzzle_answers()
		self.answerable_table = puzzle.puzzle_table()

		self.table_cells = []
		self.num_choices = []
		self.clicked_cell = None
		self.clicked_num_below = None
		self.making_move = False
		self.guess_mode = True

		self._generate_game()


	def _generate_game(self):
		# generating sudoku table
		for y in range(N_CELLS):
			for x in range(N_CELLS):
				cell_value = self.answerable_table[y][x]
				is_correct_guess = True if cell_value != 0 else False
				self.table_cells.append(Cell(x, y, CELL_SIZE, cell_value, is_correct_guess))

		# generating number choices
		for x in range(N_CELLS):
			self.num_choices.append(Cell(x, N_CELLS, CELL_SIZE, x + 1))


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


	def handle_mouse_click(self, pos):
		x, y = pos[0], pos[1]

		# handling clicks
		if x <= WIDTH and y <= HEIGHT:
			x = x // CELL_SIZE[0]
			y = y // CELL_SIZE[1]
			clicked_cell = self.get_cell_from_pos((x, y))
			if clicked_cell.value == 0:
				self.clicked_cell = clicked_cell
				self.making_move = True
		elif x <= WIDTH and y > HEIGHT and y <= (HEIGHT + CELL_SIZE[1]):
			x = x // CELL_SIZE[0]
			self.clicked_num_below = self.num_choices[x].value

		if self.clicked_num_below and self.clicked_cell != None and self.clicked_cell.value == 0:
			# print(self.clicked_num_below)
			# if self.guess_mode:
			# 	if self.clicked_num_below not in same row/col and clicked_num_below not in self.clicked_cell.guesses:
			# 		self.clicked_cell.guesses.[self.clicked_num_below - 1] = self.clicked_num_below
			# else:
			self.clicked_cell.value = self.clicked_num_below
			if self.clicked_num_below == self.table[self.clicked_cell.col][self.clicked_cell.row]:
				print(self.table[self.clicked_cell.col][self.clicked_cell.row], True)
				self.clicked_cell.is_correct_guess = True
			else:
				print(self.table[self.clicked_cell.col][self.clicked_cell.row], False)
				self.clicked_cell.is_correct_guess = False
			self.clicked_num_below = None
			self.clicked_cell = None
			self.making_move = False
		else:
			self.clicked_num_below = None

		# `````PSEUDO`````
		# if clicked_modes_below: # guess mode on/off, erase
		# 	execute_modes_below()


	def update(self):
		[cell.update(self.screen) for cell in self.table_cells]

		[num.update(self.screen) for num in self.num_choices]

		self._draw_grid()
