from scripts.utils import load_images
from scripts.tilemap import Tilemap
import pygame
import sys

REDNDER_SCALE = 2.0


class Editor:
 def __init__(self):
		pygame.init()
		pygame.display.set_caption("Level Editor")
		
		self.screen = pygame.display.set_mode((640, 480))
		self.display = pygame.Surface((320, 240))
		self.clock = pygame.time.Clock()
		
		self.assets = {
			'decor': load_images('tiles/decor'),
			'grass': load_images('tiles/grass'),
			'large_decor': load_images('tiles/large_decor'),
			'stone': load_images('tiles/stone'),
			'rock': load_images('rock'),
		}
		self.textimages = {
			'letters': load_images('characters/letters'),
			'numbers': load_images('characters/numbers'),
			'punctuation': load_images('characters/punctuation'),
			'text_box': load_images('characters/text_box'),
		}
		
		self.movement = [False, False, False, False]
		self.tilemap = Tilemap(self, tile_size=16)
		self.cameralocation = [0, 0]
		
		self.tilelist = list(self.assets)
		self.tilegroup = 0
		self.tilevariant = 0
 
 def run(self):
		while True:
			self.clicking = False
			self.rightclicking = False
			self.shift = False
			
			self.display.fill((0, 0, 0))
			
			currenttileimg = self.assets[self.tilelist[self.tilegroup]][self.tilevariant].copy()
			currenttileimg.set_alpha(100)
			
			self.display.blit(currenttileimg, (5, 5))
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
					
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						clicking = True
					if event.button == 3:
						self.rightclicking = True
					if self.shift:
						if event.button == 4:
							self.tilevariant = (self.tilevariant - 1) % len(self.assets[self.tilelist[self.tilegroup]])
						if event.button == 5:
							self.tilevariant = (self.tilevariant + 1) % len(self.assets[self.tilelist[self.tilegroup]])
					else:
						if event.button == 4:
							self.tilegroup = (self.tilegroup - 1) % len(self.tilelist)
							self.tile_variant = 0
						if event.button == 5:
							self.tilegroup = (self.tilegroup + 1) % len(self.tilelist)
							self.tile_variant = 0
					if event.type == pygame.MOUSEBUTTONUP:
						if event.button == 1:
							self.clicking = False
						if event.button == 3:
							self.right_clicking = False
				
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.movement[0] = True
					if event.key == pygame.K_RIGHT:
						self.movement[1] = True
					if event.key == pygame.K_UP:
						self.movement[2] = True
					if event.key == pygame.K_DOWN:
						self.movement[3] = True
						
					if event.key == pygame.K_LSHIFT:
						self.shift = True
				
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT:
						self.movement[0] = False
					if event.key == pygame.K_RIGHT:
						self.movement[1] = False
					if event.key == pygame.K_UP:
						self.movement[2] = False
					if event.key == pygame.K_DOWN:
						self.movement[3] = False
				
			self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
			pygame.display.update()
			self.clock.tick(60)

			

if __name__ == "__main__":
 Editor().run()