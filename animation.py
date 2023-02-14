import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.group = pygame.sprite.Group()
        self.image = pygame.image.load(name)
        self.rect = pygame.Rect(750, 450, 100, 100)


sprites = [Animation('images/1.png'), Animation('images/2.png'), Animation('images/3.png'),
           Animation('images/4.png'), Animation('images/5.png'), Animation('images/6.png'),
           Animation('images/7.png'), Animation('images/8.png'), Animation('images/1.png')]
