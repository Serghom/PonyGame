from all_texture import world
from pygame.sprite import Group
import person


class level(Group):
    def __init__(self, col, gr):
        Group.__init__(self)
        self.sprite_group = Group()
        self.Collision = []
        self.collevel = col
        self.grlevel = gr
        self.level_width = 0
        self.level_height = 0

    def create_level(self, hero):

        ''' Нижний (задний, за персонажем) слой прорисовки '''

        self.level_width = len(self.collevel[0]) * 150
        self.level_height = len(self.collevel) * 64


        x = y = 0
        for row in self.collevel:
            for col in row:
                if col == 't':
                    filename = 'sprite/Dert.png'
                    terra = world(filename, x, y, 150, 64)
                    self.sprite_group.add(terra)
                    self.Collision.append(terra)
                if col == 'i':
                    filename = 'sprite/Flying island.png'
                    fisland = world(filename, x, y, 50, 64)
                    self.sprite_group.add(fisland)
                    self.Collision.append(fisland)
                    #print(fisland.rect)
                if col == 'd':
                    filename = 'sprite/tree.png'
                    Tree = world(filename, x, y - 90, 0, 0)
                    self.sprite_group.add(Tree)
                if col == 'c':
                    filename = 'sprite/cloud.png'
                    cloud = world(filename, x, y, 0, 0)
                    self.sprite_group.add(cloud)
                    filename = 'sprite/Null.png'
                    col_cloud = world(filename, x, y + 100, 370, 100)
                    self.Collision.append(col_cloud)
                x += 150
            y += 64
            x = 0

        ''' Прорисовка персонажа '''
        self.sprite_group.add(hero)
        #self.sprite_group.add(person.celi(55, 55))
        ''' #Верхний (передний, перед персонажем) слой прорисовки  '''
        x = y = 0
        for row in self.grlevel:
            for col in row:
                if col == 'g':
                    filename = 'sprite/Grass.png'
                    grass = world(filename, x, y - 26, 0, 0)
                    self.sprite_group.add(grass)
                if col == 'c':
                    i = 1
                    while i < 7:
                        filename = 'sprite/ffcloud.png'
                        ffcloud = world(filename, x + (i * 50), y + 40, 0, 0)
                        self.sprite_group.add(ffcloud)
                        i += 1
                x += 150
            y += 64
            x = 0
