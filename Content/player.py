
from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from pygame.key import get_pressed
from pygame import constants
from pygame import Rect
from Levels import level
import animation
import pyganim


walk = 4.3
jump = 7
FORSE = 1000
GRAVITY = .2
UPFLYING = .05
class Pony(Sprite):

    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((96, 86))
        #self.image.fill((27, 27, 27))
        #self.rect = self.image.get_rect()
        self.rect = Rect(33, 10, 40, 50)
        self.Right = True
        self.Left = False
        self.Walk = False
        self.Fly = False
        self.Down = False
        self.comment = False
        self.message = False
        self.counter = 0
        self.score = 0
        self.FlyCounter = 0
        self.yvel = 0
        self.xvel = 0
        self.rect.x = x
        self.rect.y = y
        self.onGround = False

        self.image.set_colorkey((0, 255, 40))
        '''Анимация когда песонаж стоит (направо)'''
        self.AnimStayRight = pyganim.PygAnimation(animation.PONY_STAY_RIGHT)
        self.AnimStayRight.play()
        '''Анимация когда песонаж стоит (налево)'''
        self.AnimStayLeft = pyganim.PygAnimation(animation.PONY_STAY_LEFT)
        self.AnimStayLeft.play()


        '''Анимация ходьбы направо'''
        self.AnimWalkRight = pyganim.PygAnimation(animation.PONY_WALK_RIGHT)
        self.AnimWalkRight.play()
        '''Анимация ходьбы навлево'''
        self.AnimWalkLeft = pyganim.PygAnimation(animation.PONY_WALK_LEFT)
        self.AnimWalkLeft.play()


        '''Анимация Полета (направо)'''
        self.AnimFlyRight = pyganim.PygAnimation(animation.PONY_FLY_RIGHT)
        self.AnimFlyRight.play()
        '''Анимация Полета (налево)'''
        self.AnimFlyLeft = pyganim.PygAnimation(animation.PONY_FLY_LEFT)
        self.AnimFlyLeft.play()

    def control(self, WIDTH, HEIGHT):
        # Блок отслеживания нажатия клавиш
        keys = get_pressed()
        # Если нажат робел - прыгнуть
        if keys[constants.K_SPACE]:
            if self.onGround and self.counter + 170 < FORSE:
                self.yvel -= jump
                self.counter += 50
        # Если Зажат W или стрелка вверх - полететь
        if (keys[constants.K_w] and self.rect.y - 86 > 0) or (keys[constants.K_UP] and self.rect.y - 86 > 0):
            self.Fly = True
            if self.counter < FORSE and self.Fly:
                self.counter += 1
                #self.rect.y -= .5
                if self.yvel > 0:
                    self.yvel -= GRAVITY + UPFLYING + .2
                else:
                    self.yvel -= GRAVITY + UPFLYING

        # Если нажата S или Стрелка вниз - Спрыгнуть с платформы
        if keys[constants.K_s] and self.rect.y < 1720:
            self.Down = True
        # Если Зажата D или Стрелка вправо - идти вправо
        if keys[constants.K_d] or keys[constants.K_RIGHT]:
            if self.FlyCounter > 0 and self.counter < FORSE:
                self.xvel = walk + 2
            else:
                self.xvel = walk
            self.Right = True
            self.Left = False
            self.Walk = True
        # Если Зажата A или Стрелка влево - идти влево
        #if (keys[constants.K_a] and self.rect.x > 2) or (keys[constants.K_LEFT] and self.rect.x > 2):
        if keys[constants.K_a] or keys[constants.K_LEFT]:
            if self.FlyCounter > 0 and self.counter < FORSE:
                self.xvel = -walk - 2
            else:
                self.xvel = -walk
            self.Right = False
            self.Left = True
            self.Walk = True

        # Тестовые кнопки
        # Респавн (на случай выпада из мира)
        if keys[constants.K_r]:
            self.rect.y = HEIGHT - 150
            self.rect.x = 55
        if keys[constants.K_g]:
            self.rect.y = HEIGHT - 150
            self.rect.x = WIDTH - 150
        if self.rect.y > HEIGHT - 114:
            self.rect.y = HEIGHT - 114
            self.yvel = 0
        # Восполнение Силы
        if keys[constants.K_h]:
            self.counter = 0
        self.AnimPony()
        self.onGround = False
        self.Fly = False
        #self.Walk = False


    def AnimPony(self):
        # Определение стоит ли персонаж или нет
        if not self.Walk:
            # В какую чторону он смотрит
            if self.Right:
                self.image.fill((0, 255, 40))
                self.AnimStayRight.blit(self.image, (0, 0))
            if self.Left:
                self.image.fill((0, 255, 40))
                self.AnimStayLeft.blit(self.image, (0, 0))
        # Если не стоит то идет
        else:
            # В какую сторону идет
            if self.Right:
                self.image.fill((0, 255, 40))
                self.AnimWalkRight.blit(self.image, (0, 0))
            if self.Left:
                self.image.fill((0, 255, 40))
                self.AnimWalkLeft.blit(self.image, (0, 0))
        # Летит ли счас персонаж и хватает ли ему силы
        if self.Fly and self.counter < FORSE:
            self.FlyCounter = 1
            if self.Right:
                self.image.fill((0, 255, 40))
                self.AnimFlyRight.blit(self.image, (0, 0))
            if self.Left:
                self.image.fill((0, 255, 40))
                self.AnimFlyLeft.blit(self.image, (0, 0))
        # Если персонаж не летит но находится в воздухе после полета - проигрывать туже анимацию
        if not self.Fly and self.FlyCounter > 0 and not self.onGround:
            self.FlyCounter -= .007
            if self.Right:
                self.image.fill((0, 255, 40))
                self.AnimFlyRight.blit(self.image, (0, 0))
            if self.Left:
                self.image.fill((0, 255, 40))
                self.AnimFlyLeft.blit(self.image, (0, 0))

    def gravity(self, Collision):
        if not self.onGround:
            if self.FlyCounter > 0 and self.FlyCounter < 1:
                self.yvel += GRAVITY / 2
            else:
                self.yvel += GRAVITY
        if self.Walk:
            self.rect.x += self.xvel
            self.Walk = False


        # Вызов: Проверка на столконовения героя с обьектами 
        self.collide(self.xvel, 0, Collision)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, Collision)
        self.Down = False

        keys = get_pressed()
        if not self.Fly and self.counter >= .5 and not keys[constants.K_w] and not keys[constants.K_UP]:
            self.counter -= .5
    # Проверка на столконовения героя с обьектами
    def collide(self, xvel, yvel, Collision):
        for ob in Collision:
            if collide_rect(self, ob):
                if xvel > 0:
                    self.rect.right = ob.rect.left
                if xvel < 0:
                    self.rect.left = ob.rect.right
                if yvel > 0:
                    self.rect.bottom = ob.rect.top
                    self.onGround = True
                    self.yvel = 0
                    self.FlyCounter = 0
                if yvel < 0:
                    self.rect.top = ob.rect.bottom
                    self.yvel = 0


                if self.Down:
                    self.rect.top = ob.rect.bottom
                    self.Down = False

    def collect_clue(self, xvel, yvel, clu, cluespr, check):
        for ob in clu:
            if collide_rect(self, ob):
                if xvel > 0:
                    self.message = True
                    if check:
                        self.score += 1
                        clu.remove(ob)
                        cluespr.remove(ob)
                        self.comment = True
                if xvel < 0:
                    self.message = True
                    if check:
                        self.score += 1
                        clu.remove(ob)
                        cluespr.remove(ob)
                        self.comment = True
                # if yvel > 0:
                #     self.score += 1
                #     clu.remove(ob)
                #     cluespr.remove(ob)
                #     self.comment = True
                # if yvel < 0:
                #     self.score += 1
                #     clu.remove(ob)
                #     cluespr.remove(ob)
                #     self.comment = True
