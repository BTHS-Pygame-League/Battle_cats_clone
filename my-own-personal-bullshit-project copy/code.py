import pygame
import pgzrun
import random
import time
import math
from pgzhelper import *

#constants
HEIGHT = 600
WIDTH = 600
CENTER_X = 300
CENTER_Y = 300
CENTER = (CENTER_X, CENTER_Y)



#menus, buttons, and icons
start_button = Actor("start_button")
start_button.pos = CENTER

lineup_button = Actor("lineup_button")
lineup_button.pos = (CENTER_X, CENTER_Y + 150)

upgrade_button = Actor("upgrade_button")
upgrade_button.pos = (CENTER_X, CENTER_Y - 150)


back_button = Actor("back_button")
back_button.pos = (70, 70)

pause_button = Actor("pause_button")
pause_button.pos = (70, 70)

danger_icon = Actor("danger_icon")
danger_icon.pos = (240, 70)

in_game_menu = Actor("in_game_menu")
in_game_menu.pos = (300, 300)

coins_box = Actor("coins_box")
coins_box.pos = (530, 70)
coins_box_outline = Rect(480, 53, 100, 67)

paper = Actor("paper")
paper.pos = (530, 50)
paper_amount_box = Rect(430, 25, 50, 50)
paper_owned = 0
paper_won_per_level = 0
paper_won_per_level_box = Rect(250, 400, 50, 50)

forward_arrow = Actor("forward_arrow")
forward_arrow.pos = (450, 530)
backward_arrow = Actor("back_arrow")
backward_arrow.pos = (150, 530)


#size of this is 166 by 112
back_to_game_button = Actor("back_to_game_button")
#move on the x 83 from the menu and on the y 64. Figured out using math and some guessing and checking.
back_to_game_button.pos = (217, 364)

back_to_main_menu_button = Actor("back_to_main_menu_button")
back_to_main_menu_button.pos = (383, 364)

level_frames = ["level_locked_icon", "level_fighting_icon", "level_completed_icon"]
level_buttons = []
level_one_button = Actor(level_frames[0])
level_one_button.pos = (185, 70)
level_buttons.append(level_one_button)
level_two_button = Actor(level_frames[0])
level_two_button.pos = (300, 70)
level_buttons.append(level_two_button)
level_three_button = Actor(level_frames[0])
level_three_button.pos = (415, 70)
level_buttons.append(level_three_button)
level_four_button = Actor(level_frames[0])
level_four_button.pos = (530, 70)
level_buttons.append(level_four_button)
level_five_button = Actor(level_frames[0])
level_five_button.pos = (70, 185)
level_buttons.append(level_five_button)
level_six_button = Actor(level_frames[0])
level_six_button.pos = (185, 185)
level_buttons.append(level_six_button)
level_seven_button = Actor(level_frames[0])
level_seven_button.pos = (300, 185)
level_buttons.append(level_seven_button)
level_eight_button = Actor(level_frames[0])
level_eight_button.pos = (415, 185)
level_buttons.append(level_eight_button)
level_nine_button = Actor(level_frames[0])
level_nine_button.pos = (530, 185)
level_buttons.append(level_nine_button)
level_ten_button = Actor(level_frames[0])
level_ten_button.pos = (70, 300)
level_buttons.append(level_ten_button)


#charecter icons
globy_icon = Actor("globy_icon")
globy_icon.equip_menu_mode = "Unselected"
globy_icon.slot = "none"
globy_icon.upgrade_cost = 400
globy_icon.level = 1
upgrade_globy_button = Actor("internal_upgrade_button")
globy_level_box = Rect(138, 365, 100, 100)
globy_upgrade_cost = Rect(253, 365, 100, 100)

ergam_icon = Actor("ergam_icon")
ergam_icon.equip_menu_mode = "Unselected"
ergam_icon.slot = "none"
ergam_icon.upgrade_cost = 500
ergam_icon.level = 1
upgrade_ergam_button = Actor("internal_upgrade_button")
ergam_level_box = Rect(138, 365, 100, 100)
ergam_upgrade_cost = Rect(253, 365, 100, 100)

zap_ball_icon = Actor("zap_ball_icon")
zap_ball_icon.equip_menu_mode = "Unselected"
zap_ball_icon.slot = "none"
zap_ball_icon.upgrade_cost = 600
zap_ball_icon.level = 1
upgrade_zap_ball_button = Actor("internal_upgrade_button")
zap_ball_level_box = Rect(138, 135, 100, 100)
zap_ball_upgrade_cost = Rect(253, 135, 100, 100)

zlumpy_icon = Actor("zlumpy_icon")
zlumpy_icon.equip_menu_mode = "Unselected"
zlumpy_icon.slot = "none"
zlumpy_icon.upgrade_cost = 450
zlumpy_icon.level = 1
upgrade_zlumpy_button = Actor("internal_upgrade_button")
zlumpy_level_box = Rect(138, 250, 100, 100)
zlumpy_upgrade_cost = Rect(253, 250, 100, 100)

guardo_icon = Actor("guardo_icon")
guardo_icon.equip_menu_mode = "Unselected"
guardo_icon.slot = "none"
guardo_icon.upgrade_cost = 750
guardo_icon.level = 1
upgrade_guardo_button = Actor("internal_upgrade_button")
guardo_level_box = Rect(138, 365, 100, 100)
guardo_upgrade_cost = Rect(253, 365, 100, 100)

#other miscilaneous upgrade icons
money_generation_speed_icon = Actor("money_generation_speed_icon")
money_generation_speed_icon.level = 1
money_generation_speed_icon.upgrade_cost = 1000
upgrade_money_generation_speed_button = Actor("internal_upgrade_button")
money_generation_speed_level_box = Rect(138, 135, 100, 100)
money_generation_speed_upgrade_cost = Rect(253, 135, 100, 100)

enemy_death_money_icon = Actor("enemy_death_money_icon")
enemy_death_money_icon.level = 1
enemy_death_money_icon.upgrade_cost = 1000
upgrade_enemy_death_money_button = Actor("internal_upgrade_button")
enemy_death_money_level_box = Rect(138, 250, 100, 100)
enemy_death_money_upgrade_cost = Rect(253, 250, 100, 100)

base_health_icon = Actor("base_health_icon")
base_health_icon.level = 1
base_health_icon.upgrade_cost = 1000
upgrade_base_health_button = Actor("internal_upgrade_button")
base_health_level_box = Rect(138, 135, 100, 100)
base_health_upgrade_cost = Rect(253, 135, 100, 100)

paper_per_level_icon = Actor("paper_per_level_icon")
paper_per_level_icon.level = 1
paper_per_level_icon.upgrade_cost = 1000
upgrade_paper_per_level_button = Actor("internal_upgrade_button")
paper_per_level_level_box = Rect(138, 250, 100, 100)
paper_per_level_upgrade_cost = Rect(253, 250, 100, 100)


lineup = []
empty_slot_1 = Actor("empty_icon_spot")
empty_slot_1.taken = False
lineup.append(empty_slot_1)
empty_slot_2 = Actor("empty_icon_spot")
empty_slot_2.taken = False
lineup.append(empty_slot_1)
empty_slot_3 = Actor("empty_icon_spot")
empty_slot_3.taken = False
lineup.append(empty_slot_1)
empty_slot_4 = Actor("empty_icon_spot")
empty_slot_4.taken = False
lineup.append(empty_slot_1)
empty_slot_5 = Actor("empty_icon_spot")
empty_slot_5.taken = False
lineup.append(empty_slot_1)

#bases
starting_base = Actor("starting_base")
starting_base.pos = (530, 360)
starting_base.health = 1000
your_bases = []
your_bases.append(starting_base)
your_base_health_box = Actor("base_health")
your_base_health_box.pos = (530, 185)
your_base_health_box_outline = Rect(480, 160, 100, 73)
equiped_base = 0

level_one_enemy_base = Actor("level_1_enemy_base")
level_one_enemy_base.pos = (70, 360)
enemy_bases = []
enemy_bases.append(level_one_enemy_base)
level_two_enemy_base = Actor("level_2_enemy_base")
level_two_enemy_base.pos = (69, 360)
enemy_bases.append(level_two_enemy_base)
level_three_and_four_enemy_base = Actor("level_3_and_4_enemy_base")
level_three_and_four_enemy_base.pos = (69, 360)
enemy_bases.append(level_three_and_four_enemy_base)
level_five_and_six_enemy_base = Actor("level_5_and_6_enemy_base")
level_five_and_six_enemy_base.pos = (69, 360)
enemy_bases.append(level_five_and_six_enemy_base)


#level states

victory_screen = Rect(100, 100, 400, 400)
game_over_screen = Rect(100, 100, 400, 400)

#level_one = Actor("void_object")
#level_one.completion_status = "Incomplete"
#level_one.time_between_spawns = random.randint(600, 800)


level_one = object()
level_one_time_between_spawns = random.randint(600, 800)
level_two = object()
level_two_blaze_bot_time_between_spawns = random.randint(300, 600)
level_two_scorium_slug_time_between_spawns = random.randint(700, 900)
level_three = object()
level_three_blaze_bot_time_between_spawns = random.randint(200, 400)
level_three_scorium_slug_time_between_spawns = random.randint(500, 700)
level_three_crying_magnum_time_between_spawns = random.randint(1000, 1200)
level_four = object()
level_four_blaze_bot_time_between_spawns = random.randint(100, 300)
level_four_scorium_slug_time_between_spawns = random.randint(400, 600)
level_four_crying_magnum_time_between_spawns = random.randint(700, 900)
level_five = object()
level_five_blaze_bot_time_between_waves = 1000
level_five_blaze_bot_time_between_spawns = 50
level_five_blaze_bot_amount_per_wave = 3
level_five_crying_magnum_time_between_spawns = random.randint(950, 1050)
level_six = object()
level_six_blaze_bot_time_between_waves = 1200
level_six_blaze_bot_time_between_spawns = 50
level_six_blaze_bot_amount_per_wave = 4
level_six_scorium_slug_time_between_waves = 1300
level_six_scorium_slug_time_between_spawns = 70
level_six_scorium_slug_amount_per_wave = 3
level_seven = object()
level_seven_blaze_bot_time_between_spawns = random.randint(200, 340)
level_seven_crying_magnum_time_between_waves = 1800
level_seven_crying_magnum_time_between_spawns = 120
level_seven_crying_magnum_amount_per_wave = 2
level_eight = object()
level_eight_scorium_slug_time_between_spawns = random.randint(200, 340)
level_eight_danger_blaze_bot_time_between_spawns = 30
level_eight_danger_blaze_bot_amount = 20
level_eight_danger_crying_magnum_time_between_spawns = 75
level_eight_danger_crying_magnum_amount = 8
level_nine = object()
level_nine_scorium_slug_time_between_waves = 400
level_nine_scorium_slug_time_between_spawns = 50
level_nine_scorium_slug_amount_per_wave = 2
level_nine_blaze_bot_time_between_spawns = random.randint(100, 140)
level_nine_crying_magnum_time_between_spawns = random.randint(400, 440)
level_ten = object()
level_ten_blaze_bot_time_between_spawns = 0
level_ten_scorium_slug_time_between_spawns = 300
level_ten_crying_magnum_time_between_spawns = 600
level_eleven = object()
level_eleven_blaze_bot_time_between_spawns = 100
level_twelve = object()
level_twelve_blaze_bot_time_between_spawns = 100
level_thirteen = object()
level_thirteen_blaze_bot_time_between_spawns = 100
level_fourteen = object()
level_fourteen_blaze_bot_time_between_spawns = 100
level_fifteen = object()
level_fifteen_blaze_bot_time_between_spawns = 100


levels = [ [level_one, "Unlocked", "Incomplete", [1, level_one_time_between_spawns], 1000, 1000],
           
           [level_two, "Locked", "Incomplete",
            [
                [1, level_two_blaze_bot_time_between_spawns],
                [1, level_two_scorium_slug_time_between_spawns]
            ],
            1500, 1100],
           
           [level_three, "Locked", "Incomplete",
            [
                [1, level_three_blaze_bot_time_between_spawns],
                [1, level_three_scorium_slug_time_between_spawns],
                [1, level_three_crying_magnum_time_between_spawns]
            ],
            2000, 1300],
           
           [level_four, "Locked", "Incomplete",
            [
                [1, level_four_blaze_bot_time_between_spawns],
                [1, level_four_scorium_slug_time_between_spawns],
                [1, level_four_crying_magnum_time_between_spawns]
            ],
            3000, 1500],

           [level_five, "Locked", "Incomplete",
            [
                [1, level_five_blaze_bot_time_between_waves, level_five_blaze_bot_time_between_spawns, level_five_blaze_bot_amount_per_wave],
                [1, level_five_crying_magnum_time_between_spawns]
            ],
            5000, 1800],

           [level_six, "Locked", "Incomplete",
            [
                [1.5, level_six_blaze_bot_time_between_waves, level_six_blaze_bot_time_between_spawns, level_six_blaze_bot_amount_per_wave],
                [1, level_six_scorium_slug_time_between_waves, level_six_scorium_slug_time_between_spawns, level_six_scorium_slug_amount_per_wave]
            ],
            7500, 2100],
           
           [level_seven, "Locked", "Incomplete",
            [
                [1.25, level_seven_blaze_bot_time_between_spawns],
                [1, level_seven_crying_magnum_time_between_waves, level_seven_crying_magnum_time_between_spawns, level_seven_crying_magnum_amount_per_wave]
            ],
            10000, 2400],
           [level_eight, "Locked", "Incomplete",
            [
                [1, level_eight_scorium_slug_time_between_spawns],
                [
                    ["DANGER", "Deactivated"],
                    [1, level_eight_danger_blaze_bot_time_between_spawns, level_eight_danger_blaze_bot_amount],
                    [1, level_eight_danger_crying_magnum_time_between_spawns, level_eight_danger_crying_magnum_amount]
                ]
            ],
            12000, 2700],
           [level_nine, "Locked", "Incomplete",
            [
                [1.5, level_nine_blaze_bot_time_between_spawns],
                [3, level_nine_scorium_slug_time_between_waves, level_nine_scorium_slug_time_between_spawns, level_nine_scorium_slug_amount_per_wave],
                [1.25, level_nine_crying_magnum_time_between_spawns]
            ],
            15000, 3000],

           [level_ten, "Locked", "Incomplete",
            [
                [3, level_ten_blaze_bot_time_between_spawns],
                [5, level_ten_scorium_slug_time_between_spawns],
                [2, level_ten_crying_magnum_time_between_spawns],
                [
                    ["BOSS", "Deactivated"],
                    [1, "magma_turtle"]
                ]
            ],
            17500, 3500],
           [level_eleven, "Locked", "Incomplete",
            [
                [0.1, level_eleven_blaze_bot_time_between_spawns],
                [
                   ["BOSS", "Deactivated"],
                   [10, "blaze_bot"]
                ]
            ],
            10000, 2000],
           [level_twelve, "Locked", "Incomplete", level_twelve_blaze_bot_time_between_spawns],
           [level_thirteen, "Locked", "Incomplete", level_thirteen_blaze_bot_time_between_spawns],
           [level_fourteen, "Locked", "Incomplete", level_fourteen_blaze_bot_time_between_spawns],
           [level_fifteen, "Locked", "Incomplete", level_fifteen_blaze_bot_time_between_spawns]
           ]

enemy_base_health_box = Actor("base_health")
enemy_base_health_box.pos = (70, 185)
enemy_base_health_box_outline = Rect(20, 160, 100, 73)

#levels[0].append(level_one_time_between_spawns)


#your troops and their projectiles
globies = []
globy_frames = ["globy_movement_frame_1", "globy_movement_frame_2", "globy_battle_frame"]
globy_projectiles = []

ergams = []
ergam_frames = ["ergam_frame_1", "ergam_frame_2", "ergam_frame_3", "ergam_frame_4"]

zap_balls = []
zap_ball_frames = ["zap_ball_frame_1", "zap_ball_frame_2", "zap_ball_frame_3", "zap_ball_frame_4"]

zlumpies = []
zlumpy_frames = ["zlumpy_frame_1", "zlumpy_frame_2", "zlumpy_frame_3"]
zlumpy_projectiles = []

guardos = []
guardo_frames = ["guardo_movement_frame_1", "guardo_movement_frame_2",
                       "guardo_battle_frame_1", "guardo_battle_frame_2", "guardo_battle_frame_3", "guardo_battle_frame_4" ]
guardo_projectiles = []


#your enemies' troops and their projectiles
blaze_bots = []
blaze_bot_projectiles = []
scorium_slugs = []
scorium_slug_frames = ["scorium_slug_frame_1", "scorium_slug_frame_2"]
scorium_slug_projectiles = []
crying_magnums = []
crying_magnum_frames = ["crying_magnum_frame_1", "crying_magnum_frame_2", "crying_magnum_frame_3", "crying_magnum_frame_4"]
crying_magnum_projectiles = []
magma_turtles = []
magma_turtle_frames = ["magma_turtle_movement_frame_1", "magma_turtle_movement_frame_2", "magma_turtle_movement_frame_3", "magma_turtle_movement_frame_4",
                       "magma_turtle_battle_frame_1", "magma_turtle_battle_frame_2", "magma_turtle_battle_frame_3", "magma_turtle_battle_frame_4" ]
magma_turtle_projectiles = []
magma_turtle_projectile_frames = ["magma_turtle_projectile_frame_1", "magma_turtle_projectile_frame_2", "magma_turtle_projectile_frame_3", "magma_turtle_projectile_frame_4"]

#class enemy_base:

#globals
game_state = "Start Screen"
level_state = "Playing"
upgrade_menu_page = 1
upgrade_menu_page_max = 2
coins = 0
coin_delay = 4
bonus_coin_delay = (16 - (money_generation_speed_icon.level - 1) )
DANGER = False
BOSS = False

def add_one_coin():
    global coins
    global coin_delay
    global bonus_coin_delay
    if coin_delay <= 0:
        coins += 1
        coin_delay = 4
        """
    elif money_generation_speed_icon.level == 10:
        coin_delay -= 4000
        """
    else:
        coin_delay -= 1# + (333 * (money_generation_speed_icon.level - 1))
        #print(coin_delay)
        
    if bonus_coin_delay <= 0 and money_generation_speed_icon.level > 1:
        coins += 1
        bonus_coin_delay = (16 - (money_generation_speed_icon.level - 1) )
        #print(bonus_coin_delay)
        #print(money_generation_speed_icon.level)
    else:
        if money_generation_speed_icon.level > 1:
            bonus_coin_delay -= 1
            #print(bonus_coin_delay)


#Behavior of all of your troops
        #All of the Globy Behaviors
def globy_skin_change():

    for globy in globies:
        #print(globy.skin_change_time)
        if globy.mode == "Moving":
            
            if globy.image == globy_frames[2]:
                globy.image = globy_frames[0]
                

            if globy.skin_change_time <= 0:
                    
                if globy.image == globy_frames[0]:
                    #print("the frame is indeed zero")
                    globy.image = globy_frames[1]
                    globy.skin_change_time = 50
                    #print("changed skins")
                        
                elif globy.image == globy_frames[1]:
                    #print("The Frame Is Indeed One")
                    globy.image = globy_frames[0]
                    globy.skin_change_time = 50
                    #print("changed skins")

            else:
                globy.skin_change_time -= 1

        if globy.mode == "Fighting":
            globy.image = globy_frames[2]
        
def globy_behavior():
    globy_skin_change()
    
    for globy in globies:
        if globy.health <= 0:
            globies.remove(globy)

        globy.near_blaze_bot = False
        globy.near_scorium_slug = False
        globy.near_crying_magnum = False
        globy.near_magma_turtle = False
        globy.near_base = False

        for base in enemy_bases:
            if globy.x - base.x <= random.randint(114, 116):
                globy.near_base = True
                break
            else:
                globy.near_base = False

        for blaze_bot in blaze_bots:
            if globy.x - blaze_bot.x <= random.randint(114, 116):
                globy.near_blaze_bot = True
                break
            else:
                globy.near_blaze_bot = False

        for scorium_slug in scorium_slugs:
            if globy.x - scorium_slug.x <= random.randint(114, 116):
                globy.near_scorium_slug = True
                break
            else:
                globy.near_scorium_slug = False

        for crying_magnum in crying_magnums:
            if globy.x - crying_magnum.x <= random.randint(114, 116):
                globy.near_crying_magnum = True
                break
            else:
                globy.near_crying_magnum = False

        for magma_turtle in magma_turtles:
            if globy.x - magma_turtle.x <= random.randint(174, 176):
                globy.near_magma_turtle = True
                break
            else:
                globy.near_magma_turtle = False

        if globy.near_base or globy.near_blaze_bot or globy.near_scorium_slug or globy.near_crying_magnum or globy.near_magma_turtle:
            if globy.mode != "Being Knocked Back":
                globy.mode = "Fighting"

        elif not globy.near_base and not globy.near_blaze_bot and not globy.near_scorium_slug and not globy.near_crying_magnum and not globy.near_magma_turtle:
            if globy.mode != "Being Knocked Back":
                globy.mode = "Moving"
            
        
        if globy.mode == "Moving":
            globy.x -= 0.5
                    

        if globy.mode == "Fighting":
            globy_attack()

        if globy.mode == "Being Knocked Back":
            globy.x += 5
            globy.knock_back_distance -= 5

            if globy.knock_back_distance <= 0:
                globy.mode = "Moving"

        
            
            """
            for base in enemy_bases:
                    
                if globy.x - base.x <= random.randint(114, 116):
                    if globy.can_move == True:
                        globy.can_move = False
                        break
                    if globy.can_move == False:
                        break

            for blaze_bot in blaze_bots:

                if globy.x - blaze_bot.x <= random.randint(114, 116):

                    if globy.can_move == True:
                        globy.can_move = False
                        break
                    if globy.can_move == False:
                        break

            for scorium_slug in scorium_slugs:
                
                if globy.x - scorium_slug.x <= random.randint(114, 116):

                    if globy.can_move == True:
                        globy.can_move = False
                        break
                    if globy.can_move == False:
                        break

            for crying_magnum in crying_magnums:

                if globy.x - crying_magnum.x <= random.randint(114, 116):

                    if globy.can_move == True:
                        globy.can_move = False
                        break
                    if globy.can_move == False:
                        break

            #if globy.can_move == False:
                #print("false")

            for blaze_bot in blaze_bots:
                print("in blaze bots")
                        
                if globy.x - blaze_bot.x >= random.randint(114, 116):
                    print("checking distance to blaze bots")
                            
                else:
                    break

                    for scorium_slug in scorium_slugs:
                        print("in scorium slugs")
                                    
                        if globy.x - scorium_slug.x >= random.randint(114, 116):
                            print("checking distance to scorium slugs")

                        else:
                            break

                            for crying_magnum in crying_magnums:
                                print("in crying magnums")
                                                
                                if globy.x - crying_magnum.x >= random.randint(114, 116):
                                    print("checking distance to crying magnums")
                                    globy.can_move = True
                                    break
                                else:
                                    break
                    break
            break
"""

                    
                    
"""
                    for blaze_bot in blaze_bots:

                        for crying_magnum in crying_magnums:

                            for scorium_slug in scorium_slugs:


                                if globy.x - scorium_slug.x <= random.randint(114, 116):
                                    globy.mode = "Fighting"
                                    break


                                elif globy.x - scorium_slug.x >= random.randint(114, 116):
                                    break
                                    

                            if globy.x - crying_magnum.x <= random.randint(114, 116):
                                globy.mode = "Fighting"
                                break
                            
                            elif globy.x - crying_magnum.x >= random.randint(114, 116):
                                break
                            
                            
                        if globy.x - blaze_bot.x <= random.randint(114, 116):
                            globy.mode = "Fighting"
                            break
                        
                        elif globy.x - blaze_bot.x >= random.randint(114, 116):
                            globy.mode = "Moving"
"""

def summon_globy():
    global coins
    coins -= 50
    globy = Actor(globy_frames[0])
    globy.index = 0
    globy.mode = "Moving"
    globy.can_move = False
    globy.y = random.randint(409, 411)
    globy.pos = (530, globy.y)
    globy.skin_change_time = 50
    globy.time_between_attacks = 50
    globy.health = int(160 + ( (globy_icon.level - 1) * 20) )
    #print(globy.health)
    globies.append(globy)

def globy_attack():
    
    for globy in globies:

        if globy.mode == "Fighting":
            #print("We are attacking")
            #print(globy.time_between_attacks)
            
            if globy.time_between_attacks <= 0:
                create_globy_projectile(globy.x, globy.y)
                globy.time_between_attacks = 50

            else:
                globy.time_between_attacks -= 1

        else:
            pass


    #globy_projectile behaviors
def globy_projectile_behavior():
    global game_state

    for globy_projectile in globy_projectiles:
        #globy_projectile.range = 100
        #print(projectile.range)

        #while globy_projectile.range > 0:
            #print(globy_projectile.range)
        globy_projectile.x -= 1
        globy_projectile.range -= 1

        for base in enemy_bases:
            
            if globy_projectile.colliderect(base):
                
                if game_state == "Level 1":

                    levels[0][4] -= globy_projectile.damage
                    #print("collided with 1")
                    globy_projectile.delete = True
                    break

                if game_state == "Level 2":
                    #print("Game State is 2")
                    levels[1][4] -= globy_projectile.damage
                    #print(levels[1][4])
                    #print("collided with 2")
                    globy_projectile.delete = True
                    break
                    #pass
                
                if game_state == "Level 3":
                    levels[2][4] -= globy_projectile.damage
                    globy_projectile.delete = True
                    break

                if game_state == "Level 4":
                    levels[3][4] -= globy_projectile.damage
                    globy_projectile.delete = True
                    break

                if game_state == "Level 5":
                    levels[4][4] -= globy_projectile.damage
                    globy_projectile.delete = True
                    break
                if game_state == "Level 6":
                    levels[5][4] -= globy_projectile.damage
                    globy_projectile.delete = True
                    break
                if game_state == "Level 7":
                    levels[6][4] -= globy_projectile.damage
                    globy_projectile.delete = True
                    break
                if game_state == "Level 8":
                    levels[7][4] -= globy_projectile.damage
                    globy_projectile.delete = True
                    break
                if game_state == "Level 9":
                    levels[8][4] -= globy_projectile.damage
                    globy_projectile.delete = True
                    break
                if game_state == "Level 10":
                    levels[9][4] -= globy_projectile.damage
                    globy_projectile.delete = True
                    break


        for blaze_bot in blaze_bots:
            if globy_projectile.colliderect(blaze_bot):
                globy_projectile.delete = True
                blaze_bot.health -= globy_projectile.damage
                break

        for scorium_slug in scorium_slugs:
            if globy_projectile.colliderect(scorium_slug):
                globy_projectile.delete = True
                scorium_slug.health -= globy_projectile.damage
                break
                    #pass

        for crying_magnum in crying_magnums:
            if globy_projectile.colliderect(crying_magnum):
                globy_projectile.delete = True
                crying_magnum.health -= globy_projectile.damage
                break

        for magma_turtle in magma_turtles:
            if globy_projectile.colliderect(magma_turtle):
                globy_projectile.delete = True
                magma_turtle.health -= globy_projectile.damage
                break
                
        if globy_projectile.delete == True:
            #print("broken")
            globy_projectiles.remove(globy_projectile)
            break

        if globy_projectile.range <= 0:
            globy_projectiles.remove(globy_projectile)
            #print("removed projectile")
        
        
def create_globy_projectile(x, y):
    globy_projectile = Actor("globy_projectile")
    globy_projectile.x = x - 20
    globy_projectile.y = y + 30
    globy_projectile.delete = False
    globy_projectile.damage = int(22 + ( (globy_icon.level - 1) * 4) )
    #print(globy_projectile.damage)
    globy_projectile.range = 80
    globy_projectiles.append(globy_projectile)
    #print("Created projectile.")

    # all of the argom behaviors
def summon_ergam():
    global coins
    coins -= 150
    ergam = Actor(ergam_frames[0])
    ergam.scale = 1.25
    ergam.index = 0
    ergam.mode = "Charging"
    ergam.collided = "False"
    ergam.y = random.randint(409, 411)
    ergam.pos = (530, ergam.y)
    ergam.skin_change_time = 5
    ergam.time_between_attacks = 200
    ergam.damage = int(100 + ( (ergam_icon.level - 1) * 10) )
    #print(ergam.damage)
    ergam.bonus_charge_damage = int(40 + ( ( ergam_icon.level - 1 ) * 2 ) )
    print(ergam.bonus_charge_damage)
    ergam.health = int(640 + ( ( ergam_icon.level - 1) * 20) )
    ergam.has_hit_base_with_bonus_charge = False
    #print(ergam.health)
    ergams.append(ergam)

def ergam_skin_change():

    for ergam in ergams:
        #print(globy.skin_change_time)
        if ergam.mode == "Resting":
            
            if ergam.image == ergam_frames[1] or ergam.image == ergam_frames[3]:
                ergam.image = ergam_frames[0]

        if ergam.mode == "Charging":
                

            if ergam.skin_change_time <= 0:
                    
                if ergam.image == ergam_frames[0]:
                    #print("the frame is indeed zero")
                    ergam.image = ergam_frames[1]
                    ergam.skin_change_time = 10
                    #print("changed skins")
                        
                elif ergam.image == ergam_frames[1]:
                    #print("The Frame Is Indeed One")
                    ergam.image = ergam_frames[2]
                    ergam.skin_change_time = 10
                    #print("changed skins")

                elif ergam.image == ergam_frames[2]:
                    #print("The Frame Is Indeed One")
                    ergam.image = ergam_frames[3]
                    ergam.skin_change_time = 10
                    #print("changed skins")

                elif ergam.image == ergam_frames[3]:
                    #print("The Frame Is Indeed One")
                    ergam.image = ergam_frames[0]
                    ergam.skin_change_time = 10
                    #print("changed skins")

            else:
                ergam.skin_change_time -= 1

        
def ergam_behavior():
    ergam_skin_change()
    
    
    for ergam in ergams:
        if ergam.health <= 0:
            ergams.remove(ergam)
        ergam.scale = 1.25
        #print(ergam.mode)

        if ergam.mode == "Bonus Charge":
            ergam.x -= 5
            ergam.bonus_charge_distance -= 5
            for base in enemy_bases:
                if base.colliderect(ergam):
                    if ergam.has_hit_base_with_bonus_charge == False:
                        if game_state == "Level 1":
                            levels[0][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True
                        if game_state == "Level 2":
                            levels[1][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True
                        if game_state == "Level 3":
                            levels[2][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True
                        if game_state == "Level 4":
                            levels[3][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True
                        if game_state == "Level 5":
                            levels[4][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True
                        if game_state == "Level 6":
                            levels[5][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True
                        if game_state == "Level 7":
                            levels[6][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True
                        if game_state == "Level 8":
                            levels[7][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True
                        if game_state == "Level 9":
                            levels[8][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True
                        if game_state == "Level 10":
                            levels[9][4] -= ergam.bonus_charge_damage
                            ergam.has_hit_base_with_bonus_charge = True

            for blaze_bot in blaze_bots:
                if blaze_bot.has_been_hit_by_ergam_bonus_charge == False:
                    if blaze_bot.colliderect(ergam):
                        blaze_bot.mode = "Being Knocked Back"
                        blaze_bot.knock_back_distance = 50
                        blaze_bot.health -= ergam.bonus_charge_damage
                        blaze_bot.has_been_hit_by_ergam_bonus_charge = True
                    
            for scorium_slug in scorium_slugs:
                if scorium_slug.has_been_hit_by_ergam_bonus_charge == False:
                    if scorium_slug.colliderect(ergam):
                        scorium_slug.mode = "Being Knocked Back"
                        scorium_slug.knock_back_distance = 50
                        scorium_slug.health -= ergam.bonus_charge_damage
                        scorium_slug.has_been_hit_by_ergam_bonus_charge = True

            for crying_magnum in crying_magnums:
                if crying_magnum.has_been_hit_by_ergam_bonus_charge == False:
                    if crying_magnum.colliderect(ergam):
                        crying_magnum.mode = "Being Knocked Back"
                        crying_magnum.knock_back_distance = 50
                        crying_magnum.health -= ergam.bonus_charge_damage
                        crying_magnum.has_been_hit_by_ergam_bonus_charge = True

            for magma_turtle in magma_turtles:
                if magma_turtle.has_been_hit_by_ergam_bonus_charge == False:
                    if magma_turtle.colliderect(ergam):
                        magma_turtle.mode = "Being Knocked Back"
                        magma_turtle.knock_back_distance = 50
                        magma_turtle.health -= ergam.bonus_charge_damage
                        magma_turtle.has_been_hit_by_ergam_bonus_charge = True

            if ergam.bonus_charge_distance <= 0:
                ergam.mode = "Recoiling"
                ergam.recoil_distance = 75
                for blaze_bot in blaze_bots:
                    blaze_bot.has_been_hit_by_ergam = False
                    blaze_bot.has_been_hit_by_ergam_bonus_charge = False
                for scorium_slug in scorium_slugs:
                    scorium_slug.has_been_hit_by_ergam = False
                    scorium_slug.has_been_hit_by_ergam_bonus_charge = False
                for crying_magnum in crying_magnums:
                    crying_magnum.has_been_hit_by_ergam = False
                    crying_magnum.has_been_hit_by_ergam_bonus_charge = False
                for magma_turtle in magma_turtles:
                    magma_turtle.has_been_hit_by_ergam = False
                    magma_turtle.has_been_hit_by_ergam_bonus_charge = False

        if ergam.mode == "Recoiling":
            ergam.x += 5
            ergam.recoil_distance -= 5
            if ergam.recoil_distance <= 0:
                ergam.mode = "Resting"

        if ergam.mode == "Resting":
            ergam.time_between_attacks -= 1

            if ergam.time_between_attacks <= 0:
                ergam.mode = "Charging"
                ergam.collided = "False"
                ergam.has_hit_base_with_bonus_charge = False
                    

        if ergam.mode == "Charging":
            ergam.x -= 1

            for base in enemy_bases:
                if base.colliderect(ergam):
                    ergam.collided = "True"
                    
                    if game_state == "Level 1":
                        levels[0][4] -= ergam.damage
                    if game_state == "Level 2":
                        levels[1][4] -= ergam.damage
                    if game_state == "Level 3":
                        levels[2][4] -= ergam.damage
                    if game_state == "Level 4":
                        levels[3][4] -= ergam.damage
                    if game_state == "Level 5":
                        levels[4][4] -= ergam.damage
                    if game_state == "Level 6":
                        levels[5][4] -= ergam.damage
                    if game_state == "Level 7":
                        levels[6][4] -= ergam.damage
                    if game_state == "Level 8":
                        levels[7][4] -= ergam.damage
                    if game_state == "Level 9":
                        levels[8][4] -= ergam.damage
                    if game_state == "Level 10":
                        levels[9][4] -= ergam.damage

            for blaze_bot in blaze_bots:
                if blaze_bot.colliderect(ergam):
                    if blaze_bot.has_been_hit_by_ergam == False:
                        blaze_bot.mode = "Being Knocked Back"
                        blaze_bot.knock_back_distance = 50
                        blaze_bot.health -= ergam.damage
                        blaze_bot.has_been_hit_by_ergam = True
                        ergam.collided = "True"
                    
            for scorium_slug in scorium_slugs:
                if scorium_slug.colliderect(ergam):
                    if scorium_slug.has_been_hit_by_ergam == False:
                        scorium_slug.mode = "Being Knocked Back"
                        scorium_slug.knock_back_distance = 50
                        scorium_slug.health -= ergam.damage
                        scorium_slug.has_been_hit_by_ergam = True
                        ergam.collided = "True"

            for crying_magnum in crying_magnums:
                if crying_magnum.colliderect(ergam):
                    if crying_magnum.has_been_hit_by_ergam == False:
                        crying_magnum.mode = "Being Knocked Back"
                        crying_magnum.knock_back_distance = 50
                        crying_magnum.health -= ergam.damage
                        crying_magnum.has_been_hit_by_ergam = True
                        ergam.collided = "True"

            for magma_turtle in magma_turtles:
                if magma_turtle.colliderect(ergam):
                    if magma_turtle.has_been_hit_by_ergam == False:
                        magma_turtle.mode = "Being Knocked Back"
                        magma_turtle.knock_back_distance = 50
                        magma_turtle.health -= ergam.damage
                        magma_turtle.has_been_hit_by_ergam = True
                        ergam.collided = "True"

        if ergam.mode == "Being Knocked Back":
            ergam.x += 5
            ergam.knock_back_distance -= 5

            if ergam.knock_back_distance <= 0:
                ergam.mode = "Charging"

        if ergam.collided == "True":
            ergam.time_between_attacks = 200
            ergam.mode = "Bonus Charge"
            ergam.bonus_charge_distance = 25
            ergam.collided = "False"

#all zap ball behaviors
def summon_zap_ball():
    global coins
    coins -= 200
    zap_ball = Actor(zap_ball_frames[0])
    zap_ball.index = 0
    zap_ball.mode = "Moving"
    zap_ball.collided = False
    zap_ball.y = random.randint(409, 411)
    zap_ball.pos = (530, zap_ball.y)
    zap_ball.speed = 2
    zap_ball.original_division_shield = zap_ball_icon.level
    zap_ball.division_shield = zap_ball_icon.level
    zap_ball.skin_change_time = 100
    zap_ball.damage = int(20 + ( (zap_ball_icon.level - 1) * 4) )
    zap_ball.health = int(180 + ( (zap_ball_icon.level - 1) * 10) )
    zap_ball.has_hit_base = False
    zap_ball.stun_duration = int(200 + ( (zap_ball_icon.level - 1) * 50) )
    zap_balls.append(zap_ball)

def zap_ball_behavior():  
    for zap_ball in zap_balls:
        #print(zap_ball.mode)
        if zap_ball.health <= 0:
            zap_balls.remove(zap_ball)

        if zap_ball.mode == "Moving":
            zap_ball.division_shield = 1
            zap_ball.x -= zap_ball.speed

            for blaze_bot in blaze_bots:
                if blaze_bot.colliderect(zap_ball):
                    zap_ball.collided = True

            for scorium_slug in scorium_slugs:
                if scorium_slug.colliderect(zap_ball):
                    zap_ball.collided = True

            for crying_magnum in crying_magnums:
                if crying_magnum.colliderect(zap_ball):
                    zap_ball.collided = True

            for magma_turtle in magma_turtles:
                if magma_turtle.colliderect(zap_ball):
                    zap_ball.collided = True

            for base in enemy_bases:
                if base.colliderect(zap_ball):
                    zap_ball.collided = "True"

            if zap_ball.collided:
                zap_ball.mode = "Exploding"

        if zap_ball.mode == "Exploding":
            zap_ball.division_shield = zap_ball.original_division_shield
            if zap_ball.image == zap_ball_frames[0]:
                zap_ball.image = zap_ball_frames[1]

            if zap_ball.image == zap_ball_frames[1]:
                if zap_ball.skin_change_time >= 0:
                    zap_ball.x -= 0.2
                    zap_ball.y = random.randint(409, 411)
                    zap_ball.skin_change_time -= 1
                else:
                    zap_ball.image = zap_ball_frames[2]
                    zap_ball.x -= 20
                    zap_ball.skin_change_time = 100

            if zap_ball.image == zap_ball_frames[2]:
                if zap_ball.skin_change_time <= 0:
                    zap_ball.health = 0
                    for blaze_bot in blaze_bots:
                        blaze_bot.has_been_hit_by_zap_ball = False
                    for scorium_slug in scorium_slugs:
                        scorium_slug.has_been_hit_by_zap_ball = False
                    for crying_magnum in crying_magnums:
                        crying_magnum.has_been_hit_by_zap_ball = False
                    for magma_turtle in magma_turtles:
                        magma_turtle.has_been_hit_by_zap_ball = False
                else:
                    zap_ball.skin_change_time -= 1

                for blaze_bot in blaze_bots:
                    if blaze_bot.has_been_hit_by_zap_ball == False:
                        if blaze_bot.colliderect(zap_ball):
                            blaze_bot.health -= zap_ball.damage
                            blaze_bot.has_been_hit_by_zap_ball = True
                            blaze_bot.mode = "Stunned"
                            blaze_bot.time_stunned = zap_ball.stun_duration
                for scorium_slug in scorium_slugs:
                    if scorium_slug.colliderect(zap_ball):
                        if scorium_slug.has_been_hit_by_zap_ball == False:
                            scorium_slug.health -= zap_ball.damage
                            scorium_slug.has_been_hit_by_zap_ball = True
                            scorium_slug.mode = "Stunned"
                            scorium_slug.time_stunned = zap_ball.stun_duration
                for crying_magnum in crying_magnums:
                    if crying_magnum.colliderect(zap_ball):
                        if crying_magnum.has_been_hit_by_zap_ball == False:
                            crying_magnum.health -= zap_ball.damage
                            crying_magnum.has_been_hit_by_zap_ball = True
                            crying_magnum.mode = "Stunned"
                            crying_magnum.time_stunned = zap_ball.stun_duration
                for magma_turtle in magma_turtles:
                    if magma_turtle.colliderect(zap_ball):
                        if magma_turtle.has_been_hit_by_zap_ball == False:
                            magma_turtle.health -= zap_ball.damage
                            magma_turtle.has_been_hit_by_zap_ball = True
                            magma_turtle.mode = "Stunned"
                            magma_turtle.time_stunned = zap_ball.stun_duration
                for base in enemy_bases:
                    if base.colliderect(zap_ball):
                        if zap_ball.has_hit_base == False:
                            zap_ball.has_hit_base = True
                            if game_state == "Level 1":
                                levels[0][4] -= zap_ball.damage
                            if game_state == "Level 2":
                                levels[1][4] -= zap_ball.damage
                            if game_state == "Level 3":
                                levels[2][4] -= zap_ball.damage
                            if game_state == "Level 4":
                                levels[3][4] -= zap_ball.damage
                            if game_state == "Level 5":
                                levels[4][4] -= zap_ball.damage
                            if game_state == "Level 6":
                                levels[5][4] -= zap_ball.damage
                            if game_state == "Level 7":
                                levels[6][4] -= zap_ball.damage
                            if game_state == "Level 8":
                                levels[7][4] -= zap_ball.damage
                            if game_state == "Level 9":
                                levels[8][4] -= zap_ball.damage
                            if game_state == "Level 10":
                                levels[9][4] -= zap_ball.damage

# All Zlumpy Behaviors
def zlumpy_skin_change():

    for zlumpy in zlumpies:
        if zlumpy.mode == "Moving":
            if zlumpy.image == zlumpy_frames[2]:
                zlumpy.image = zlumpy_frames[0]
                

            if zlumpy.skin_change_time <= 0:
                    
                if zlumpy.image == zlumpy_frames[0]:
                    zlumpy.image = zlumpy_frames[1]
                    zlumpy.y = random.randint(419, 421)
                    zlumpy.skin_change_time = 50
                        
                elif zlumpy.image == zlumpy_frames[1]:
                    zlumpy.image = zlumpy_frames[0]
                    zlumpy.y = random.randint(409, 411)
                    zlumpy.skin_change_time = 50

            else:
                zlumpy.skin_change_time -= 1

        if zlumpy.mode == "Fighting":
            zlumpy.y = random.randint(409, 411)
            zlumpy.image =zlumpy_frames[2]
        
def zlumpy_behavior():
    zlumpy_skin_change()
    
    for zlumpy in zlumpies:
        if zlumpy.health <= 0:
            zlumpies.remove(zlumpy)

        zlumpy.near_blaze_bot = False
        zlumpy.near_scorium_slug = False
        zlumpy.near_crying_magnum = False
        zlumpy.near_magma_turtle = False
        zlumpy.near_base = False

        for base in enemy_bases:
            if zlumpy.x - base.x <= random.randint(134, 136):
                zlumpy.near_base = True
                break
            else:
                zlumpy.near_base = False

        for blaze_bot in blaze_bots:
            if zlumpy.x - blaze_bot.x <= random.randint(134, 136):
                zlumpy.near_blaze_bot = True
                break
            else:
                zlumpy.near_blaze_bot = False

        for scorium_slug in scorium_slugs:
            if zlumpy.x - scorium_slug.x <= random.randint(134, 136):
                zlumpy.near_scorium_slug = True
                break
            else:
                zlumpy.near_scorium_slug = False

        for crying_magnum in crying_magnums:
            if zlumpy.x - crying_magnum.x <= random.randint(134, 136):
                zlumpy.near_crying_magnum = True
                break
            else:
                zlumpy.near_crying_magnum = False

        for magma_turtle in magma_turtles:
            if zlumpy.x - magma_turtle.x <= random.randint(204, 206):
                zlumpy.near_magma_turtle = True
                break
            else:
                zlumpy.near_magma_turtle = False

        if zlumpy.near_base or zlumpy.near_blaze_bot or zlumpy.near_scorium_slug or zlumpy.near_crying_magnum or zlumpy.near_magma_turtle:
            if zlumpy.mode != "Being Knocked Back":
                zlumpy.mode = "Fighting"

        elif not zlumpy.near_base and not zlumpy.near_blaze_bot and not zlumpy.near_scorium_slug and not zlumpy.near_crying_magnum and not zlumpy.near_magma_turtle:
            if zlumpy.mode != "Being Knocked Back":
                zlumpy.mode = "Moving"
            
        
        if zlumpy.mode == "Moving":
            zlumpy.x -= 1
                    

        if zlumpy.mode == "Fighting":
            zlumpy_attack()

        if zlumpy.mode == "Being Knocked Back":
            zlumpy.x += 5
            zlumpy.knock_back_distance -= 5

            if zlumpy.knock_back_distance <= 0:
                zlumpy.mode = "Moving"


def summon_zlumpy():
    global coins
    coins -= 75
    zlumpy = Actor(zlumpy_frames[0])
    zlumpy.index = 0
    zlumpy.mode = "Moving"
    zlumpy.can_move = False
    zlumpy.y = random.randint(409, 411)
    zlumpy.pos = (530, zlumpy.y)
    zlumpy.skin_change_time = 50
    zlumpy.time_between_attacks = 35
    zlumpy.hurt_recoil = 25
    zlumpy.health = int(160 + ( (zlumpy_icon.level - 1) * 20) )
    zlumpies.append(zlumpy)

def zlumpy_attack():
    #NOTE TO FIX LATER: ALL MY PROJECTILE UNITS AND ENEMIES IN THIS GAME SEEM TO INCREASE THEIR ATTACK SPEED DEPENDING ON HOW MANY OF THAT UNIT/ENEMY THERE IS ON SCREEN
    for zlumpy in zlumpies:

        if zlumpy.mode == "Fighting":
            #print(zlumpy.time_between_attacks)
            if zlumpy.time_between_attacks <= 0:
                create_zlumpy_projectile(zlumpy.x, zlumpy.y)
                zlumpy.time_between_attacks = 35

            else:
                zlumpy.time_between_attacks -= 1

        else:
            pass


    #zlumpy_projectile behaviors
def zlumpy_projectile_behavior():
    global game_state

    for zlumpy_projectile in zlumpy_projectiles:
        zlumpy_projectile.x -= 2
        zlumpy_projectile.range -= 2

        for base in enemy_bases:
            if zlumpy_projectile.colliderect(base):
                if game_state == "Level 1":
                    levels[0][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break
                if game_state == "Level 2":
                    levels[1][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break
                if game_state == "Level 3":
                    levels[2][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break
                if game_state == "Level 4":
                    levels[3][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break
                if game_state == "Level 5":
                    levels[4][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break
                if game_state == "Level 6":
                    levels[5][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break
                if game_state == "Level 7":
                    levels[6][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break
                if game_state == "Level 8":
                    levels[7][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break
                if game_state == "Level 9":
                    levels[8][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break
                if game_state == "Level 10":
                    levels[9][4] -= zlumpy_projectile.damage
                    zlumpy_projectile.delete = True
                    break


        for blaze_bot in blaze_bots:
            if zlumpy_projectile.colliderect(blaze_bot):
                zlumpy_projectile.delete = True
                blaze_bot.health -= zlumpy_projectile.damage
                break

        for scorium_slug in scorium_slugs:
            if zlumpy_projectile.colliderect(scorium_slug):
                zlumpy_projectile.delete = True
                scorium_slug.health -= zlumpy_projectile.damage
                break
                    #pass

        for crying_magnum in crying_magnums:
            if zlumpy_projectile.colliderect(crying_magnum):
                zlumpy_projectile.delete = True
                crying_magnum.health -= zlumpy_projectile.damage
                break

        for magma_turtle in magma_turtles:
            if zlumpy_projectile.colliderect(magma_turtle):
                zlumpy_projectile.delete = True
                magma_turtle.health -= zlumpy_projectile.damage
                break
                
        if zlumpy_projectile.delete == True:
            zlumpy_projectiles.remove(zlumpy_projectile)
            break

        if zlumpy_projectile.range <= 0:
            zlumpy_projectiles.remove(zlumpy_projectile)
        
        
def create_zlumpy_projectile(x, y):
    zlumpy_projectile = Actor("zlumpy_projectile")
    zlumpy_projectile.x = x - 20
    zlumpy_projectile.y = y + 25
    zlumpy_projectile.delete = False
    zlumpy_projectile.damage = int(12 + ( (zlumpy_icon.level - 1) * 3) )
    zlumpy_projectile.range = 100
    zlumpy_projectiles.append(zlumpy_projectile)





def guardo_skin_change():

    for guardo in guardos:
        if guardo.mode == "Moving":
            if guardo.time_between_attack_frames <= 0:
                if guardo.image == guardo_frames[2] or guardo.image == guardo_frames[3]:
                        guardo.image = guardo_frames[0]
                        guardo.skin_change_time = 50
                        
                if guardo.image == guardo_frames[4] or guardo.image == guardo_frames[5]:
                        guardo.image = guardo_frames[0]
                        guardo.skin_change_time = 50
            else:
                guardo.time_between_attack_frames -= 1

                        
            if guardo.skin_change_time <= 0:
                    
                if guardo.image == guardo_frames[0]:
                    guardo.image = guardo_frames[1]
                    guardo.skin_change_time = 50
                        
                elif guardo.image == guardo_frames[1]:
                    guardo.image = guardo_frames[0]
                    guardo.skin_change_time = 50

            else:
                guardo.skin_change_time -= 1

        if guardo.mode == "Fighting":
            if guardo.skin_change_time <= 0:
                if guardo.image == guardo_frames[0] or guardo.image == guardo_frames[1]:
                    guardo.image = guardo_frames[2]
                    guardo.time_between_attack_frames = 50
            else:
                guardo.skin_change_time -= 1

            if guardo.time_between_attack_frames <= 0:
                if guardo.time_between_attacks <= 0:
                    if guardo.image == guardo_frames[2]:
                        guardo.image = guardo_frames[3]
                        guardo.time_between_attack_frames = 50
                    
                    elif guardo.image == guardo_frames[3]:
                        guardo.image = guardo_frames[4]
                        guardo.time_between_attack_frames = 50
                        
                    elif guardo.image == guardo_frames[4]:
                        guardo.image = guardo_frames[5]
                        guardo.time_between_attack_frames = 50
                        
                    elif guardo.image == guardo_frames[5]:
                        guardo.image = guardo_frames[2]
                        guardo.time_between_attack_frames = 50
                else:
                    guardo.time_between_attacks -= 1

            else:
                guardo.time_between_attack_frames -= 1


def guardo_behavior():
    guardo_skin_change()
    
    for guardo in guardos:
        if guardo.health <= 0:
            guardos.remove(guardo)

        guardo.near_blaze_bot = False
        guardo.near_scorium_slug = False
        guardo.near_crying_magnum = False
        guardo.near_magma_turtle = False
        guardo.near_base = False

        for base in enemy_bases:
            if guardo.x - base.x <= random.randint(104, 106):
                guardo.near_base = True
                break
            else:
                guardo.near_base = False

        for blaze_bot in blaze_bots:
            if guardo.x - blaze_bot.x <= random.randint(104, 106):
                guardo.near_blaze_bot = True
                break
            else:
                guardo.near_blaze_bot = False

        for scorium_slug in scorium_slugs:
            if guardo.x - scorium_slug.x <= random.randint(104, 106):
                guardo.near_scorium_slug = True
                break
            else:
                guardo.near_scorium_slug = False

        for crying_magnum in crying_magnums:
            if guardo.x - crying_magnum.x <= random.randint(104, 106):
                guardo.near_crying_magnum = True
                break
            else:
                guardo.near_crying_magnum = False

        for magma_turtle in magma_turtles:
            if guardo.x - magma_turtle.x <= random.randint(174, 176):
                guardo.near_magma_turtle = True
                break
            else:
                guardo.near_magma_turtle = False

        if guardo.near_base or guardo.near_blaze_bot or guardo.near_scorium_slug or guardo.near_crying_magnum or guardo.near_magma_turtle:
            if guardo.mode != "Being Knocked Back":
                guardo.mode = "Fighting"

        elif not guardo.near_base and not guardo.near_blaze_bot and not guardo.near_scorium_slug and not guardo.near_crying_magnum and not guardo.near_magma_turtle:
            if guardo.mode != "Being Knocked Back":
                guardo.mode = "Moving"
            
        
        if guardo.mode == "Moving":
            guardo.x -= 0.25
                    

        if guardo.mode == "Fighting":
            guardo_attack()

        if guardo.mode == "Being Knocked Back":
            guardo.x += 5
            guardo.knock_back_distance -= 5

            if guardo.knock_back_distance <= 0:
                guardo.mode = "Moving"


def summon_guardo():
    global coins
    coins -= 100
    guardo = Actor(guardo_frames[0])
    guardo.index = 0
    guardo.mode = "Moving"
    guardo.can_move = False
    guardo.y = random.randint(399, 401)
    guardo.pos = (530, guardo.y)
    guardo.skin_change_time = 50
    guardo.time_between_attacks = 100
    guardo.time_between_attack_frames = 50
    guardo.health = int(860 + ( (guardo_icon.level - 1) * 80) )
    guardo.has_shot = False
    guardo.pause_time = 50
    guardos.append(guardo)

def guardo_attack():
    #NOTE TO FIX LATER: ALL MY PROJECTILE UNITS AND ENEMIES IN THIS GAME SEEM TO INCREASE THEIR ATTACK SPEED DEPENDING ON HOW MANY OF THAT UNIT/ENEMY THERE IS ON SCREEN
    for guardo in guardos:

        if guardo.mode == "Fighting":
            
            if guardo.image == guardo_frames[4]:
                if guardo.has_shot == False:
                    if guardo.time_between_attacks <= 0:
                        create_guardo_projectile(guardo.x, guardo.y)
                        guardo.time_between_attacks = 100
                        guardo.has_shot = True
                        #guardo.image = guardo_frames[5]

                    else:
                        guardo.time_between_attacks -= 1
                if guardo.has_shot == True:
                    if guardo.pause_time <= 0:
                        guardo.image = guardo_frames[5]
                        guardo.has_shot = False
                        guardo.pause_time = 50
                    else:
                        guardo.pause_time -= 1


    #zlumpy_projectile behaviors
def guardo_projectile_behavior():
    global game_state

    for guardo_projectile in guardo_projectiles:
        guardo_projectile.x -= 2
        guardo_projectile.y += 2
        guardo_projectile.range -= 2

        for base in enemy_bases:
            if guardo_projectile.colliderect(base):
                if game_state == "Level 1":
                    levels[0][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break
                if game_state == "Level 2":
                    levels[1][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break
                if game_state == "Level 3":
                    levels[2][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break
                if game_state == "Level 4":
                    levels[3][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break
                if game_state == "Level 5":
                    levels[4][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break
                if game_state == "Level 6":
                    levels[5][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break
                if game_state == "Level 7":
                    levels[6][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break
                if game_state == "Level 8":
                    levels[7][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break
                if game_state == "Level 9":
                    levels[8][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break
                if game_state == "Level 10":
                    levels[9][4] -= guardo_projectile.damage
                    guardo_projectile.delete = True
                    break


        for blaze_bot in blaze_bots:
            if guardo_projectile.colliderect(blaze_bot):
                guardo_projectile.delete = True
                blaze_bot.health -= guardo_projectile.damage

        for scorium_slug in scorium_slugs:
            if guardo_projectile.colliderect(scorium_slug):
                guardo_projectile.delete = True
                scorium_slug.health -= guardo_projectile.damage

        for crying_magnum in crying_magnums:
            if guardo_projectile.colliderect(crying_magnum):
                guardo_projectile.delete = True
                crying_magnum.health -= guardo_projectile.damage

        for magma_turtle in magma_turtles:
            if guardo_projectile.colliderect(magma_turtle):
                guardo_projectile.delete = True
                magma_turtle.health -= guardo_projectile.damage
                
        if guardo_projectile.delete == True:
            guardo_projectiles.remove(guardo_projectile)
            break

        if guardo_projectile.range <= 0:
            guardo_projectiles.remove(guardo_projectile)
        
        
def create_guardo_projectile(x, y):
    guardo_projectile = Actor("guardo_projectile")
    print("created")
    guardo_projectile.x = x - 50
    guardo_projectile.y = y - 19
    guardo_projectile.delete = False
    guardo_projectile.damage = int(50 + ( (guardo_icon.level - 1) * 2) )
    guardo_projectile.range = 100
    guardo_projectiles.append(guardo_projectile)


                            
                    

#Behavior of all of your enemy's troops
    #all of the Blaze Bot behaviors
def summon_blaze_bot(buff):
    #print(buff)
    blaze_bot = Actor("blaze_bot")
    blaze_bot.mode = "Moving"
    blaze_bot.pos = (70, 410)
    blaze_bot.time_between_attacks = 45
    blaze_bot.health = int(270 * buff)
    blaze_bot.damage = int(35 * buff)
    blaze_bot.has_been_hit_by_ergam = False
    blaze_bot.has_been_hit_by_ergam_bonus_charge = False
    blaze_bot.has_been_hit_by_zap_ball = False
    blaze_bot.time_stunned = 0
    blaze_bots.append(blaze_bot)

#No skin change required for blaze_bot

def blaze_bot_behavior():
    global coins

    for blaze_bot in blaze_bots:
        if blaze_bot.health <= 0:
            blaze_bots.remove(blaze_bot)
            if enemy_death_money_icon.level > 1:
                coins += int(10 * (1.1 ** enemy_death_money_icon.level))

            else:
                coins += 10

        if blaze_bot.mode == "Being Knocked Back":
            blaze_bot.x -= 5
            blaze_bot.knock_back_distance -= 5

            if blaze_bot.knock_back_distance <= 0:
                blaze_bot.mode = "Moving"

        blaze_bot.near_globy = False
        blaze_bot.near_ergam = False
        blaze_bot.near_zap_ball = False
        blaze_bot.near_zlumpy = False
        blaze_bot.near_guardo = False
        blaze_bot.near_base = False

        for base in your_bases:
            if base.x - blaze_bot.x <= random.randint(109, 111):
                blaze_bot.near_base = True
                break
            else:
                blaze_bot.near_base = False

        for globy in globies:
            if globy.x - blaze_bot.x <= random.randint(109, 111):
                blaze_bot.near_globy = True
                break
            else:
                blaze_bot.near_globy = False

        for ergam in ergams:
            if ergam.x - blaze_bot.x <= random.randint(119, 121):
                blaze_bot.near_ergam = True
                break
            else:
                blaze_bot.near_ergam = False

        for zap_ball in zap_balls:
            if zap_ball.x - blaze_bot.x <= random.randint(119, 121):
                blaze_bot.near_zap_ball = True
                break
            else:
                blaze_bot.near_zap_ball = False

        for zlumpy in zlumpies:
            if zlumpy.x - blaze_bot.x <= random.randint(119, 121):
                blaze_bot.near_zlumpy = True
                break
            else:
                blaze_bot.near_zlumpy = False

        for guardo in guardos:
            if guardo.x - blaze_bot.x <= random.randint(119, 121):
                blaze_bot.near_guardo = True
                break
            else:
                blaze_bot.near_guardo = False


        if blaze_bot.near_base or blaze_bot.near_globy or blaze_bot.near_ergam or blaze_bot.near_zap_ball or blaze_bot.near_zlumpy or blaze_bot.near_guardo:
            if blaze_bot.mode != "Being Knocked Back":
                if blaze_bot.mode != "Stunned":
                    blaze_bot.mode = "Fighting"

        elif not blaze_bot.near_base and not blaze_bot.near_globy and not blaze_bot.near_ergam and not blaze_bot.near_zap_ball and not blaze_bot.near_zlumpy and not blaze_bot.near_guardo:
            if blaze_bot.mode != "Being Knocked Back":
                if blaze_bot.mode != "Stunned":
                    blaze_bot.mode = "Moving"

        if blaze_bot.mode == "Moving":
            blaze_bot.x += 0.55

        if blaze_bot.mode == "Fighting":
            blaze_bot_attack()

        if blaze_bot.mode == "Stunned":
            if blaze_bot.time_stunned <= 0:
                blaze_bot.mode = "Moving"
            else:
                blaze_bot.time_stunned -= 1

def blaze_bot_attack():
    
    for blaze_bot in blaze_bots:

        if blaze_bot.mode == "Fighting":
            #print("We are attacking")
            #print(globy.time_between_attacks)
            
            if blaze_bot.time_between_attacks <= 0:
                create_blaze_bot_projectile(blaze_bot.x, blaze_bot.y, blaze_bot.damage)
                #print(blaze_bot.damage)
                blaze_bot.time_between_attacks = 45

            else:
                blaze_bot.time_between_attacks -= 1

        else:
            pass

    #blaze_bot projectile behaviors
def blaze_bot_projectile_behavior():

    for blaze_bot_projectile in blaze_bot_projectiles:
        #globy_projectile.range = 100
        #print(projectile.range)

        #while globy_projectile.range > 0:
            #print(globy_projectile.range)
        blaze_bot_projectile.x += 1
        blaze_bot_projectile.range -= 1
        #print("moving")

        for base in your_bases:
            if blaze_bot_projectile.colliderect(base):
                base.health -= blaze_bot_projectile.damage
                blaze_bot_projectile.delete = True
                #print("did damage")
                break
                    #pass


        for globy in globies:
            if blaze_bot_projectile.colliderect(globy):
                blaze_bot_projectile.delete = True
                globy.health -= blaze_bot_projectile.damage
                break
                    #pass

        for ergam in ergams:
            if blaze_bot_projectile.colliderect(ergam):
                ergam.health -= blaze_bot_projectile.damage
                blaze_bot_projectile.delete = True
                break

        for zap_ball in zap_balls:
            if blaze_bot_projectile.colliderect(zap_ball):
                zap_ball.health -= (blaze_bot_projectile.damage/zap_ball.division_shield)
                print(blaze_bot_projectile.damage/zap_ball.division_shield)
                blaze_bot_projectile.delete = True
                break

        for zlumpy in zlumpies:
            if blaze_bot_projectile.colliderect(zlumpy):
                blaze_bot_projectile.delete = True
                zlumpy.health -= blaze_bot_projectile.damage
                zlumpy.mode = "Being Knocked Back"
                zlumpy.knock_back_distance = zlumpy.hurt_recoil
                break

        for guardo in guardos:
            if blaze_bot_projectile.colliderect(guardo):
                blaze_bot_projectile.delete = True
                guardo.health -= blaze_bot_projectile.damage
                break
                
        if blaze_bot_projectile.delete == True:
            #print("broken")
            blaze_bot_projectiles.remove(blaze_bot_projectile)
            break

        if blaze_bot_projectile.range <= 0:
            blaze_bot_projectiles.remove(blaze_bot_projectile)
            #print("removed projectile")
        
        
def create_blaze_bot_projectile(x, y, blaze_bot_damage):
    blaze_bot_projectile = Actor("blaze_bot_projectile")
    blaze_bot_projectile.x = x + 20
    blaze_bot_projectile.y = y - 30
    blaze_bot_projectile.delete = False
    blaze_bot_projectile.damage = blaze_bot_damage
    blaze_bot_projectile.range = 80
    blaze_bot_projectiles.append(blaze_bot_projectile)
    #print("Created projectile.")

    #all of the scorium_slug behaviors
def summon_scorium_slug(buff):
    scorium_slug = Actor(scorium_slug_frames[0])
    scorium_slug.index = 0
    scorium_slug.skin_change_time = 50
    scorium_slug.mode = "Moving"
    scorium_slug.pos = (70, 435)
    scorium_slug.time_between_attacks = 30
    scorium_slug.health = int(180 * buff)
    scorium_slug.damage = int(10 * buff)
    scorium_slug.has_been_hit_by_ergam = False
    scorium_slug.has_been_hit_by_ergam_bonus_charge = False
    scorium_slug.has_been_hit_by_zap_ball = False
    scorium_slug.time_stunned = 0
    scorium_slugs.append(scorium_slug)

def scorium_slug_skin_change():

    for scorium_slug in scorium_slugs:
        #print(globy.skin_change_time)
        if scorium_slug.mode == "Moving":

            if scorium_slug.skin_change_time <= 0:
                    
                if scorium_slug.image == scorium_slug_frames[0]:
                    #print("the frame is indeed zero")
                    scorium_slug.image = scorium_slug_frames[1]
                    scorium_slug.skin_change_time = 50
                    #print("changed skins")
                        
                elif scorium_slug.image == scorium_slug_frames[1]:
                    #print("The Frame Is Indeed One")
                    scorium_slug.image = scorium_slug_frames[0]
                    scorium_slug.skin_change_time = 50
                    #print("changed skins")

            else:
                scorium_slug.skin_change_time -= 1

        #if globy.mode == "Fighting":
            #globy.image = globy_frames[2]

def scorium_slug_behavior():
    global coins
    scorium_slug_skin_change()

    for scorium_slug in scorium_slugs:
        if scorium_slug.health <= 0:
            scorium_slugs.remove(scorium_slug)
            if enemy_death_money_icon.level > 1:
                coins += int(15 * (1.1 ** enemy_death_money_icon.level))
            else:
                coins += 15

        if scorium_slug.mode == "Being Knocked Back":
            scorium_slug.x -= 5
            scorium_slug.knock_back_distance -= 5

            if scorium_slug.knock_back_distance <= 0:
                scorium_slug.mode = "Moving"

        scorium_slug.near_globy = False
        scorium_slug.near_ergam = False
        scorium_slug.near_zap_ball = False
        scorium_slug.near_zlumpy = False
        scorium_slug.near_guardo = False
        scorium_slug.near_base = False

        for base in your_bases:
            if base.x - scorium_slug.x <= random.randint(119, 121):
                scorium_slug.near_base = True
                break
            else:
                scorium_slug.near_base = False

        for globy in globies:
            if globy.x - scorium_slug.x <= random.randint(119, 121):
                scorium_slug.near_globy = True
                break
            else:
                scorium_slug.near_globy = False

        for ergam in ergams:
            if ergam.x - scorium_slug.x <= random.randint(129, 131):
                scorium_slug.near_ergam = True
                break
            else:
                scorium_slug.near_ergam = False

        for zap_ball in zap_balls:
            if zap_ball.x - scorium_slug.x <= random.randint(129, 131):
                scorium_slug.near_zap_ball = True
                break
            else:
                scorium_slug.near_zap_ball = False

        for zlumpy in zlumpies:
            if zlumpy.x - scorium_slug.x <= random.randint(129, 131):
                scorium_slug.near_zlumpy = True
                break
            else:
                scorium_slug.near_zlumpy = False

        for guardo in guardos:
            if guardo.x - scorium_slug.x <= random.randint(129, 131):
                scorium_slug.near_guardo = True
                break
            else:
                scorium_slug.near_guardo = False


        if scorium_slug.near_base or scorium_slug.near_globy or scorium_slug.near_ergam or scorium_slug.near_zap_ball or scorium_slug.near_zlumpy or scorium_slug.near_guardo:
            if scorium_slug.mode != "Being Knocked Back":
                if scorium_slug.mode != "Stunned":
                    scorium_slug.mode = "Fighting"

        elif not scorium_slug.near_base and not scorium_slug.near_globy and not scorium_slug.near_ergam and not scorium_slug.near_zap_ball and not scorium_slug.near_zlumpy and not scorium_slug.near_guardo:
            if scorium_slug.mode != "Being Knocked Back":
                if scorium_slug.mode != "Stunned":
                    scorium_slug.mode = "Moving"

        if scorium_slug.mode == "Moving":
            scorium_slug.x += 0.7

        if scorium_slug.mode == "Fighting":
            scorium_slug_attack()

        if scorium_slug.mode == "Stunned":
            if scorium_slug.time_stunned <= 0:
                scorium_slug.mode = "Moving"
            else:
                scorium_slug.time_stunned -= 1

def scorium_slug_attack():
    
    for scorium_slug in scorium_slugs:

        if scorium_slug.mode == "Fighting":
            #print("We are attacking")
            #print(globy.time_between_attacks)
            
            if scorium_slug.time_between_attacks <= 0:
                create_scorium_slug_projectile(scorium_slug.x, scorium_slug.y, scorium_slug.damage)
                scorium_slug.time_between_attacks = 30

            else:
                scorium_slug.time_between_attacks -= 1

        else:
            pass

def scorium_slug_projectile_behavior():

    for scorium_slug_projectile in scorium_slug_projectiles:
        #globy_projectile.range = 100
        #print(projectile.range)

        #while globy_projectile.range > 0:
            #print(globy_projectile.range)
        scorium_slug_projectile.x += 1
        scorium_slug_projectile.range -= 1
        #print("moving")

        for base in your_bases:
            if scorium_slug_projectile.colliderect(base):
                base.health -= scorium_slug_projectile.damage
                scorium_slug_projectile.delete = True
                #print("did damage")
                break
                    #pass


        for globy in globies:
            if scorium_slug_projectile.colliderect(globy):
                scorium_slug_projectile.delete = True
                globy.health -= scorium_slug_projectile.damage
                globy.time_between_attacks += 25
                break

        for ergam in ergams:
            if scorium_slug_projectile.colliderect(ergam):
                scorium_slug_projectile.delete = True
                ergam.health -= scorium_slug_projectile.damage
                ergam.time_between_attacks += 25
                break

        for zap_ball in zap_balls:
            if scorium_slug_projectile.colliderect(zap_ball):
                scorium_slug_projectile.delete = True
                zap_ball.health -= (scorium_slug_projectile.damage/zap_ball.division_shield)
                break
                    #pass

        for zlumpy in zlumpies:
            if scorium_slug_projectile.colliderect(zlumpy):
                scorium_slug_projectile.delete = True
                zlumpy.health -= scorium_slug_projectile.damage
                zlumpy.time_between_attacks += 25
                zlumpy.mode = "Being Knocked Back"
                zlumpy.knock_back_distance = zlumpy.hurt_recoil
                break

        for guardo in guardos:
            if scorium_slug_projectile.colliderect(guardo):
                scorium_slug_projectile.delete = True
                guardo.health -= scorium_slug_projectile.damage
                guardo.time_between_attacks += 25
                break
                
        if scorium_slug_projectile.delete == True:
            #print("broken")
            scorium_slug_projectiles.remove(scorium_slug_projectile)
            break

        if scorium_slug_projectile.range <= 0:
            scorium_slug_projectiles.remove(scorium_slug_projectile)
            #print("removed projectile")

def create_scorium_slug_projectile(x, y, scorium_slug_damage):
    scorium_slug_projectile = Actor("scorium_slug_projectile")
    scorium_slug_projectile.x = x + 20
    scorium_slug_projectile.y = y
    scorium_slug_projectile.delete = False
    scorium_slug_projectile.damage = scorium_slug_damage
    scorium_slug_projectile.range = 100
    scorium_slug_projectiles.append(scorium_slug_projectile)
    #print("Created projectile.")

    #all of the crying_magnum behaviors
def summon_crying_magnum(buff):
    crying_magnum = Actor(crying_magnum_frames[0])
    crying_magnum.index = 0
    crying_magnum.skin_change_time = 10
    crying_magnum.mode = "Moving"
    crying_magnum.pos = (30, 400)
    crying_magnum.time_between_attacks = 100
    crying_magnum.health = int(120 * buff)
    crying_magnum.damage = int(500 * buff)
    crying_magnum.has_been_hit_by_ergam = False
    crying_magnum.has_been_hit_by_ergam_bonus_charge = False
    crying_magnum.has_been_hit_by_zap_ball = False
    crying_magnum.time_stunned = 0
    crying_magnums.append(crying_magnum)

def crying_magnum_skin_change():

    for crying_magnum in crying_magnums:
        #print(globy.skin_change_time)
        if crying_magnum.mode == "Moving":

            if crying_magnum.skin_change_time <= 0:
                    
                if crying_magnum.image == crying_magnum_frames[0]:
                    #print("the frame is indeed zero")
                    crying_magnum.image = crying_magnum_frames[1]
                    crying_magnum.skin_change_time = 10
                    #print("changed skins")
                        
                elif crying_magnum.image == crying_magnum_frames[1]:
                    #print("The Frame Is Indeed One")
                    crying_magnum.image = crying_magnum_frames[2]
                    crying_magnum.skin_change_time = 10
                    #print("changed skins")

                elif crying_magnum.image == crying_magnum_frames[2]:
                    #print("The Frame Is Indeed One")
                    crying_magnum.image = crying_magnum_frames[3]
                    crying_magnum.skin_change_time = 10
                    #print("changed skins")

                elif crying_magnum.image == crying_magnum_frames[3]:
                    #print("The Frame Is Indeed One")
                    crying_magnum.image = crying_magnum_frames[0]
                    crying_magnum.skin_change_time = 10
                    #print("changed skins")

            else:
                crying_magnum.skin_change_time -= 1

        if crying_magnum.mode == "Fighting":
            crying_magnum.image = crying_magnum_frames[0]

def crying_magnum_behavior():
    global coins
    crying_magnum_skin_change()

    for crying_magnum in crying_magnums:
        #print(crying_magnum.mode)
        if crying_magnum.health <= 0:
            crying_magnums.remove(crying_magnum)
            if enemy_death_money_icon.level > 1:
                coins += int(20 * (1.1 ** enemy_death_money_icon.level))
            else:
                coins += 20

        if crying_magnum.mode == "Being Knocked Back":
            crying_magnum.x -= 5
            crying_magnum.knock_back_distance -= 5

            if crying_magnum.knock_back_distance <= 0:
                crying_magnum.mode = "Moving"

        crying_magnum.near_globy = False
        crying_magnum.near_ergam = False
        crying_magnum.near_zap_ball = False
        crying_magnum.near_zlumpy = False
        crying_magnum.near_guardo = False
        crying_magnum.near_base = False

        for base in your_bases:
            if base.x - crying_magnum.x <= random.randint(179, 181):
                crying_magnum.near_base = True
                break
            else:
                crying_magnum.near_base = False

        for globy in globies:
            if globy.x - crying_magnum.x <= random.randint(179, 181):
                crying_magnum.near_globy = True
                break
            else:
                crying_magnum.near_globy = False

        for ergam in ergams:
            if ergam.x - crying_magnum.x <= random.randint(189, 191):
                crying_magnum.near_ergam = True
                break
            else:
                crying_magnum.near_ergam = False

        for zap_ball in zap_balls:
            if zap_ball.x - crying_magnum.x <= random.randint(189, 191):
                crying_magnum.near_zap_ball = True
                break
            else:
                crying_magnum.near_zap_ball = False

        for zlumpy in zlumpies:
            if zlumpy.x - crying_magnum.x <= random.randint(189, 191):
                crying_magnum.near_zlumpy = True
                break
            else:
                crying_magnum.near_zlumpy = False

        for guardo in guardos:
            if guardo.x - crying_magnum.x <= random.randint(189, 191):
                crying_magnum.near_guardo = True
                break
            else:
                crying_magnum.near_guardo = False


        if crying_magnum.near_base or crying_magnum.near_globy or crying_magnum.near_ergam or crying_magnum.near_zap_ball or crying_magnum.near_zlumpy or crying_magnum.near_guardo:
            if crying_magnum.mode != "Being Knocked Back":
                if crying_magnum.mode != "Stunned":
                    crying_magnum.mode = "Fighting"

        elif not crying_magnum.near_base and not crying_magnum.near_globy and not crying_magnum.near_ergam and not crying_magnum.near_zap_ball and not crying_magnum.near_zlumpy and not crying_magnum.near_guardo:
            if crying_magnum.mode != "Being Knocked Back":
                if crying_magnum.mode != "Stunned":
                    crying_magnum.mode = "Moving"

        if crying_magnum.mode == "Moving":
            crying_magnum.x += 0.3

        if crying_magnum.mode == "Fighting":
            crying_magnum_attack()

        if crying_magnum.mode == "Stunned":
            if crying_magnum.time_stunned <= 0:
                crying_magnum.mode = "Moving"
            else:
                crying_magnum.time_stunned -= 1


def crying_magnum_attack():
    
    for crying_magnum in crying_magnums:

        if crying_magnum.mode == "Fighting":
            #print("We are attacking")
            #print(globy.time_between_attacks)
            
            if crying_magnum.time_between_attacks <= 0:
                create_crying_magnum_projectile(crying_magnum.x, crying_magnum.y, crying_magnum.damage)
                crying_magnum.time_between_attacks = 300

            else:
                crying_magnum.time_between_attacks -= 1

        else:
            pass

def crying_magnum_projectile_behavior():

    for crying_magnum_projectile in crying_magnum_projectiles:
        #globy_projectile.range = 100
        #print(projectile.range)

        #while globy_projectile.range > 0:
            #print(globy_projectile.range)
        crying_magnum_projectile.x += 1
        crying_magnum_projectile.range -= 1
        #print("moving")

        for base in your_bases:
            if crying_magnum_projectile.colliderect(base):
                base.health -= crying_magnum_projectile.damage
                crying_magnum_projectile.delete = True
                #print("did damage")
                break
                    #pass


        for globy in globies:
            if crying_magnum_projectile.colliderect(globy):
                crying_magnum_projectile.delete = True
                globy.health -= crying_magnum_projectile.damage
                break
                    #pass
            
        for ergam in ergams:
            if crying_magnum_projectile.colliderect(ergam):
                crying_magnum_projectile.delete = True
                ergam.health -= crying_magnum_projectile.damage
                break

        for zap_ball in zap_balls:
            if crying_magnum_projectile.colliderect(zap_ball):
                crying_magnum_projectile.delete = True
                zap_ball.health -= (crying_magnum_projectile.damage/zap_ball.division_shield)
                break

        for zlumpy in zlumpies:
            if crying_magnum_projectile.colliderect(zlumpy):
                crying_magnum_projectile.delete = True
                zlumpy.health -= crying_magnum_projectile.damage
                zlumpy.mode = "Being Knocked Back"
                zlumpy.knock_back_distance = zlumpy.hurt_recoil
                break
            
        for guardo in guardos:
            if crying_magnum_projectile.colliderect(guardo):
                crying_magnum_projectile.delete = True
                guardo.health -= crying_magnum_projectile.damage
                break
                
        if crying_magnum_projectile.delete == True:
            #print("broken")
            crying_magnum_projectiles.remove(crying_magnum_projectile)
            break

        if crying_magnum_projectile.range <= 0:
            crying_magnum_projectiles.remove(crying_magnum_projectile)
            #print("removed projectile")

def create_crying_magnum_projectile(x, y, crying_magnum_damage):
    crying_magnum_projectile = Actor("crying_magnum_projectile")
    crying_magnum_projectile.x = x + 20
    crying_magnum_projectile.y = y
    crying_magnum_projectile.delete = False
    crying_magnum_projectile.damage = crying_magnum_damage
    crying_magnum_projectile.range = 150
    crying_magnum_projectiles.append(crying_magnum_projectile)
    #print("Created projectile.")


#all magma turtle behaviours
def summon_magma_turtle(buff):
    magma_turtle = Actor(magma_turtle_frames[0])
    magma_turtle.index = 0
    magma_turtle.scale = 1.25
    magma_turtle.skin_change_time = 10
    magma_turtle.time_between_attack_frames = 15
    magma_turtle.mode = "Moving"
    magma_turtle.pos = (10, 350)
    magma_turtle.time_between_attacks = 100
    magma_turtle.health = int(4800 * buff)
    magma_turtle.damage = int(300 * buff)
    magma_turtle.has_been_hit_by_ergam = False
    magma_turtle.has_been_hit_by_ergam_bonus_charge = False
    magma_turtle.has_been_hit_by_zap_ball = False
    magma_turtle.time_stunned = 0
    magma_turtles.append(magma_turtle)

def magma_turtle_skin_change():

    for magma_turtle in magma_turtles:
        #print(globy.skin_change_time)
        if magma_turtle.mode == "Moving":
            if magma_turtle.time_between_attack_frames <= 0:
                if magma_turtle.image == magma_turtle_frames[4] or magma_turtle.image == magma_turtle_frames[5]:
                        magma_turtle.image = magma_turtle_frames[0]
                        magma_turtle.skin_change_time = 10
                        
                if magma_turtle.image == magma_turtle_frames[6] or magma_turtle.image == magma_turtle_frames[7]:
                        magma_turtle.image = magma_turtle_frames[0]
                        magma_turtle.skin_change_time = 10
            else:
                magma_turtle.time_between_attack_frames -= 1

                        
            if magma_turtle.skin_change_time <= 0:
                    
                if magma_turtle.image == magma_turtle_frames[0]:
                    #print("the frame is indeed zero")
                    magma_turtle.image = magma_turtle_frames[1]
                    magma_turtle.skin_change_time = 10
                    #print("changed skins")
                        
                elif magma_turtle.image == magma_turtle_frames[1]:
                    #print("The Frame Is Indeed One")
                    magma_turtle.image = magma_turtle_frames[2]
                    magma_turtle.skin_change_time = 10
                    #print("changed skins")

                elif magma_turtle.image == magma_turtle_frames[2]:
                    #print("The Frame Is Indeed One")
                    magma_turtle.image = magma_turtle_frames[3]
                    magma_turtle.skin_change_time = 10
                    #print("changed skins")

                elif magma_turtle.image == magma_turtle_frames[3]:
                    #print("The Frame Is Indeed One")
                    magma_turtle.image = magma_turtle_frames[0]
                    magma_turtle.skin_change_time = 10
                    #print("changed skins")

            else:
                magma_turtle.skin_change_time -= 1

        if magma_turtle.mode == "Fighting":
            #print(magma_turtle.skin_change_time)
            if magma_turtle.skin_change_time <= 0:
                if magma_turtle.image == magma_turtle_frames[0] or magma_turtle.image == magma_turtle_frames[1]:
                    magma_turtle.image = magma_turtle_frames[4]
                    magma_turtle.time_between_attack_frames = 15
                if magma_turtle.image == magma_turtle_frames[2] or magma_turtle.image == magma_turtle_frames[3]:
                    magma_turtle.image = magma_turtle_frames[4]
                    magma_turtle.time_between_attack_frames = 15
                print(magma_turtle.time_between_attack_frames)
            else:
                magma_turtle.skin_change_time -= 1

            if magma_turtle.time_between_attack_frames <= 0:
                if magma_turtle.time_between_attacks <= 0:
                    if magma_turtle.image == magma_turtle_frames[4]:
                        magma_turtle.image = magma_turtle_frames[5]
                        magma_turtle.time_between_attack_frames = 15
                    
                    elif magma_turtle.image == magma_turtle_frames[5]:
                        magma_turtle.image = magma_turtle_frames[6]
                        magma_turtle.time_between_attack_frames = 15
                        
                    elif magma_turtle.image == magma_turtle_frames[6]:
                        magma_turtle.image = magma_turtle_frames[7]
                        magma_turtle.time_between_attack_frames = 15
                        
                    elif magma_turtle.image == magma_turtle_frames[7]:
                        magma_turtle.image = magma_turtle_frames[4]
                        magma_turtle.time_between_attack_frames = 15
                else:
                    magma_turtle.time_between_attacks -= 1

            else:
                magma_turtle.time_between_attack_frames -= 1

def magma_turtle_attack():
    
    for magma_turtle in magma_turtles:

        if magma_turtle.mode == "Fighting":
            #print("We are attacking")
            #print(globy.time_between_attacks)

            if magma_turtle.image == magma_turtle_frames[6]:
            
                if magma_turtle.time_between_attacks <= 0:
                    create_magma_turtle_projectile(magma_turtle.x, magma_turtle.y, magma_turtle.damage)
                    magma_turtle.time_between_attacks = 50
                    magma_turtle.image = magma_turtle_frames[7]

                else:
                    magma_turtle.time_between_attacks -= 1


def magma_turtle_behavior():
    global coins
    magma_turtle_skin_change()

    for magma_turtle in magma_turtles:
        magma_turtle.scale = 1.25
        #print(crying_magnum.mode)
        if magma_turtle.health <= 0:
            magma_turtles.remove(magma_turtle)
            if enemy_death_money_icon.level > 1:
                coins += int(500 * (1.1 ** enemy_death_money_icon.level))
            else:
                coins += 20

        if magma_turtle.mode == "Being Knocked Back":
            magma_turtle.x -= 5
            magma_turtle.knock_back_distance -= 10

            if magma_turtle.knock_back_distance <= 0:
                magma_turtle.mode = "Moving"

        if magma_turtle.mode == "Stunned":
            if magma_turtle.time_stunned <= 0:
                magma_turtle.mode = "Moving"
            else:
                magma_turtle.time_stunned -= 1

        magma_turtle.near_globy = False
        magma_turtle.near_ergam = False
        magma_turtle.near_zap_ball = False
        magma_turtle.near_zlumpy = False
        magma_turtle.near_guardo = False
        magma_turtle.near_base = False

        for base in your_bases:
            if base.x - magma_turtle.x <= random.randint(199, 201):
                magma_turtle.near_base = True
                break
            else:
                magma_turtle.near_base = False

        for globy in globies:
            if globy.x - magma_turtle.x <= random.randint(199, 201):
                magma_turtle.near_globy = True
                break
            else:
                magma_turtle.near_globy = False

        for ergam in ergams:
            if ergam.x - magma_turtle.x <= random.randint(209, 211):
                magma_turtle.near_ergam = True
                break
            else:
                magma_turtle.near_ergam = False

        for zap_ball in zap_balls:
            if zap_ball.x - magma_turtle.x <= random.randint(209, 211):
                magma_turtle.near_zap_ball = True
                break
            else:
                magma_turtle.near_zap_ball = False

        for zlumpy in zlumpies:
            if zlumpy.x - magma_turtle.x <= random.randint(209, 211):
                magma_turtle.near_zlumpy = True
                break
            else:
                magma_turtle.near_zlumpy = False

        for guardo in guardos:
            if guardo.x - magma_turtle.x <= random.randint(209, 211):
                magma_turtle.near_guardo = True
                break
            else:
                magma_turtle.near_guardo = False
                

        if magma_turtle.near_base or magma_turtle.near_globy or magma_turtle.near_ergam or magma_turtle.near_zap_ball or magma_turtle.near_zlumpy or magma_turtle.near_guardo:
            if magma_turtle.mode != "Being Knocked Back":
                if magma_turtle.mode != "Stunned":
                    magma_turtle.mode = "Fighting"

        elif not magma_turtle.near_base and not magma_turtle.near_globy and not magma_turtle.near_ergam and not magma_turtle.near_zap_ball and not magma_turtle.near_zlumpy and not magma_turtle.near_guardo:
            if magma_turtle.mode != "Being Knocked Back":
                if magma_turtle.mode != "Stunned":
                    magma_turtle.mode = "Moving"

        if magma_turtle.mode == "Moving":
            magma_turtle.x += 0.2

        if magma_turtle.mode == "Fighting":
            magma_turtle_attack()

def magma_turtle_projectile_behavior():

    for magma_turtle_projectile in magma_turtle_projectiles:

        if magma_turtle_projectile.image == magma_turtle_projectile_frames[0]:
            magma_turtle_projectile.y += magma_turtle_projectile.y_speed
            magma_turtle_projectile.y_speed -= magma_turtle_projectile.y_speed_decay
            magma_turtle_projectile.x += 5
            
            if magma_turtle_projectile.y >= 425:
                magma_turtle_projectile.image = magma_turtle_projectile_frames[1]

        if magma_turtle_projectile.image == magma_turtle_projectile_frames[1]:
            magma_turtle_projectile.image = magma_turtle_projectile_frames[2]
            
            for base in your_bases:
                if magma_turtle_projectile.colliderect(base):
                    base.health -= magma_turtle_projectile.damage


            for globy in globies:
                if magma_turtle_projectile.colliderect(globy):
                    globy.health -= magma_turtle_projectile.damage
                
            for ergam in ergams:
                if magma_turtle_projectile.colliderect(ergam):
                    ergam.health -= magma_turtle_projectile.damage

            for zap_ball in zap_balls:
                if magma_turtle_projectile.colliderect(zap_ball):
                    zap_ball.health -= (magma_turtle_projectile.damage/zap_ball.division_shield)

            for zlumpy in zlumpies:
                if magma_turtle_projectile.colliderect(zlumpy):
                    zlumpy.health -= magma_turtle_projectile.damage
                    zlumpy.mode = "Being Knocked Back"
                    zlumpy.knock_back_distance = zlumpy.hurt_recoil

            for guardo in guardos:
                if magma_turtle_projectile.colliderect(guardo):
                    guardo.health -= magma_turtle_projectile.damage


        if magma_turtle_projectile.image == magma_turtle_projectile_frames[2]:
            
            if magma_turtle_projectile.time_between_frames <= 0:
                #print("hello")
                magma_turtle_projectile.image = magma_turtle_projectile_frames[3]
                magma_turtle_projectile.time_between_frames = 15
            else:
                magma_turtle_projectile.time_between_frames = magma_turtle_projectile.time_between_frames - 1
                #print(magma_turtle_projectile.time_between_frames)

        if magma_turtle_projectile.image == magma_turtle_projectile_frames[3]:
            print("hello")
            if magma_turtle_projectile.time_between_frames <= 0:
                magma_turtle_projectile.delete = True
            else:
                magma_turtle_projectile.time_between_frames -= 1
                
        if magma_turtle_projectile.delete == True:
            #print("broken")
            magma_turtle_projectiles.remove(magma_turtle_projectile)
            break


def create_magma_turtle_projectile(x, y, magma_turtle_damage):
    magma_turtle_projectile = Actor(magma_turtle_projectile_frames[0])
    magma_turtle_projectile.x = x + 20
    magma_turtle_projectile.y = y
    magma_turtle_projectile.y_speed = -25
    magma_turtle_projectile.y_speed_decay = -2.5
    magma_turtle_projectile.time_between_frames = 15
    magma_turtle_projectile.delete = False
    magma_turtle_projectile.damage = magma_turtle_damage
    magma_turtle_projectiles.append(magma_turtle_projectile)
    #print("Created projectile.")
                

#base health calculations
def calculate_your_base_health():
    global starting_base
    global equiped_base
    global level_state

    for base in your_bases:
        if base.health <= 0:
            base.health = 0

        if base.health == 0:
            level_state = "Game Over"

    for blaze_bot_projectile in blaze_bot_projectiles:

        for base in your_bases:
            pass
        
            #if equiped_base == 0:
                
            #if base.colliderect(blaze_bot_projectile):
                #print("Calculating base HP")
                #base.health -= blaze_bot_projectile.damage

"""
    for base in your_bases:
        
        for blaze_bot_projectile in blaze_bot_projectiles:

            if base.colliderect(blaze_bot_projectile):

                base.health -= blaze_bot_projectile.damage
"""

def boss_wave():
    print("Boss Wave")
    for globy in globies:
        globy.mode = "Being Knocked Back"
        globy.knock_back_distance = 150
    for ergam in ergams:
        ergam.mode = "Being Knocked Back"
        ergam.knock_back_distance = 150
    for zap_ball in zap_balls:
        zap_ball.mode = "Being Knocked Back"
        zap_ball.knock_back_distance = 150
    for zlumpy in zlumpies:
        zlumpy.mode = "Being Knocked Back"
        zlumpy.knock_back_distance = 150

    

#Different Level AI's
def level_1_waves():
    global level_one
    global level_one_time_between_spawns
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    calculate_your_base_health()
    
    if level_one_time_between_spawns <= 0:
        summon_blaze_bot(levels[0][3][0])
        level_one_time_between_spawns = random.randint(500, 700)

    else:
        level_one_time_between_spawns -= 1

def reset_level_1_waves():
    global level_one_time_between_spawns
    level_one_time_between_spawns = random.randint(500, 700)

def level_2_waves():
    global level_two
    global level_two_blaze_bot_time_between_spawns
    global level_two_scorium_slug_time_between_spawns
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    scorium_slug_behavior()
    scorium_slug_projectile_behavior()
    calculate_your_base_health()

    if level_two_blaze_bot_time_between_spawns <= 0:
        summon_blaze_bot(levels[1][3][0][0])
        level_two_blaze_bot_time_between_spawns = random.randint(300, 600)

    else:
        level_two_blaze_bot_time_between_spawns -= 1

    if level_two_scorium_slug_time_between_spawns <= 0:
        summon_scorium_slug(levels[1][3][1][0])
        level_two_scorium_slug_time_between_spawns = random.randint(700, 900)

    else:
        level_two_scorium_slug_time_between_spawns -= 1

def reset_level_2_waves():
    global level_two_blaze_bot_time_between_spawns
    global level_two_scorium_slug_time_between_spawns
    level_two_blaze_bot_time_between_spawns = random.randint(300, 600)
    level_two_scorium_slug_time_between_spawns = random.randint(700, 900)

def level_3_waves():
    global level_three
    global level_three_blaze_bot_time_between_spawns
    global level_three_scorium_slug_time_between_spawns
    global level_three_crying_magnum_time_between_spawns
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    scorium_slug_behavior()
    scorium_slug_projectile_behavior()
    crying_magnum_behavior()
    crying_magnum_projectile_behavior()
    calculate_your_base_health()

    if level_three_blaze_bot_time_between_spawns <= 0:
        summon_blaze_bot(levels[2][3][0][0])
        level_three_blaze_bot_time_between_spawns = random.randint(200, 400)

    else:
        level_three_blaze_bot_time_between_spawns -= 1

    if level_three_scorium_slug_time_between_spawns <= 0:
        summon_scorium_slug(levels[2][3][1][0])
        level_three_scorium_slug_time_between_spawns = random.randint(500, 700)

    else:
        level_three_scorium_slug_time_between_spawns -= 1

    if level_three_crying_magnum_time_between_spawns <= 0:
        summon_crying_magnum(levels[2][3][2][0])
        level_three_crying_magnum_time_between_spawns = random.randint(1000, 1200)

    else:
        level_three_crying_magnum_time_between_spawns -= 1

def reset_level_3_waves():
    global level_three_blaze_bot_time_between_spawns
    global level_three_scorium_slug_time_between_spawns
    global level_three_crying_magnum_time_between_spawns
    level_three_blaze_bot_time_between_spawns = random.randint(200, 400)
    level_three_scorium_slug_time_between_spawns = random.randint(500, 700)
    level_three_crying_magnum_time_between_spawns = random.randint(1000, 1200)


def level_4_waves():
    global level_four
    global level_four_blaze_bot_time_between_spawns
    global level_four_scorium_slug_time_between_spawns
    global level_four_crying_magnum_time_between_spawns
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    scorium_slug_behavior()
    scorium_slug_projectile_behavior()
    crying_magnum_behavior()
    crying_magnum_projectile_behavior()
    calculate_your_base_health()

    if level_four_blaze_bot_time_between_spawns <= 0:
        summon_blaze_bot(levels[3][3][0][0])
        level_four_blaze_bot_time_between_spawns = random.randint(100, 300)

    else:
        level_four_blaze_bot_time_between_spawns -= 1

    if level_four_scorium_slug_time_between_spawns <= 0:
        summon_scorium_slug(levels[3][3][1][0])
        level_four_scorium_slug_time_between_spawns = random.randint(400, 600)

    else:
        level_four_scorium_slug_time_between_spawns -= 1

    if level_four_crying_magnum_time_between_spawns <= 0:
        summon_crying_magnum(levels[3][3][2][0])
        level_four_crying_magnum_time_between_spawns = random.randint(700, 900)

    else:
        level_four_crying_magnum_time_between_spawns -= 1

def reset_level_4_waves():
    global level_four_blaze_bot_time_between_spawns
    global level_four_scorium_slug_time_between_spawns
    global level_four_crying_magnum_time_between_spawns
    level_four_blaze_bot_time_between_spawns = random.randint(100, 300)
    level_four_scorium_slug_time_between_spawns = random.randint(400, 600)
    level_four_crying_magnum_time_between_spawns = random.randint(700, 900)

def level_5_waves():
    global level_five
    global level_five_blaze_bot_time_between_waves
    global level_five_blaze_bot_time_between_spawns
    global level_five_blaze_bot_amount_per_wave
    global level_five_crying_magnum_time_between_spawns
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    crying_magnum_behavior()
    crying_magnum_projectile_behavior()
    calculate_your_base_health()

    if level_five_blaze_bot_time_between_waves <= 0:
        
        if level_five_blaze_bot_time_between_spawns <= 0:
            
            if level_five_blaze_bot_amount_per_wave >= 1:
                summon_blaze_bot(levels[4][3][0][0])
                level_five_blaze_bot_amount_per_wave -= 1
                level_five_blaze_bot_time_between_spawns = 50
                
            else:
                level_five_blaze_bot_time_between_waves = 1000
                level_five_blaze_bot_time_between_spawns = 50
                level_five_blaze_bot_amount_per_wave = 3

        else:
            level_five_blaze_bot_time_between_spawns -= 1

    else:
        level_five_blaze_bot_time_between_waves -= 1
        #print(level_five_blaze_bot_time_between_waves)

    if level_five_crying_magnum_time_between_spawns <= 0:
        summon_crying_magnum(levels[4][3][1][0])
        level_five_crying_magnum_time_between_spawns = random.randint(950, 1050)

    else:
        level_five_crying_magnum_time_between_spawns -= 1

def reset_level_5_waves():
    global level_five_blaze_bot_time_between_waves
    global level_five_blaze_bot_time_between_spawns
    global level_five_blaze_bot_amount_per_wave
    global level_five_crying_magnum_time_between_spawns
    level_five_blaze_bot_time_between_waves = 1000
    level_five_blaze_bot_time_between_waves = 50
    level_five_blaze_bot_amount_per_wave = 3
    level_five_crying_magnum_time_between_spawns = random.randint(950, 1050)


def level_6_waves():
    global level_six
    global level_six_blaze_bot_time_between_waves
    global level_six_blaze_bot_time_between_spawns
    global level_six_blaze_bot_amount_per_wave
    global level_six_scorium_slug_time_between_waves
    global level_six_scorium_slug_time_between_spawns
    global level_six_scorium_slug_amount_per_wave
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    scorium_slug_behavior()
    scorium_slug_projectile_behavior()
    calculate_your_base_health()

    if level_six_blaze_bot_time_between_waves <= 0:
        
        if level_six_blaze_bot_time_between_spawns <= 0:
            
            if level_six_blaze_bot_amount_per_wave >= 1:
                summon_blaze_bot(levels[5][3][0][0])
                level_six_blaze_bot_amount_per_wave -= 1
                level_six_blaze_bot_time_between_spawns = 50
                
            else:
                level_six_blaze_bot_time_between_waves = 1200
                level_six_blaze_bot_time_between_spawns = 50
                level_six_blaze_bot_amount_per_wave = 4

        else:
            level_six_blaze_bot_time_between_spawns -= 1

    else:
        level_six_blaze_bot_time_between_waves -= 1
        print(level_six_blaze_bot_time_between_waves)

    if level_six_scorium_slug_time_between_waves <= 0:
        
        if level_six_scorium_slug_time_between_spawns <= 0:
            
            if level_six_scorium_slug_amount_per_wave >= 1:
                summon_scorium_slug(levels[5][3][1][0])
                level_six_scorium_slug_amount_per_wave -= 1
                level_six_scorium_slug_time_between_spawns = 50
                
            else:
                level_six_scorium_slug_time_between_waves = 1300
                level_six_scorium_slug_time_between_spawns = 70
                level_six_scorium_slug_amount_per_wave = 3

        else:
            level_six_scorium_slug_time_between_spawns -= 1

    else:
        level_six_scorium_slug_time_between_waves -= 1
        #print(level_six_scorium_slug_time_between_waves)

def reset_level_6_waves():
    global level_six_blaze_bot_time_between_waves
    global level_six_blaze_bot_time_between_spawns
    global level_six_blaze_bot_amount_per_wave
    global level_six_scorium_slug_time_between_waves
    global level_six_scorium_slug_time_between_spawns
    global level_six_scorium_slug_amount_per_wave
    level_six_blaze_bot_time_between_waves = 1200
    level_six_blaze_bot_time_between_spawns = 50
    level_six_blaze_bot_amount_per_wave = 4
    level_six_scorium_slug_time_between_waves = 1300
    level_six_scorium_slug_time_between_spawns = 70
    level_six_scorium_slug_amount_per_wave = 3

def level_7_waves():
    global level_seven
    global level_seven_crying_magnum_time_between_waves
    global level_seven_crying_magnum_time_between_spawns
    global level_seven_crying_magnum_amount_per_wave
    global level_seven_blaze_bot_time_between_spawns
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    crying_magnum_behavior()
    crying_magnum_projectile_behavior()
    calculate_your_base_health()

    if level_seven_crying_magnum_time_between_waves <= 0:
        
        if level_seven_crying_magnum_time_between_spawns <= 0:
            
            if level_seven_crying_magnum_amount_per_wave >= 1:
                summon_crying_magnum(levels[6][3][1][0])
                level_seven_crying_magnum_amount_per_wave -= 1
                level_seven_crying_magnum_time_between_spawns = 120
                
            else:
                level_seven_crying_magnum_time_between_waves = 1800
                level_seven_crying_magnum_time_between_spawns = 120
                level_seven_crying_magnum_amount_per_wave = 2

        else:
            level_seven_crying_magnum_time_between_spawns -= 1

    else:
        level_seven_crying_magnum_time_between_waves -= 1
        #print(level_five_blaze_bot_time_between_waves)

    if level_seven_blaze_bot_time_between_spawns <= 0:
        summon_blaze_bot(levels[6][3][0][0])
        level_seven_blaze_bot_time_between_spawns = random.randint(200, 340)

    else:
        level_seven_blaze_bot_time_between_spawns -= 1

def reset_level_7_waves():
    global level_seven_crying_magnum_time_between_waves
    global level_seven_crying_magnum_time_between_spawns
    global level_seven_crying_magnum_amount_per_wave
    global level_seven_blaze_bot_time_between_spawns
    level_seven_crying_magnum_time_between_waves = 1800
    level_seven_crying_magnum_time_between_waves = 120
    level_seven_crying_magnum_amount_per_wave = 2
    level_blaze_bot_time_between_spawns = random.randint(200, 340)

def level_8_waves():
    global level_eight
    global level_eight_scorium_slug_time_between_spawns
    global level_eight_danger_blaze_bot_time_between_spawns
    global level_eight_danger_blaze_bot_amount
    global level_eight_danger_crying_magnum_time_between_spawns
    global level_eight_danger_crying_magnum_amount
    global DANGER
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    crying_magnum_behavior()
    crying_magnum_projectile_behavior()
    scorium_slug_behavior()
    scorium_slug_projectile_behavior()
    calculate_your_base_health()
    #print(DANGER)
    
    if level_eight_scorium_slug_time_between_spawns <= 0:
        summon_scorium_slug(levels[7][3][0][0])
        level_eight_scorium_slug_time_between_spawns = random.randint(200, 340)

    else:
        level_eight_scorium_slug_time_between_spawns -= 1

    if levels[7][4] < 12000:
        DANGER = True

    if DANGER == True:
        if levels[7][3][1][0][1] == "Deactivated":
            
            if level_eight_danger_blaze_bot_time_between_spawns <= 0:
                if level_eight_danger_blaze_bot_amount >= 0:
                    summon_blaze_bot(levels[7][3][1][1][0])
                    level_eight_danger_blaze_bot_amount -= 1
                    level_eight_danger_blaze_bot_time_between_spawns = 30
            else:
                level_eight_danger_blaze_bot_time_between_spawns -= 1

            if level_eight_danger_crying_magnum_time_between_spawns <= 0:
                if level_eight_danger_crying_magnum_amount >= 0:
                    summon_crying_magnum(levels[7][3][1][2][0])
                    level_eight_danger_crying_magnum_amount -= 1
                    level_eight_danger_crying_magnum_time_between_spawns = 75
            else:
                level_eight_danger_crying_magnum_time_between_spawns -= 1

            if level_eight_danger_blaze_bot_amount <= 0:
                if level_eight_danger_crying_magnum_amount <= 0:
                    levels[7][3][1][0][1] = "Activated"

def reset_level_8_waves():
    global DANGER
    global level_eight_scorium_slug_time_between_spawns
    global level_eight_danger_crying_magnum_amount
    global level_eight_danger_crying_magnum_time_between_spawns
    global level_eight_danger_blaze_bot_amount
    global level_eight_danger_blaze_bot_time_between_spawns
    DANGER = False
    print(DANGER)
    levels[7][3][1][0][1] = "Deactivated"
    level_eight_scorium_slug_time_between_spawns = random.randint(200, 340)
    level_eight_danger_blaze_bot_time_between_spawns = 30
    level_eight_danger_blaze_bot_amount = 20
    level_eight_danger_crying_magnum_time_between_spawns = 75
    level_eight_danger_crying_magnum_amount = 8

def level_9_waves():
    global level_nine
    global level_nine_blaze_bot_time_between_spawns
    global level_nine_crying_magnum_time_between_spawns
    global level_nine_scorium_slug_time_between_waves, level_nine_scorium_slug_time_between_spawns
    global level_nine_scorium_slug_amount_per_wave
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    scorium_slug_behavior()
    scorium_slug_projectile_behavior()
    crying_magnum_behavior()
    crying_magnum_projectile_behavior()
    calculate_your_base_health()

    if level_nine_scorium_slug_time_between_waves <= 0:
        
        if level_nine_scorium_slug_time_between_spawns <= 0:
            
            if level_nine_scorium_slug_amount_per_wave >= 1:
                summon_scorium_slug(levels[8][3][1][0])
                level_nine_scorium_slug_amount_per_wave -= 1
                level_nine_scorium_slug_time_between_spawns = 50
                
            else:
                level_nine_scorium_slug_time_between_waves = 400
                level_nine_scorium_slug_time_between_spawns = 50
                level_nine_scorium_slug_amount_per_wave = 2

        else:
            level_nine_scorium_slug_time_between_spawns -= 1

    else:
        level_nine_scorium_slug_time_between_waves -= 1
        #print(level_five_blaze_bot_time_between_waves)

    if level_nine_blaze_bot_time_between_spawns <= 0:
        summon_blaze_bot(levels[8][3][0][0])
        level_nine_blaze_bot_time_between_spawns = random.randint(100, 140)

    else:
        level_nine_blaze_bot_time_between_spawns -= 1

    if level_nine_crying_magnum_time_between_spawns <= 0:
        summon_crying_magnum(levels[8][3][2][0])
        level_nine_crying_magnum_time_between_spawns = random.randint(400, 440)

    else:
        level_nine_crying_magnum_time_between_spawns -= 1



def reset_level_9_waves():
    global level_nine_blaze_bot_time_between_spawns
    global level_nine_crying_magnum_time_between_spawns
    global level_nine_scorium_slug_time_between_waves
    global level_nine_scorium_slug_time_between_spawns
    global level_nine_scorium_slug_amount_per_wave
    level_nine_blaze_bot_time_between_spawns = random.randint(100, 140)
    level_nine_crying_magnum_time_between_spawns = random.randint(400, 440)
    level_nine_scorium_slug_time_between_waves = 400
    level_nine_scorium_slug_time_between_spawns = 50
    level_nine_scorium_slug_amount_per_wave = 2

def level_10_waves():
    global level_ten
    global level_ten_blaze_bot_time_between_spawns
    global level_ten_scorium_slug_time_between_spawns
    global level_ten_crying_magnum_time_between_spawns
    global BOSS
    blaze_bot_behavior()
    blaze_bot_projectile_behavior()
    crying_magnum_behavior()
    crying_magnum_projectile_behavior()
    scorium_slug_behavior()
    scorium_slug_projectile_behavior()
    magma_turtle_behavior()
    magma_turtle_projectile_behavior()
    calculate_your_base_health()
    #print(DANGER)

    if level_ten_blaze_bot_time_between_spawns <= 0:
        summon_blaze_bot(levels[9][3][0][0])
        level_ten_blaze_bot_time_between_spawns = 900

    else:
        level_ten_blaze_bot_time_between_spawns -= 1
    
    if level_ten_scorium_slug_time_between_spawns <= 0:
        summon_scorium_slug(levels[9][3][1][0])
        level_ten_scorium_slug_time_between_spawns = 900

    else:
        level_ten_scorium_slug_time_between_spawns -= 1

    if level_ten_crying_magnum_time_between_spawns <= 0:
        summon_crying_magnum(levels[9][3][2][0])
        level_ten_crying_magnum_time_between_spawns = 900

    else:
        level_ten_crying_magnum_time_between_spawns -= 1

    if levels[9][4] < 17500:
        BOSS = True

    if BOSS == True:
        if levels[9][3][3][0][1] == "Deactivated":
            summon_magma_turtle(levels[9][3][3][1][0])
            levels[9][3][3][0][1] = "Activated"
            boss_wave()

def reset_level_10_waves():
    global BOSS
    global level_ten_blaze_bot_time_between_spawns
    global level_ten_scorium_slug_time_between_spawns
    global level_ten_crying_magnum_time_between_spawns
    BOSS = False
    print(DANGER)
    levels[9][3][3][0][1] = "Deactivated"
    level_ten_blaze_bot_time_between_spawns = 0
    level_ten_scorium_slug_time_between_spawns = 300
    level_ten_crying_magnum_time_between_spawns = 600




def draw():
    global starting_base
    global equiped_base
    global coins
    global paper_owned, paper_won_per_level
    global globy_icon_slot
    global level_state, game_state
    global upgrade_menu_page, upgrade_menu_page_max
    global DANGER
    global BOSS
    screen.clear()
    
    if game_state == "Start Screen":
        screen.fill("teal")
        start_button.draw()
        lineup_button.draw()
        upgrade_button.draw()
        paper.pos = (530, 50)
        paper.draw()
        screen.draw.filled_rect(paper_amount_box, "yellow")
        screen.draw.textbox(str(paper_owned), paper_amount_box, color = "black")

    if game_state == "Level Select":
        screen.fill("yellow")
        back_button.draw()

        for level_button in level_buttons:
            level_button.draw()

        if levels[0][1] == "Locked":
            level_one_button.image = level_frames[0]
        elif levels[0][1] == "Unlocked" and levels[0][2] == "Incomplete":
            level_one_button.image = level_frames[1]
        elif levels[0][2] == "Complete":
            level_one_button.image = level_frames[2]
            
        if levels[1][1] == "Locked":
            level_two_button.image = level_frames[0]
        elif levels[1][1] == "Unlocked" and levels[1][2] == "Incomplete":
            level_two_button.image = level_frames[1]
        elif levels[1][2] == "Complete":
            level_two_button.image = level_frames[2]

        if levels[2][1] == "Locked":
            level_three_button.image = level_frames[0]
        elif levels[2][1] == "Unlocked" and levels[2][2] == "Incomplete":
            level_three_button.image = level_frames[1]
        elif levels[2][2] == "Complete":
            level_three_button.image = level_frames[2]

        if levels[3][1] == "Locked":
            level_four_button.image = level_frames[0]
        elif levels[3][1] == "Unlocked" and levels[3][2] == "Incomplete":
            level_four_button.image = level_frames[1]
        elif levels[3][2] == "Complete":
            level_four_button.image = level_frames[2]

        if levels[4][1] == "Locked":
            level_five_button.image = level_frames[0]
        elif levels[4][1] == "Unlocked" and levels[4][2] == "Incomplete":
            level_five_button.image = level_frames[1]
        elif levels[4][2] == "Complete":
            level_five_button.image = level_frames[2]

        if levels[5][1] == "Locked":
            level_six_button.image = level_frames[0]
        elif levels[5][1] == "Unlocked" and levels[5][2] == "Incomplete":
            level_six_button.image = level_frames[1]
        elif levels[5][2] == "Complete":
            level_six_button.image = level_frames[2]

        if levels[6][1] == "Locked":
            level_seven_button.image = level_frames[0]
        elif levels[6][1] == "Unlocked" and levels[6][2] == "Incomplete":
            level_seven_button.image = level_frames[1]
        elif levels[6][2] == "Complete":
            level_seven_button.image = level_frames[2]

        if levels[7][1] == "Locked":
            level_eight_button.image = level_frames[0]
        elif levels[7][1] == "Unlocked" and levels[7][2] == "Incomplete":
            level_eight_button.image = level_frames[1]
        elif levels[7][2] == "Complete":
            level_eight_button.image = level_frames[2]

        if levels[8][1] == "Locked":
            level_nine_button.image = level_frames[0]
        elif levels[8][1] == "Unlocked" and levels[8][2] == "Incomplete":
            level_nine_button.image = level_frames[1]
        elif levels[8][2] == "Complete":
            level_nine_button.image = level_frames[2]

        if levels[9][1] == "Locked":
            level_ten_button.image = level_frames[0]
        elif levels[9][1] == "Unlocked" and levels[9][2] == "Incomplete":
            level_ten_button.image = level_frames[1]
        elif levels[9][2] == "Complete":
            level_ten_button.image = level_frames[2]

    if game_state == "Lineup Menu":
        screen.fill("orange")
        back_button.draw()

        starting_x_value_for_equiped_icons = 70
        for empty_slot in lineup:
            empty_slot.pos = (starting_x_value_for_equiped_icons, 185)
            empty_slot.draw()
            starting_x_value_for_equiped_icons += 115

        if globy_icon.slot == "none":
            globy_icon.pos = (70, 300)
        elif globy_icon.slot == "one":
            globy_icon.pos = (70, 185)
        elif globy_icon.slot == "two":
            globy_icon.pos = (185, 185)
        elif globy_icon.slot == "three":
            globy_icon.pos = (300, 185)
        elif globy_icon.slot == "four":
            globy_icon.pos = (415, 185)
        elif globy_icon.slot == "five":
            globy_icon.pos = (530, 185)
            
        globy_icon.draw()


        if levels[2][2] == "Complete":
            if ergam_icon.slot == "none":
                ergam_icon.pos = (185, 300)
            elif ergam_icon.slot == "one":
                ergam_icon.pos = (70, 185)
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 185)
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 185)
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 185)
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 185)
                
            ergam_icon.draw()

        if levels[4][2] == "Complete":
            if zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (300, 300)
            elif zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 185)
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 185)
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 185)
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 185)
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 185)
                
            zap_ball_icon.draw()

        if levels[6][2] == "Complete":
            if zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (415, 300)
            elif zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 185)
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 185)
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 185)
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 185)
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 185)
                
            zlumpy_icon.draw()

        if levels[8][2] == "Complete":
            if guardo_icon.slot == "none":
                guardo_icon.pos = (530, 300)
            elif guardo_icon.slot == "one":
                guardo_icon.pos = (70, 185)
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 185)
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 185)
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 185)
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 185)
                
            guardo_icon.draw()

    if game_state == "Upgrade Menu":
        screen.fill("dark green")
        back_button.draw()
        paper.draw()
        screen.draw.filled_rect(paper_amount_box, "yellow")
        screen.draw.textbox(str(paper_owned), paper_amount_box, color = "black")


        if upgrade_menu_page == 1:
            forward_arrow.draw()
        
            money_generation_speed_icon.pos = (70, 185)
            money_generation_speed_icon.draw()
            upgrade_money_generation_speed_button.pos = (470, 185)
            upgrade_money_generation_speed_button.draw()
            screen.draw.filled_rect(money_generation_speed_upgrade_cost, "gold" )
            screen.draw.textbox("Cost: " + str(money_generation_speed_icon.upgrade_cost), money_generation_speed_upgrade_cost, color = "black")
            screen.draw.filled_rect(money_generation_speed_level_box, "yellow" )
            if money_generation_speed_icon.level < 10:
                screen.draw.textbox("Level: " + str(money_generation_speed_icon.level), money_generation_speed_level_box, color = "black" )
            else:
                screen.draw.textbox("Level: MAX", money_generation_speed_level_box, color = "black" )

            enemy_death_money_icon.pos = (70, 300)
            enemy_death_money_icon.draw()
            upgrade_enemy_death_money_button.pos = (470, 300)
            upgrade_enemy_death_money_button.draw()
            screen.draw.filled_rect(enemy_death_money_upgrade_cost, "gold" )
            screen.draw.textbox("Cost: " + str(enemy_death_money_icon.upgrade_cost), enemy_death_money_upgrade_cost, color = "black")
            screen.draw.filled_rect(enemy_death_money_level_box, "yellow" )
            if enemy_death_money_icon.level < 10:
                screen.draw.textbox("Level: " + str(enemy_death_money_icon.level), enemy_death_money_level_box, color = "black" )
            else:
                screen.draw.textbox("Level: MAX", enemy_death_money_level_box, color = "black" )
            
            globy_icon.pos = (70, 415)
            globy_icon.draw()
            upgrade_globy_button.pos = (470, 415)
            upgrade_globy_button.draw()
            screen.draw.filled_rect(globy_upgrade_cost, "gold" )
            screen.draw.textbox("Cost: " + str(globy_icon.upgrade_cost), globy_upgrade_cost, color = "black")
            screen.draw.filled_rect(globy_level_box, "yellow" )
            if globy_icon.level < 10:
                screen.draw.textbox("Level: " + str(globy_icon.level), globy_level_box, color = "black" )
            else:
                screen.draw.textbox("Level: MAX", globy_level_box, color = "black" )

        if upgrade_menu_page == 2:
            if levels[4][2] == "Complete":
                forward_arrow.draw()
            backward_arrow.draw()

            if levels[2][2] == "Complete":
                ergam_icon.pos = (70, 415)
                ergam_icon.draw()
                upgrade_ergam_button.pos = (470, 415)
                upgrade_ergam_button.draw()
                screen.draw.filled_rect(ergam_upgrade_cost, "gold" )
                screen.draw.textbox("Cost: " + str(ergam_icon.upgrade_cost), ergam_upgrade_cost, color = "black")
                screen.draw.filled_rect(ergam_level_box, "yellow" )
                if ergam_icon.level < 10:
                    screen.draw.textbox("Level: " + str(ergam_icon.level), ergam_level_box, color = "black" )
                else:
                    screen.draw.textbox("Level: MAX", ergam_level_box, color = "black" )

            base_health_icon.pos = (70, 185)
            base_health_icon.draw()
            upgrade_base_health_button.pos = (470, 185)
            upgrade_base_health_button.draw()
            screen.draw.filled_rect(base_health_upgrade_cost, "gold" )
            screen.draw.textbox("Cost: " + str(base_health_icon.upgrade_cost), base_health_upgrade_cost, color = "black")
            screen.draw.filled_rect(base_health_level_box, "yellow" )
            if base_health_icon.level < 10:
                screen.draw.textbox("Level: " + str(base_health_icon.level), base_health_level_box, color = "black" )
            else:
                screen.draw.textbox("Level: MAX", base_health_level_box, color = "black" )

            paper_per_level_icon.pos = (70, 300)
            paper_per_level_icon.draw()
            upgrade_paper_per_level_button.pos = (470, 300)
            upgrade_paper_per_level_button.draw()
            screen.draw.filled_rect(paper_per_level_upgrade_cost, "gold" )
            screen.draw.textbox("Cost: " + str(paper_per_level_icon.upgrade_cost), paper_per_level_upgrade_cost, color = "black")
            screen.draw.filled_rect(paper_per_level_level_box, "yellow" )
            if paper_per_level_icon.level < 10:
                screen.draw.textbox("Level: " + str(paper_per_level_icon.level), paper_per_level_level_box, color = "black" )
            else:
                screen.draw.textbox("Level: MAX", paper_per_level_level_box, color = "black" )

        if upgrade_menu_page == 3:
            backward_arrow.draw()

            if levels[4][2] == "Complete":
                zap_ball_icon.pos = (70, 185)
                zap_ball_icon.draw()
                upgrade_zap_ball_button.pos = (470, 185)
                upgrade_zap_ball_button.draw()
                screen.draw.filled_rect(zap_ball_upgrade_cost, "gold" )
                screen.draw.textbox("Cost: " + str(zap_ball_icon.upgrade_cost), zap_ball_upgrade_cost, color = "black")
                screen.draw.filled_rect(zap_ball_level_box, "yellow" )
                if zap_ball_icon.level < 10:
                    screen.draw.textbox("Level: " + str(zap_ball_icon.level), zap_ball_level_box, color = "black" )
                else:
                    screen.draw.textbox("Level: MAX", zap_ball_level_box, color = "black" )

            if levels[6][2] == "Complete":
                zlumpy_icon.pos = (70, 300)
                zlumpy_icon.draw()
                upgrade_zlumpy_button.pos = (470, 300)
                upgrade_zlumpy_button.draw()
                screen.draw.filled_rect(zlumpy_upgrade_cost, "gold" )
                screen.draw.textbox("Cost: " + str(zlumpy_icon.upgrade_cost), zlumpy_upgrade_cost, color = "black")
                screen.draw.filled_rect(zlumpy_level_box, "yellow" )
                if zlumpy_icon.level < 10:
                    screen.draw.textbox("Level: " + str(zlumpy_icon.level), zlumpy_level_box, color = "black" )
                else:
                    screen.draw.textbox("Level: MAX", zlumpy_level_box, color = "black" )

            if levels[8][2] == "Complete":
                guardo_icon.pos = (70, 415)
                guardo_icon.draw()
                upgrade_guardo_button.pos = (470, 415)
                upgrade_guardo_button.draw()
                screen.draw.filled_rect(guardo_upgrade_cost, "gold" )
                screen.draw.textbox("Cost: " + str(guardo_icon.upgrade_cost), guardo_upgrade_cost, color = "black")
                screen.draw.filled_rect(guardo_level_box, "yellow" )
                if guardo_icon.level < 10:
                    screen.draw.textbox("Level: " + str(guardo_icon.level), guardo_level_box, color = "black" )
                else:
                    screen.draw.textbox("Level: MAX", guardo_level_box, color = "black" )

    if game_state == "Level 1":
        screen.fill("sky blue")
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, "green")
        level_one_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()

        if level_state == "Beat Level 1":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[0][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()
            

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[0][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )

        
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for ergam in ergams:
                ergam.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

    
    if game_state == "Level 2":
        screen.fill("sky blue")
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, "green")
        level_two_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()

        if level_state == "Beat Level 2":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[1][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[1][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )
                
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for ergam in ergams:
                ergam.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for scorium_slug in scorium_slugs:
                scorium_slug.draw()

            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

            for scorium_slug_projectile in scorium_slug_projectiles:
                scorium_slug_projectile.draw()

    if game_state == "Level 3":
        screen.fill((255, 105, 180))
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, "light gray")
        level_three_and_four_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()

        if level_state == "Beat Level 3":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[2][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[2][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )
                
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for ergam in ergams:
                ergam.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for scorium_slug in scorium_slugs:
                scorium_slug.draw()

            for crying_magnum in crying_magnums:
                crying_magnum.draw()

            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

            for scorium_slug_projectile in scorium_slug_projectiles:
                scorium_slug_projectile.draw()

            for crying_magnum_projectile in crying_magnum_projectiles:
                crying_magnum_projectile.draw()


    if game_state == "Level 4":
        screen.fill((255, 105, 220))
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, "gray")
        level_three_and_four_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()

        if level_state == "Beat Level 4":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[3][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[3][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )
                
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for ergam in ergams:
                ergam.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for scorium_slug in scorium_slugs:
                scorium_slug.draw()

            for crying_magnum in crying_magnums:
                crying_magnum.draw()

            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

            for scorium_slug_projectile in scorium_slug_projectiles:
                scorium_slug_projectile.draw()

            for crying_magnum_projectile in crying_magnum_projectiles:
                crying_magnum_projectile.draw()

    if game_state == "Level 5":
        screen.fill((204, 0, 0))
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, (32, 32, 32))
        level_five_and_six_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()

        if level_state == "Beat Level 5":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[4][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[4][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )
                
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for ergam in ergams:
                ergam.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for crying_magnum in crying_magnums:
                crying_magnum.draw()

            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

            for crying_magnum_projectile in crying_magnum_projectiles:
                crying_magnum_projectile.draw()


    if game_state == "Level 6":
        screen.fill((204, 0, 0))
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, (32, 32, 32))
        level_five_and_six_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()

        if level_state == "Beat Level 6":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[5][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[5][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )
                
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for ergam in ergams:
                ergam.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for scorium_slug in scorium_slugs:
                scorium_slug.draw()


            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

            for scorium_slug_projectile in scorium_slug_projectiles:
                scorium_slug_projectile.draw()


    
    if game_state == "Level 7":
        screen.fill((204, 0, 0))
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, (32, 32, 32))
        level_five_and_six_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()

        if level_state == "Beat Level 7":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[6][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[6][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )
                
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for ergam in ergams:
                ergam.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for crying_magnum in crying_magnums:
                crying_magnum.draw()

            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

            for crying_magnum_projectile in crying_magnum_projectiles:
                crying_magnum_projectile.draw()

    
    if game_state == "Level 8":
        screen.fill((255, 105, 220))
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, "gray")
        level_two_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()

        if level_state == "Beat Level 8":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[7][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":

            if DANGER == True:
                danger_icon.draw()

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[7][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )
                
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for ergam in ergams:
                ergam.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for scorium_slug in scorium_slugs:
                scorium_slug.draw()

            for crying_magnum in crying_magnums:
                crying_magnum.draw()

            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

            for scorium_slug_projectile in scorium_slug_projectiles:
                scorium_slug_projectile.draw()

            for crying_magnum_projectile in crying_magnum_projectiles:
                crying_magnum_projectile.draw()


    if game_state == "Level 9":
        screen.fill((204, 0, 0))
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, (32, 32, 32))
        level_five_and_six_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()

        if level_state == "Beat Level 9":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[8][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[8][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )
                
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for ergam in ergams:
                ergam.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for scorium_slug in scorium_slugs:
                scorium_slug.draw()

            for crying_magnum in crying_magnums:
                crying_magnum.draw()


            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

            for scorium_slug_projectile in scorium_slug_projectiles:
                scorium_slug_projectile.draw()

            for crying_magnum_projectile in crying_magnum_projectiles:
                crying_magnum_projectile.draw()

    
    if game_state == "Level 10":
        screen.fill((204, 0, 0))
        ground = Rect(0, 400, 600, 600)
        screen.draw.filled_rect(ground, (32, 32, 32))
        level_five_and_six_enemy_base.draw()

        if equiped_base == 0:
            starting_base.draw()


        if level_state == "Beat Level 10":
            back_button.draw()
            #screen.draw.rect(victory_screen, "gold" )
            screen.draw.textbox(str("VICTORY"), victory_screen, color = ("black") )
            screen.draw.filled_rect(paper_won_per_level_box, "gold")
            paper_won_per_level = levels[9][5]
            screen.draw.textbox("+" + str(int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) ) ), paper_won_per_level_box, color = ("black") )
            paper.pos = (350, 425)
            paper.draw()

        if level_state == "Game Over":
            back_button.draw()
            #screen.draw.rect(game_over_screen, "black")
            screen.draw.textbox(str("Defeat"), game_over_screen, color = ("black"))

        if level_state == "Paused":
            in_game_menu.draw()
            back_to_game_button.draw()
            back_to_main_menu_button.draw()

        if level_state == "Playing":
            if BOSS == True:
                danger_icon.draw()

            pause_button.draw()
            coins_box.draw()
            screen.draw.rect(coins_box_outline, (0, 0, 0))
            screen.draw.textbox(str(coins), coins_box_outline, color = ("black") )
            your_base_health_box.draw()
            screen.draw.rect(your_base_health_box_outline, (0, 0, 0))
            enemy_base_health_box.draw()
            screen.draw.rect(enemy_base_health_box_outline, (0, 0, 0) )
            screen.draw.textbox(str(levels[9][4]), enemy_base_health_box_outline, color = ("black") )

            if equiped_base == 0:
                screen.draw.textbox(str(starting_base.health), your_base_health_box_outline, color = ("black") )
                
            starting_x_value_for_equiped_icons = 70
            for empty_slot in lineup:
                empty_slot.pos = (starting_x_value_for_equiped_icons, 530)
                empty_slot.draw()
                starting_x_value_for_equiped_icons += 115

            if globy_icon.slot == "one":
                globy_icon.pos = (70, 530)
                globy_icon.draw()
            elif globy_icon.slot == "two":
                globy_icon.pos = (185, 530)
                globy_icon.draw()
            elif globy_icon.slot == "three":
                globy_icon.pos = (300, 530)
                globy_icon.draw()
            elif globy_icon.slot == "four":
                globy_icon.pos = (415, 530)
                globy_icon.draw()
            elif globy_icon.slot == "five":
                globy_icon.pos = (530, 530)
                globy_icon.draw()
            elif globy_icon.slot == "none":
                globy_icon.pos = (10000, 10000)

            if ergam_icon.slot == "one":
                ergam_icon.pos = (70, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "two":
                ergam_icon.pos = (185, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "three":
                ergam_icon.pos = (300, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "four":
                ergam_icon.pos = (415, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "five":
                ergam_icon.pos = (530, 530)
                ergam_icon.draw()
            elif ergam_icon.slot == "none":
                ergam_icon.pos = (10000, 10000)

            if zap_ball_icon.slot == "one":
                zap_ball_icon.pos = (70, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "two":
                zap_ball_icon.pos = (185, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "three":
                zap_ball_icon.pos = (300, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "four":
                zap_ball_icon.pos = (415, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "five":
                zap_ball_icon.pos = (530, 530)
                zap_ball_icon.draw()
            elif zap_ball_icon.slot == "none":
                zap_ball_icon.pos = (10000, 10000)

            if zlumpy_icon.slot == "one":
                zlumpy_icon.pos = (70, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "two":
                zlumpy_icon.pos = (185, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "three":
                zlumpy_icon.pos = (300, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "four":
                zlumpy_icon.pos = (415, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "five":
                zlumpy_icon.pos = (530, 530)
                zlumpy_icon.draw()
            elif zlumpy_icon.slot == "none":
                zlumpy_icon.pos = (10000, 10000)

            if guardo_icon.slot == "one":
                guardo_icon.pos = (70, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "two":
                guardo_icon.pos = (185, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "three":
                guardo_icon.pos = (300, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "four":
                guardo_icon.pos = (415, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "five":
                guardo_icon.pos = (530, 530)
                guardo_icon.draw()
            elif guardo_icon.slot == "none":
                guardo_icon.pos = (10000, 10000)

            for globy in globies:
                globy.draw()

            for zap_ball in zap_balls:
                zap_ball.draw()

            for ergam in ergams:
                ergam.draw()

            for zlumpy in zlumpies:
                zlumpy.draw()

            for guardo in guardos:
                guardo.draw()

            for blaze_bot in blaze_bots:
                blaze_bot.draw()

            for scorium_slug in scorium_slugs:
                scorium_slug.draw()

            for crying_magnum in crying_magnums:
                crying_magnum.draw()


            for globy_projectile in globy_projectiles:
                globy_projectile.draw()

            for zlumpy_projectile in zlumpy_projectiles:
                zlumpy_projectile.draw()

            for guardo_projectile in guardo_projectiles:
                guardo_projectile.draw()

            for blaze_bot_projectile in blaze_bot_projectiles:
                blaze_bot_projectile.draw()

            for scorium_slug_projectile in scorium_slug_projectiles:
                scorium_slug_projectile.draw()

            for crying_magnum_projectile in crying_magnum_projectiles:
                crying_magnum_projectile.draw()

            for magma_turtle in magma_turtles:
                magma_turtle.draw()

            for magma_turtle_projectile in magma_turtle_projectiles:
                magma_turtle_projectile.draw()
        





#icon_selected = False
def on_mouse_down(pos):
    global equiped_base
    global level_state, game_state
    global start_button, pause_button
    global coins, coin_delay
    global paper_owned, paper_won_per_level
    global upgrade_menu_page, upgrade_menu_page_max

    if game_state == "Start Screen":
        
        if start_button.collidepoint(pos):
            game_state = "Level Select"

        if lineup_button.collidepoint(pos):
            game_state = "Lineup Menu"

        if upgrade_button.collidepoint(pos):
            game_state = "Upgrade Menu"

    if game_state == "Level Select":

        if back_button.collidepoint(pos):
            game_state = "Start Screen"

        if level_one_button.collidepoint(pos):
            reset_level_1_waves()
            game_state = "Level 1"
            level_state = "Playing"
            coins = 0
            coin_delay = 4
            globies.clear()
            globy_projectiles.clear()
            ergams.clear()
            zap_balls.clear()
            zlumpies.clear()
            zlumpy_projectiles.clear()
            guardos.clear()
            guardo_projectiles.clear()
            blaze_bots.clear()
            blaze_bot_projectiles.clear()
            scorium_slugs.clear()
            scorium_slug_projectiles.clear()
            crying_magnums.clear()
            crying_magnum_projectiles.clear()
            levels[0][4] = 1000

            if equiped_base == 0:
                your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

        if levels[1][1] == "Unlocked":
            if level_two_button.collidepoint(pos):
                reset_level_2_waves()
                game_state = "Level 2"
                level_state = "Playing"
                coins = 0
                coin_delay = 5
                globies.clear()
                globy_projectiles.clear()
                ergams.clear()
                zap_balls.clear()
                zlumpies.clear()
                zlumpy_projectiles.clear()
                guardos.clear()
                guardo_projectiles.clear()
                blaze_bots.clear()
                blaze_bot_projectiles.clear()
                scorium_slugs.clear()
                scorium_slug_projectiles.clear()
                crying_magnums.clear()
                crying_magnum_projectiles.clear()
                levels[1][4] = 1500

                if equiped_base == 0:
                    your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

        if levels[2][1] == "Unlocked":
            if level_three_button.collidepoint(pos):
                reset_level_3_waves()
                game_state = "Level 3"
                level_state = "Playing"
                coins = 0
                coin_delay = 5
                globies.clear()
                globy_projectiles.clear()
                ergams.clear()
                zap_balls.clear()
                zlumpies.clear()
                zlumpy_projectiles.clear()
                guardos.clear()
                guardo_projectiles.clear()
                blaze_bots.clear()
                blaze_bot_projectiles.clear()
                scorium_slugs.clear()
                scorium_slug_projectiles.clear()
                crying_magnums.clear()
                crying_magnum_projectiles.clear()
                levels[2][4] = 2000

                if equiped_base == 0:
                    your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

        if levels[3][1] == "Unlocked":
            if level_four_button.collidepoint(pos):
                reset_level_4_waves()
                game_state = "Level 4"
                level_state = "Playing"
                coins = 0
                coin_delay = 5
                globies.clear()
                globy_projectiles.clear()
                ergams.clear()
                zap_balls.clear()
                zlumpies.clear()
                zlumpy_projectiles.clear()
                guardos.clear()
                guardo_projectiles.clear()
                blaze_bots.clear()
                blaze_bot_projectiles.clear()
                scorium_slugs.clear()
                scorium_slug_projectiles.clear()
                crying_magnums.clear()
                crying_magnum_projectiles.clear()
                levels[3][4] = 3000

                if equiped_base == 0:
                    your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

        if levels[4][1] == "Unlocked":
            if level_five_button.collidepoint(pos):
                reset_level_5_waves()
                game_state = "Level 5"
                level_state = "Playing"
                coins = 0
                coin_delay = 5
                globies.clear()
                globy_projectiles.clear()
                ergams.clear()
                zap_balls.clear()
                zlumpies.clear()
                zlumpy_projectiles.clear()
                guardos.clear()
                guardo_projectiles.clear()
                blaze_bots.clear()
                blaze_bot_projectiles.clear()
                scorium_slugs.clear()
                scorium_slug_projectiles.clear()
                crying_magnums.clear()
                crying_magnum_projectiles.clear()
                levels[4][4] = 5000

                if equiped_base == 0:
                    your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

        if levels[5][1] == "Unlocked":
            if level_six_button.collidepoint(pos):
                reset_level_6_waves()
                game_state = "Level 6"
                level_state = "Playing"
                coins = 0
                coin_delay = 5
                globies.clear()
                globy_projectiles.clear()
                ergams.clear()
                zap_balls.clear()
                zlumpies.clear()
                zlumpy_projectiles.clear()
                guardos.clear()
                guardo_projectiles.clear()
                blaze_bots.clear()
                blaze_bot_projectiles.clear()
                scorium_slugs.clear()
                scorium_slug_projectiles.clear()
                crying_magnums.clear()
                crying_magnum_projectiles.clear()
                levels[5][4] = 7500

                if equiped_base == 0:
                    your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

        if levels[6][1] == "Unlocked":
            if level_seven_button.collidepoint(pos):
                reset_level_7_waves()
                game_state = "Level 7"
                level_state = "Playing"
                coins = 0
                coin_delay = 5
                globies.clear()
                globy_projectiles.clear()
                ergams.clear()
                zap_balls.clear()
                zlumpies.clear()
                zlumpy_projectiles.clear()
                guardos.clear()
                guardo_projectiles.clear()
                blaze_bots.clear()
                blaze_bot_projectiles.clear()
                scorium_slugs.clear()
                scorium_slug_projectiles.clear()
                crying_magnums.clear()
                crying_magnum_projectiles.clear()
                levels[6][4] = 10000

                if equiped_base == 0:
                    your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

        if levels[7][1] == "Unlocked":
            if level_eight_button.collidepoint(pos):
                reset_level_8_waves()
                game_state = "Level 8"
                level_state = "Playing"
                coins = 0
                coin_delay = 5
                globies.clear()
                globy_projectiles.clear()
                ergams.clear()
                zap_balls.clear()
                zlumpies.clear()
                zlumpy_projectiles.clear()
                guardos.clear()
                guardo_projectiles.clear()
                blaze_bots.clear()
                blaze_bot_projectiles.clear()
                scorium_slugs.clear()
                scorium_slug_projectiles.clear()
                crying_magnums.clear()
                crying_magnum_projectiles.clear()
                levels[7][4] = 12000

                if equiped_base == 0:
                    your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

        if levels[8][1] == "Unlocked":
            if level_nine_button.collidepoint(pos):
                reset_level_9_waves()
                game_state = "Level 9"
                level_state = "Playing"
                coins = 0
                coin_delay = 5
                globies.clear()
                globy_projectiles.clear()
                ergams.clear()
                zap_balls.clear()
                zlumpies.clear()
                zlumpy_projectiles.clear()
                guardos.clear()
                guardo_projectiles.clear()
                blaze_bots.clear()
                blaze_bot_projectiles.clear()
                scorium_slugs.clear()
                scorium_slug_projectiles.clear()
                crying_magnums.clear()
                crying_magnum_projectiles.clear()
                levels[8][4] = 15000

                if equiped_base == 0:
                    your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

        if levels[9][1] == "Unlocked":
            if level_ten_button.collidepoint(pos):
                reset_level_10_waves()
                game_state = "Level 10"
                level_state = "Playing"
                coins = 0
                coin_delay = 5
                globies.clear()
                globy_projectiles.clear()
                ergams.clear()
                zap_balls.clear()
                zlumpies.clear()
                zlumpy_projectiles.clear()
                guardos.clear()
                guardo_projectiles.clear()
                blaze_bots.clear()
                blaze_bot_projectiles.clear()
                scorium_slugs.clear()
                scorium_slug_projectiles.clear()
                crying_magnums.clear()
                crying_magnum_projectiles.clear()
                magma_turtles.clear()
                magma_turtle_projectiles.clear()
                levels[9][4] = 17500

                if equiped_base == 0:
                    your_bases[0].health = int(1000 + ( (base_health_icon.level - 1) * 500) )

    if game_state == "Lineup Menu":

        if back_button.collidepoint(pos):
            game_state = "Start Screen"

        if globy_icon.collidepoint(pos):
            globy_icon.equip_menu_mode = "Selected"
            ergam_icon.equip_menu_mode = "Unselected"
            zap_ball_icon.equip_menu_mode = "Unselected"
            zlumpy_icon.equip_menu_mode = "Unselected"
            guardo_icon.equip_menu_mode = "Unselected"

        if ergam_icon.collidepoint(pos):
            ergam_icon.equip_menu_mode = "Selected"
            globy_icon.equip_menu_mode = "Unselected"
            zap_ball_icon.equip_menu_mode = "Unselected"
            zlumpy_icon.equip_menu_mode = "Unselected"
            guardo_icon.equip_menu_mode = "Unselected"

        if zap_ball_icon.collidepoint(pos):
            zap_ball_icon.equip_menu_mode = "Selected"
            globy_icon.equip_menu_mode = "Unselected"
            ergam_icon.equip_menu_mode = "Unselected"
            zlumpy_icon.equip_menu_mode = "Unselected"
            guardo_icon.equip_menu_mode = "Unselected"

        if zlumpy_icon.collidepoint(pos):
            zlumpy_icon.equip_menu_mode = "Selected"
            globy_icon.equip_menu_mode = "Unselected"
            ergam_icon.equip_menu_mode = "Unselected"
            zap_ball_icon.equip_menu_mode = "Unselected"
            guardo_icon.equip_menu_mode = "Unselected"

        if guardo_icon.collidepoint(pos):
            guardo_icon.equip_menu_mode = "Selected"
            globy_icon.equip_menu_mode = "Unselected"
            ergam_icon.equip_menu_mode = "Unselected"
            zap_ball_icon.equip_menu_mode = "Unselected"
            zlumpy_icon.equip_menu_mode = "Unselected"

    if game_state == "Upgrade Menu":

        if back_button.collidepoint(pos):
            game_state = "Start Screen"

        upgrade_menu_page_max = 2
        if levels[4][2] == "Complete":
            upgrade_menu_page_max = 3
 
        if upgrade_menu_page != upgrade_menu_page_max:
            if forward_arrow.collidepoint(pos):
                if upgrade_menu_page < upgrade_menu_page_max:
                    upgrade_menu_page += 1
                
        if upgrade_menu_page != 1:
            if backward_arrow.collidepoint(pos):
                if upgrade_menu_page > 1:
                    upgrade_menu_page -=1

        if upgrade_menu_page == 1:

            if upgrade_globy_button.collidepoint(pos):
                if globy_icon.level < 10:
                    if paper_owned >= globy_icon.upgrade_cost:
                        globy_icon.level += 1
                        print(globy_icon.level)
                        paper_owned -= globy_icon.upgrade_cost
                        if globy_icon.level == 10:
                            globy_icon.upgrade_cost = "N/A"
                        else:
                            globy_icon.upgrade_cost = int(globy_icon.upgrade_cost * 1.5)

            if upgrade_money_generation_speed_button.collidepoint(pos):
                if money_generation_speed_icon.level < 10:
                    if paper_owned >= money_generation_speed_icon.upgrade_cost:
                        money_generation_speed_icon.level += 1
                        print(money_generation_speed_icon.level)
                        paper_owned -= money_generation_speed_icon.upgrade_cost
                        if money_generation_speed_icon.level == 10:
                            money_generation_speed_icon.upgrade_cost = "N/A"
                        else:
                            money_generation_speed_icon.upgrade_cost = int(money_generation_speed_icon.upgrade_cost * 1.5)

            if upgrade_enemy_death_money_button.collidepoint(pos):
                if enemy_death_money_icon.level < 10:
                    if paper_owned >= enemy_death_money_icon.upgrade_cost:
                        enemy_death_money_icon.level += 1
                        print(enemy_death_money_icon.level)
                        paper_owned -= enemy_death_money_icon.upgrade_cost
                        if enemy_death_money_icon.level == 10:
                            enemy_death_money_icon.upgrade_cost = "N/A"
                        else:
                            enemy_death_money_icon.upgrade_cost = int(enemy_death_money_icon.upgrade_cost * 1.5)

        if upgrade_menu_page == 2:

            if levels[2][2] == "Complete":

                if upgrade_ergam_button.collidepoint(pos):
                    if ergam_icon.level < 10:
                        if paper_owned >= ergam_icon.upgrade_cost:
                            ergam_icon.level += 1
                            print(ergam_icon.level)
                            paper_owned -= ergam_icon.upgrade_cost
                            if ergam_icon.level == 10:
                                ergam_icon.upgrade_cost = "N/A"
                            else:
                                ergam_icon.upgrade_cost = int(ergam_icon.upgrade_cost * 1.5)

            if upgrade_base_health_button.collidepoint(pos):
                if base_health_icon.level < 10:
                    if paper_owned >= base_health_icon.upgrade_cost:
                        base_health_icon.level += 1
                        print(base_health_icon.level)
                        paper_owned -= base_health_icon.upgrade_cost
                        if base_health_icon.level == 10:
                            base_health_icon.upgrade_cost = "N/A"
                        else:
                            base_health_icon.upgrade_cost = int(base_health_icon.upgrade_cost * 1.5)

            if upgrade_paper_per_level_button.collidepoint(pos):
                if paper_per_level_icon.level < 10:
                    if paper_owned >= paper_per_level_icon.upgrade_cost:
                        paper_per_level_icon.level += 1
                        print(paper_per_level_icon.level)
                        paper_owned -= paper_per_level_icon.upgrade_cost
                        if paper_per_level_icon.level == 10:
                            paper_per_level_icon.upgrade_cost = "N/A"
                        else:
                            paper_per_level_icon.upgrade_cost = int(paper_per_level_icon.upgrade_cost * 1.5)

        if upgrade_menu_page == 3:

            if levels[4][2] == "Complete":

                if upgrade_zap_ball_button.collidepoint(pos):
                    if zap_ball_icon.level < 10:
                        if paper_owned >= zap_ball_icon.upgrade_cost:
                            zap_ball_icon.level += 1
                            print(zap_ball_icon.level)
                            paper_owned -= zap_ball_icon.upgrade_cost
                            if zap_ball_icon.level == 10:
                                zap_ball_icon.upgrade_cost = "N/A"
                            else:
                                zap_ball_icon.upgrade_cost = int(zap_ball_icon.upgrade_cost * 1.5)

            if levels[6][2] == "Complete":

                if upgrade_zlumpy_button.collidepoint(pos):
                    if zlumpy_icon.level < 10:
                        if paper_owned >= zlumpy_icon.upgrade_cost:
                            zlumpy_icon.level += 1
                            paper_owned -= zlumpy_icon.upgrade_cost
                            if zlumpy_icon.level == 10:
                                zlumpy_icon.upgrade_cost = "N/A"
                            else:
                                #print(zlumpy_icon.upgrade_cost * 1.5)
                                zlumpy_icon.upgrade_cost = int(zlumpy_icon.upgrade_cost * 1.5)

            if levels[8][2] == "Complete":

                if upgrade_guardo_button.collidepoint(pos):
                    if guardo_icon.level < 10:
                        if paper_owned >= guardo_icon.upgrade_cost:
                            guardo_icon.level += 1
                            print(guardo_icon.level)
                            paper_owned -= guardo_icon.upgrade_cost
                            if guardo_icon.level == 10:
                                guardo_icon.upgrade_cost = "N/A"
                            else:
                                guardo_icon.upgrade_cost = int(guardo_icon.upgrade_cost * 1.5)

    if game_state == "Level 1":

        if level_state == "Playing":

            if pause_button.collidepoint(pos):
                level_state = "Paused"


            if globy_icon.collidepoint(pos) and coins >= 50:
                summon_globy()
            if ergam_icon.collidepoint(pos) and coins >= 150:
                summon_ergam()
            if zap_ball_icon.collidepoint(pos) and coins >= 200:
                summon_zap_ball()
            if zlumpy_icon.collidepoint(pos) and coins >= 75:
                summon_zlumpy()
            if guardo_icon.collidepoint(pos) and coins >= 100:
                summon_guardo()

        if level_state == "Paused":

            if back_to_game_button.collidepoint(pos):
                level_state = "Playing"

            if back_to_main_menu_button.collidepoint(pos):
                level_state = "Playing"
                game_state = "Start Screen"

        if level_state == "Beat Level 1":

            if back_button.collidepoint(pos):
                game_state = "Level Select"
                paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                paper_won_per_level = 0
                levels[0][5] = int(levels[0][5] * 0.9)

        if level_state == "Game Over":

            if back_button.collidepoint(pos):
                game_state = "Level Select"
                

    if game_state == "Level 2":

        if level_state == "Playing":

            if pause_button.collidepoint(pos):
                level_state = "Paused"


            if globy_icon.collidepoint(pos) and coins >= 50:
                summon_globy()
            if ergam_icon.collidepoint(pos) and coins >= 150:
                summon_ergam()
            if zap_ball_icon.collidepoint(pos) and coins >= 200:
                summon_zap_ball()
            if zlumpy_icon.collidepoint(pos) and coins >= 75:
                summon_zlumpy()
            if guardo_icon.collidepoint(pos) and coins >= 100:
                summon_guardo()

        if level_state == "Paused":

            if back_to_game_button.collidepoint(pos):
                level_state = "Playing"

            if back_to_main_menu_button.collidepoint(pos):
                level_state = "Playing"
                game_state = "Start Screen"

        if level_state == "Beat Level 2":

            if back_button.collidepoint(pos):
                game_state = "Level Select"
                paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                paper_won_per_level = 0
                levels[1][5] = int(levels[1][5] * 0.9)

        if level_state == "Game Over":

            if back_button.collidepoint(pos):
                game_state = "Level Select"
                

    if game_state == "Level 3":

            if level_state == "Playing":

                if pause_button.collidepoint(pos):
                    level_state = "Paused"


                if globy_icon.collidepoint(pos) and coins >= 50:
                    summon_globy()
                if ergam_icon.collidepoint(pos) and coins >= 150:
                    summon_ergam()
                if zap_ball_icon.collidepoint(pos) and coins >= 200:
                    summon_zap_ball()
                if zlumpy_icon.collidepoint(pos) and coins >= 75:
                    summon_zlumpy()
                if guardo_icon.collidepoint(pos) and coins >= 100:
                    summon_guardo()

            if level_state == "Paused":

                if back_to_game_button.collidepoint(pos):
                    level_state = "Playing"

                if back_to_main_menu_button.collidepoint(pos):
                    level_state = "Playing"
                    game_state = "Start Screen"

            if level_state == "Beat Level 3":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"
                    paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                    paper_won_per_level = 0
                    levels[2][5] = int(levels[2][5] * 0.9)

            if level_state == "Game Over":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"

    if game_state == "Level 4":

            if level_state == "Playing":

                if pause_button.collidepoint(pos):
                    level_state = "Paused"


                if globy_icon.collidepoint(pos) and coins >= 50:
                    summon_globy()
                if ergam_icon.collidepoint(pos) and coins >= 150:
                    summon_ergam()
                if zap_ball_icon.collidepoint(pos) and coins >= 200:
                    summon_zap_ball()
                if zlumpy_icon.collidepoint(pos) and coins >= 75:
                    summon_zlumpy()
                if guardo_icon.collidepoint(pos) and coins >= 100:
                    summon_guardo()

            if level_state == "Paused":

                if back_to_game_button.collidepoint(pos):
                    level_state = "Playing"

                if back_to_main_menu_button.collidepoint(pos):
                    level_state = "Playing"
                    game_state = "Start Screen"

            if level_state == "Beat Level 4":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"
                    paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                    paper_won_per_level = 0
                    levels[3][5] = int(levels[3][5] * 0.9)

            if level_state == "Game Over":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"


    if game_state == "Level 5":

            if level_state == "Playing":

                if pause_button.collidepoint(pos):
                    level_state = "Paused"


                if globy_icon.collidepoint(pos) and coins >= 50:
                    summon_globy()
                if ergam_icon.collidepoint(pos) and coins >= 150:
                    summon_ergam()
                if zap_ball_icon.collidepoint(pos) and coins >= 200:
                    summon_zap_ball()
                if zlumpy_icon.collidepoint(pos) and coins >= 75:
                    summon_zlumpy()
                if guardo_icon.collidepoint(pos) and coins >= 100:
                    summon_guardo()

            if level_state == "Paused":

                if back_to_game_button.collidepoint(pos):
                    level_state = "Playing"

                if back_to_main_menu_button.collidepoint(pos):
                    level_state = "Playing"
                    game_state = "Start Screen"

            if level_state == "Beat Level 5":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"
                    paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                    paper_won_per_level = 0
                    levels[4][5] = int(levels[4][5] * 0.9)

            if level_state == "Game Over":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"


    if game_state == "Level 6":

            if level_state == "Playing":

                if pause_button.collidepoint(pos):
                    level_state = "Paused"


                if globy_icon.collidepoint(pos) and coins >= 50:
                    summon_globy()
                if ergam_icon.collidepoint(pos) and coins >= 150:
                    summon_ergam()
                if zap_ball_icon.collidepoint(pos) and coins >= 200:
                    summon_zap_ball()
                if zlumpy_icon.collidepoint(pos) and coins >= 75:
                    summon_zlumpy()
                if guardo_icon.collidepoint(pos) and coins >= 100:
                    summon_guardo()

            if level_state == "Paused":

                if back_to_game_button.collidepoint(pos):
                    level_state = "Playing"

                if back_to_main_menu_button.collidepoint(pos):
                    level_state = "Playing"
                    game_state = "Start Screen"

            if level_state == "Beat Level 6":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"
                    paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                    paper_won_per_level = 0
                    levels[5][5] = int(levels[5][5] * 0.9)

            if level_state == "Game Over":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"

    if game_state == "Level 7":

            if level_state == "Playing":

                if pause_button.collidepoint(pos):
                    level_state = "Paused"


                if globy_icon.collidepoint(pos) and coins >= 50:
                    summon_globy()
                if ergam_icon.collidepoint(pos) and coins >= 150:
                    summon_ergam()
                if zap_ball_icon.collidepoint(pos) and coins >= 200:
                    summon_zap_ball()
                if zlumpy_icon.collidepoint(pos) and coins >= 75:
                    summon_zlumpy()
                if guardo_icon.collidepoint(pos) and coins >= 100:
                    summon_guardo()

            if level_state == "Paused":

                if back_to_game_button.collidepoint(pos):
                    level_state = "Playing"

                if back_to_main_menu_button.collidepoint(pos):
                    level_state = "Playing"
                    game_state = "Start Screen"

            if level_state == "Beat Level 7":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"
                    paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                    paper_won_per_level = 0
                    levels[6][5] = int(levels[6][5] * 0.9)

            if level_state == "Game Over":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"

    if game_state == "Level 8":

            if level_state == "Playing":

                if pause_button.collidepoint(pos):
                    level_state = "Paused"


                if globy_icon.collidepoint(pos) and coins >= 50:
                    summon_globy()
                if ergam_icon.collidepoint(pos) and coins >= 150:
                    summon_ergam()
                if zap_ball_icon.collidepoint(pos) and coins >= 200:
                    summon_zap_ball()
                if zlumpy_icon.collidepoint(pos) and coins >= 75:
                    summon_zlumpy()
                if guardo_icon.collidepoint(pos) and coins >= 100:
                    summon_guardo()

            if level_state == "Paused":

                if back_to_game_button.collidepoint(pos):
                    level_state = "Playing"

                if back_to_main_menu_button.collidepoint(pos):
                    level_state = "Playing"
                    game_state = "Start Screen"

            if level_state == "Beat Level 8":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"
                    paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                    paper_won_per_level = 0
                    levels[7][5] = int(levels[7][5] * 0.9)

            if level_state == "Game Over":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"

    if game_state == "Level 9":

            if level_state == "Playing":

                if pause_button.collidepoint(pos):
                    level_state = "Paused"


                if globy_icon.collidepoint(pos) and coins >= 50:
                    summon_globy()
                if ergam_icon.collidepoint(pos) and coins >= 150:
                    summon_ergam()
                if zap_ball_icon.collidepoint(pos) and coins >= 200:
                    summon_zap_ball()
                if zlumpy_icon.collidepoint(pos) and coins >= 75:
                    summon_zlumpy()
                if guardo_icon.collidepoint(pos) and coins >= 100:
                    summon_guardo()

            if level_state == "Paused":

                if back_to_game_button.collidepoint(pos):
                    level_state = "Playing"

                if back_to_main_menu_button.collidepoint(pos):
                    level_state = "Playing"
                    game_state = "Start Screen"

            if level_state == "Beat Level 9":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"
                    paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                    paper_won_per_level = 0
                    levels[8][5] = int(levels[8][5] * 0.9)

            if level_state == "Game Over":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"

    if game_state == "Level 10":

            if level_state == "Playing":

                if pause_button.collidepoint(pos):
                    level_state = "Paused"


                if globy_icon.collidepoint(pos) and coins >= 50:
                    summon_globy()
                if ergam_icon.collidepoint(pos) and coins >= 150:
                    summon_ergam()
                if zap_ball_icon.collidepoint(pos) and coins >= 200:
                    summon_zap_ball()
                if zlumpy_icon.collidepoint(pos) and coins >= 75:
                    summon_zlumpy()
                if guardo_icon.collidepoint(pos) and coins >= 100:
                    summon_guardo()

            if level_state == "Paused":

                if back_to_game_button.collidepoint(pos):
                    level_state = "Playing"

                if back_to_main_menu_button.collidepoint(pos):
                    level_state = "Playing"
                    game_state = "Start Screen"

            if level_state == "Beat Level 10":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"
                    paper_owned += int(paper_won_per_level * (1 + ( (paper_per_level_icon.level - 1) * 0.1) ) )
                    paper_won_per_level = 0
                    levels[9][5] = int(levels[9][5] * 0.9)

            if level_state == "Game Over":

                if back_button.collidepoint(pos):
                    game_state = "Level Select"




def update():
    global game_state, level_state
    keys = pygame.key.get_pressed()
    
    if game_state == "Lineup Menu":
        print(levels[1][2])

        for empty_slot in lineup:
            if globy_icon.pos == empty_slot.pos:
                #print("taken")
                empty_slot.taken = True

            elif ergam_icon.pos == empty_slot.pos:
                empty_slot.taken = True
                #print("taken")

            elif zap_ball_icon.pos == empty_slot.pos:
                empty_slot.taken = True
                #print("taken")

            elif zlumpy_icon.pos == empty_slot.pos:
                empty_slot.taken = True
                #print("taken")

            if globy_icon.pos != empty_slot.pos and ergam_icon.pos != empty_slot.pos and zap_ball_icon.pos != empty_slot.pos and zlumpy_icon.pos != empty_slot.pos:
                empty_slot.taken = False
                #print("free")
        
        if globy_icon.equip_menu_mode == "Selected":

            if keys[pygame.K_1]:
                if empty_slot_1.taken == False:
                    globy_icon.slot = "one"
                    globy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_2]:
                if empty_slot_2.taken == False:
                    globy_icon.slot = "two"
                    globy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_3]:
                if empty_slot_3.taken == False:
                    globy_icon.slot = "three"
                    globy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_4]:
                if empty_slot_4.taken == False:
                    globy_icon.slot = "four"
                    globy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_5]:
                if empty_slot_5.taken == False:
                    globy_icon.slot = "five"
                    globy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_BACKSPACE]:
                globy_icon.slot = "none"
                globy_icon.equip_menu_mode = "Unselected"

        if ergam_icon.equip_menu_mode == "Selected":

            if keys[pygame.K_1]:
                if empty_slot_1.taken == False:
                    ergam_icon.slot = "one"
                    ergam_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_2]:
                if empty_slot_2.taken == False:
                    ergam_icon.slot = "two"
                    ergam_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_3]:
                if empty_slot_3.taken == False:
                    ergam_icon.slot = "three"
                    ergam_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_4]:
                if empty_slot_4.taken == False:
                    ergam_icon.slot = "four"
                    ergam_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_5]:
                if empty_slot_5.taken == False:
                    ergam_icon.slot = "five"
                    ergam_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_BACKSPACE]:
                ergam_icon.slot = "none"
                ergam_icon.equip_menu_mode = "Unselected"

        if zap_ball_icon.equip_menu_mode == "Selected":

            if keys[pygame.K_1]:
                if empty_slot_1.taken == False:
                    zap_ball_icon.slot = "one"
                    zap_ball_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_2]:
                if empty_slot_2.taken == False:
                    zap_ball_icon.slot = "two"
                    zap_ball_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_3]:
                if empty_slot_3.taken == False:
                    zap_ball_icon.slot = "three"
                    zap_ball_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_4]:
                if empty_slot_4.taken == False:
                    zap_ball_icon.slot = "four"
                    zap_ball_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_5]:
                if empty_slot_5.taken == False:
                    zap_ball_icon.slot = "five"
                    zap_ball_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_BACKSPACE]:
                zap_ball_icon.slot = "none"
                zap_ball_icon.equip_menu_mode = "Unselected"

        if zlumpy_icon.equip_menu_mode == "Selected":

            if keys[pygame.K_1]:
                if empty_slot_1.taken == False:
                    zlumpy_icon.slot = "one"
                    zlumpy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_2]:
                if empty_slot_2.taken == False:
                    zlumpy_icon.slot = "two"
                    zlumpy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_3]:
                if empty_slot_3.taken == False:
                    zlumpy_icon.slot = "three"
                    zlumpy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_4]:
                if empty_slot_4.taken == False:
                    zlumpy_icon.slot = "four"
                    zlumpy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_5]:
                if empty_slot_5.taken == False:
                    zlumpy_icon.slot = "five"
                    zlumpy_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_BACKSPACE]:
                zlumpy_icon.slot = "none"
                zlumpy_icon.equip_menu_mode = "Unselected"

        if guardo_icon.equip_menu_mode == "Selected":

            if keys[pygame.K_1]:
                if empty_slot_1.taken == False:
                    guardo_icon.slot = "one"
                    guardo_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_2]:
                if empty_slot_2.taken == False:
                    guardo_icon.slot = "two"
                    guardo_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_3]:
                if empty_slot_3.taken == False:
                    guardo_icon.slot = "three"
                    guardo_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_4]:
                if empty_slot_4.taken == False:
                    guardo_icon.slot = "four"
                    guardo_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_5]:
                if empty_slot_5.taken == False:
                    guardo_icon.slot = "five"
                    guardo_icon.equip_menu_mode = "Unselected"
            if keys[pygame.K_BACKSPACE]:
                guardo_icon.slot = "none"
                guardo_icon.equip_menu_mode = "Unselected"


    if game_state == "Level 1":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_1_waves()

            if levels[0][4] <= 0:
                levels[0][4] = 0

            if levels[0][4] == 0:
                level_state = "Beat Level 1"

        if level_state == "Beat Level 1":
            levels[0][2] = "Complete"
            levels[1][1] = "Unlocked"

    if game_state == "Level 2":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_2_waves()

            if levels[1][4] <= 0:
                levels[1][4] = 0

            if levels[1][4] == 0:
                level_state = "Beat Level 2"

        if level_state == "Beat Level 2":
            levels[1][2] = "Complete"
            levels[2][1] = "Unlocked"

    if game_state == "Level 3":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_3_waves()

            if levels[2][4] <= 0:
                levels[2][4] = 0

            if levels[2][4] == 0:
                level_state = "Beat Level 3"

        if level_state == "Beat Level 3":
            levels[2][2] = "Complete"
            levels[3][1] = "Unlocked"

    if game_state == "Level 4":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_4_waves()

            if levels[3][4] <= 0:
                levels[3][4] = 0

            if levels[3][4] == 0:
                level_state = "Beat Level 4"

        if level_state == "Beat Level 4":
            levels[3][2] = "Complete"
            levels[4][1] = "Unlocked"

    if game_state == "Level 5":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_5_waves()

            if levels[4][4] <= 0:
                levels[4][4] = 0

            if levels[4][4] == 0:
                level_state = "Beat Level 5"

        if level_state == "Beat Level 5":
            levels[4][2] = "Complete"
            levels[5][1] = "Unlocked"


    if game_state == "Level 6":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_6_waves()

            if levels[5][4] <= 0:
                levels[5][4] = 0

            if levels[5][4] == 0:
                level_state = "Beat Level 6"

        if level_state == "Beat Level 6":
            levels[5][2] = "Complete"
            levels[6][1] = "Unlocked"


    if game_state == "Level 7":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_7_waves()

            if levels[6][4] <= 0:
                levels[6][4] = 0

            if levels[6][4] == 0:
                level_state = "Beat Level 7"

        if level_state == "Beat Level 7":
            levels[6][2] = "Complete"
            levels[7][1] = "Unlocked"

    if game_state == "Level 8":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_8_waves()

            if levels[7][4] <= 0:
                levels[7][4] = 0

            if levels[7][4] == 0:
                level_state = "Beat Level 8"

        if level_state == "Beat Level 8":
            levels[7][2] = "Complete"
            levels[8][1] = "Unlocked"

    if game_state == "Level 9":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_9_waves()

            if levels[8][4] <= 0:
                levels[8][4] = 0

            if levels[8][4] == 0:
                level_state = "Beat Level 9"

        if level_state == "Beat Level 9":
            levels[8][2] = "Complete"
            levels[9][1] = "Unlocked"

    if game_state == "Level 10":

        if level_state == "Playing":

            add_one_coin()
            globy_behavior()
            globy_projectile_behavior()
            ergam_behavior()
            zap_ball_behavior()
            zlumpy_behavior()
            zlumpy_projectile_behavior()
            guardo_behavior()
            guardo_projectile_behavior()
            level_10_waves()

            if levels[9][4] <= 0:
                levels[9][4] = 0

            if levels[9][4] == 0:
                level_state = "Beat Level 10"

        if level_state == "Beat Level 10":
            levels[9][2] = "Complete"
            levels[10][1] = "Unlocked"




pgzrun.go()
