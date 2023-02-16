import pygame
from vars import *

# шрифты для текста
font_title = pygame.font.Font('Arkhip.ttf', 80)
font_content = pygame.font.Font('Arkhip.ttf', 40)
font_sm_content = pygame.font.Font('Arkhip.ttf', 30)
font_help_content = pygame.font.Font('Arkhip.ttf', 20)

# стартовый экран
start_text = font_title.render('Ultimate Puzzle', True, purple)
start_rect = start_text.get_rect()
start_rect.center = (width // 2, height // 2 - 160)

file_text = font_sm_content.render("Нажмите ПРОБЕЛ для выбора изображения", True, white)
file_rect = file_text.get_rect()
file_rect.center = (width // 2, height // 2 + 60)

# экран ошибки разрешения
file_error = font_sm_content.render("Разрешение изображения больше", True, white)
file_error_rect = file_error.get_rect()
file_error_rect.center = (width // 2, height // 2 + 20)

file_error1 = font_sm_content.render("разрешения монитора.", True, white)
file_error1_rect = file_error1.get_rect()
file_error1_rect.center = (width // 2, height // 2 + 60)

#  текст ошибки минимального разрешения
min_size = font_sm_content.render("Изображение меньше формата 300x300 ", True, white)
min_size_rect = min_size.get_rect()
min_size_rect.center = (width // 2, height // 2 + 60)

# пробел для продолжения
file_error2 = font_sm_content.render("Нажмите ПРОБЕЛ чтобы продолжить", True, white)
file_error2_rect = file_error2.get_rect()
file_error2_rect.center = (width // 2, height // 2 + 160)

# экран выбора сложности
title_text = font_title.render('Ultimate Puzzle', True, purple)
title_rect = title_text.get_rect()
title_rect.center = (width // 2, height // 2 - 160)

# выбор сложности
choose_text = font_content.render('Выберите сложность', True, purple)
choose_rect = choose_text.get_rect()
choose_rect.center = (width // 2, height // 2 - 20)

# выбор лёгкого режима
easy_text = font_content.render("Нажмите '1' - Easy (3x3)", True, white)
easy_rect = easy_text.get_rect()
easy_rect.center = (width // 2, height // 2 + 60)

# выбор среднего режима
medium_text = font_content.render("Нажмите '2' - Medium (5x5)", True, white)
medium_rect = medium_text.get_rect()
medium_rect.center = (width // 2, height // 2 + 110)

# выбор сложного режима
hard_text = font_content.render("Нажмите '3' - Hard (10x10)", True, white)
hard_rect = hard_text.get_rect()
hard_rect.center = (width // 2, height // 2 + 160)

# выбор хардкор режима
hardkor_text = font_sm_content.render("Не нажимайте '4'", True, red)
hardkor_rect = hardkor_text.get_rect()
hardkor_rect.center = (width // 2, height // 2 + 240)

# подсказка для загрузки сохранения
f3_text = font_help_content.render("*D для загрузки последнего сохранения", True, white)
f3_rect = f3_text.get_rect()
f3_rect.center = (width // 2, height - 100)

# текст отсутсвия файла сохранения
saving_error_text = font_sm_content.render("Файл сохранения отсутствует", True, white)
saving_error_rect = saving_error_text.get_rect()
saving_error_rect.center = (width // 2, height - 100)
