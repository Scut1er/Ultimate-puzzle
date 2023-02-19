import pygame.image

from defs import converting
from texts import *

# цвета, шрифты и размеры
screen = pygame.display.set_mode((900, 600))
anim_count = 0


# Спрайты анимации
class Animation(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.group = pygame.sprite.Group()
        self.image = pygame.image.load(name)
        self.rect = pygame.Rect(750, 450, 100, 100)


sprites = [Animation('images/1.png'), Animation('images/2.png'), Animation('images/3.png'),
           Animation('images/4.png'), Animation('images/5.png'), Animation('images/6.png'),
           Animation('images/7.png'), Animation('images/8.png'), Animation('images/1.png')]


# рендер стартового меню
def start_screen_render():
    global anim_count
    pygame.mixer.music.stop()
    screen.fill(black)
    screen.blit(start_text, start_rect)
    screen.blit(file_text, file_rect)
    current_sprite = sprites[anim_count // 5]
    screen.blit(current_sprite.image, current_sprite.rect)
    if anim_count >= 40:
        anim_count = 0
    else:
        anim_count += 1


# рендер экрана ошибки разрешения
def resolution_error_render(flag):
    screen = pygame.display.set_mode((900, 600))
    screen.fill(black)
    screen.blit(start_text, start_rect)
    if flag == 'max':
        screen.blit(file_error, file_error_rect)
        screen.blit(file_error1, file_error1_rect)
        screen.blit(file_error2, file_error2_rect)
    elif flag == 'min':
        screen.blit(min_size, min_size_rect)
        screen.blit(file_error2, file_error2_rect)


# рендер экрана выбора сложности
def choose_difficulty_render():
    screen.fill(black)
    screen.blit(title_text, title_rect)
    screen.blit(choose_text, choose_rect)
    screen.blit(easy_text, easy_rect)
    screen.blit(medium_text, medium_rect)
    screen.blit(hard_text, hard_rect)


# рендер таймера
def timer_render(duration, start_ticks, width, flag):
    global timer
    if not flag:
        seconds = (duration + pygame.time.get_ticks() - start_ticks) // 1000 % 60
        minutes = (duration + pygame.time.get_ticks() - start_ticks) // 1000 // 60
        if seconds < 10:
            timer = f'{minutes}:{"0" + str(seconds)}'
        else:
            timer = f'{minutes}:{seconds}'
        timer_text = font_sm_content.render(timer, True, white)
        timer_rect = timer_text.get_rect()
        timer_rect.center = (width // 2, 20)
        s = pygame.Surface((timer_text.get_width() + 10, timer_text.get_height()))
        s.set_alpha(150)
        s.fill(black)
        screen.blit(s, (width // 2 - timer_text.get_width() // 2 - 5, 1))
        screen.blit(timer_text, timer_rect)
    if flag:
        return timer


# рендер пазлов
def puzzles_render(cells, bg, cell_width, cell_height):
    for i, val in enumerate(cells):
        pos = cells[i]['pos']
        img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
        screen.blit(bg, cells[i]['rect'], img_area)
        pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)


# рендер финального экрана
def game_over_render(width, height, duration, start_ticks, im, bg_rect):
    if width >= height:
        font_title1 = pygame.font.Font('Arkhip.ttf', height // 12)
        font_content1 = pygame.font.Font('Arkhip.ttf', height // 24)
    else:
        font_title1 = pygame.font.Font('Arkhip.ttf', width // 12)
        font_content1 = pygame.font.Font('Arkhip.ttf', width // 24)
    play_again_text = font_title1.render('Сыграть ещё раз?', True, purple)
    play_again_rect = play_again_text.get_rect()
    play_again_rect.center = (width // 2, height // 2)

    continue_text = font_content1.render('Нажмите ПРОБЕЛ', True, white)
    continue_rect = continue_text.get_rect()
    continue_rect.center = (width // 2, height // 2 + 100)

    final_time = font_content1.render(f'Ваше время {timer_render(duration, start_ticks, width, True)}', True, white)
    final_rect = final_time.get_rect()
    final_rect.center = (width // 2, height // 2 - 100)

    screen.blit(converting(im), bg_rect)
    s = pygame.Surface((width, height))
    s.set_alpha(210)
    s.fill(black)
    screen.blit(s, (0, 0))
    screen.blit(play_again_text, play_again_rect)
    screen.blit(continue_text, continue_rect)
    screen.blit(final_time, final_rect)
