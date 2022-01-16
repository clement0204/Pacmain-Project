#!/usr/bin/python3
import sys
import pygame
from random import randint
from game.game import gameplay
from game.video_analysis.player_movements import *

pygame.init()


class Game:

	def __init__(self, screen):
		self.clock = pygame.time.Clock()
		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.size = self.scr_width, self.scr_height
		self.jeu = True

	def run(self,level):
		gameplay(level)
		self.jeu = False
