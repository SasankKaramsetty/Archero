import pygame
import random

pygame.init()
pii = 3.14

screen = pygame.display.set_mode((1024, 600))
pygame.display.set_caption("ARCHERO")

# Loading all the images needed for the game and also scaling them to the required size
pause = pygame.image.load('pause_button_64.png')
replay = pygame.image.load('replay_64.png')
exit_p = pygame.image.load('exit_64.png')
resume = pygame.image.load('play2_64.png')
cursor_img = pygame.image.load('cursor_color_24.png')
cursor_img_rect = cursor_img.get_rect()
arrow_ascend = pygame.image.load('arrow_48_prev_ui.png')
arrow_descend = pygame.image.load('arrow_32_cw_135.png')
you_lose_img = pygame.image.load('you_lose.jpg')
you_lose_img = pygame.transform.scale(you_lose_img, (1024, 600))
you_win_img = pygame.image.load('you_win.jpg')
you_win_img = pygame.transform.scale(you_win_img, (1024, 600))
loading_archer = pygame.image.load('loading_archer3.jpg')
loading_archer = pygame.transform.scale(loading_archer, (1024, 600))
pause_archer = pygame.image.load('loading_archer.jpg')
pause_archer = pygame.transform.scale(pause_archer, (1024, 600))
main_menu_bg = pygame.image.load('main_menu_bg.jpg')
main_menu_bg = pygame.transform.scale(main_menu_bg, (1024, 600))
ground_bg = pygame.image.load('ground_bg.jpg')
ground_bg = pygame.transform.scale(ground_bg, (1024, 300))
archer_icon = pygame.image.load('game_icon.jpg')
archer_icon = pygame.transform.scale(archer_icon, (2150, 2150))
pygame.display.set_icon(archer_icon)
play_music = pygame.image.load('play_music2_64.png')
stop_music = pygame.image.load('Stop_music2_64 (2).png')

# Loading music and sounds into the game
arrow_release = pygame.mixer.Sound('arrow_release.wav')
arrow_hit = pygame.mixer.Sound('arrow_hit3.wav')
mouse_click = pygame.mixer.Sound('click.mp3')
thud = pygame.mixer.Sound('thud.mp3')
pygame.mixer.music.load('alexander-nakarada-superepic.mp3')

# Creating font variables of the desired font and size
loading_text = pygame.font.Font('High Jersey Italic.ttf', 40)
controls = pygame.font.Font('High Jersey.ttf', 30)
question_mark = pygame.font.Font('High Jersey Italic.ttf', 30)
welcome_text = pygame.font.Font('High Jersey.ttf', 100)
easy = pygame.font.Font('High Jersey.ttf', 40)
medium = pygame.font.Font('High Jersey.ttf', 40)
hard = pygame.font.Font('High Jersey.ttf', 40)
exitp = pygame.font.Font('freesansbold.ttf', 35)
game_paused = pygame.font.Font('High Jersey.ttf', 200)
yese = pygame.font.Font('freesansbold.ttf', 20)
noe = pygame.font.Font('freesansbold.ttf', 20)
statement = pygame.font.Font('freesansbold.ttf', 25)
control_player_movement = pygame.font.Font('freesansbold.ttf', 20)
control_power_change = pygame.font.Font('freesansbold.ttf', 20)
control_aim_change = pygame.font.Font('freesansbold.ttf', 20)
you_lose = pygame.font.Font('High Jersey.ttf', 200)
you_win = pygame.font.Font('High Jersey.ttf', 200)

# Global variables
white = (255, 255, 255)
black = (0, 0, 0)
active_red = (255, 0, 0)
button_hard_color = passive_red = (180, 0, 0)
active_yellow = (255, 255, 0)
button_medium_color = passive_yellow = (180, 180, 0)
active_green = (0, 255, 0)
button_easy_color = passive_green = (0, 180, 0)
addon_x, addon_y = 250, 35
addon_width = 0.95
epoz = 800
player_health, enemy_health = 250, 150
loadingbar_x = 1
loadingbar_status = 0
music = True
paused = False


def loading_menu():
    global loadingbar_x, loadingbar_status
    running = True

    while running:
        screen.blit(loading_archer, (0, 0))
        loadingtext = loading_text.render("loading...", True, (200, 0, 0))
        screen.blit(loadingtext, (200, 457))
        # Rectangles that are used to depict the loading process
        pygame.draw.rect(screen, (0, 0, 255), (200, 500, 300, 40), 1)
        pygame.draw.rect(screen, (0, 255, 0), (203, 503, loadingbar_x, 34))

        if loadingbar_x < 293:      # If the width of the inner rectangle is less than the outer rectangle, then it's width continues to increase
            loadingbar_status = 0
            loadingbar_x += 0.1
        else:
            loadingbar_status = 1
            running = False

        if loadingbar_status:   # If the loading bar status is 1 i.e., complete, then the screen changes to main menu
            main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # If the exit button is clicked then the exit window appears
                exit_window()

        pygame.display.update()


def main_menu():
    pygame.mouse.set_visible(True)      # Visibility of the mouse is set to True
    global button_easy_color, button_hard_color, button_medium_color, addon_width, paused, music
    running = True
    music_button = screen.blit(play_music, (850, 10))
    music_button2 = screen.blit(stop_music, (850, 10))

    pygame.mixer.music.play(-1)     # Playing the background music

    while running:
        screen.fill(black)
        welcometext = welcome_text.render("ARCHERO", True, (255, 0, 0))
        easy_text = easy.render("easy", True, white)
        medium_text = medium.render("medium", True, white)
        hard_text = hard.render("hard", True, white)
        screen.blit(main_menu_bg, (0, 0))
        screen.blit(welcometext, (350, 0))

        x, y = pygame.mouse.get_pos()

        # Drawing the Buttons(Rectangles)
        button_hard = pygame.draw.rect(screen, button_hard_color, (70, 390, 230, 70))
        button_medium = pygame.draw.rect(screen, button_medium_color, (70, 280, 230, 70))
        button_easy = pygame.draw.rect(screen, button_easy_color, (70, 170, 230, 70))

        # Writing the text on the respective buttons
        screen.blit(easy_text, (150, 180))
        screen.blit(medium_text, (140, 295))
        screen.blit(hard_text, (150, 400))

        # Rectangles that are displayed on either side of "ARCHERO"
        pygame.draw.rect(screen, active_red, (addon_x, addon_y, int(addon_width), 15))
        pygame.draw.rect(screen, active_red, (addon_x - 30, addon_y + 25, int(addon_width + 30), 15))
        pygame.draw.rect(screen, active_red, (addon_x - 60, addon_y + 50, int(addon_width + 60), 15))
        pygame.draw.rect(screen, active_red, (addon_x + 350, addon_y, int(addon_width), 15))
        pygame.draw.rect(screen, active_red, (addon_x + 350, addon_y + 25, int(addon_width + 30), 15))
        pygame.draw.rect(screen, active_red, (addon_x + 350, addon_y + 50, int(addon_width + 60), 15))

        if addon_width < 95:        # If the width of rectangles on either side of "ARCHRO" are less than 95, then their width continues to increase
            addon_width += 0.08

        if button_hard.collidepoint(x, y):      # If the mouse is hovered on the "hard" button, then the intensity of red colour increases
            button_hard_color = active_red
            if pygame.mouse.get_pressed()[0]:
                mouse_click.play()
                running = False
                game_play("hard")       # Going to the game play in "hard" mode
        else:
            button_hard_color = passive_red

        if button_medium.collidepoint(x, y):    # If the mouse is hovered on the "medium" button, then the intensity of yellow colour increases
            button_medium_color = active_yellow
            if pygame.mouse.get_pressed()[0]:
                mouse_click.play()
                running = False
                game_play("medium")     # Going to the game play in "medium" mode
        else:
            button_medium_color = passive_yellow

        if button_easy.collidepoint(x, y):      # If the mouse is hovered on the "easy" button, then the intensity of green colour increases
            button_easy_color = active_green
            if pygame.mouse.get_pressed()[0]:
                mouse_click.play()
                running = False
                game_play("easy")       # Going to the game play in "easy" mode
        else:
            button_easy_color = passive_green

        if music:
            screen.blit(play_music, (850, 10))
        else:
            screen.blit(stop_music, (850, 10))

        if x in range(850, 914) and y in range(10, 74):     # If the mouse is hovered on the music icon, then the cursor will be changed from arrow to pointer
            pygame.mouse.set_visible(False)
            cursor_img_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor_img, cursor_img_rect)
        else:
            pygame.mouse.set_visible(True)

        button_main_controls = pygame.draw.circle(screen, (0, 170, 230), (970, 40), 30)
        questionmark = question_mark.render("?", True, (255, 255, 255))
        screen.blit(questionmark, (955, 25))

        if button_main_controls.collidepoint(x, y):     # As long as the mouse is on the circle, controls will be displayed
            pygame.draw.rect(screen, (0, 170, 230), (350, 40, 620, 180))
            control = controls.render("Controls", True, (255, 255, 255))
            control_player = control_player_movement.render("Player Movement - Left and Right arrows", True, (255, 255, 255))
            control_power = control_power_change.render("To shoot - 'S'", True, (255, 255, 255))
            control_aim = control_aim_change.render("To aim up and down - Up and Down arrows", True, white)
            screen.blit(control, (620, 45))
            screen.blit(control_player, (360, 85))
            screen.blit(control_power, (360, 125))
            screen.blit(control_aim, (360, 165))

        for event in pygame.event.get():
            # If the music icon is clicked, then the icon displayed and the volume of music will be changed depending on the value stored in the music variable
            if not music and music_button.collidepoint(x, y) and pygame.mouse.get_pressed()[0]:
                mouse_click.play()      # Sound effect of clicking
                screen.blit(stop_music, (850, 10))
                music = True
                pygame.mixer.music.set_volume(1)

            elif music and music_button2.collidepoint(x, y) and pygame.mouse.get_pressed()[0]:
                mouse_click.play()      # Sound effect of clicking
                screen.blit(play_music, (850, 10))
                music = False
                pygame.mixer.music.set_volume(0)

            if event.type == pygame.QUIT:
                exit_window()

        pygame.display.update()


def archer(x, pos):
    y = 405
    mul = pos/20
    # Possible hand positions of the archer
    possible_hand_position = [
                       (x + 13 + 10, y - 19),
                       (x + 11 + 10, y - 21),
                       (x + 9 + 10, y - 23),
                       (x + 7 + 10, y - 25),
                       (x + 5 + 10, y - 27),
                       (x + 3 + 10, y - 29),
                       (x + 1 + 10, y - 31),
                       (x - 1 + 10, y - 33),
                       (x - 3 + 10, y - 35),
                       (x - 5 + 10, y - 37),
                       (x - 7 + 10, y - 39),
                       (x - 9 + 10, y - 41),
                       (x - 11 + 10, y - 43),
                       (x - 13 + 10, y - 45)]

    pygame.draw.circle(screen, white, (x+10, 385), 15)      # Face
    pygame.draw.rect(screen, white, (x, 400, 20, 60), 0, 100)   # Body
    pygame.draw.rect(screen, white, (x+3, 450, 15, 50), 0, 0, -1, -1, 5, 5)     # Legs
    pygame.draw.line(screen, white, (x-3, y), possible_hand_position[pos], 8)     # Right hand of the player
    pygame.draw.line(screen, white, (x, y), (possible_hand_position[pos][0] + 40, possible_hand_position[pos][1] - 10), 8)    # Left hand of the player
    pygame.draw.arc(screen, white, (possible_hand_position[pos][0] - 20, possible_hand_position[pos][1] - 30, 60, 70), (-pii/2)+(mul+0.1), (pii/2)+(mul+0.1), 5)      # Bow of the player
    pygame.draw.line(screen, white, (possible_hand_position[pos][0] + (pii/2)+(mul+0.1) + 20, possible_hand_position[pos][1] + 30), possible_hand_position[pos], 2)  # Lower part of the elongated thread
    pygame.draw.line(screen, white, (possible_hand_position[pos][0] - (-pii/2)+(mul+0.1), possible_hand_position[pos][1] - 30), possible_hand_position[pos], 2)  # Upper part of the elongated thread


def enemy(x, pos):
    y = 405
    mul = pos/20
    # Possible hand positions of the enemy
    possible_hand_position = [
                        (x - 13 + 10, y - 19),
                        (x - 11 + 10, y - 21),
                        (x - 9 + 10, y - 23),
                        (x - 7 + 10, y - 25),
                        (x - 5 + 10, y - 27),
                        (x - 3 + 10, y - 29),
                        (x - 1 + 10, y - 31),
                        (x + 1 + 10, y - 33),
                        (x + 3 + 10, y - 35),
                        (x + 5 + 10, y - 37),
                        (x + 7 + 10, y - 39),
                        (x + 9 + 10, y - 41),
                        (x + 11 + 10, y - 43),
                        (x + 13 + 10, y - 45)]

    pygame.draw.circle(screen, white, (x + 10, 385), 15)  # Face
    pygame.draw.rect(screen, white, (x, 400, 20, 60), 0, 100)  # Body
    pygame.draw.rect(screen, white, (x + 3, 450, 15, 50), 0, 0, -1, -1, 5, 5)  # Legs
    pygame.draw.line(screen, white, (x + 3, y), possible_hand_position[pos], 8)  # Left hand of the enemy
    pygame.draw.arc(screen, white, (possible_hand_position[pos][0] - 35, possible_hand_position[pos][1] - 30, 60, 70), (pii/2) - (mul + 0.1), (3*pii/2) - (mul + 0.1), 5) # Bow of the enemy
    pygame.draw.line(screen, white, (x+3, y), (possible_hand_position[pos][0] - 30, possible_hand_position[pos][1] - 10), 8)     # Right hand of the enemy
    pygame.draw.line(screen, white, (possible_hand_position[pos][0] + (pii / 2) + (mul + 0.1) - 20, possible_hand_position[pos][1] + 30), possible_hand_position[pos], 2)  # Lower part of the elongated thread
    pygame.draw.line(screen, white, (possible_hand_position[pos][0] - (-pii / 2) - (mul + 0.1), possible_hand_position[pos][1] - 30), possible_hand_position[pos], 2)  # Upper part of the elongated thread


def projectilearch(x, a, barrier):
    shoot = True
    yb = 395
    xb = x + 10
    fx = x
    fa = a
    b = 1
    hit = False

    while shoot:
        archer(fx, fa)
        enemy(epoz, 0)
        if yb <= 0:
            b = 0
            x = xb
            y = yb

        if b:
            if a == 0:
                xb += 0.5
                yb -= 0.4075
            elif a == 1:
                xb += 0.5
                yb -= 0.5 / 1.168
            elif a == 2:
                xb += 0.5
                yb -= 0.5 * 0.933
            elif a == 3:
                xb += 0.5
                yb -= 0.5 * 1.025
            elif a == 4:
                xb += 0.5
                yb -= 0.5 * 1.1376
            elif (a == 5):
                xb += 0.5
                yb -= 0.5 * 1.2776
            elif (a == 6):
                xb += 0.5
                yb -= 0.5 * 1.4568
            elif (a == 7):
                xb += 0.5
                yb -= 0.5 * 1.6945
            elif (a == 8):
                xb += 0.5
                yb -= 0.5 * 2.025
            elif (a == 9):
                xb += 0.5
                yb -= 0.5 * 2.5155
            elif (a == 10):
                xb += 0.5
                yb -= 0.5 * 3.319
            elif (a == 11):
                xb += 0.5
                yb -= 0.5 * 4.8795
            elif (a == 12):
                xb += 0.5
                yb -= 0.5 * 9.2045
        else:
            if (a == 0):
                xb += 0.5
                yb += 0.4075
            elif (a == 1):
                xb += 0.5
                yb += 0.5 / 1.168
            elif (a == 2):
                xb += 0.5
                yb += 0.5 * 0.933
            elif (a == 3):
                xb += 0.5
                yb += 0.5 * 1.025
            elif (a == 4):
                xb += 0.5
                yb += 0.5 * 1.1376
            elif (a == 5):
                xb += 0.5
                yb += 0.5 * 1.2776
            elif (a == 6):
                xb += 0.5
                yb += 0.5 * 1.4568
            elif (a == 7):
                xb += 0.5
                yb += 0.5 * 1.6945
            elif (a == 8):
                xb += 0.5
                yb += 0.5 * 2.025
            elif (a == 9):
                xb += 0.5
                yb += 0.5 * 2.5155
            elif (a == 10):
                xb += 0.5
                yb += 0.5 * 3.319
            elif (a == 11):
                xb += 0.5
                yb += 0.5 * 4.8795
            elif (a == 12):
                xb += 0.5
                yb += 0.5 * 9.2045
        if barrier.collidepoint(xb, yb):
            thud.play()
            hit = True
        if (b) and not hit:
            pygame.draw.line(screen, (165, 255, 42), (fx,395), (xb, yb), 6)
        elif not(b) and not hit:
            pygame.draw.line(screen, (165, 255, 42), (x, y), (xb, yb), 6)

        if(not(b)):
            if (yb < 500 and yb >= 375):
                if (abs(xb - epoz) <= 40):
                    shoot = False
                    colldetect(xb, 2, 0, hit)

        if (yb > 500 or xb > 1024):
            shoot = False
            colldetect(xb, 2, 0, hit)

        pygame.display.update()


def enemyhit(x, barrier):
    global kill
    yb = 405
    xb = epoz
    ep = True
    b = 1
    hit = False

    if (kill == 1):
        c = random.randrange(1, 7, 1)
        if (c == 1 or c == 2):
            while (ep):
                if (yb <= 0):
                    x1 = xb
                    y1 = yb
                    b = 0

                if (b):
                    xb -= 0.5
                    yb -= 0.5 * 405 / abs(epoz - 512)

                else:
                    xb -= 0.5
                    yb += 0.5 * 500 / abs(512 - x)

                if barrier.collidepoint(xb, yb):
                    thud.play()
                    hit = True

                if (b) and not hit:
                    pygame.draw.line(screen, active_red, (epoz-10, 405), (xb, yb), 6)
                elif not(b) and not hit:
                    if (c == 1 or c == 2 or c == 3 or c == 4):
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)
                    else:
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)

                if (yb >= 500 or xb <= 0):
                    colldetect(xb, 1, x, hit)
                    ep = False
                pygame.display.update()

        else:
            while ep:
                if (yb <= 0):
                    x1 = xb
                    y1 = yb
                    b = 0

                if (b):
                    xb -= 0.5
                    yb -= 0.5 * 405 / abs(epoz - 512)

                else:
                    xb -= 0.5
                    yb += 0.5 * 500 / abs(512 - x - 80)

                if barrier.collidepoint(xb, yb):
                    thud.play()
                    hit = True

                if (b) and not hit:
                    pygame.draw.line(screen, active_red, (epoz-10, 405), (xb, yb), 6)

                elif not(b) and not hit:
                    if (c == 1 or c == 2 or c == 3 or c == 4):
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)
                    else:
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)

                if (yb >= 500 or xb <= 0):
                    colldetect(xb, 1, x, hit)
                    ep = False
                pygame.display.update()

    if kill == 2:
        c = random.randrange(1, 7, 1)
        if (c == 1 or c == 2 or c == 3 or c == 4):
            while ep:
                if (yb <= 0):
                    x1 = xb
                    y1 = yb
                    b = 0

                if (b):
                    xb -= 0.5
                    yb -= 0.5 * 405 / abs(epoz - 512)

                else:
                    xb -= 0.5
                    yb += 0.5 * 500 / abs(512 - x)

                if barrier.collidepoint(xb, yb):
                    thud.play()
                    hit = True

                if (b) and not hit:
                    pygame.draw.line(screen, active_red, (epoz-10, 405), (xb, yb), 6)
                elif not(b) and not hit:
                    if (c == 1 or c == 2 or c == 3 or c == 4):
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)
                    else:
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)

                if (yb >= 500 or xb <= 0):
                    colldetect(xb, 1, x, hit)
                    ep = False
                pygame.display.update()

        else:
            while ep:
                if (yb <= 0):
                    x1 = xb
                    y1 = yb
                    b = 0

                if (b):
                    xb -= 0.5
                    yb -= 0.5 * 405 / abs(epoz - 512)

                else:
                    xb -= 0.5
                    yb += 0.5 * 500 / abs(512 - x - 80)

                if barrier.collidepoint(xb, yb):
                    thud.play()
                    hit = True

                if (b) and not hit:
                    pygame.draw.line(screen, active_red, (epoz-10, 405), (xb, yb), 6)
                elif not(b) and not hit:
                    if (c == 1 or c == 2 or c == 3 or c == 4):
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)
                    else:
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)

                if (yb >= 500 or xb <= 0):
                    colldetect(xb, 1, x, hit)
                    ep = False
                pygame.display.update()

    else:
        c = random.randrange(1, 7, 1)
        if (c == 1 or c == 2 or c == 3 or c == 4 or c == 5):
            while (ep):
                if (yb <= 0):
                    x1 = xb
                    y1 = yb
                    b = 0

                if (b):
                    xb -= 0.5
                    yb -= 0.5 * 405 / abs(epoz - 512)

                else:
                    xb -= 0.5
                    yb += 0.5 * 500 / abs(512 - x)

                if barrier.collidepoint(xb, yb):
                    thud.play()
                    hit = True

                if (b) and not hit:
                    pygame.draw.line(screen, active_red, (epoz-10, 405), (xb, yb), 6)
                elif not(b) and not hit:
                    if (c == 1 or c == 2 or c == 3 or c == 4):
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)
                    else:
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)

                if (yb >= 500 or xb <= 0):
                    colldetect(xb, 1, x, hit)
                    ep = False
                pygame.display.update()

        else:
            while (ep):
                if (yb <= 0):
                    x1 = xb
                    y1 = yb
                    b = 0

                if (b):
                    xb -= 0.5
                    yb -= 0.5 * 405 / abs(epoz - 512)

                else:
                    xb -= 0.5
                    yb += 0.5 * 500 / abs(512 - x - 80)

                if barrier.collidepoint(xb, yb):
                    thud.play()
                    hit = True

                if (b) and not hit:
                    pygame.draw.line(screen, active_red, (epoz-10, 405), (xb, yb), 6)
                elif not(b) and not hit:
                    if (c == 1 or c == 2 or c == 3 or c == 4):
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)
                    else:
                        pygame.draw.line(screen, active_red, (x1, y1), (xb, yb), 6)

                if (yb >= 500 or xb <= 0):
                    colldetect(xb, 1, x, hit)
                    ep = False
                pygame.display.update()


def colldetect(xb, z, x, hit):
    global kill, enemy_health, player_health

    if not hit:
        if(z==1):
            if(abs(x-xb)<=30):
                arrow_hit.play()
                if kill != 3:
                    player_health -= 20
                else:
                    player_health -= 15
        else:
            if (abs(epoz-xb)<=40 and (1 or (xb - epoz)<=50)):
                arrow_hit.play()
                enemy_health -= 30/kill

# Displays the health of the player and the enemy
def health(playerhealth, enemyhealth):
    pygame.draw.rect(screen, active_green, (50, 10, playerhealth, 40))
    pygame.draw.rect(screen, active_red, (774, 10, enemyhealth, 40))


def game_play(mode):
    global epoz, player_health, enemy_health, kill
    player_health, enemy_health = 250, 150
    pygame.mouse.set_visible(True)
    pos = 0
    pygame.mixer.music.stop()
    running = True
    x = 15
    x_change = 0

    while running:
        if mode == "easy":
            kill = 1
        elif mode == "medium":
            kill = 2
        else:
            kill = 3

        screen.fill(black)
        screen.blit(ground_bg, (0, 300))
        cur_x, cur_y = pygame.mouse.get_pos()
        screen.blit(pause, (500, 10))       # Pause button on the top of the screen

        if cur_x in range(500, 564) and cur_y in range(10, 74):
            pygame.mouse.set_visible(False)     # If the mouse is hovered on the pause icon, then the arrow cursor is changed to a pointer
            cursor_img_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor_img, cursor_img_rect)
            if pygame.mouse.get_pressed()[0]:
                mouse_click.play()      # Sound effect of mouse click
                pause_menu(mode)
        else:
            pygame.mouse.set_visible(True)

        barrier = pygame.draw.rect(screen, passive_green, (474, 300, 100, 200))     # Barrier between the players

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_window()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    choice = random.randint(0, 1)       # Variable, chosen randomly, to move the enemy forward or backward
                    arrow_release.play()        # Sound of the arrow when released by the player
                    projectilearch(x, pos, barrier)

                    if choice:
                        epoz += 50
                        if epoz >= 950:
                            epoz = 950
                    elif choice == 0:
                        epoz -= 50
                        if epoz <= 670:
                            epoz = 670

                    arrow_release.play()        # Sound of the arrow when released by the enemy
                    enemyhit(x, barrier)
                    screen.fill(black)
                    archer(x, pos)
                    enemy(epoz, pos)
                    health(player_health, enemy_health)
                    screen.blit(pause, (500, 10))
                    pygame.display.update()

                # Up and down arrows used to aim up and down
                if event.key == pygame.K_UP:
                    pos += 1
                if event.key == pygame.K_DOWN:
                    pos -= 1
                # Left and right arrow keys used to move the player left and right
                if event.key == pygame.K_LEFT:
                    x_change = -0.2
                if event.key == pygame.K_RIGHT:
                    x_change = 0.2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pos = pos

        # Guideline of the player
        s = 405/(502-(pos-1)*39)
        yt = 330 + (13 - pos)*1.75
        xt = x + 10 + (395-yt)/s
        pygame.draw.line(screen, active_green, (x+10, 395), (xt, yt), 7)

        x += x_change
        if x >= 400:
            x = 400
        if x <= 0:
            x = 0
        if pos > 12:
            pos = 12
        elif pos < 0:
            pos = 0

        archer(x, pos)
        enemy(epoz, 7)
        health(player_health, enemy_health)

        if player_health <= 0 or enemy_health <= 0:
            running = False
            result(mode)

        pygame.display.update()


def pause_menu(mode):
    global paused
    paused = True

    while paused:
        screen.fill(black)
        screen.blit(pause_archer, (0, 0))
        paused_text = game_paused.render(" game    paused", True, active_red)
        screen.blit(paused_text, (20, 200))
        screen.blit(resume, (460, 100))
        screen.blit(exit_p, (460, 250))
        screen.blit(replay, (460, 400))

        x, y = pygame.mouse.get_pos()

        if x in range(460, 524) and y in range(100, 164):
            a = 1
            pygame.mouse.set_visible(False)
            cursor_img_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor_img, cursor_img_rect)
            if pygame.mouse.get_pressed()[0]:
                mouse_click.play()
                paused = False
        else:
            a = 0

        if x in range(460, 514) and y in range(400, 464):
            b = 1
            pygame.mouse.set_visible(False)
            cursor_img_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor_img, cursor_img_rect)
            if pygame.mouse.get_pressed()[0]:
                mouse_click.play()
                paused = False
                game_play(mode)
        else:
            b = 0

        if x in range(460, 512) and y in range(250, 314):
            c = 1
            pygame.mouse.set_visible(False)
            cursor_img_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor_img, cursor_img_rect)
            if pygame.mouse.get_pressed()[0]:
                mouse_click.play()
                paused = False
                main_menu()
        else:
            c = 0

        if not(a or b or c):              # If none of the above conditions are satisfied, then the visibility of the mouse is set to True
            pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_window()

        pygame.display.update()


def result(mode):
    global player_health, enemy_health
    if player_health <= 0:
        player_health = 250
        enemy_health = 150
        lost = True
        while lost:
            screen.fill((0, 0, 0))
            screen.blit(you_lose_img, (0, 0))
            screen.blit(exit_p, (120, 150))
            screen.blit(replay, (120, 350))

            x, y = pygame.mouse.get_pos()

            if (x in range(120, 184) and y in range(150, 214)) or (x in range(120, 184) and y in range(350, 414)):
                pygame.mouse.set_visible(False)
                cursor_img_rect.center = pygame.mouse.get_pos()
                screen.blit(cursor_img, cursor_img_rect)
                if (x in range(120, 184) and y in range(150, 214)) and pygame.mouse.get_pressed()[0]:
                    mouse_click.play()
                    lost = False
                    main_menu()
                elif (x in range(120, 184) and y in range(350, 414)) and pygame.mouse.get_pressed()[0]:
                    mouse_click.play()
                    lost = False
                    game_play(mode)
            else:
                pygame.mouse.set_visible(True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_window()
            pygame.display.update()

    elif enemy_health <= 0:
        win = True
        enemy_health = 150
        player_health = 250
        while win:
            screen.fill((0, 0, 0))
            screen.blit(you_win_img, (0, 0))
            screen.blit(exit_p, (320, 450))
            screen.blit(replay, (640, 450))
            x, y = pygame.mouse.get_pos()
            if (x in range(320, 364) and y in range(450, 512)) or (x in range(640, 704) and y in range(450, 512)):
                pygame.mouse.set_visible(False)
                cursor_img_rect.center = pygame.mouse.get_pos()
                screen.blit(cursor_img, cursor_img_rect)
                if (x in range(320, 364) and y in range(450, 512)) and pygame.mouse.get_pressed()[0]:
                    mouse_click.play()
                    win = False
                    main_menu()
                elif (x in range(640, 704) and y in range(450, 512)) and pygame.mouse.get_pressed()[0]:
                    mouse_click.play()
                    win = False
                    game_play(mode)
            else:
                pygame.mouse.set_visible(True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_window()
            pygame.display.update()


def exit_window():
    button_exit_yes_colour = passive_red
    button_exit_no_colour = passive_green
    running = True

    while running:
        pygame.draw.rect(screen, (0, 0, 190), (330, 220, 400, 100))
        yese_text = yese.render("Yes", True, white)
        noe_text = noe.render("No", True, white)
        statement_text = statement.render("Are you sure you want to exit ?", True, white)
        screen.blit(statement_text, (340, 240))
        x, y = pygame.mouse.get_pos()
        button_exit_yes = pygame.draw.rect(screen, button_exit_yes_colour, (410, 285, 40, 30))
        button_exit_no = pygame.draw.rect(screen, button_exit_no_colour, (600, 285, 40, 30))

        screen.blit(yese_text, (413, 290))
        screen.blit(noe_text, (605, 290))

        for event in pygame.event.get():
            if button_exit_yes.collidepoint(x, y):
                button_exit_yes_colour = active_red
                if pygame.mouse.get_pressed()[0]:
                    mouse_click.play()
                    pygame.quit()
                    quit()
            else:
                button_exit_yes_colour = passive_red

            if button_exit_no.collidepoint(x, y):
                button_exit_no_colour = active_green
                if pygame.mouse.get_pressed()[0]:
                    mouse_click.play()
                    running = False
            else:
                button_exit_no_colour = passive_green
        pygame.display.update()

loading_menu()