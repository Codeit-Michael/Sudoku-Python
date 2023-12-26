import pygame

pygame.font.init()

class Cell:
	def __init__(self, row, col, cell_size, value):
		self.row = row
		self.col = col
		self.cell_size = cell_size
		self.width = self.cell_size[0]
		self.height = self.cell_size[1]
		self.abs_x = row * self.width
		self.abs_y = col * self.height
		
		self.value = value
		self.is_correct_guess = True
		self.guesses = None if self.value != 0 else []

		self.color = pygame.Color("white")
		self.font_color = pygame.Color("black") if self.is_correct_guess else pygame.Color("red")
		self.font = pygame.font.SysFont('monospace', self.cell_size[0])

		self.rect = pygame.Rect(self.abs_x,self.abs_y,self.width,self.height)


	def update(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
		
		if self.value != 0:
			num_val = self.font.render(str(self.value), True, self.font_color)
			screen.blit(num_val, (self.abs_x, self.abs_y))