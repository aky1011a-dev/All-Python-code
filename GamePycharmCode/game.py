from scripts.entities import PhysicsEntity, Player
from scripts.utils import load_image, load_images, Animation
from scripts.tilemap import Tilemap
import pygame
import sys


#character customise
#speedrunner move
#fps option
#saves - 3 + 1 backup
#autosave - also when game closed
#keybinds - multiple binds to one and keybinds where its e.g. ctrl+c
#buttons
#menu - quit option - is pause menu - credits -say it's fine to mod and use stuff
#how to play
#character select
#hat,hair,skin,eye colour

#make big menu where you scroll along like totk and botw
#weapons, armour?, healing/food, keyitems, map, keybinds, saves, settings, credits

#loading zones - every fram check if player touches an entrance/exit
#eventually have resize thing - pygame.VIDEORESIZE
#hide mouse


def save_data(save=False, loadsave=False, savebackup=False, loadbackupsave=False, autosave=False, loadautosave=False):
	pass
	#have auto save symbol




class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Thalryndor: Alpha")

		self.screen = pygame.display.set_mode((640, 480))
		self.display = pygame.Surface((320, 240))

		self.pause_overlay = pygame.Surface((320, 240), pygame.SRCALPHA)
		self.pause_overlay.fill((0, 0, 0, 150))  # black with 150 transparency

		self.clock = pygame.time.Clock()
		self.paused = False

		self.direction = 'None'

		self.defaultkeybinds = {
			"up": (pygame.K_w, pygame.K_UP),
			"down": (pygame.K_s, pygame.K_DOWN),
			"left": (pygame.K_a, pygame.K_LEFT),
			"right": (pygame.K_d, pygame.K_RIGHT),
		 
		 	"menu": (pygame.K_p, pygame.K_ESCAPE),
			"interact": (pygame.K_e, pygame.K_RETURN),
			"use": (pygame.K_q, pygame.K_SPACE)
		}
		self.keybinds = {
			"up": (),
		 	"down": (),
			"left": (),
			"right": (),
		 	
		 	"menu": (),
		 	"use": (),
			"interact": ()
		}#user keybinds^^^ save in savedata()
		#for now vvv
		self.keybinds = self.defaultkeybinds

		self.assets = {
			'decor': load_images('tiles/decor'),
			'grass': load_images('tiles/grass'),
			'large_decor': load_images('tiles/large_decor'),
			'stone': load_images('tiles/stone'),
		 	'rock': load_images('rock'),
			'player': load_image('entities/player/player.png'),
		 
      'player/run/down': Animation(load_images('entities/player/run/down'), img_dur=10),
      'player/run/up': Animation(load_images('entities/player/run/up'), img_dur=10),
      'player/run/left': Animation(load_images('entities/player/run/left'), img_dur=10),
      'player/run/right': Animation(load_images('entities/player/run/right'), img_dur=10),
		 
			'player/idle/down': Animation(load_images('entities/player/idle/down'), img_dur=10),
			'player/idle/up': Animation(load_images('entities/player/idle/up'), img_dur=10),
			'player/idle/left': Animation(load_images('entities/player/idle/left'), img_dur=10),
			'player/idle/right': Animation(load_images('entities/player/idle/right'), img_dur=10),
		 
			'pause_menu': load_image('pause_menu.png'),
			'background': load_image('grass_background.png'),
		}

		self.textimages = {
			'letters': load_images('characters/letters'),
			'numbers': load_images('characters/numbers'),
			'punctuation': load_images('characters/punctuation'),
			'text_box': load_images('characters/text_box'),
		}

		self.player = Player(self, (50, 50), (8, 15))
		
		self.tilemap = Tilemap(self, tile_size=16)

		self.cameralocation = [0,0]
	
	def run(self):
		while True:
			self.display.blit(self.assets['background'], (0,0))
	
			#camera
			self.cameralocation[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.cameralocation[0]) / 30 #camera technically at top left
			self.cameralocation[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.cameralocation[1]) / 30 #1/30th at a time
			render_scroll = (int(self.cameralocation[0]), int(self.cameralocation[1])) #stops jitters from floats
	
			# Only update the world if not paused
			if not self.paused:
				self.tilemap.render(self.display, offset=render_scroll)
				
				movement_x = 0
				movement_y = 0
				if self.direction == 'up': #elifs make diagonals not allowed
					movement_y = -1
				elif self.direction == 'down':
					movement_y = 1
				elif self.direction == 'left':
					movement_x = -1
				elif self.direction == 'right':
					movement_x = 1
				
				self.player.update(self.tilemap, (movement_x, movement_y))
				self.player.render(self.display, offset=render_scroll)
				
			else:
				# Draw world but freeze player movement
				self.tilemap.render(self.display, offset=render_scroll)
				self.player.render(self.display, offset=render_scroll)
	
				# Draw pause menu on top
				if self.paused:
					# darken screen
					self.display.blit(self.pause_overlay, (0, 0))
					self.display.blit(self.assets['pause_menu'], (0, 0))
	
			#INPUTS
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					save_data(autosave=True)
					pygame.quit()
					sys.exit()
				# Auto pause when window loses focus
				elif event.type in (pygame.WINDOWMINIMIZED,pygame.WINDOWFOCUSLOST):
					self.paused = True
	
				elif event.type == pygame.KEYDOWN:
					if event.key in self.keybinds['menu']:
						self.paused = not self.paused
						
					for direction in ('up','down','left','right'):
						if event.key in self.keybinds[direction]:
							self.direction = direction
	
				elif event.type == pygame.KEYUP:
					if event.key in self.keybinds['up'] + self.keybinds['down'] + self.keybinds['left'] + self.keybinds['right']:
						self.direction = 'None'
	
			# Scale the display surface to the screen
			self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
	
			pygame.display.update()
			self.clock.tick(60)
	

if __name__ == "__main__":
	Game().run()