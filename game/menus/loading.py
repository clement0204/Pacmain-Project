#!/usr/bin/python3
import sys
import pygame
pygame.init()


class GameLoading:

	def __init__(
		self, screen, bg_color=(0, 0, 0), font=None,
		font_size=100, font_color=(255, 255, 255)):

		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height

		# Background Main Menu
		self.bg_color = bg_color
		self.bg_loading = pygame.image.load('resources/images/background/loading.png')
		self.bg_loading_rect = self.bg_loading.get_rect()

		# Sound Menu Change
		self.menu_sound = pygame.mixer.Sound('resources/sounds/menu_noise.wav')
		self.valid_menu_sound = pygame.mixer.Sound('resources/sounds/menu_valid_sound.wav')

		# Menu Music
		self.menu_music = pygame.mixer.music.load('resources/sounds/menu_music.mp3')
		pygame.mixer.music.set_volume(0.5)

		# Main Menu
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont(font, font_size)

		self.paddingx = 8
		self.paddingy = 20

		self.menu_selected = False
		self.start_selected = False
		self.settings_selected = False
		self.quit_select = False


	def run(self):

		duree_chargement = 5 #secondes
		start_ticks=pygame.time.get_ticks() #compteur de temps

		mainloop = True

		while mainloop:

			seconds=round((pygame.time.get_ticks()-start_ticks)/1000,1)

			# Dès que l'on atteint 10s, on quitte la page de chargement

			if duree_chargement - seconds < 0:
				self.menu_selected = True
				pygame.mixer.music.fadeout(1000)
				mainloop = False

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					mainloop = False
					sys.exit()

			# Limit frame speed to 50 FPS
			# self.clock.tick(20)
			if not pygame.mixer.music.get_busy():
				pygame.mixer.music.rewind()
				pygame.mixer.music.play()
							
			# Redraw the background
			self.screen.fill(self.bg_color)

			if not self.start_selected or not self.settings_selected:
				self.screen.blit(self.bg_loading, self.bg_loading_rect)

			pygame.display.flip()
