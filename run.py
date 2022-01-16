#!/usr/bin/python3

import pygame
from game.game_class import Game
from game.menus.level import GameLevel
from game.menus.menu import GameMenu
from game.menus.settings import GameSettings
from game.menus.loading import GameLoading
from game.menus.ending import GameEnding

pygame.init()

# Créer une fenêtre de jeu
# set_mode(resolution=(width, height), flags=0, depth=0)
screen = pygame.display.set_mode((1250, 700), 0, 32) 
pygame.display.set_caption('Pacmain : le jeu de rééducation de la main')

# Couleur de la fenêtre
bg_color = (0, 0, 0)

# Loading
gload = GameLoading(screen)

# Game Menu
menu_items = ('Jouer', 'Tutoriel', 'Quitter')
gm = GameMenu(screen, menu_items)

# Level Menu
level_items = ('Niveau 3', 'Niveau 2', 'Niveau 1')
gl = GameLevel(screen, level_items)

# Tutorial
gs = GameSettings(screen)

# End
gf = GameEnding(screen)


# Par défaut, la fenêtre de lancement sera la page de chargement
loading_selected = True

# l'écran Game sera créé dynamiquement pour permettre le redémarrage au début
g = None

# Par défaut, la boucle tourne à l'infini.
mainloop = True

while mainloop:

    # Rafraichit l'écran en noir à chaque boucle
    screen.fill(bg_color)

    # Démarre l'écran de chargement
    if loading_selected:
        gload.run()
        loading_selected = False

    # Démarre l'écran menu par défaut ou après ECHAP
    if gload.menu_selected:
        gm.run()
        gload.menu_selected = False


# Démarre l'écran de jeu
    if gm.start_selected:
        g = GameLevel(screen,level_items)
        g.run()
        if g.level1_selected:
            gl.level1_selected = True
        if g.level2_selected:
            gl.level2_selected = True
        if g.level3_selected:
            gl.level3_selected = True
        gm.start_selected = False
        gm.quit_select = False

    # Démarre l'écran de jeu
    if gl.level1_selected:
        g = Game(screen)
        g.run('niveau 1')
        if not g.jeu:
            gf.ending_selected = True 
        gl.level1_selected = False  

    if gl.level2_selected:
        g = Game(screen)
        g.run('niveau 2')
        if not g.jeu:
            gf.ending_selected = True 
        gl.level2_selected = False  

    if gl.level3_selected:
        g = Game(screen)
        g.run('niveau 3')
        if not g.jeu:
            gf.ending_selected = True 
        gl.level3_selected = False  

    if gf.ending_selected:
        g = GameEnding(screen)
        g.run()
        mainloop = False

    # Démarre l'écran de configuration
    if gm.settings_selected:
        gs.run()
        gm.settings_selected = False
        gload.menu_selected = True

    # Ferme la fenêtre si Quit est séléctionnée
    if gm.quit_select is True:
        mainloop = False
    
    pygame.display.flip()


