from all_texture import world
from pygame.sprite import Group
import person
import animation

class clues(Group):
    def __init__(self, clue):
        Group.__init__(self)
        self.sprite_group = Group()
        self.Collision = []
        self.clue = clue

    def create_clues(self):
        x = y = 0
        for row in self.clue:
            for col in row:
                if col == 'y':
                    # filename = 'sprite\clue.png'
                    clue = person.spurkle(100, 100, x, y, animation.CLUE)
                    #cl = world(clue.image, x, y, 150, 150)
                    self.sprite_group.add(clue)
                    self.Collision.append(clue)
                x += 150
            y += 64
            x = 0
