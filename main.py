import pygame, sys
from settings import WIDTH, HEIGHT
from table import Table

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + 80))
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

				# key clicks could be this way or through .get_pressed and idetify each one of them
			# 	if event.type == pygame.KEYDOWN:
			# 		try:
			# 			if int(event.unicode) >= 0 or int(event.unicode) <= 9:
			# 				clicked_num = event.unicode
			# 		except:
			# 			pass

			# table._get_key_clicked(clicked_num)
			table.update()
			pygame.display.update()
			self.FPS.tick(30)


if __name__ == "__main__":
	play = Main(screen)
	play.main()