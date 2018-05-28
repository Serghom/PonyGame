import pygame, os
from all_texture import world
from player import Pony
from player import FORSE
from sys import exit
from time import sleep
import Levels
import evidence
import template
import Music_and_Sounds
import settingsFile
import story
import animation
import person


pygame.init()
# Текст
pygame.font.init()
sh = 12
myfont = pygame.font.SysFont('Calibri', sh, 1)
scorefont = pygame.font.SysFont('Calibri', 20, 1, 1)
swichfont = pygame.font.SysFont('Calibri', 40, 0, 1)
act_font = pygame.font.SysFont('Calibri', 15, 0, 1)
end_font = pygame.font.SysFont('Calibri', 30, 0, 1)
# Название окна
# Параметры окна
# разрешение экрана
try:
    file = open('settings/sett.set')
except IOError as e:
    #print(u'не удалось открыть файл')
    W = pygame.display.list_modes(0, pygame.FULLSCREEN)[0][0]
    H = pygame.display.list_modes(0, pygame.FULLSCREEN)[0][1]
    fullscreen = True
    Mus = False
    W, H, fullscreen, Mus = settingsFile.opensett(True, W, H, fullscreen, Mus)
else:
    with file:
        W, H, fullscreen, Mus = settingsFile.opensett(True, 0, 0, 0, 0)


width, height = W, H




print(pygame.display.list_modes(0, pygame.FULLSCREEN))
print(len(pygame.display.list_modes(0, pygame.FULLSCREEN)) - 6)

#SIZE = pygame.display.list_modes(0, pygame.FULLSCREEN)[0]
# Флаги экрана
#flag = pygame.RESIZABLE
flag = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.RESIZABLE

window = pygame.display.set_mode((W, H), flag)
screen = pygame.Surface((W, H))

def create_window(WIDTH, HEIGHT, fullscreen):
    global screen, window
    """создание окна под новые размеры весоты и ширины"""
    #if not os.getenv('SDL_VIDEODRIVER'):
    # Окно
    if fullscreen:
        #WIDTH, HEIGHT = 640, 480
        screen = pygame.Surface((WIDTH, HEIGHT))
        window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        print(window.get_size())
    else:
        print(window.get_size())
        screen = pygame.Surface((WIDTH, HEIGHT))
        window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)


    return window


# Константы цвета
SKY = (1, 147, 204)
GRASS = (1, 162, 26)


# Создание героя
hero = Pony(55, 2000)



# Создание уровня
def SwLevel(Nomber):
    global back, Level, ArBack, sdvig, Middle, Front, fon, evid
    # Задний Фон
    if Nomber == 1:
        back = world('background/Mountain.png', 0, 0, 0, 0)
        fon = back.image
        back.image = pygame.transform.scale(fon, (width + 100, height + 500))
        evid = evidence.clues(template.First_clue)
        evid.create_clues()
        Level = Levels.level(template.First_collevel, template.First_Grlevel)
        Level.create_level(hero)
        ArBack = pygame.sprite.Group()
        Middle = pygame.sprite.Group()
        Front = pygame.sprite.Group()
        for i in range(int(Level.level_width / 587) + 1):
            front = world('background/everfree/front.png', 587 * i, height - 600, 0, 0)
            front.x = front.rect.x
            front.y = front.rect.y
            Front.add(front)

        for i in range(int(Level.level_width / 587) + 1):
            midd = world('background/everfree/middle.png', 587 * i, height - 600, 0, 0)
            midd.x = midd.rect.x
            midd.y = midd.rect.y
            Middle.add(midd)

        for i in range(int(Level.level_width / 587) + 1):
            bac = world('background/everfree/back.png', 587 * i, height - 600, 0, 0)
            bac.x = bac.rect.x
            bac.y = bac.rect.y
            ArBack.add(bac)
        #Levels.first_level(hero)
        back.sdvig = Level.level_width / 1600  # 1600 - длинна бэкграунда

    if Nomber == 2:
        Level = Levels.level(template.Second_collevel, template.Second_Grlevel)
        Level.create_level(hero)
        evid = evidence.clues(template.Second_clue)
        evid.create_clues()
        back = world('background/ponyville/sky.png', 0, 0, 0, 0)
        fon = back.image
        back.image = pygame.transform.scale(fon, (width, height))
        #print("Уровень фона на 2 уровне: " + str(back.rect.y))
        #sdvig = Level.level_width / 800  # 800 - длинна бэкграунда
        ArBack = pygame.sprite.Group()
        Middle = pygame.sprite.Group()
        Front = pygame.sprite.Group()

        for i in range(int(Level.level_width / 1916) + 1):
            front = world('background/ponyville/front.png', 1894 * i, height - 500, 0, 0)

            front.x = front.rect.x
            front.y = front.rect.y
            Front.add(front)

        for i in range(int(Level.level_width / 2045) + 1):
            midd = world('background/ponyville/middle.png', 2045 * i, height - 280, 0, 0)
            midd.x = midd.rect.x
            midd.y = midd.rect.y
            Middle.add(midd)

        ArBack.add(back)
    if Nomber == 3:
        back = world('background/tron/canterlot_throne_room_background.png', 0, 0, 0, 0)
        fon = back.image
        back.image = pygame.transform.scale(fon, (width, height))
        Level = Levels.level(template.Therd_collevel, template.Therd_collevel)
        Level.create_level(hero)
        evid = evidence.clues(template.Therd_collevel)
        evid.create_clues()

Nomber = 1
SwLevel(Nomber)

# Установка координат заднего фона
back.rect.x = -((W/2)/ back.sdvig)/back.sdvig
print('back sdvig: ' + str(back.sdvig))
print('back x: ' + str(back.rect.x))

# Музыка
#Music_and_Sounds.Music()
# Камера
class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_func(camera, target_rect):
    l = -target_rect.x + width/2
    t = -target_rect.y + height/2

    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - width), l)
    t = max(-(camera.height - height), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)

# Класс меню
class Start_Menu:
    def __init__(self, punkts):
        self.punkts = punkts

    def render(self, poverhost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self, window, st, b, timer, s):
        global width, height, W, H, fullscreen, newimage, Mus
        done = True
        font_menu = pygame.font.SysFont('Calibri', 30, 1)
        punkt = 0
        counter = 0
        newimage = pygame.transform.scale(b, (window.get_size()))
        while done:
            screen.blit(newimage, (0, 0))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    if punkt != i[5]:
                        punkt = i[5]
                        Music_and_Sounds.Sound_Switch.play(0)
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                pygame.key.set_repeat(1, 1)
                if e.type == pygame.QUIT:
                    W, H, fullscreen, Mus = settingsFile.opensett(False, width, height, fullscreen, Mus)
                    window.blit(screen, (0, 0))
                    pygame.display.flip()
                    timer.tick(120)
                    pygame.quit()
                if e.type == pygame.VIDEORESIZE:
                    width, height = e.size
                    # перерисовка окна под новый размер
                    window = create_window(width, height, fullscreen)
                    print(window.get_size())  # Вывод размера окна
                    newimage = pygame.transform.scale(b, (width, height))
                    setting.punkts = pun(height)[1]
                    back.image = pygame.transform.scale(fon, (width, height))

                # блок отслеживание выбора пунктов с помощью клавишь
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        if not st:
                            done = False
                            newimage = pygame.transform.scale(b, (width, height))
                        # else:
                        #     exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                            Music_and_Sounds.Sound_Switch.play(1)
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                            Music_and_Sounds.Sound_Switch.play(1)
                    if e.key == pygame.K_SPACE:
                        Music_and_Sounds.Sound_Click.play(1)
                        if punkt == 0:
                            done = False
                        if punkt == 1:
                            setting.menu(window, False, BackMenu, timer, True)
                        if punkt == 2:
                            W, H, fullscreen, Mus = settingsFile.opensett(False, width, height, fullscreen, Mus)
                            fullscreen = False
                            window = create_window(W, H, fullscreen)
                            window.blit(screen, (0, 0))
                            pygame.display.flip()
                            timer.tick(120)
                            pygame.quit()
                            exit(0)
                        if punkt == 3:
                            if not fullscreen:
                                fullscreen = True
                                window = create_window(W, H, fullscreen)
                                width, height = window.get_size()
                            else:
                                fullscreen = False
                                window = create_window(W, H, fullscreen)
                                width, height = window.get_size()
                            newimage = pygame.transform.scale(b, (width, height))
                            back.image = pygame.transform.scale(fon, (width, height))
                        if punkt == 4:
                            done = False
                # Отслежывание мышки в меню
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    Music_and_Sounds.Sound_Click.play(1)
                    if punkt == 0:
                        done = False
                    if punkt == 1:
                        setting.menu(window, False, BackMenu, timer, True)
                    if punkt == 2:
                        W, H, fullscreen, Mus = settingsFile.opensett(False, width, height, fullscreen, Mus)
                        fullscreen = False
                        window = create_window(W, H, fullscreen)
                        window.blit(screen, (0, 0))
                        pygame.display.flip()
                        timer.tick(120)
                        pygame.quit()
                        exit(0)
                    if punkt == 3:
                        if not fullscreen:
                            fullscreen = True
                            window = create_window(W, H, fullscreen)
                            width, height = window.get_size()
                        else:
                            fullscreen = False
                            window = create_window(W, H, fullscreen)
                            width, height = window.get_size()
                        newimage = pygame.transform.scale(b, (width, height))
                        back.image = pygame.transform.scale(fon, (width, height))
                        #self.punkts[3][1] = height - 20
                    #
                    # if punkt == 4:
                    #     if counter <= len(pygame.display.list_modes(0, pygame.FULLSCREEN)) - 7:
                    #         counter += 1
                    #         print(counter)
                    #     else:
                    #         counter = 0
                    #     W, H = pygame.display.list_modes(0, pygame.FULLSCREEN)[counter]
                    #
                    if punkt == 5:
                        done = False
                        W, H = window.get_size()
                    if punkt == 6:
                        window = create_window(W, H, fullscreen)
                        width, height = window.get_size()
                        self.punkts = pun(height)[1]
                        newimage = pygame.transform.scale(b, (width, height))
                        back.image = pygame.transform.scale(fon, (width, height))
                    if punkt == 7:
                        if counter <= len(pygame.display.list_modes(0, pygame.FULLSCREEN)) - 7:
                            counter += 1
                            print(counter)
                        W, H = pygame.display.list_modes(0, pygame.FULLSCREEN)[counter]
                    if punkt == 8:
                        if counter > 0:
                            counter -= 1
                            print(counter)
                        W, H = pygame.display.list_modes(0, pygame.FULLSCREEN)[counter]
                        #self.punkts[3][1] = H - 20
                    if punkt == 9:
                        pygame.mixer.music.stop()
                        if not Mus:
                            Mus = True
                        else:
                            Mus = False

            if s:
                screen.blit(font_menu.render(u'(' + str(W) + u' x ' + str(H) + u')', 1, (255, 255, 0)), (20 + 180, 20 + 50))
                screen.blit(font_menu.render(str(fullscreen), 1, (255, 255, 0)), (20 + 145, 20))
                screen.blit(font_menu.render(str(Mus), 1, (255, 255, 0)), (20 + 145, 20 + 100))
            window.blit(screen, (0, 0))
            timer.tick(120)
            pygame.display.flip()
        return fullscreen


def com(time, swcom, level_score):
    if Nomber == 1:
        comment = story.comment(swcom)
        if level_score == 1:
            swcom += 1
            time = pygame.time.get_ticks()
        if level_score == 2:
            swcom += 1
            time = pygame.time.get_ticks()
        if level_score == 5:
            swcom += 1
            time = pygame.time.get_ticks()
        if level_score == 9:
            swcom += 1
            time = pygame.time.get_ticks()
        if level_score == 10:
            time = pygame.time.get_ticks()

    if Nomber == 2:
        comment = story.commet_second(swcom)
        if level_score == 1:
            swcom += 1
            time = pygame.time.get_ticks()
        if level_score == 2:
            swcom += 1
            time = pygame.time.get_ticks()
        if level_score == 4:
            swcom += 1
            time = pygame.time.get_ticks()
        if level_score == 5:
            swcom += 1
            time = pygame.time.get_ticks()

    hero.comment = False
    return time, swcom, comment

# def next_level(Nomber):



camera = Camera(camera_func, Level.level_width, Level.level_height)
# Блок вывода инфы
def info():
    screen.blit(myfont.render(u'X: ' + str(hero.rect.x), 1, (0, 0, 0)), (5, height - 60))
    screen.blit(myfont.render(u'Y: ' + str(hero.rect.y), 1, (0, 0, 0)), (5, height - 60 - sh - 1))
    screen.blit(myfont.render(u'FlyCounter: ' + str(hero.FlyCounter), 1, (0, 0, 0)), (5, height - 60 - 2*sh - 2))
    screen.blit(myfont.render(u'onGround: ' + str(hero.onGround), 1, (0, 0, 0)), (5, height - 60 - 3*sh - 3))
    screen.blit(myfont.render(u'fullscreen: ' + str(fullscreen), 1, (0, 0, 0)), (5, height - 60 - 4*sh - 4))
    screen.blit(myfont.render(u'Hero Down: ' + str(hero.Down), 1, (0, 0, 0)), (5, height - 60 - 5*sh - 5))
    screen.blit(myfont.render(u'FPS: ' + str(int(timer.get_fps())), 1, (0, 0, 0)), (5, height - 60 - 6*sh - 6))
    screen.blit(myfont.render(u'Level: ' + str(hero.rect.y) + ' ' + str(Level.level_height - 200) + ' ' + str(hero.rect.y < Level.level_height - 200), 1, (0, 0, 0)), (5, height - 60 - 7*sh - 7))
    screen.blit(myfont.render(u'yVel: ' + str(hero.yvel), 1, (0, 0, 0)), (5, height - 60 - 8*sh - 8))
    screen.blit(myfont.render(u'Size: ' + str(window.get_size()), 1, (0, 0, 0)), (5, height - 60 - 9*sh - 9))
    screen.blit(myfont.render(u'Level №: ' + str(Nomber), 1, (0, 0, 0)), (5, height - 60 - 10*sh - 10))
    screen.blit(myfont.render(u'Driver: ' + str(pygame.display.get_driver()), 1, (0, 0, 0)), (5, height - 60 - 11*sh - 11))
    screen.blit(myfont.render(u'Score: ' + str(hero.score), 1, (0, 0, 0)), (5, height - 60 - 12*sh - 12))
    screen.blit(myfont.render(u'Comment: ' + str(hero.comment) + ' ' + str(swcom), 1, (0, 0, 0)), (5, height - 60 - 13*sh - 13))
    screen.blit(myfont.render(u'Time: ' + str(time) + ' ' + str(pygame.time.get_ticks()) + ' ' + str(time + 3000 > pygame.time.get_ticks()), 1, (0, 0, 0)), (5, height - 60 - 14*sh - 14))
    screen.blit(myfont.render(u'Mp: ' + str(pygame.mouse.get_pos()), 1, (0, 0, 0)), (5, height - 60 - 15*sh - 15))
    screen.blit(myfont.render(u'Level Score: ' + str(level_score), 1, (0, 0, 0)), (5, height - 60 - 16*sh - 16))
    #print(pygame.display.Info())

logo = pygame.image.load('sprite/nobackground.png').convert_alpha()
logo = pygame.transform.scale(logo, (640, 360))
# Титры в конце
def end_ti(screen, px_lev):

    indent = 60

    screen.blit(end_font.render(u'Главный разработчик:', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Главный разработчик:')[0] / 2, px_lev))
    screen.blit(end_font.render(u'Сергей Хомутов', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Сергей Хомутов')[0] / 2, end_font.size(u'Главный разработчик:')[1] + px_lev))


    px_lev += indent + end_font.size(u'Главный разработчик:')[1]

    screen.blit(end_font.render(u'Автор идеи:', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Автор идеи:')[0] / 2, px_lev))
    screen.blit(end_font.render(u'Сергей Хомутов', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Сергей Хомутов')[0] / 2,
                 end_font.size(u'Автор идеи:')[1] + px_lev))


    px_lev += indent + end_font.size(u'Автор идеи:')[1]

    screen.blit(end_font.render(u'Автор сценария:', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Автор сценария:')[0] / 2, px_lev))
    screen.blit(end_font.render(u'Сергей Хомутов', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Сергей Хомутов')[0] / 2,
                 end_font.size(u'Автор сценария:')[1] + px_lev))


    px_lev += indent + end_font.size(u'Автор сценария:')[1]

    screen.blit(end_font.render(u'Арт дизайнер:', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Автор сценария:')[0] / 2, px_lev))
    screen.blit(end_font.render(u'Сергей Хомутов', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Сергей Хомутов')[0] / 2,
                 end_font.size(u'Арт дизайнер:')[1] + px_lev))
    screen.blit(end_font.render(u'Олег Плаксин', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Олег Плаксин')[0] / 2,
                 end_font.size(u'Арт дизайнер:')[1] + end_font.size(u'Сергей Хомутов')[1] + px_lev))


    px_lev += indent + end_font.size(u'Арт дизайнер:')[1] + end_font.size(u'Сергей Хомутов')[1]

    screen.blit(end_font.render(u'Alpha-тестер:', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Alpha-тестер:')[0] / 2, px_lev))
    screen.blit(end_font.render(u'Сергей Хомутов', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Сергей Хомутов')[0] / 2,
                 end_font.size(u'Alpha-тестер:')[1] + px_lev))
    screen.blit(end_font.render(u'Олег Плаксин', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Олег Плаксин')[0] / 2,
                 end_font.size(u'Alpha-тестер:')[1] + end_font.size(u'Сергей Хомутов')[1] + px_lev))
    screen.blit(end_font.render(u'Даниил Трушин', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Даниил Трушин')[0] / 2,
                 end_font.size(u'Alpha-тестер:')[1] + end_font.size(u'Сергей Хомутов')[1] + end_font.size(u'Олег Плаксин')[1] + px_lev))

    px_lev += indent + end_font.size(u'Alpha-тестер:')[1] + end_font.size(u'Сергей Хомутов')[1] + end_font.size(u'Олег Плаксин')[1]

    screen.blit(end_font.render(u'Музыка:', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Музыка:')[0] / 2, px_lev))
    screen.blit(end_font.render(u'Energy Tone', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Energy Tone')[0] / 2,
                 end_font.size(u'Музыка:')[1] + px_lev))
    screen.blit(end_font.render(u'Melodic Pony', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Melodic Pony')[0] / 2,
                 end_font.size(u'Музыка:')[1] + end_font.size(u'Energy Tone')[1] + px_lev))


    px_lev += indent + end_font.size(u'Музыка:')[1] + end_font.size(u'Energy Tone')[1]

    screen.blit(end_font.render(u'Отдельная благодарность:', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Отдельная благодарность:')[0] / 2, px_lev))
    screen.blit(end_font.render(u'Олег Плаксин', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Олег Плаксин')[0] / 2,
                 end_font.size(u'Отдельная благодарность:')[1] + px_lev))
    screen.blit(end_font.render(u'Даниил Трушин', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Даниил Трушин')[0] / 2,
                 end_font.size(u'Отдельная благодарность:')[1] + end_font.size(u'Даниил Трушин')[1] + px_lev))


    px_lev += indent + end_font.size(u'Отдельная благодарность:')[1] + end_font.size(u'Даниил Трушин')[1]

    screen.blit(end_font.render(u'Смотрел за психической стабильностью главного разработчика: ', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Смотрел за психической стабильностью главного разработчика: ')[0] / 2, px_lev))
    screen.blit(end_font.render(u'Даниил Трушин', 1, (255, 255, 255)),
                (W / 2 - end_font.size(u'Даниил Трушин')[0] / 2,
                 end_font.size(u'Смотрел за психической стабильностью главного разработчика: ')[1] + px_lev))

    px_lev += end_font.size(u'Смотрел за психической стабильностью главного разработчика: ')[1]
    return screen, px_lev


''' Меню '''
BackMenu = pygame.image.load('background/menuback.png')
def pun(height):
    punkts = [(20, 20, u'Play', (255, 255, 0), (0, 255, 0), 0),
              (20, 20 + 50, u'Settings', (255, 255, 0), (0, 255, 0), 1),
              (20, 20 + 100, u'Exit', (255, 255, 0), (0, 255, 0), 2)]

    settings = [(20, 20, u'Fullscreen:', (255, 255, 0), (0, 255, 0), 3),
                (20, 20 + 50, u'Resolution:', (255, 255, 0), (255, 255, 0), 4),
                (20, 20 + 150, u'Back', (255, 255, 0), (0, 255, 0), 5),
                (20, height - 50, u'Accepted', (255, 255, 0), (0, 255, 0), 6),
                (20 + 150, 20 + 50, u'<', (255, 255, 0), (0, 255, 0), 7),
                (20 + 340, 20 + 50, u'>', (255, 255, 0), (0, 255, 0), 8),
                (20, 20 + 100, u'Music:', (255, 255, 0), (0, 255, 0), 9)]
    return punkts, settings
punkts, settings = pun(height)
timer = pygame.time.Clock()
game = Start_Menu(punkts)
setting = Start_Menu(settings)
game.menu(window, True, BackMenu, timer, False)

# Создание окна
window = create_window(W, H, fullscreen)
pygame.display.set_caption('It\'s PONY, CARL')
# Иконкаа окна
a = pygame.image.load('icon/Twilight.ico')
a.set_colorkey((0, 0, 0))
pygame.display.set_icon(a)

celi = person.personage(192, 140, 939, 305, animation.CELESTIA_STAND)
gard = person.personage(192, 140, 670, 567, animation.GUARD_LEFT)
alt_gard = person.personage(192, 140, 413, 521, animation.ALT_GUARD_LEFT)


intro =  person.spurkle(600, 600, -200, 0, animation.INTRO)
intro2 =  person.spurkle(600, 600, W - 400, 0, animation.INTRO)

inf = False
check = False
exet = False
done = True
swst = 0
#Интро
while done:
    pygame.mouse.set_visible(0)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.KEYDOWN:
            pygame.key.set_repeat(1, 1)
            if e.key == pygame.K_ESCAPE:
                done = False
            if e.key == pygame.K_RIGHT:
                swst += 1
    if swst > 6:
        break



    st = story.introductory_story(swst)
    screen.fill((0, 0, 0))

    intro.anim()
    intro2.anim()
    screen.blit(intro.image, (intro.rect.x, intro.rect.y))
    screen.blit(intro2.image, (intro2.rect.x, intro2.rect.y))

    screen.blit(swichfont.render(st, 1, (255, 255, 255), ),
                (width / 2 - swichfont.size(st)[0] / 2, height / 2))

    screen.blit(act_font.render(u'Esc - Пропустить      Right - Следующий', 1, (255, 255, 255)), (
    width / 2 - act_font.size(u'Esc - Пропустить      Right - Следующий')[0] / 2, height - 30))
    window.blit(screen, (0, 0))
    pygame.display.flip()


# Основной цикл
swcom = 0
time = 0
time_end = 0
level_score = 0
p = 0
i = 0
px_lev = width - 200
done = True
while done:
    # Блок управления событиями
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.KEYDOWN:
            pygame.key.set_repeat(1, 1)
            if e.key == pygame.K_ESCAPE:
                pygame.mouse.set_visible(1)
                game.menu(window, False, BackMenu, timer, False)
            '''
            if e.key == pygame.K_k:
                if not fullscreen:
                    fullscreen = True
                    window = create_window(W, H, fullscreen)
                else:
                    fullscreen = False
                    window = create_window(W, H, fullscreen)
            '''
            if e.key == pygame.K_i:
                if not inf:
                    inf = True
                else:
                    inf = False
            if e.key == pygame.K_f:
                check = True
            if e.key == pygame.K_b:
                level_score += 10
        if e.type == pygame.KEYUP:
            pygame.key.set_repeat(1, 1)
            if e.key == pygame.K_f:
                check = False

        if e.type == pygame.VIDEORESIZE:
            width, height = e.size
            # перерисовка окна под новый размер
            game = Start_Menu(punkts)
            window = create_window(width, height, fullscreen)
            setting.punkts = pun(height)[1]
            back.image = pygame.transform.scale(fon, (width, height))
            print(window.get_size())  # Вывод размера окна

    pygame.mouse.set_visible(0)
    if Nomber == 1:
        screen.blit(back.image, (back.rect.x, back.rect.y))
        # if hero.rect.x > (width / 2) and hero.rect.x < Level.level_width - width / 2:
        #     back.rect.x = -(hero.rect.x / back.sdvig)/ back.sdvig
        ''' Задний слой фона '''
        for bc in ArBack:
            screen.blit(bc.image, (bc.rect.x, bc.rect.y))
            if hero.rect.x > (width / 2) and hero.rect.x < Level.level_width - (width / 2):
                bc.rect.x = -(int(hero.rect.x /8) - bc.x) + (width / 2) / 8

            if hero.rect.y < Level.level_height - (height / 2):
                bc.rect.y = -((hero.rect.y /3) - bc.y) + 4 * ((height / 2) / 3)
        ''' Средний слой фона '''
        for mi in Middle:
            screen.blit(mi.image, (mi.rect.x, mi.rect.y))
            if hero.rect.x > width / 2 and hero.rect.x < Level.level_width - (width / 2):
                mi.rect.x = -(int(hero.rect.x /4) - mi.x) + (width / 2) / 4

            if hero.rect.y < Level.level_height - (height / 2):
                mi.rect.y = -((hero.rect.y /2) - mi.y) + 4 * ((height / 2) / 2)
        ''' Передний слой фона '''
        for fr in Front:
            screen.blit(fr.image, (fr.rect.x, fr.rect.y))
            if hero.rect.x > width / 2 and hero.rect.x < Level.level_width - (width / 2):
                fr.rect.x = -(int(hero.rect.x /2) - fr.x) + (width / 2) / 2

            if hero.rect.y < Level.level_height - (height / 2):
                fr.rect.y = -((hero.rect.y /1.5) - fr.y) + 4 * ((height / 2) / 1.5)
            # Отображение героя
        hero.control(Level.level_width, Level.level_height)
        hero.gravity(Level.Collision)
        hero.collect_clue(hero.xvel, 0, evid.Collision, evid.sprite_group, check)
        '''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Второй уровень =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''
    elif Nomber == 2:
        screen.blit(back.image,(back.rect.x, back.rect.y))
        ''' Средний слой фона '''
        for mi in Middle:
            screen.blit(mi.image, (mi.rect.x, mi.rect.y))
            if hero.rect.x > width / 2 and hero.rect.x < Level.level_width - width / 2:
                mi.rect.x = -((hero.rect.x /4) - mi.x) + (width / 2) / 4

            if hero.rect.y < Level.level_height - (height / 2) - 300:
                mi.rect.y = -((hero.rect.y /2) - mi.y) + 4 * ((height / 2) / 2) - 150
            # elif hero.rect.y < Level.level_height - (height / 2) - 100:
            #     mi.rect.y = -((hero.rect.y / 10) - mi.y) + 4 * ((height / 2) / 10) - 10

        ''' Передний слой фона '''
        for fr in Front:
            screen.blit(fr.image, (fr.rect.x, fr.rect.y))
            if hero.rect.x > width / 2 and hero.rect.x < Level.level_width - width / 2:
                fr.rect.x = -((hero.rect.x /2) - fr.x) + (width / 2) / 2

            if hero.rect.y < Level.level_height - (height / 2):
                fr.rect.y = -((hero.rect.y /1.5) - fr.y) + 4 * ((height / 2) / 1.5)
        # Отображение героя
        hero.control(Level.level_width, Level.level_height)
        hero.gravity(Level.Collision)
        hero.collect_clue(hero.xvel, 0, evid.Collision, evid.sprite_group, check)
        #print('back x: ' + str(back.rect.x))
        '''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Третий уровень =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''
    elif Nomber == 3:
        pygame.mouse.set_visible(0)
        screen.blit(back.image, (back.rect.x, back.rect.y))

        hero.AnimPony()
        celi.anim()
        gard.anim()
        alt_gard.anim()

        screen.blit(celi.image, (celi.rect.x, celi.rect.y))
        screen.blit(gard.image, (gard.rect.x, gard.rect.y))
        screen.blit(alt_gard.image, (alt_gard.rect.x, alt_gard.rect.y))
        for e in Level.sprite_group:
            screen.blit(e.image, camera.apply(e))


        if time_end + 3000 > pygame.time.get_ticks():
            comment = story.end_dialog(p, i)
            if p == 0:
                pygame.draw.rect(screen, (255, 255, 255, 0),
                                 [camera.apply(hero)[0] - 5, camera.apply(hero)[1] - 25, scorefont.size(comment)[0] + 5,
                                  scorefont.size(comment)[1] + 5])
                screen.blit(scorefont.render(comment, 1, (0, 0, 0)),
                            (camera.apply(hero)[0], camera.apply(hero)[1] - 20))
            if p == 1:
                pygame.draw.rect(screen, (255, 255, 255, 0),
                                 [904, 280, scorefont.size(comment)[0] + 5,
                                  scorefont.size(comment)[1] + 5])
                screen.blit(scorefont.render(comment, 1, (0, 0, 0)), (904, 280))
        elif p == 0:  p = 1
        elif i < 7:
            i += 1
            time_end = pygame.time.get_ticks()
        else:
            screen.fill(0)
            px_lev -= 1
            if px_lev > -1000:
                screen, logo_y = end_ti(screen, px_lev)

            if logo_y + 180 > H / 2:
                screen.blit(logo, (W / 2 - 640 / 2, logo_y))
            else:
                screen.blit(logo, (W / 2 - 640 / 2, H / 2 - 180))

            window.blit(screen, (0, 0))






    camera.update(hero)

    if Nomber != 3:
        for e in Level.sprite_group:
            screen.blit(e.image, camera.apply(e))
        for e in evid.sprite_group:
            e.anim()
            screen.blit(e.image, camera.apply(e))

        # Шкала выносливости
        pygame.draw.rect(screen, (2, 165, 1), [20, 10, (FORSE - hero.counter) / 4.5, 10])
        pygame.draw.rect(screen, (0, 0, 0), [20, 10, FORSE / 4.5, 10], 2)
        screen.blit(scorefont.render(u'Информации найдено: ' + str(hero.score), 1, (255, 215, 0)), (20, 30))

    if hero.message:
        screen.blit(act_font.render(u'F - собрать информацию', 1, (255, 255, 255)),
                        (width / 2 - act_font.size(u'F - собрать информацию')[0] / 2, height - 20))
        check = False
        hero.message = False


    # Levels.sprite_group.draw(screen)
    # Инфа
    if inf:
        info()

    # Музыка
    if Mus:
        Music_and_Sounds.Music()
    #print(camera.apply(hero)[0])

    if hero.comment:
        level_score += 1
        time, swcom, comment = com(time, swcom, level_score)

    if time + 3000 > pygame.time.get_ticks() and not Level.level_width <= hero.rect.x + 750:
        pygame.draw.rect(screen, (255, 255, 255, 0), [camera.apply(hero)[0] - 5, camera.apply(hero)[1] - 25, scorefont.size(comment)[0] + 5, scorefont.size(comment)[1] + 5])
        screen.blit(scorefont.render(comment, 1, (0, 0, 0)),
                    (camera.apply(hero)[0], camera.apply(hero)[1] - 20))

    if exet:
        pygame.draw.rect(screen, (255, 255, 255, 0), [camera.apply(hero)[0] - 255, camera.apply(hero)[1] - 25,
                                                      scorefont.size(u'Еще не все тут собрала, надо поискать...')[0] + 5,
                                                      scorefont.size(u'Еще не все тут собрала, надо поискать...')[
                                                          1] + 5])
        screen.blit(scorefont.render(u'Еще не все тут собрала, надо поискать...', 1, (0, 0, 0)),
                    (camera.apply(hero)[0] - 250, camera.apply(hero)[1] - 20))
        if time + 3000 < pygame.time.get_ticks():
            exet = False
    # Переход на след уровень
    if Level.level_width <= hero.rect.x + 1:
        if Nomber < 3:
            if Nomber == 1 and level_score < 10:
                time = pygame.time.get_ticks()
                if time + 3000 > pygame.time.get_ticks():
                    exet = True
            elif Nomber == 2 and level_score < 5:
                time = pygame.time.get_ticks()
                if time + 3000 > pygame.time.get_ticks():
                    exet = True
            else:
                screen.fill((0, 0, 0))
                screen.blit(swichfont.render(u'Некоторое время спустя', 1, (255, 255, 255)),
                            (width / 2 - swichfont.size(u'Некоторое время спустя')[0] / 2, height / 2))
                window.blit(screen, (0, 0))
                pygame.display.flip()
                Nomber += 1
                SwLevel(Nomber)
                hero.rect.x = -10
                hero.rect.y -= 10
                screen.fill((0, 0, 0))
                if Nomber == 2:
                    screen.blit(swichfont.render(u'Город Понивиль', 1, (255, 255, 255)),
                                (width / 2 - swichfont.size(u'Город Понивиль')[0] / 2, height / 2))
                    window.blit(screen, (0, 0))
                    pygame.display.flip()
                    level_score = 0
                    swcom = 0
                sleep(1)
                if Nomber == 3:
                    screen.blit(swichfont.render(u'Тронный зал', 1, (255, 255, 255)),
                                (width / 2 - swichfont.size(u'Тронный зал')[0] / 2, height / 2))
                    window.blit(screen, (0, 0))
                    pygame.display.flip()
                    level_score = 0
                    swcom = 0
                    hero.rect.x = 448
                    hero.rect.y = 1712
                    hero.FlyCounter = 0
                    hero.onGround = True
                    sleep(1)
                    time_end = pygame.time.get_ticks()
        else:
            hero.rect.x = Level.level_width - 1

    # Отображаем рабочую поверхность в окне


    window.blit(screen, (0, 0))
    # Обновляем окно
    pygame.display.flip()


    timer.tick(80)

# Exit
#pygame.time.wait(1000)
W, H, fullscreen, Mus = settingsFile.opensett(True, width, height, fullscreen, Mus)
pygame.quit()
