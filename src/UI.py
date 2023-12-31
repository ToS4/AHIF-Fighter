
##
# @file UI.py
#
# @brief Uses functions to create menus
#
# @section desciption_UI Description
# Defines functions for the following menus:
# - selecting_character (not a menu; used to load the selected character)
# - main_menu
# - pause_menu
# - settings_menu
# - p1_setings_menu
# - p2_setings_menu
# - play_menu
# - gameover_menu
#
# @section libraries_UI Libraries/Modules
# - pygame library (https://www.pygame.org/news)
# - json library
# - sys library
# - os library
# - ButtonController module
# - Samurai module
# - VampireGirl module
# - LightningMage module
# - FireWizard module
# - AnimationController module
# 
# @section author_UI Author(s)
# - Created by mirko4001
# - Modified by mirko4001 & ToS4

import pygame
import json
import sys
import os
from ButtonController import Button, InputBox, CharacterBox
from Samurai import Samurai
from VampireGirl import VampireGirl
from LightningMage import LightningMage
from FireWizard import FireWizard
from AnimationController import Animation

pygame.init()
pygame.mixer.init()

pygame.mixer.music.set_volume(1)

# fixed Screen
WIDTH = 1000
HEIGHT = 600

# Fullscreen
SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
MAIN_WIDTH = SCREEN.get_width()
MAIN_HEIGHT = SCREEN.get_height()

# this is for scaling the font to fit the according screen
font_scaled = pygame.font.Font(None, int(35*MAIN_HEIGHT/HEIGHT))
# transparent color
transparent = pygame.Color(255,255,255,a=255)

# variable to reset the game
reset = False

select_p1 = None
select_p2 = None

player1 = None
player2 = None

# dict for theme color of every character
char_list = {"Samurai":"aquamarine2",
             "FireWizard":"orange",
             "LightningMage":"darkolivegreen1",
             "VampireGirl":"hotpink3"}

def select_character(name, player,settings):
    """! Loads a different class based on the selected character

    @param name     Character name
    @param player   Player 1 or Player 2
    @param settings The saved settings in settings.txt

    @return selected_character  The class of the selected character
    """

    pos = (800 if player == 2 else 200,160) # (x, y)
    scale_factor = (MAIN_WIDTH / WIDTH, MAIN_HEIGHT / HEIGHT)    #  (width_factor, height_factor)
    character_hitbox_size = (60,120)    # (width_hitbox, height_hitbox)
    flip = True if player == 2 else False
    controls = settings["player1"] if player == 1 else settings["player2"]

    if name == "Samurai":

        files = []

        files.append((pygame.image.load("src/assets/imgs/Samurai/Idle.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/Samurai/Run.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/Samurai/Jump.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/Samurai/Attack1.png").convert_alpha(),8))
        files.append((pygame.image.load("src/assets/imgs/Samurai/Attack2.png").convert_alpha(),8))
        files.append((pygame.image.load("src/assets/imgs/Samurai/Attack3.png").convert_alpha(),8))
        files.append((pygame.image.load("src/assets/imgs/Samurai/Hurt.png").convert_alpha(),30))
        files.append((pygame.image.load("src/assets/imgs/Samurai/Ability.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/Samurai/Dead.png").convert_alpha(),14))

        animations = [Animation(animation[0], 128, 128, animation[1]) for animation in files]
            
        return Samurai( pos, scale_factor, character_hitbox_size, flip, controls, animations)
    
    elif name == "LightningMage":

        files = []

        files.append((pygame.image.load("src/assets/imgs/LightningMage/Idle.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Run.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Jump.png").convert_alpha(),7))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Hurt.png").convert_alpha(),30))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Dead.png").convert_alpha(),14))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Ability.png").convert_alpha(),6))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Attack1.png").convert_alpha(),5))
        files.append((pygame.image.load("src/assets/imgs/LightningMage/Attack2.png").convert_alpha(),10))

        animations = [Animation(animation[0], 128, 128, animation[1]) for animation in files]
            
        return LightningMage( pos, scale_factor, character_hitbox_size, flip, controls, animations)

    elif name == "FireWizard":

        files = []

        files.append((pygame.image.load("src/assets/imgs/FireWizard/Idle.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Run.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Jump.png").convert_alpha(),7))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Hurt.png").convert_alpha(),30))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Dead.png").convert_alpha(),14))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Ability.png").convert_alpha(),6))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Attack1.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/FireWizard/Attack2.png").convert_alpha(),10))

        animations = [Animation(animation[0], 128, 128, animation[1]) for animation in files]
            
        return FireWizard( pos, scale_factor, character_hitbox_size, flip, controls, animations)

    elif name == "VampireGirl":

        files = []

        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Idle.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Run.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Jump.png").convert_alpha(),7))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Hurt.png").convert_alpha(),30))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Dead.png").convert_alpha(),14))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Ability.png").convert_alpha(),8))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Attack1.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Attack2.png").convert_alpha(),10))
        files.append((pygame.image.load("src/assets/imgs/VampireGirl/Attack3.png").convert_alpha(),10))

        animations = [Animation(animation[0], 128, 128, animation[1]) for animation in files]
            
        return VampireGirl( pos, scale_factor, character_hitbox_size, flip, controls, animations)

def main_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    """! Creates a main menu

    @param scale_width_factor   The scaling factor for the width
    @param scale_height_factor  The scaling factor for the height
    @param dest_gameloop        The main game loop
    @param settings             The Keybinds that are saved in settings.txt
    """
    main_music = pygame.mixer.music.load("src/assets/sounds/main_menu_music.wav")
    pygame.mixer.music.play(-1)
    global reset
    reset = True
    # Creating the play button and settings its position
    play_button = Button(0,0,250,80,"black","PLAY","White",font_scaled
                        ,scale_width_factor, scale_height_factor, lambda: play_menu(MAIN_WIDTH/WIDTH, MAIN_HEIGHT/HEIGHT,
                                                                                    dest_gameloop, settings))
    play_button.rect.center = (MAIN_WIDTH/2 + 0*scale_width_factor, MAIN_HEIGHT/2-150*scale_height_factor)

    # Creating settings button and setting its position
    settings_button  = Button(0,0,300,80,"black","SETTINGS","white",font_scaled,
                            scale_width_factor, scale_height_factor, lambda: settings_menu(MAIN_WIDTH/WIDTH, MAIN_HEIGHT/HEIGHT,
                                dest_gameloop, settings))
    settings_button.rect.center = (MAIN_WIDTH/2+ 0*scale_width_factor, MAIN_HEIGHT/2)

    # Creating quit button and setting its position
    quit_button  = Button(0,0,250,80,"black","QUIT","white",font_scaled,
                            scale_width_factor, scale_height_factor, lambda: sys.exit())
    quit_button.rect.center = (MAIN_WIDTH/2+ 0*scale_width_factor, MAIN_HEIGHT/2 + 150*scale_height_factor)

    # MAIN MENU LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_button.handle_event(event)
                settings_button.handle_event(event)
                quit_button.handle_event(event)
            

        # always get the current mouse position
        mouse_position = pygame.mouse.get_pos()

        # these functions are responsible for the color change when hovering over the button
        play_button.hover_effect(mouse_position)
        settings_button.hover_effect(mouse_position)
        quit_button.hover_effect(mouse_position)

        # fill the screen white
        SCREEN.fill((255,255,255))

        #draws the buttons
        play_button.draw(SCREEN)
        settings_button.draw(SCREEN)
        quit_button.draw(SCREEN)

        pygame.display.update()

def pause_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    """! Draws a menu when the escape key is pressed

    @param scale_width_factor   The scaling factor for the width
    @param scale_height_factor  The scaling factor for the height
    @param dest_gameloop        The main game loop
    @param settings             The Keybinds that are saved in settings.txt
    """
    global reset, player1, player2
    reset = False
    # Creating the play button and settings its position
    continue_button = Button(0,0,250,80,"black","CONTINUE","White",font_scaled
                        ,scale_width_factor, scale_height_factor, lambda: dest_gameloop(player1, player2))
    continue_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2-75*scale_height_factor)

    # Creating quit button and setting its position
    back_button  = Button(0,0,250,80,"black","BACK TO MENU","white",font_scaled,
                            scale_width_factor, scale_height_factor, lambda: main_menu(scale_width_factor, scale_height_factor,
                                                                                        dest_gameloop, settings))
    back_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 + 75*scale_height_factor)

    # MAIN MENU LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                continue_button.handle_event(event)
                back_button.handle_event(event)
            

        # always get the current mouse position
        mouse_position = pygame.mouse.get_pos()

        # these functions are responsible for the color change when hovering over the button
        continue_button.hover_effect(mouse_position)
        back_button.hover_effect(mouse_position)

        # fill the screen white
        SCREEN.fill((255,255,255))

        #draws the buttons
        continue_button.draw(SCREEN)
        back_button.draw(SCREEN)

        pygame.display.update()

def settings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    """! Creates a menu when the settings button is pressed

    @param scale_width_factor   The scaling factor for the width
    @param scale_height_factor  The scaling factor for the height
    @param dest_gameloop        The main game loop
    @param settings             The Keybinds that are saved in settings.txt
    """
    # The responsible buttons for each players settings
    keybinds_p1_button = Button(0,0,300,80,"black","PLAYER 1","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: p1_setings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings))
    keybinds_p1_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2-150*scale_height_factor))

    keybinds_p2_button = Button(0,0,300,80,"black","PLAYER 2","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: p2_setings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings))
    keybinds_p2_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2))

    # a Button that returns you to the Main Menu
    back_button = Button(0,0,250,80,"black","BACK","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: main_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings))
    back_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2+150*scale_height_factor))

    # This is to save the Keybinds every time you go back from p1- or p2-settings
    with open("settings.txt", "w") as file:
        text = json.dumps(settings)
        file.write(text)

    # Setting Menu loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                keybinds_p1_button.handle_event(event)
                keybinds_p2_button.handle_event(event)
                back_button.handle_event(event)

        mouse_position = pygame.mouse.get_pos()

        keybinds_p1_button.hover_effect(mouse_position)
        keybinds_p2_button.hover_effect(mouse_position)
        back_button.hover_effect(mouse_position)

        SCREEN.fill("white")

        keybinds_p1_button.draw(SCREEN)
        keybinds_p2_button.draw(SCREEN)
        back_button.draw(SCREEN)
        
        pygame.display.update()

def p1_setings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    """! Creates the settings menu for the keybinds (player1)

    @param scale_width_factor   The scaling factor for the width
    @param scale_height_factor  The scaling factor for the height
    @param dest_gameloop        The main game loop
    @param settings             The Keybinds that are saved in settings.txt
    """
    # This is to create a "text", in reality it is a button with no functionality
    p1_text = Button(0,0,300,80,transparent,"PLAYER 1","black", font_scaled,scale_width_factor, scale_height_factor, None)
    p1_text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 250*scale_height_factor)
    
    # a Button that returns you to the Main Menu
    back_button = Button(0,0,250,80,"black","BACK","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: settings_menu(MAIN_WIDTH/WIDTH, MAIN_HEIGHT/HEIGHT, dest_gameloop, settings))
    back_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2 + 250*scale_height_factor))

    # all input boxes for the keybinds
    left_kb_text = Button(0,0,300,80,transparent,"Move Left","black", font_scaled,scale_width_factor, scale_height_factor, None)
    left_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2 - 175*scale_height_factor)
    left_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                       pygame.key.name(settings["player1"]["left"]))
    left_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2 - 175*scale_height_factor)

    right_kb_text = Button(0,0,300,80,transparent,"Move Right","black", font_scaled,scale_width_factor, scale_height_factor, None)
    right_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2 - 100*scale_height_factor)
    right_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                        pygame.key.name(settings["player1"]["right"]))
    right_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2-100*scale_height_factor)

    jump_kb_text = Button(0,0,300,80,transparent,"Jump","black", font_scaled,scale_width_factor, scale_height_factor, None)
    jump_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2-25*scale_height_factor)
    jump_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                       pygame.key.name(settings["player1"]["jump"]))
    jump_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2-25*scale_height_factor)

    attack_kb_text = Button(0,0,300,80,transparent,"Attack","black", font_scaled,scale_width_factor, scale_height_factor, None)
    attack_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2+50*scale_height_factor)
    attack_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                         pygame.key.name(settings["player1"]["attack"]))
    attack_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2+50*scale_height_factor)

    ability_kb_text = Button(0,0,300,80,transparent,"Ability","black", font_scaled,scale_width_factor, scale_height_factor, None)
    ability_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2+125*scale_height_factor)
    ability_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                         pygame.key.name(settings["player1"]["ability"]))
    ability_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2+125*scale_height_factor)

    # list that contains all the input boxes
    inputs = [left_kb, right_kb, jump_kb, attack_kb, ability_kb]

    # list that contains the texts of these boxes
    texts = [left_kb_text, right_kb_text, attack_kb_text, jump_kb_text, ability_kb_text]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_button.handle_event(event)
            
            settings["player1"]["left"] = pygame.key.key_code(left_kb.handle_event(event))
            settings["player1"]["right"] = pygame.key.key_code(right_kb.handle_event(event))
            settings["player1"]["jump"] = pygame.key.key_code(jump_kb.handle_event(event))
            settings["player1"]["attack"] = pygame.key.key_code(attack_kb.handle_event(event))
            settings["player1"]["ability"] = pygame.key.key_code(ability_kb.handle_event(event))
        
        mouse_position = pygame.mouse.get_pos()

        # p1_button should not be added here, since its not displayed as a button
        back_button.hover_effect(mouse_position)
        
        SCREEN.fill((255,255,255))

        p1_text.draw(SCREEN)
        back_button.draw(SCREEN)

        for i in texts:
            i.draw(SCREEN)
        for i in inputs:
            i.draw(SCREEN)

        pygame.display.update()

def p2_setings_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    """! Creates the settings menu for the keybinds (player2)

    @param scale_width_factor   The scaling factor for the width
    @param scale_height_factor  The scaling factor for the height
    @param dest_gameloop        The main game loop
    @param settings             The Keybinds that are saved in settings.txt
    """
    # This is to create a "text", in reality it is a button with no functionality
    p2_text = Button(0,0,300,80,transparent,"PLAYER 2","black", font_scaled,scale_width_factor, scale_height_factor, None)
    p2_text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 250*scale_height_factor)
    
    # a Button that returns you to the Main Menu
    back_button = Button(0,0,250,80,"black","BACK","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: settings_menu(MAIN_WIDTH/WIDTH, MAIN_HEIGHT/HEIGHT, dest_gameloop, settings))
    back_button.rect.center = ((MAIN_WIDTH/2, MAIN_HEIGHT/2 + 250*scale_height_factor))

    # all input boxes for the keybinds
    left_kb_text = Button(0,0,300,80,transparent,"Move Left","black", font_scaled,scale_width_factor, scale_height_factor, None)
    left_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2 - 175*scale_height_factor)
    left_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                       pygame.key.name(settings["player2"]["left"]))
    left_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2 - 175*scale_height_factor)

    right_kb_text = Button(0,0,300,80,transparent,"Move Right","black", font_scaled,scale_width_factor, scale_height_factor, None)
    right_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2 - 100*scale_height_factor)
    right_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                        pygame.key.name(settings["player2"]["right"]))
    right_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2-100*scale_height_factor)

    jump_kb_text = Button(0,0,300,80,transparent,"Jump","black", font_scaled,scale_width_factor, scale_height_factor, None)
    jump_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2-25*scale_height_factor)
    jump_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                       pygame.key.name(settings["player2"]["jump"]))
    jump_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2-25*scale_height_factor)

    attack_kb_text = Button(0,0,300,80,transparent,"Attack","black", font_scaled,scale_width_factor, scale_height_factor, None)
    attack_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2+50*scale_height_factor)
    attack_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                         pygame.key.name(settings["player2"]["attack"]))
    attack_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2+50*scale_height_factor)

    ability_kb_text = Button(0,0,300,80,transparent,"Ability","black", font_scaled,scale_width_factor, scale_height_factor, None)
    ability_kb_text.rect.center = (MAIN_WIDTH/2-75*scale_width_factor, MAIN_HEIGHT/2+125*scale_height_factor)
    ability_kb = InputBox(0,0,50,50,font_scaled, (0,0,0), (33, 239, 234), scale_width_factor,scale_height_factor, settings,
                         pygame.key.name(settings["player2"]["ability"]))
    ability_kb.rect.center = (MAIN_WIDTH/2+75*scale_width_factor, MAIN_HEIGHT/2+125*scale_height_factor)

    # list that contains all the input boxes
    inputs = [left_kb, right_kb, jump_kb, attack_kb, ability_kb]

    # list that contains the texts of these boxes
    texts = [left_kb_text, right_kb_text, attack_kb_text, jump_kb_text, ability_kb_text]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_button.handle_event(event)
            
            settings["player2"]["left"] = pygame.key.key_code(left_kb.handle_event(event))
            settings["player2"]["right"] = pygame.key.key_code(right_kb.handle_event(event))
            settings["player2"]["jump"] = pygame.key.key_code(jump_kb.handle_event(event))
            settings["player2"]["attack"] = pygame.key.key_code(attack_kb.handle_event(event))
            settings["player2"]["ability"] = pygame.key.key_code(ability_kb.handle_event(event))
        
        mouse_position = pygame.mouse.get_pos()

        # p1_button should not be added here, since its not displayed as a button
        back_button.hover_effect(mouse_position)
        
        SCREEN.fill((255,255,255))

        p2_text.draw(SCREEN)
        back_button.draw(SCREEN)

        for i in texts:
            i.draw(SCREEN)
        for i in inputs:
            i.draw(SCREEN)

        pygame.display.update()

def play_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings):
    """! Creates a menu for character selection

    @param scale_width_factor   The scaling factor for the width
    @param scale_height_factor  The scaling factor for the height
    @param dest_gameloop        The main game loop
    @param settings             The Keybinds that are saved in settings.txt
    """
    global select_p1, select_p2, player1, player2

    select_p1 = None
    select_p2 = None
    
    player = 1

    # This will be the box for the samurai selection
    samurai_box = CharacterBox(0,0,100,100,"white",scale_width_factor, scale_height_factor, "Samurai")
    samurai_box.rect.center = (MAIN_WIDTH/2-180*scale_width_factor, MAIN_HEIGHT/2 - 80 * scale_height_factor)
    samurai_img = pygame.image.load(os.path.join("src/assets/imgs/Samurai/Icon.png")).convert_alpha()
    samurai_img = pygame.transform.scale(samurai_img, (99*scale_width_factor, 99*scale_height_factor))
    samurai_select = False

    # This is a surface of the whole character for when he is selected
    samurai_surface = pygame.image.load("src/assets/imgs/Samurai/Ability.png").convert_alpha()
    samurai_surface = pygame.transform.scale(samurai_surface, (550,600))

    # This will be the box for the mage selection
    mage_box = CharacterBox(0,0,100,100,"white",scale_width_factor, scale_height_factor, "LightningMage")
    mage_box.rect.center = (MAIN_WIDTH/2-60*scale_width_factor, MAIN_HEIGHT/2 - 80 * scale_height_factor)
    mage_img = pygame.image.load(os.path.join("src/assets/imgs/LightningMage/Icon.png")).convert_alpha()
    mage_img = pygame.transform.scale(mage_img, (99*scale_width_factor, 99*scale_height_factor))
    mage_select = False

    mage_surface = pygame.image.load("src/assets/imgs/LightningMage/Standing.png").convert_alpha()
    mage_surface = pygame.transform.scale(mage_surface, (550,600))

    # This will be the box for the fire wizard selection
    fire_box = CharacterBox(0,0,100,100,"white",scale_width_factor, scale_height_factor, "FireWizard")
    fire_box.rect.center = (MAIN_WIDTH/2+60*scale_width_factor, MAIN_HEIGHT/2 - 80 * scale_height_factor)
    fire_img = pygame.image.load(os.path.join("src/assets/imgs/FireWizard/Icon.png")).convert_alpha()
    fire_img = pygame.transform.scale(fire_img, (99*scale_width_factor, 99*scale_height_factor))
    fire_select = False

    fire_surface = pygame.image.load("src/assets/imgs/FireWizard/Standing.png").convert_alpha()
    fire_surface = pygame.transform.scale(fire_surface, (550,600))

    # This will be the box for the vampire selection
    vampire_box = CharacterBox(0,0,100,100,"white",scale_width_factor, scale_height_factor, "VampireGirl")
    vampire_box.rect.center = (MAIN_WIDTH/2+180*scale_width_factor, MAIN_HEIGHT/2 - 80 * scale_height_factor)
    vampire_img = pygame.image.load(os.path.join("src/assets/imgs/VampireGirl/Icon.png")).convert_alpha()
    vampire_img = pygame.transform.scale(vampire_img, (99*scale_width_factor, 99*scale_height_factor))
    vampire_select = False

    vampire_surface = pygame.image.load("src/assets/imgs/VampireGirl/Standing.png").convert_alpha()
    vampire_surface = pygame.transform.scale(vampire_surface, (550,600))

    char = ""
    text = Button(0,0,300,80,(255,255,255,0),char,"black", font_scaled,scale_width_factor, scale_height_factor, None)
    text.rect.width = 10
    text.rect.height = 10
    text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 40*scale_height_factor)

    def draw_char_player1(screen, char_p1, char_p2):
        if char_p1:
            surface = pygame.image.load(f"src/assets/imgs/{char_p1}/Standing.png").convert_alpha()
            surface = pygame.transform.scale(surface, (550,600))
            screen.blit(surface, (-50*scale_width_factor,-120*scale_height_factor))

        if char_p2:
            surface = pygame.image.load(f"src/assets/imgs/{char_p2}/Standing.png").convert_alpha()
            surface = pygame.transform.scale(surface, (550,600))
            screen.blit(surface, ((WIDTH-350)*scale_width_factor,-120*scale_height_factor))

    
    def draw_stats(screen, char_p1, char_p2):
        if char_p1:
            temp_char = eval(f"{char_p1}")((0,0),(0,0),(0,0),False,{},[])
            damage = temp_char.damage
            health = temp_char.health
            damage_surface = font_scaled.render(f"Damage: {str(damage)}", True, char_list[char_p1])
            health_surface = font_scaled.render(f"Health: {str(health)}", True, char_list[char_p1])
            screen.blit(damage_surface, (100*scale_width_factor,350*scale_height_factor))
            screen.blit(health_surface, (100*scale_width_factor,400*scale_height_factor))
        if char_p2:
            temp_char = eval(f"{char_p2}")((0,0),(0,0),(0,0),False,{},[])
            damage = temp_char.damage
            health = temp_char.health
            damage_surface = font_scaled.render(f"Damage: {str(damage)}", True, char_list[char_p2])
            health_surface = font_scaled.render(f"Health: {str(health)}", True, char_list[char_p2])
            screen.blit(damage_surface, ((WIDTH-250)*scale_width_factor,350*scale_height_factor))
            screen.blit(health_surface, ((WIDTH-250)*scale_width_factor,400*scale_height_factor))

    def draw_stats_hovered(screen, char, player):
        temp_char = eval(f"{char}")((0,0),(0,0),(0,0),False,{},[])
        damage = temp_char.damage
        health = temp_char.health
        damage_surface = font_scaled.render(f"Damage: {str(damage)}", True, char_list[char])
        health_surface = font_scaled.render(f"Health: {str(health)}", True, char_list[char])
        if player == 1:
            screen.blit(damage_surface, (100*scale_width_factor,350*scale_height_factor))
            screen.blit(health_surface, (100*scale_width_factor,400*scale_height_factor))
        if player == 2:
            screen.blit(damage_surface, ((WIDTH-250)*scale_width_factor,350*scale_height_factor))
            screen.blit(health_surface, ((WIDTH-250)*scale_width_factor,400*scale_height_factor))
            

    while True:
        if player == "2":
            start_button = Button(0,0,250,80,"black","START","white",font_scaled,scale_width_factor, scale_height_factor, lambda: dest_gameloop(player1, player2))
            start_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 + 200 * scale_height_factor)
        else:
            start_button = Button(0,0,250,80,"black","START","white",font_scaled,scale_width_factor, scale_height_factor, lambda: None)
            start_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 + 200 * scale_height_factor)

        player1 = select_character(select_p1,1, settings)
        player2 = select_character(select_p2,2, settings)

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_button.handle_event(event)
                if player == 1:
                    if samurai_box.rect.collidepoint(mouse_pos):
                        select_p1 = "Samurai"
                        samurai_box.select(char_list,select_p1)
                        player += 1
                        samurai_select = True
                    elif mage_box.rect.collidepoint(mouse_pos):
                        select_p1 = "LightningMage"
                        mage_box.select(char_list,select_p1)
                        player += 1
                        mage_select = True
                    elif fire_box.rect.collidepoint(mouse_pos):
                        select_p1 = "FireWizard"
                        fire_box.select(char_list,select_p1)
                        player += 1
                        fire_select = True
                    elif vampire_box.rect.collidepoint(mouse_pos):
                        select_p1 = "VampireGirl"
                        vampire_box.select(char_list,select_p1)
                        player += 1
                        vampire_select = True

                elif player == 2:
                    if samurai_box.rect.collidepoint(mouse_pos) and not samurai_select:
                        select_p2 = "Samurai"
                        samurai_box.select(char_list,select_p2)
                        player = "2"
                    elif mage_box.rect.collidepoint(mouse_pos) and not mage_select:
                        select_p2 = "LightningMage"
                        mage_box.select(char_list,select_p2)
                        
                        player = "2"
                    elif fire_box.rect.collidepoint(mouse_pos) and not fire_select:
                        select_p2 = "FireWizard"
                        fire_box.select(char_list,select_p2)
                        
                        player = "2"
                    elif vampire_box.rect.collidepoint(mouse_pos) and not vampire_select:
                        select_p2 = "VampireGirl"
                        vampire_box.select(char_list,select_p2)
                        player = "2"
        
        text = Button(0,0,300,80,(255,255,255,0),char,"black", font_scaled,scale_width_factor, scale_height_factor, None)
        text.rect.width = 10
        text.rect.height = 10
        text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 + 30*scale_height_factor)

        selecting_text = Button(0,0,400,150,transparent, f"Player {player} is selecting...","black",font_scaled,
                            scale_width_factor,scale_height_factor)
        selecting_text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 220 * scale_height_factor)

    
        SCREEN.fill((255,255,255))

        if samurai_box.rect.collidepoint(mouse_pos):
            char = samurai_box.char
            if player == 1:
                SCREEN.blit(samurai_surface, (-50*scale_width_factor,-120*scale_height_factor))
            elif player == 2:
                SCREEN.blit(samurai_surface, ((WIDTH-350)*scale_width_factor,-120*scale_height_factor))
            draw_stats_hovered(SCREEN, char, player)
        elif mage_box.rect.collidepoint(mouse_pos):
            char = mage_box.char
            if player == 1:
                SCREEN.blit(mage_surface, (-50*scale_width_factor,-120*scale_height_factor))
            elif player == 2:
                SCREEN.blit(mage_surface, ((WIDTH-350)*scale_width_factor,-120*scale_height_factor))
            draw_stats_hovered(SCREEN, char, player)
        elif fire_box.rect.collidepoint(mouse_pos):
            char = fire_box.char
            if player == 1:
                SCREEN.blit(fire_surface, (-50*scale_width_factor,-120*scale_height_factor))
            elif player == 2:
                SCREEN.blit(fire_surface, ((WIDTH-350)*scale_width_factor,-120*scale_height_factor))
            draw_stats_hovered(SCREEN, char, player)
        elif vampire_box.rect.collidepoint(mouse_pos):
            char = vampire_box.char
            if player == 1:
                SCREEN.blit(vampire_surface, (-50*scale_width_factor,-120*scale_height_factor))
            elif player == 2:
                SCREEN.blit(vampire_surface, ((WIDTH-350)*scale_width_factor,-120*scale_height_factor))
            draw_stats_hovered(SCREEN, char, player)
        else:
            char = ""

        start_button.hover_effect(mouse_pos)

        selecting_text.draw(SCREEN)
        start_button.draw(SCREEN)
        samurai_box.draw(SCREEN)
        mage_box.draw(SCREEN)
        fire_box.draw(SCREEN)
        vampire_box.draw(SCREEN)
        text.draw(SCREEN)

        # This will draw the Character for player 1 on the left
        draw_char_player1(SCREEN, select_p1, select_p2)

        # Draw the stats
        draw_stats(SCREEN,select_p1, select_p2)

        # this will blit the images into the boxes
        SCREEN.blit(samurai_img, samurai_box)
        SCREEN.blit(mage_img, mage_box)
        SCREEN.blit(fire_img, fire_box)
        SCREEN.blit(vampire_img, vampire_box)
        
        
        pygame.display.update()

def gameover_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings, player):
    """! Creates a Gameover menu

    @param scale_width_factor   The scaling factor for the width
    @param scale_height_factor  The scaling factor for the height
    @param dest_gameloop        The main game loop
    @param settings             The Keybinds that are saved in settings.txt
    @param player               An Integer for the players
    """
    global player1, player2, reset
    reset = True

    who_won_text = Button(0,0,250,80,transparent,f"{player} won!","black", font_scaled,scale_width_factor, scale_height_factor, None)
    who_won_text.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 - 250*scale_height_factor)

    play_button = Button(0,0,250,80,"black","PLAY AGAIN","White",font_scaled
                        ,scale_width_factor, scale_height_factor, lambda: play_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings))
    play_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2- 50*scale_height_factor)

    back_button = Button(0,0,300,80,"black","BACK TO LOBBY","white",font_scaled, scale_width_factor, scale_height_factor,
                                 lambda: main_menu(scale_width_factor, scale_height_factor, dest_gameloop, settings))
    back_button.rect.center = (MAIN_WIDTH/2, MAIN_HEIGHT/2 + 150*scale_height_factor)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play_button.handle_event(event)
                back_button.handle_event(event)

        mouse_position = pygame.mouse.get_pos()

        play_button.hover_effect(mouse_position)
        back_button.hover_effect(mouse_position)

        SCREEN.fill((255,255,255))
        
        play_button.draw(SCREEN)
        back_button.draw(SCREEN)
        who_won_text.draw(SCREEN)

        pygame.display.update()

