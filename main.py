import pygame, random, shelve
from tkinter import *
from tkinter import filedialog
from PIL import Image
from vars import *
from animation import *
from screens import *
from defs import converting


class Save:
    def __init__(self):
        self.file = shelve.open('save')

    def saving(self):
        self.file['data'] = cells
        im.save('save_img.jpg')
        self.file['rect'] = bg_rect
        self.file['w'] = cell_width
        self.file['h'] = cell_height

    def get_info(self):
        sv_data = self.file['data']
        sv_file_name = self.file['back']
        sv_rect = self.file['rect']
        sv_w = self.file['w']
        sv_h = self.file['h']
        return [sv_data, sv_file_name, sv_rect, sv_w, sv_h]

    def __del__(self):
        self.file.close()


saving = Save()

pygame.display.set_caption('Ultimate Puzzles')
clock = pygame.time.Clock()


def start_game(num):
    global cells, cell_width, cell_height, show_start_screen
    rows = num
    cols = num
    num_cells = rows * cols

    cell_width = width // rows
    cell_height = height // cols

    cells = []
    rand_indexes = list(range(0, num_cells))

    for i in range(num_cells):
        x = (i % rows) * cell_width
        y = (i // cols) * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)
        rand_pos = random.choice(rand_indexes)
        rand_indexes.remove(rand_pos)
        cells.append({'rect': rect, 'border': white, 'order': i, 'pos': rand_pos})

    show_start_screen = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if show_start_screen:
                tk = Tk()
                tk.withdraw()
                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    file_name = filedialog.askopenfilename(title='IMAGES',
                                                           filetypes=[('JPEG images', '.jpg'), ('PNG images', '.png'),
                                                                      ('BMP images', '.bmp')])
                    if file_name != '':
                        im = Image.open(file_name)
                        (width, height) = im.size
                        pixels = im.load()
                        # проверка на ошибку разрешения
                        if width <= dp_w and height <= dp_h:
                            bg = pygame.image.load(file_name)
                            bg_rect = bg.get_rect()
                            bg_rect.topleft = (0, 0)
                            choose_difficulty = True
                            error = False

                        else:
                            show_start_screen = False
                            error = True
                            is_game_over = True

                if keys[pygame.K_F3]:
                    cells = saving.get_info()[0]
                    bg = pygame.image.load('save_img.jpg')
                    bg_rect = saving.get_info()[2]
                    im = Image.open('save_img.jpg')
                    (width, height) = im.size
                    cell_width = saving.get_info()[3]
                    cell_height = saving.get_info()[4]

                    screen = pygame.display.set_mode((width, height))
                    error = False
                    show_start_screen = False

                if choose_difficulty is True:
                    if keys[pygame.K_1]:
                        choose_difficulty = False

                        screen = pygame.display.set_mode((width, height))
                        start_game(3)
                    elif keys[pygame.K_2]:
                        choose_difficulty = False

                        screen = pygame.display.set_mode((width, height))
                        start_game(5)
                    elif keys[pygame.K_3]:
                        choose_difficulty = False

                        screen = pygame.display.set_mode((width, height))
                        start_game(10)

            if is_game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    is_game_over = False
                    show_start_screen = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_game_over:
            mouse_pos = pygame.mouse.get_pos()

            for cell in cells:
                rect = cell['rect']
                order = cell['order']

                if rect.collidepoint(mouse_pos):
                    if not selected_img:
                        selected_img = cell
                        cell['border'] = red
                    else:
                        current_img = cell
                        if current_img['order'] != selected_img['order']:
                            # перестановка клеток
                            temp = selected_img['pos']
                            cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                            cells[current_img['order']]['pos'] = temp
                            cells[selected_img['order']]['border'] = white
                            selected_img = None
                            # проверка собран ли пазл
                            is_game_over = True
                            for cell in cells:
                                if cell['order'] != cell['pos']:
                                    is_game_over = False

    if show_start_screen:
        screen = pygame.display.set_mode((900, 600))
        screen.fill(black)
        screen.blit(start_text, start_rect)
        screen.blit(file_text, file_rect)
        current_sprite = sprites[anim_count // 5]
        screen.blit(current_sprite.image, current_sprite.rect)
        if anim_count >= 40:
            anim_count = 0
        else:
            anim_count += 1

    else:  # ошибка разешения изображения
        if error is True:
            screen = pygame.display.set_mode((900, 600))
            screen.fill(black)
            screen.blit(start_text, start_rect)
            screen.blit(file_error, file_error_rect)
            screen.blit(file_error1, file_error1_rect)
            screen.blit(file_error2, file_error2_rect)

        screen.fill(black)
        screen.blit(start_text, start_rect)
        screen.blit(file_error, file_error_rect)
        screen.blit(file_error1, file_error1_rect)
        screen.blit(file_error2, file_error2_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            show_start_screen = True

    if not is_game_over:
        for i, val in enumerate(cells):
            pos = cells[i]['pos']
            img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
            screen.blit(bg, cells[i]['rect'], img_area)
            pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            saving.saving()
    if is_game_over is True and error is False:
        if width >= height:
            font_title1 = pygame.font.Font('Arkhip.ttf', height // 12)
            font_content1 = pygame.font.Font('Arkhip.ttf', height // 24)
        else:
            font_title1 = pygame.font.Font('Arkhip.ttf', width // 12)
            font_content1 = pygame.font.Font('Arkhip.ttf', width // 24)
        play_again_text = font_title1.render('Сыграть ещё раз?', True, purple)
        play_again_rect = play_again_text.get_rect()
        play_again_rect.center = (width // 2, height // 2)

        continue_text = font_content1.render('Нажмите ПРОБЕЛ', True, cian)
        continue_rect = continue_text.get_rect()
        continue_rect.center = (width // 2, height // 2 + 100)
        screen.blit(converting(im), bg_rect)
        screen.blit(play_again_text, play_again_rect)
        screen.blit(continue_text, continue_rect)
        cells.clear()

    if choose_difficulty:
        screen.fill(black)
        screen.blit(title_text, title_rect)
        screen.blit(choose_text, choose_rect)
        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
