import pygame
from settings import *

class Menu:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.match_font(FONT_NAME)

    def text(self, text, size, colour, x, y):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def display_menu(self):
        self.title = "Assignment 2"
        self.begin = "Start"
        self.end = "Quit"
        self.help = "Help"
        self.instructions = "Controls:"
        self.left = "Left Arrow Key: Move Left"
        self.right = "Right Arrow Key: Move Right"
        self.space = "Space: Jump"
        self.pause = "P: Pause"
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill(BLACK)
            self.text(str(self.title), 80, WHITE, WIDTH / 2, 15)

            # RESUME HERE
            # pygame.draw.rect(self.screen, GREEN, (BUTTON_1_X, BUTTON_2_Y, BUTTON_1_WIDTH, BUTTON_1_HEIGHT))
            # pygame.draw.rect(self.screen, RED, (BUTTON_1_X, BUTTON_1_Y, BUTTON_1_WIDTH, BUTTON_1_HEIGHT))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if BUTTON_1_X + BUTTON_1_WIDTH > mouse[0] > BUTTON_1_X and BUTTON_2_Y + BUTTON_1_HEIGHT > mouse[1] > BUTTON_2_Y:
                pygame.draw.rect(self.screen, LIGHTBLUE, (BUTTON_1_X, BUTTON_2_Y, BUTTON_1_WIDTH, BUTTON_1_HEIGHT))
                if click[0] == 1:
                    menu = False
            else:
                pygame.draw.rect(self.screen, GREEN, (BUTTON_1_X, BUTTON_2_Y, BUTTON_1_WIDTH, BUTTON_1_HEIGHT))
            if BUTTON_1_X + BUTTON_1_WIDTH > mouse[0] > BUTTON_1_X and BUTTON_1_Y + BUTTON_1_HEIGHT > mouse[
                1] > BUTTON_1_Y:
                pygame.draw.rect(self.screen, LIGHTBLUE, (BUTTON_1_X, BUTTON_1_Y, BUTTON_1_WIDTH, BUTTON_1_HEIGHT))
                if click[0] == 1:
                    pygame.display.quit()
            else:
                pygame.draw.rect(self.screen, RED, (BUTTON_1_X, BUTTON_1_Y, BUTTON_1_WIDTH, BUTTON_1_HEIGHT))
            if BUTTON_1_X + BUTTON_1_WIDTH > mouse[0] > BUTTON_1_X and BUTTON_3_Y + BUTTON_1_HEIGHT > mouse[
                1] > BUTTON_3_Y:
                pygame.draw.rect(self.screen, LIGHTBLUE, (BUTTON_1_X, BUTTON_3_Y, BUTTON_1_WIDTH, BUTTON_1_HEIGHT))
                if click[0] == 1:
                    self.text(str(self.instructions), 20, WHITE, BUTTON_1_X + (BUTTON_1_WIDTH / 2),
                              (TEXT_HEIGHT + (BUTTON_1_HEIGHT / 2)) - 62)
                    self.text(str(self.left), 20, WHITE, BUTTON_1_X + (BUTTON_1_WIDTH / 2),
                              (TEXT_HEIGHT + (BUTTON_1_HEIGHT / 2)) - 42)
                    self.text(str(self.right), 20, WHITE, BUTTON_1_X + (BUTTON_1_WIDTH / 2),
                              (TEXT_HEIGHT + (BUTTON_1_HEIGHT / 2)) - 22)
                    self.text(str(self.space), 20, WHITE, BUTTON_1_X + (BUTTON_1_WIDTH / 2),
                              (TEXT_HEIGHT + (BUTTON_1_HEIGHT / 2)) - 2)
                    self.text(str(self.pause), 20, WHITE, BUTTON_1_X + (BUTTON_1_WIDTH / 2),
                              (TEXT_HEIGHT + (BUTTON_1_HEIGHT / 2)) + 22)
            else:
                pygame.draw.rect(self.screen, GREEN, (BUTTON_1_X, BUTTON_3_Y, BUTTON_1_WIDTH, BUTTON_1_HEIGHT))

            self.text(str(self.begin), 20, BLACK, BUTTON_1_X + (BUTTON_1_WIDTH / 2),
                      (BUTTON_2_Y + (BUTTON_1_HEIGHT / 2)) - 12)
            self.text(str(self.end), 20, BLACK, BUTTON_1_X + (BUTTON_1_WIDTH / 2),
                      (BUTTON_1_Y + (BUTTON_1_HEIGHT / 2)) - 12)
            self.text(str(self.help), 20, BLACK, BUTTON_1_X + (BUTTON_1_WIDTH / 2),
                      (BUTTON_3_Y + (BUTTON_1_HEIGHT / 2)) - 12)
            pygame.display.flip()
