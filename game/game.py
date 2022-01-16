from unittest import result
import pygame, sys
import cv2
import mediapipe as mp
import numpy as np
import os
import time
import random
from game.video_analysis.player_movements import *
import pandas as pd
from game.video_analysis.hand_analyse import *

def gameplay(level):

###################### DÉFINITION FONCTIONS INTERNES #########################

    # Vérifie que le personnage est sur le sol ou non
    def is_onthefloor(character_position,floor_y_position):
        if character_position >= floor_y_position-33:
            return True
        else:
            return False
    
    # Génère un sol à l'infini
    def draw_floor():
        screen.blit(floor_surface,(floor_x_position,floor_y_position)) #352
        screen.blit(floor_surface,(floor_x_position+longueur_screen,floor_y_position)) #+1150

    # Génère des obstacles
    def create_obstacle():
        if next_obstacle == 'resources/images/background/snake-2.png':
            new_obstacle = obstacle_surface.get_rect(center = (1500,525))
        else:
            new_obstacle = obstacle_surface.get_rect(center = (1500,525))
        return new_obstacle

    # Fait avancer les obstacles vers le joueur
    def move_obstacle(obstacles):
        for obstacle in obstacles:
            obstacle.centerx -= vitesse_obstacle
        return obstacles

    # Affiche les obstacles    
    def draw_obstacles(obstacles):
        for obstacle in obstacles:
            screen.blit(obstacle_surface,obstacle)

    # Vérifie si le joueur est entré en collision avec un obstacle
    def check_collision(obstacles):
        for obstacle in obstacles:
            if character_rect.colliderect(obstacle):
                return True

    # Animation du joueur
    def character_animation():
        if character_rect.centery < 304:
            new_character = character_frames[4]
            new_character_rect = new_character.get_rect(center=(60,character_rect.centery))
        else:
            new_character = character_frames[character_index]
            new_character_rect = new_character.get_rect(center=(60,character_rect.centery))
        return new_character, new_character_rect

    # Couleur affichage du score
    def score_color(score):
        if score > 95:
            return (87, 185, 25)
        if score > 90 and score <= 95:
            return (129, 185, 25)
        if score > 85 and score <= 90:
            return (183, 204, 18)
        if score > 80 and score <= 85:
            return (204, 168, 18)
        if score <= 80:
            return (204, 75, 18)

    # Affiche le score
    def score_display():
        score_surface = game_font.render(str(score),True,tuple(score_color(score)))
        score_rect = score_surface.get_rect(center = (70,70))
        screen.blit(score_surface,score_rect)

    # Affiche le temps restant
    def time_display():
        time_surface = time_font.render('Temps restant :' + str(round(duree_jeu - seconds,1)) + 's',True,(255,255,255))
        time_rect = time_surface.get_rect(center = (1150,125))
        screen.blit(time_surface,time_rect)






        
################################# INITIALISATION CAMERA #################################

    cam = cv2.VideoCapture(0)
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    i = 0





################################### CONSTANTES ÉCRAN ###################################

    # Dimension de l'écran
    #longueur_screen = 1150
    #largeur_screen = 469

    longueur_screen = 1250
    largeur_screen = 700

    # Position du sol
    floor_x_position = 0
    floor_y_position = 556





##################################### ENVIRONNEMENT #######################################

    
    pygame.init()
    screen = pygame.display.set_mode((longueur_screen,largeur_screen))
    #screen = pygame.display.set_mode((1250, 700), 0, 32)
    clock = pygame.time.Clock()
    game_font = pygame.font.SysFont('comicsansms',40)
    time_font = pygame.font.SysFont('comicsansms',15)

    # Chargement de l'environnement de jeu (Backgroud & Sol)
    background_surface = pygame.image.load('resources/images/background/background.jpg').convert()
    floor_surface = pygame.image.load('resources/images/background/floor2.png').convert()
    

    # Chargement des obstacles
    obstacles = ['resources/images/background/snake-2.png','resources/images/background/palm_tree.png'] #Liste de tous les obstacles
    next_obstacle = 'resources/images/background/snake-2.png'

    obstacle_surface = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('resources/images/background/palm_tree.png').convert_alpha()))
    obstacle_list = list()

    # Vitesse apparition obstacles
    SPAWNPALM = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPALM,6500)

    # Chargement du personnage principal
    walk0 = pygame.transform.scale2x(pygame.image.load('resources/images/player/Walk-0.png').convert_alpha())
    walk1 = pygame.transform.scale2x(pygame.image.load('resources/images/player/Walk-1.png').convert_alpha())
    walk2 = pygame.transform.scale2x(pygame.image.load('resources/images/player/Walk-2.png').convert_alpha())
    walk3 = pygame.transform.scale2x(pygame.image.load('resources/images/player/Walk-3.png').convert_alpha())
    walk4 = pygame.transform.scale2x(pygame.image.load('resources/images/player/Walk-4.png').convert_alpha())
    walk5 = pygame.transform.scale2x(pygame.image.load('resources/images/player/Walk-5.png').convert_alpha())

    character_frames = [walk0,walk1,walk2,walk3,walk4,walk5]
    character_index = 0
    character_surface = character_frames[character_index]
    character_rect = character_surface.get_rect(center = (60,floor_y_position-33))

    CHAR_WALL = pygame.USEREVENT + 1
    pygame.time.set_timer(CHAR_WALL,100) 





################################# CONSTANTES DU JEU #################################

    duree_jeu = 60
    
    vitesse_sol = 30
    vitesse_obstacle = 30
    saut = 23.

    gravity = 1.8
    character_movement = 0
    is_jumping = False  

    run = True
    end = False

    score_list = [None]

    start_ticks=pygame.time.get_ticks()

    arr = np.array([[0,0]])

    angle_max = 0

######################################## LOOP #######################################

    while run:

        clock.tick()

        if i%3 == 0:
            # Récupération de la position de chaque doigt grâce à la fonction collect_data_recording
            data = collect_data_recording(mp_drawing,mp_drawing_styles,mp_hands,cam)
            i+=1
        
        else:
            i+=1


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Génère un nouvel obstacle dans la liste des obstacles à venir
            if event.type == SPAWNPALM:
                next_obstacle = random.choice(obstacles)
                obstacle_surface = pygame.image.load(next_obstacle).convert_alpha()
                obstacle_list.append(create_obstacle())


            # Permet l'animation du joueur
            if event.type == CHAR_WALL:
                if character_index < 5:
                    character_index += 1
                else:
                    character_index = 0
                character_surface, character_rect = character_animation()

        # Si la caméra capte des mains et si le geste est réalisé alors le joueur saute
        if data[0]:
            is_jumping = closed_hand(data[0]["middle4"],data[0]["index4"],data[0]["ring4"],data[0]["pinky4"],data[0]["paume"],level)

            if is_jumping:
                if is_onthefloor(character_rect.centery,floor_y_position):
                    character_movement = 0
                    character_movement -= saut

        
        # Si le joueur est en l'air : la gravité le fait redescendre
        if character_rect.centery < floor_y_position-33:
            character_movement += gravity
            character_rect.centery += character_movement
            if character_rect.centery > floor_y_position-50:
                character_movement = 0

        # Si le joueur n'est pas en l'air ou atterri, on fixe sa position en y a la position du sol
        else: 
            character_rect.centery = floor_y_position-33
            character_movement += 0.001
            character_rect.centery += character_movement

       
#################################### UPDATE VALUES ####################################

        screen.blit(background_surface,(-5,0))
        screen.blit(character_surface,character_rect)
        floor_x_position -= vitesse_sol

        # Affiche les obstacles
        obstacle_list = move_obstacle(obstacle_list)
        draw_obstacles(obstacle_list)
        draw_floor()
        if floor_x_position <= -1200:
            floor_x_position = 0


 ######################################### SCORE ########################################
        
        if check_collision(obstacle_list) != score_list[-1]:
            score_list.append(check_collision(obstacle_list))

        score = 100 - 5*score_list.count(True)

        if score <=0:
            score = 0

        pygame.draw.circle(screen,score_color(score),(70,70),60)
        pygame.draw.circle(screen,(135,170,210),(70,70),50)

        score_display()



 ######################################### TIMER ########################################

        seconds = round((pygame.time.get_ticks()-start_ticks)/1000,1)

        if duree_jeu - seconds < 0:
            end = True
            run = False

            

        time_display()



#################################### AFFICHAGE WEBCAM ###################################

        image = cv2.resize(data[1], (200, 100)) 

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow('Camera', image)
        cv2.moveWindow('Camera', 1150,-34)
        if cv2.waitKey(5) & 0xFF == 27:
            break


#################################### ACQUISITION DONNÉES ###################################   

        row = np.array([seconds,measure_angle(data)])
        arr = np.append(arr,[row],axis= 0)

        df = pd.DataFrame(arr)


        # Create a Pandas Excel writer using XlsxWriter as the engine.
        excel_file = 'data_acquisition/scatter.xlsx'
        sheet_name = 'Sheet1'

        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=sheet_name)

        # Access the XlsxWriter workbook and worksheet objects from the dataframe.
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        # Create a chart object.
        chart = workbook.add_chart({'type': 'scatter'})

        # Configure the series of the chart from the dataframe data.
        max_row = len(df)

        chart.add_series({
                        'name':       'data',
                        'categories': '=Sheet1!$B$1:$B${}'.format(max_row),
                        'values':     'Sheet1!$C$1:$C${}'.format(max_row),
                        'marker':     {'type': 'plus', 'size': 3},
        })

        # Configure the chart axes.
        chart.set_x_axis({'name': 'Frame'})
        chart.set_y_axis({'name': 'Angle en degrés',
                  'major_gridlines': {'visible': False}})


        # Insert the chart into the worksheet.
        worksheet.insert_chart('K2', chart)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()


        if measure_angle(data) is not None and measure_angle(data) > angle_max:
            angle_max = measure_angle(data)
    


#############################################################################################################

        pygame.display.update()

#################################### DONNÉES AFFICHÉES ÉCRAN FIN ###################################
    
    f=0
    nb_obstacles = len(obstacle_list) 
    obstacles_touches = score_list.count(True)
    obstacles_evites = nb_obstacles - obstacles_touches

    while end:

        pygame.draw.rect(screen, (255,255,255), (325, 150, 600, 400),)

        font = pygame.font.Font(None, 48)
        font0 = pygame.font.Font(None, 48)
        text0 = font0.render("Votre score :",1,(0,0,0))
        screen.blit(text0, (525, 200))        
        text1 = font.render("Nombre d'obstacles évités : {}".format(obstacles_evites),1,(0,0,0))
        screen.blit(text1, (345, 300))
        text2 = font.render("Nombre d'obstacles touchés : {}".format(obstacles_touches),1,(0,0,0))
        screen.blit(text2, (345, 350))
        text3 = font.render("Angle maximal de fermeture : {} °".format(angle_max),1,(0,0,0))
        screen.blit(text3, (345, 400))

        pygame.display.update()

        f+=1
        if f>1500:
            break
    
        nb_obstacles = len(obstacle_list) 
        obstacles_touches = score_list.count(True)
        obstacles_evites = nb_obstacles - obstacles_touches
