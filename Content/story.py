

def introductory_story(i):
    tie_story = [
        u'Тебя зовут Rainbow Dash.',
        u'Ты одна из носителей элементов гармонии - верность.',
        u'Ходят слухи, что империя грифонов,',
        u'The Great Empire of the Griffins,',
        u'собирается напасть на Эквестрию.',
        u'Ты, как секретны агент Ее величества Принцессы Селестии,',
        u'была отправлена собрать информацию.',
    ]
    return tie_story[i]

def comment(i):
    hero_comment = [
        u'Отлично, начало положено, осталось девять.',
        u'Эхх... И как только принцсса читает эти штуки?',
        u'Так, еще пять.',
        u'Еще одна...',
        u'Этого должно хватить, но я могу еще походить - поискать тут.'
    ]
    return hero_comment[i]

def commet_second(i):
    hero_second_comment = [
        u'В Понивиле их должно быть меньше...',
        u'Еще три штуки...',
        u'Еще одна..',
        u'Отлично, теперь можно и к Селестии.'
    ]
    return hero_second_comment[i]

def end_dialog(p, i):
    dash_speak = [u'Принцесса Селестия, вот вся информация, что мне удалось собрать']
    selectia_speak = [u'Молодец Рэйнбоу, передай их мне',
                      u'...',
                      u'Фух...',
                      u'Судя по той информации, что ты принесла...',
                      u'Никакой войны не будет...',
                      u'Это очень хорошая информация',
                      u'Еще раз спасибо тебе Рэйнбоу',
                      u'Ступай, я уже распорядилась...']
    if p == 0:
        return dash_speak[i]
    else:
        return selectia_speak[i]
