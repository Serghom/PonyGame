from pygame.sprite import Sprite
from pygame.image import load
from pygame import Rect

class world(Sprite):
    def __init__(self, filename, x, y, w, h):
        Sprite.__init__(self)
        self.image = load(filename).convert_alpha()
        #self.rect = self.image.get_rect()
        self.rect = Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y