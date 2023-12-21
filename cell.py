import pygame

class Cell:
	def __init__(self, row, col, cell_size):
		# super().__init__()
		self.row = row
		self.col = col
		self.cell_size = cell_size
		self.width = self.cell_size[0]
		self.height = self.cell_size[1]
		self.abs_x = row * self.width
		self.abs_y = col * self.height
		self.color = pygame.Color("white")

		self.rect = pygame.Rect(self.abs_x,self.abs_y,self.width,self.height)


	def update(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)