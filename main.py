import pygame
from tkinter import *
from tkinter import filedialog
from PIL import Image
from vars import *
from screens import *
from defs import change_volume, create_puzzles
from save import saver

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and playing:
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
                            # перестановка пазлов
                            temp = selected_img['pos']
                            cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                            cells[current_img['order']]['pos'] = temp
                            cells[selected_img['order']]['border'] = white
                            selected_img = None
                            # проверка собран ли пазл
                            playing = False
                            is_game_over = True
                            for cell in cells:
                                if cell['order'] != cell['pos']:
                                    playing = True
                                    is_game_over = False

    if show_start_screen:  # начальный экран
        start_playing = True
        screen = pygame.display.set_mode((900, 600))
        start_screen_render()

        if not saving_error:
            screen.blit(f3_text, f3_rect)
        else:  # демонстрация ошибки сохранения
            screen.blit(saving_error_text, saving_error_rect)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            saving_error = False
            tk = Tk()
            tk.withdraw()
            file_name = filedialog.askopenfilename(title='IMAGES',
                                                   filetypes=[('JPEG images', '.jpg'), ('PNG images', '.png'),
                                                              ('BMP images', '.bmp')])
            if file_name != '':
                im = Image.open(file_name)
                (width, height) = im.size
                pixels = im.load()
                if width > dp_w or height > dp_h:  # проверка на ошибку максимального разрешения
                    show_start_screen = False
                    resolution_error = 'max'
                elif width < 300 or height < 300:  # проверка на ошибку минимального разрешения
                    show_start_screen = False
                    resolution_error = 'min'
                else:
                    bg = pygame.image.load(file_name)
                    bg_rect = bg.get_rect()
                    bg_rect.topleft = (0, 0)
                    choose_difficulty = True
                    show_start_screen = False
                    tk.destroy()
        if keys[pygame.K_d]:
            if saver.get_info():
                saving_error = False
                cells, bg_rect, cell_width, cell_height, duration = saver.get_info()
                bg = pygame.image.load('save_img.jpg')
                im = Image.open('save_img.jpg')
                (width, height) = im.size
                screen = pygame.display.set_mode((width, height))
                playing = True
                show_start_screen = False
            else:
                saving_error = True

    if resolution_error != '':  # экран ошибки разрешения
        keys = pygame.key.get_pressed()
        if resolution_error == 'max':
            resolution_error_render('max')  # отрисовка экрана ошибки максимального разрешения
        elif resolution_error == 'min':
            resolution_error_render('min')  # отрисовка экрана ошибки минимального разрешения
        if keys[pygame.K_SPACE]:
            show_start_screen = True
            resolution_error = ''

    if choose_difficulty:  # экран выбор сложности
        choose_difficulty_render()  # отрисовка экрана выбора сложности
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            screen = pygame.display.set_mode((width, height))
            cells, cell_width, cell_height = create_puzzles(3, width, height)
            choose_difficulty = False
            playing = True

        elif keys[pygame.K_2]:
            screen = pygame.display.set_mode((width, height))
            cells, cell_width, cell_height = create_puzzles(5, width, height)
            choose_difficulty = False
            playing = True

        elif keys[pygame.K_3]:
            screen = pygame.display.set_mode((width, height))
            cells, cell_width, cell_height = create_puzzles(10, width, height)
            choose_difficulty = False
            playing = True
        elif keys[pygame.K_ESCAPE]:
            show_start_screen = True
            choose_difficulty = False

    if playing:  # экран игрового процесса
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:  # увеличение громкости музыки
            volume = change_volume(True, volume)
        if keys[pygame.K_DOWN]:  # уменьшение громкости музыки
            volume = change_volume(False, volume)
        if start_playing:
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.play(-1)
            start_playing = False
        puzzles_render(cells, bg, cell_width, cell_height)  # отрисовка пазлов на экране
        timer_render(duration, start_ticks, width, False)  # отрисовка таймера на экране
        if keys[pygame.K_ESCAPE]:
            saver.saving(cells, im, bg_rect, cell_width, cell_height, duration, start_ticks)
            duration = 0
            start_playing = True
            show_start_screen = True
            playing = False

    if is_game_over:  # экран окончания игры
        start_playing = True
        duration = 0
        game_over_render(width, height, duration, start_ticks, im, bg_rect)  # отрисовка экрана окончания игры
        cells.clear()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            is_game_over = False
            show_start_screen = True

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
