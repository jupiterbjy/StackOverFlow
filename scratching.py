# the following code will always put the screen in the top corner
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (20, 20)
import random
from pygame import *

init()
size = width, height = 1000, 700
screen = display.set_mode(size)

# define colours
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pink = (255, 192, 203)
light_pink = (255, 183, 193)
light_pink2 = (255, 192, 203)
hot_pink = (255, 105, 180)
peachpuff = (255, 218, 185)
violet = (199, 21, 133)
scoreboard = (128, 71, 3)

# define fonts
menuFont = font.SysFont("Times New Roman", 60)

# states in the Game
STATE_MENU = 0
STATE_GAME = 1
STATE_RULES = 2
STATE_QUIT = 3
player = []
playerMove = 2


def drawMenu(screen, button, mx, my, state):
    global player
    blockWidth = width // 3
    blockHeight = height // 7
    rectList = [Rect(blockWidth, blockHeight, blockWidth, blockHeight),  # game choice
                Rect(blockWidth, 3 * blockHeight, blockWidth, blockHeight),  # help choice
                Rect(blockWidth, 5 * blockHeight, blockWidth, blockHeight)]  # quite choice
    stateList = [STATE_GAME, STATE_RULES, STATE_QUIT]
    titleList = ["Play Game", "Rules", "Quit Game"]
    draw.rect(screen, peachpuff, (0, 0, width, height))

    for i in range(len(rectList)):
        rect = rectList[i]  # get the current Rect
        draw.rect(screen, violet, rect)  # draw the Rect
        text = menuFont.render(titleList[i], 1, black)  # make the font`
        textWidth, textHeight = menuFont.size(titleList[i])  # get the font size
        useW = (blockWidth - textWidth) // 2  # use for centering
        useH = (blockHeight - textHeight) // 2
        # getting a centered Rectangle
        textRect = Rect(rect[0] + useW, rect[1] + useH, textWidth, textHeight)
        screen.blit(text, textRect)  # draw to screen

        if rect.collidepoint(mx, my):
            draw.rect(screen, black, rect, 2)
            if button == 1:
                state = stateList[i]
                if STATE_GAME:
                    player = [random.randint(10, width + 10), random.randint(height // 5 - 10, height + 10)]

    return state


def drawScoreboard(screen, mx, my, button):
    # drawing the score board
    scoreboardHeight, scoreboardWidth = height // 5, width // 6
    draw.rect(screen, scoreboard, (0, 0, width, scoreboardHeight))
    draw.rect(screen, black, (0, 0, width, scoreboardHeight), 3)
    string = "Welcome to your first day as a garbage collector!"
    text = menuFont.render(string, 0, red)
    screen.blit(text, Rect(10, 500, 500, 500))
    backRect = Rect((0, 0, width // 15, scoreboardHeight // 3))
    draw.rect(screen, green, backRect)

    # if the ball collides with the back button it will either bold itself
    # or else it will just have a 1 pixel rect around
    if backRect.collidepoint(mx, my):
        draw.rect(screen, black, backRect, 3)
        if button == 1:
            return STATE_MENU
    else:
        draw.rect(screen, black, backRect, 1)


def drawGame(screen, button, mx, my, state):
    global player
    scoreboardHeight = height // 5
    draw.rect(screen, blue, (0, 0, width, height))
    draw.rect(screen, black, (0, 0, width, height), 2)
    state = drawScoreboard(screen, mx, my, button)
    # character drawing
    draw.circle(screen, light_pink2, player, 10)
    draw.circle(screen, black, player, 12, 1)

    if button == 3:
        state = STATE_MENU

    if mx < player[0] and mx >= 10 + playerMove:
        player[0] -= playerMove

    if my < player[1] and my >= scoreboardHeight + 10:
        player[1] -= playerMove

    if mx > player[0] and mx <= width - 10:
        player[0] += playerMove

    if my > player[1] and mx <= height + 10:
        player[1] += playerMove

    return state


def drawRules(screen, button, mx, my, state):
    draw.rect(screen, pink, (0, 0, width, height))
    string = "Hi there!"
    text = menuFont.render(string, 0, red)
    screen.blit(text, Rect(430, 100, 500, 500))
    if button == 3:
        state = STATE_MENU
    return state


running = True
# myClock = time.Clock()
# initializing variables
state = STATE_MENU
mx = my = 0

# Game Loop
while running:
    button = 0
    for e in event.get():  # checks all events that happen
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos
            button = e.button
        elif e.type == MOUSEMOTION:
            mx, my = e.pos
            # button = e.button

    print(state)
    if state == STATE_MENU:
        state = drawMenu(screen, button, mx, my, state)
    elif state == STATE_GAME:
        state = drawGame(screen, button, mx, my, state)
    elif state == STATE_RULES:
        state = drawRules(screen, button, mx, my, state)
    else:
        running = False

    display.flip()

# myClock.tick(60) # waits long enough to have 60 fps
event.get()
quit()
