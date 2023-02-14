import shelve, pygame


class Save:
    def __init__(self):
        self.file = shelve.open('save')

    def saving(self, cells, im, bg_rect, cell_width, cell_height, duration, start_ticks):
        self.file['data'] = cells
        im.save('save_img.jpg')
        self.file['rect'] = bg_rect
        self.file['w'] = cell_width
        self.file['h'] = cell_height
        self.file['time'] = duration + pygame.time.get_ticks() - start_ticks

    def get_info(self):
        sv_data = self.file.get('data', 'empty')
        sv_rect = self.file.get('rect', 'empty')
        sv_w = self.file.get('w', 'empty')
        sv_h = self.file.get('h', 'empty')
        save_time = self.file.get('time', 'empty')
        if sv_data == 'empty' or sv_rect == 'empty' or sv_w == 'empty' or sv_h == 'empty' or save_time == 'empty':
            return False
        else:
            return [sv_data, sv_rect, sv_w, sv_h, int(save_time)]

    def __del__(self):
        self.file.close()


saver = Save()
