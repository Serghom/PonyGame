from pygame import mixer
from random import randrange

music = 'music/ogg/'
sound = 'sounds/'

mixer.pre_init(22050, -16, 1, 300)
mixer.init()

Music_Flutter_heart = (music+'EnergyBrony - Flutter Heart.ogg')
Music_Love_Conquers_All = (music+'Melodic Pony - Love Conquers All.ogg')
Music_Lunas_Determination = (music+'Melodic Pony - Princess Twilight Orchestral Suite.ogg')
Music_Princess_Twilight = (music+'Melodic Pony - Lunas Determination.ogg')
Music_The_Return_of_Harmony = (music+'Melodic Pony - The Return of Harmony.ogg')

Sound_Click = mixer.Sound(sound+'click.ogg')
Sound_Switch = mixer.Sound(sound+'switch.ogg')



def Music():
    if not mixer.music.get_busy():
        rand = randrange(0, 5)

        if rand == 0:
            mixer.music.load(Music_Flutter_heart)
            print('Mus 0')
        elif rand == 1:
            mixer.music.load(Music_Love_Conquers_All)
            print('Mus 1')
        elif rand == 2:
            mixer.music.load(Music_Lunas_Determination)
            print('Mus 2')
        elif rand == 3:
            mixer.music.load(Music_Princess_Twilight)
            print('Mus 3')
        else:
            mixer.music.load(Music_The_Return_of_Harmony)
            print('Mus 4')

        mixer.music.play()