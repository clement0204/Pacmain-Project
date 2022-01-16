#!/usr/bin/python3
import sys
import pygame

from game.game import gameplay
pygame.init()

class GameLevel:

	def __init__(
		self, screen, items, bg_color=(0, 0, 0), font=None,
		font_size=100, font_color=(255, 255, 255)):

		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height

		# Background Main level
		self.bg_color = bg_color
		self.bg_img = pygame.image.load('resources/images/background/menu.png')
		self.bg_img_rect = self.bg_img.get_rect()

		# Sound level Change
		self.level_sound = pygame.mixer.Sound('resources/sounds/menu_noise.wav')
		self.valid_level_sound = pygame.mixer.Sound('resources/sounds/menu_valid_sound.wav')

		# Menu Music
		self.level_music = pygame.mixer.music.load('resources/sounds/menu_music.mp3')
		pygame.mixer.music.set_volume(0.5)

		# Main Menu
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont(font, font_size)

		self.paddingx = 8
		self.paddingy = 20

		self.level3_selected = False
		self.level2_selected = False
		self.level1_selected = False

		self.index_selected = 0
		self.current_item = ()
		self.level_items = []

		# Position menu titles on the menu screen
		for index, item in enumerate(items):
			label = self.font.render(item, 1, font_color)

			width = label.get_rect().width
			height = label.get_rect().height

			posx = (self.scr_width / 2) - (width / 2)

			# t_h: total height of text block
			t_h = len(items) * height

			posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
			self.level_items.append([item, label, (width, height), (posx, posy)])

	def run(self):

		mainloop = True

		while mainloop:

			# Limit frame speed to 50 FPS
			# self.clock.tick(20)

			if not pygame.mixer.music.get_busy():
				pygame.mixer.music.rewind()
				pygame.mixer.music.play()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					mainloop = False
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.level_sound.play().set_volume(0.2)
						for index, item in enumerate(self.level_items):
							if self.current_item[0] == item[0]:
								if self.index_selected > 0:
									self.index_selected -= 1
					if event.key == pygame.K_DOWN:
						self.level_sound.play().set_volume(0.2)
						for index, item in enumerate(self.level_items):
							if self.current_item[0] == item[0]:
								if self.index_selected < (len(self.level_items) - 1):
									self.index_selected += 1
					if event.key == pygame.K_RETURN:
						self.valid_level_sound.play().set_volume(0.2)
						if len(self.current_item) > 0:
							if self.current_item[0] == "Niveau 3":
								self.level3_selected = True
								#gameplay()

							elif self.current_item[0] == "Niveau 2":
								self.level2_selected = True
								#gameplay()

							elif self.current_item[0] == "Niveau 1":
								self.level1_selected = True
								#gameplay()

							pygame.mixer.music.fadeout(1000)
							mainloop = False

			self.current_item = self.level_items[self.index_selected]

			# Redraw the background
			self.screen.fill(self.bg_color)

			if not self.level3_selected or not self.level2_selected or not self.level1_selected:
				self.screen.blit(self.bg_img, self.bg_img_rect)

				for name, label, (width, height), (posx, posy) in self.level_items:
					self.screen.blit(label, (posx, posy))

				name, label, (width, height), (posx, posy) = self.current_item

				pygame.draw.rect(
					self.screen, (255, 255, 255),
					[
						posx - self.paddingx, posy - self.paddingy,
						width + self.paddingx + self.paddingx, height + self.paddingy
					], 2)

			pygame.display.flip()