import os
import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
	if "." not in path:
		path += ".png"
	img = pygame.image.load(BASE_IMG_PATH + path).convert()
	#.convert() makes more efficient for rendering
	img.set_colorkey((0, 0, 0)) #replace black with transparent
	return img

def load_images(path): #gives all images in a path
	images = []
	for img_name in sorted(os.listdir(BASE_IMG_PATH + path)): #sorted() makes it work for diff OSs as linux weird or smth
		images.append(load_image(path + '/' + img_name))
	return images


def text_image(text="", pixel_height=5, speech_bubble=False):
	TEXT_FILE_PATH = 'data/images/characters/'
	#imagewidth:"character==filename"...
	letters = {3:"IL", 4:"ABCDEFGHJKNOPRSUZ", 5:"MQTVWXY"}
	numbers = {3:"1", 4:"023456789"}
	#imagewidth:((character,filename)...)
	punctuation = {1:(("!","exclamation_mark"),(".","full_stop")),
								 2:((",","comma"),("'","apostrophe")),
								 3:(("?","question_mark")),
								 4:(('"',"speech_marks")),
								 5:(("&","ambersand"))}
	text_box = {1:"filler", 3:"end", 6:"begin"}
	text_as_images = []
	text_box_as_images = []
	
	for character in text:
		
		for key, values in letters.items():
			for item in values:
				if character == item:
					text_as_images.append(load_image(TEXT_FILE_PATH+"letters/"+item+".png"))
					if speech_bubble:
						for i in range(key):
							text_box_as_images.append(load_image(TEXT_FILE_PATH+"text_box/filler.png"))
		
		for key, values in numbers.items():
			for item in values:
				if character == item:
					text_as_images.append(load_image(TEXT_FILE_PATH+"numbers/"+item+".png"))
					if speech_bubble:
						for i in range(key):
							text_box_as_images.append(load_image(TEXT_FILE_PATH+"text_box/filler.png"))
							
		for key, values in punctuation.items():
			for item in values:
				if character == item[0]:
					text_as_images.append(load_image(TEXT_FILE_PATH+"punctuation/"+item[1]+".png"))
					if speech_bubble:
						for i in range(key):
							text_box_as_images.append(load_image(TEXT_FILE_PATH + "text_box/filler.png"))
		
		if character == " ":
			text_as_images.append(load_image(TEXT_FILE_PATH+"SPACE.png"))
			if speech_bubble:
				text_box_as_images.append(load_image(TEXT_FILE_PATH + "text/filler.png"))
	
	total_width = sum(img.get_width() for img in text_as_images)
	height = txt_as_images[0].get_height()
	combined_image = pygame.Surface((total_width, height), pygame.SRCALPHA)
	
	if speech_bubble:
		total_width = sum(img.get_width() for img in text_box_as_images)
		height = txt_as_images[0].get_height()
		combined_image_speech_bubble = pygame.Surface((total_width, height), pygame.SRCALPHA)
		return combined_image, combined_image_speech_bubble #without begin.png and end.png
	else:
		return combined_images
	
	#sort out: W!',.SPACE

class Animation:
	def __init__(self, images, img_dur=5, loop=True):
		self.images = images
		self.loop = loop
		self.img_duration = img_dur
		self.done = False
		self.frame = 0
	
	def copy(self):
		return Animation(self.images, self.img_duration, self.loop)
	
	def update(self):
		if self.loop:
			self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
		else:
			self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
			if self.frame >= self.img_duration * len(self.images) - 1:
				self.done = True
	
	def img(self):
		return self.images[int(self.frame / self.img_duration)]