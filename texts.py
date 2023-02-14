import pygame
from vars import *


font_title = pygame.font.Font('Arkhip.ttf', 80)
font_content = pygame.font.Font('Arkhip.ttf', 40)
font_sm_content = pygame.font.Font('Arkhip.ttf', 30)
font_help_content = pygame.font.Font('Arkhip.ttf', 20)


# стартовый экран
start_text = font_title.render('Ultimate Puzzles', True, purple)
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

file_error2 = font_sm_content.render("Нажмите ПРОБЕЛ чтобы продолжить", True, white)
file_error2_rect = file_error2.get_rect()
file_error2_rect.center = (width // 2, height // 2 + 160)

# экран выбора сложности
title_text = font_title.render('Ultimate Puzzles', True, purple)
title_rect = title_text.get_rect()
title_rect.center = (width // 2, height // 2 - 160)

choose_text = font_content.render('Выберите сложность', True, purple)
choose_rect = choose_text.get_rect()
choose_rect.center = (width // 2, height // 2 - 20)

easy_text = font_content.render("Press '1' - Easy (3x3)", True, white)
easy_rect = easy_text.get_rect()
easy_rect.center = (width // 2, height // 2 + 60)

medium_text = font_content.render("Press '2' - Medium (5x5)", True, white)
medium_rect = medium_text.get_rect()
medium_rect.center = (width // 2, height // 2 + 110)

hard_text = font_content.render("Press '3' - Hard (10x10)", True, white)
hard_rect = hard_text.get_rect()
hard_rect.center = (width // 2, height // 2 + 160)

f3_text = font_help_content.render("*F3 для загрузки последнего сохранения", True, white)
f3_rect = f3_text.get_rect()
f3_rect.center = (width // 2, height - 100)

saving_error_text = font_sm_content.render("Файл сохранения отсутствует", True, white)
saving_error_rect = saving_error_text.get_rect()
saving_error_rect.center = (width // 2, height - 100)
