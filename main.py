import pygame, sys
from settings import WIDTH, HEIGHT
# from table import Table

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

class Main:
	def __init__(self, screen):
		self.screen = screen
		self.FPS = pygame.time.Clock()

	def main(self):
		while True:
			self.screen.fill("white")

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()
			self.FPS.tick(30)


if __name__ == "__main__":
	play = Main(screen)
	play.main()