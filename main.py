import pygame, sys
from settings import WIDTH, HEIGHT, CELL_SIZE
from table import Table

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + (CELL_SIZE[1] * 2)))
pygame.display.set_caption("Pacman")

class Main:
	def __init__(self, screen):
		self.screen = screen
		self.FPS = pygame.time.Clock()

	def main(self):
		table = Table(self.screen)

		while True:
			clicked_num = None
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					table.handle_mouse_click(event.pos)

			table.update()
			pygame.display.update()
			self.FPS.tick(30)


if __name__ == "__main__":
	play = Main(screen)
	play.main()