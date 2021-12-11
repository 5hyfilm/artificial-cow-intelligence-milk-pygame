"""Import Libraries"""
import pygame

pygame.init()

display_width = 1080
display_height = 720

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('ArtificialCowIntelligenceMilk')

################################################################################

"""ICON"""
icon_img = pygame.image.load('./icon.png')
pygame.display.set_icon(icon_img)

################################################################################

""""STAGE"""
COW = pygame.image.load('./stage_img/cow.png')
FRAME = pygame.image.load('./stage_img/frame.png')
LINE = pygame.image.load('./stage_img/line.png')
FIREWORK = pygame.image.load('./stage_img/firework.png')
GRASS = pygame.image.load('./stage_img/grass.png')

"""COLOR_IMG"""
RED_circle = pygame.image.load('./circle_img/RED_circle.png')
GREEN_circle = pygame.image.load('./circle_img/GREEN_circle.png')
BLUE_circle = pygame.image.load('./circle_img/BLUE_circle.png')
ORANGE_circle = pygame.image.load('./circle_img/ORANGE_circle.png')
YELLOW_circle = pygame.image.load('./circle_img/YELLOW_circle.png')
VIOLET_circle = pygame.image.load('./circle_img/VIOLET_circle.png')

"""COLOR_TEXT"""
RED_text = pygame.image.load('./text_img/RED_text.png')
GREEN_text = pygame.image.load('./text_img/GREEN_text.png')
BLUE_text = pygame.image.load('./text_img/BLUE_text.png')
ORANGE_text = pygame.image.load('./text_img/ORANGE_text.png')
YELLOW_text = pygame.image.load('./text_img/YELLOW_text.png')
VIOLET_text = pygame.image.load('./text_img/VIOLET_text.png')

################################################################################

pause = False

################################################################################

"""COLOE_CODE"""
black_code = (0, 0, 0)
whit_code = (255, 255, 255)
orange_code = (255, 165, 0)

dark_red_code = (200, 0, 0)
dark_green_code = (0, 200, 0)

bright_red_code = (255, 0, 0)
bright_green_code = (0, 255, 0)

################################################################################

"""Intro"""
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.mouse.get_pressed()
    #print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            # if action == 'play':
            #     gameplay()
            # elif action == 'quit':
            #     pygame.quit()
            #     quit()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font('./font/LilitaOne-Regular.ttf', 40)
    textSurface, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurface, textRect)

def quit_game():
    pygame.quit()
    quit()

def unpaused():
    global pause
    pause = False

def nice():
    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(whit_code)
        largeText = pygame.font.Font('./font/LilitaOne-Regular.ttf',65)
        TextSurf, TextRect = text_objects('NICE', largeText)
        score_text, score_rect = text_objects('TOTAL SCORE:  1', largeText)
        TextRect.center = ((display_width/2),(display_height/3.5))
        score_rect.center = ((display_width/2),(display_height/2.5))
        #FIREWORK
        screen.blit(FIREWORK, (150, 50))
        screen.blit(FIREWORK, (630, 50))
        #GRASS
        screen.blit(GRASS, (0, 620))
        screen.blit(GRASS, (528, 620))
        screen.blit(GRASS, (1056, 620))
        #TEXT
        screen.blit(TextSurf, TextRect)
        screen.blit(score_text, score_rect)

        button('CONTINUED', 150, 450, 225, 50, dark_green_code, bright_green_code, unpaused)
        button('QUIT', 720, 450, 225, 50, dark_red_code, bright_red_code, quit_game)

        pygame.display.update()

def game_intro():
    pygame.mixer.music.load('./music/Sand_Castle.mp3')
    pygame.mixer.music.play(-1)

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(orange_code)
        largeText = pygame.font.Font('./font/LilitaOne-Regular.ttf',60)
        TextSurf, TextRect = text_objects("Artificial Cow", largeText)
        TextSurf2, TextRect2 = text_objects("Intelligence Milk", largeText)
        TextRect.center = ((display_width/1.5),(display_height/3.5))
        TextRect2.center = ((display_width/1.5),(display_height/2.75))
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf2, TextRect2)

        button('START', 675, 350, 125, 50, dark_green_code, bright_green_code, gameplay)
        button('QUIT', 675, 450, 125, 50, dark_red_code, bright_red_code, quit_game)

        screen.blit(COW, (50, 150))

        pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, black_code)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('./font/LilitaOne-Regular.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

"""STAGE"""
def frame(x, y):
    screen.blit(FRAME, (x, y))

def line(x, y):
    screen.blit(LINE, (x, y))

"""CIRCLE"""
def RED_circle_move(x, y):
        screen.blit(RED_circle, (x, y))

def GREEN_circle_move(x, y):
        screen.blit(GREEN_circle, (x, y))

def BLUE_circle_move(x, y):
        screen.blit(BLUE_circle, (x, y))

def ORANGE_circle_move(x, y):
        screen.blit(ORANGE_circle, (x, y))

def YELLOW_circle_move(x, y):
        screen.blit(YELLOW_circle, (x, y))

def VIOLET_circle_move(x, y):
        screen.blit(VIOLET_circle, (x, y))

"""TEXT"""
def RED_text_move(x, y):
        screen.blit(RED_text, (x, y))

def GREEN_text_move(x, y):
        screen.blit(GREEN_text, (x, y))

def BLUE_text_move(x, y):
        screen.blit(BLUE_text, (x, y))

def ORANGE_text_move(x, y):
        screen.blit(ORANGE_text, (x, y))

def YELLOW_text_move(x, y):
        screen.blit(YELLOW_text, (x, y))

def VIOLET_text_move(x, y):
        screen.blit(VIOLET_text, (x, y))

################################################################################

def gameplay():
    global pause

    move_X = 0
    move_Y = 90
    move_Text = 0
    text_Y = 550

    run = True

    while run:
        screen.fill(whit_code)
        move_X += 5
        move_Text -= 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = True
                    nice()

        """USING FUNCTION"""

        """STAGE"""
        frame(410, 10)
        line(0, 90)
        line(0, 475)

        """CIRCLE"""
        #POSITIVE
        YELLOW_circle_move(move_X+2700, move_Y)
        RED_circle_move(move_X+2475, move_Y)
        VIOLET_circle_move(move_X+2250, move_Y)
        ORANGE_circle_move(move_X+2025, move_Y)
        RED_circle_move(move_X+1800, move_Y)
        GREEN_circle_move(move_X+1575, move_Y)
        VIOLET_circle_move(move_X+1350, move_Y)
        GREEN_circle_move(move_X+1125, move_Y)
        BLUE_circle_move(move_X+900, move_Y)
        VIOLET_circle_move(move_X+675, move_Y)
        BLUE_circle_move(move_X+450, move_Y)
        YELLOW_circle_move(move_X+225, move_Y)

        #ZERO
        RED_circle_move(move_X, move_Y)

        #NEGATIVE
        GREEN_circle_move(move_X-225, move_Y)
        YELLOW_circle_move(move_X-450, move_Y)
        GREEN_circle_move(move_X-675, move_Y)
        BLUE_circle_move(move_X-900, move_Y)
        ORANGE_circle_move(move_X-1125, move_Y)
        RED_circle_move(move_X-1350, move_Y)
        YELLOW_circle_move(move_X-1575, move_Y)
        VIOLET_circle_move(move_X-1800, move_Y)
        RED_circle_move(move_X-2025, move_Y)
        ORANGE_circle_move(move_X-2250, move_Y)
        GREEN_circle_move(move_X-2475, move_Y)
        YELLOW_circle_move(move_X-2700, move_Y)

        """TEXT"""
        #POSITIVE
        YELLOW_text_move(move_Text+2700, text_Y)
        RED_text_move(move_Text+2475, text_Y)
        VIOLET_text_move(move_Text+2250, text_Y)
        ORANGE_text_move(move_Text+2025, text_Y)
        RED_text_move(move_Text+1800, text_Y)
        GREEN_text_move(move_Text+1575, text_Y)
        VIOLET_text_move(move_Text+1350, text_Y)
        GREEN_text_move(move_Text+1125, text_Y)
        BLUE_text_move(move_Text+900, text_Y)
        RED_text_move(move_Text+675, text_Y)
        BLUE_text_move(move_Text+450, text_Y)
        YELLOW_text_move(move_Text+225, text_Y)

        #ZERO
        RED_text_move(move_Text, text_Y)

        #NEGATIVE
        GREEN_text_move(move_Text-225, text_Y)
        ORANGE_text_move(move_Text-450, text_Y)
        GREEN_text_move(move_Text-675, text_Y)
        BLUE_text_move(move_Text-900, text_Y)
        ORANGE_text_move(move_Text-1125, text_Y)
        RED_text_move(move_Text-1350, text_Y)
        YELLOW_text_move(move_Text-1575, text_Y)
        VIOLET_text_move(move_Text-1800, text_Y)
        ORANGE_text_move(move_Text-2025, text_Y)
        RED_text_move(move_Text-2250, text_Y)
        GREEN_text_move(move_Text-2475, text_Y)
        YELLOW_text_move(move_Text-2700, text_Y)

        button('SCORE: ', 850, 30, 100, 50, whit_code, whit_code)
        button('QUIT', 850, 650, 100, 50, dark_red_code, bright_red_code, quit_game)

        pygame.display.update()

################################################################################

game_intro()
gameplay()
pygame.quit()
quit()
