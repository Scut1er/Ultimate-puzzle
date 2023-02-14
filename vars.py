import pygame

pygame.init()
dp = pygame.display.Info()
dp_w = dp.current_w
dp_h = dp.current_h

clock = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load('images/icon1.jpg'))
pygame.display.set_caption('Ultimate Puzzles')
pygame.mixer.music.load('music/Dinner Talk - Sergey Eybog.ogg')


width = 900
height = 600

white = (255, 255, 255)
purple = (128, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

bg = None
bg_rect = None
anim_count = 0
FPS = 15
volume = 1
duration = 0
pygame.mixer.music.set_volume(0.2 * volume)

start_playing = True
selected_img = None
is_game_over = False
show_start_screen = True
choose_difficulty = False
resolution_error = False
saving_error = False
playing = False


cells = None
cell_width = None
cell_height = None
start_ticks = None
im = None
