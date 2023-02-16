import pygame, random
from PIL import Image


# функция создания пазлов
def create_puzzles(num, width, height):
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
        cells.append({'rect': rect, 'border': (255, 255, 255), 'order': i, 'pos': rand_pos})
    return [cells, cell_width, cell_height]


# функция создания фона для финального экрана
def converting(image):
    im_final = image.convert("L")
    im_final.save('final.jpg')
    bg_final = pygame.image.load('final.jpg')
    return bg_final


# функция изменения громкости
def change_volume(flag, volume):
    if flag:
        if 0 <= volume < 10:
            volume += 1
            pygame.mixer.music.set_volume(0.1 * volume)
            return volume
        elif volume == 10:
            return volume
    else:
        if 0 < volume <= 10:
            volume -= 1
            pygame.mixer.music.set_volume(0.1 * volume)
            return volume
        elif volume == 0:
            return volume
