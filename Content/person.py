from pygame.sprite import Sprite
from pygame import Surface
from pygame import Rect
import pyganim
import animation
'''Анимация второстепеннных персонажей'''
class personage(Sprite):

    def __init__(self,w, h, x, y, arr_anim):
        Sprite.__init__(self)
        self.image = Surface((w, h)) #w - 192, h - 140
        self.rect = Rect(33, 10, 40, 50)
        self.rect.x = x
        self.rect.y = y

        # self.image.set_colorkey((0, 0, 0))
        self.image.set_colorkey((0, 255, 40))
        self.Pers = pyganim.PygAnimation(arr_anim)
        self.Pers.play()


    def anim(self):
        # self.image.fill((0, 0, 0))
        self.image.fill((0, 255, 40))
        self.Pers.blit(self.image, (0, 0))

'''Анимация частиц'''
class spurkle(Sprite):

    def __init__(self, w, h, x, y, arr_anim):
        Sprite.__init__(self)
        self.image = Surface((w, h))  # w - 192, h - 140
        self.rect = Rect(33, 10, 40, 50)
        self.rect.x = x
        self.rect.y = y

        self.image.set_colorkey((0, 0, 0))
        # self.image.set_colorkey((0, 255, 40))
        self.Pers = pyganim.PygAnimation(arr_anim)
        self.Pers.play()

    def anim(self):
        self.image.fill((0, 0, 0))
        # self.image.fill((0, 255, 40))
        self.Pers.blit(self.image, (0, 0))
