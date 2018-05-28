

def opensett(chek, W, H, Full, Mus):
    if chek:
        try:
            SFile = open('settings/sett.set', 'r')
        except IOError as e:
            #print(u'не удалось открыть файл')
            SFile = open('settings/sett.set', 'w')
            SFile.write(str(W) + '\n' + str(H) + '\n' + str(Full) + '\n' + str(Mus) + '\n')
            SFile.close()
            return W, H, Full, Mus
        else:
            with SFile:
                #print(u'делаем что-то с файлом')
                SFile = open('settings/sett.set', 'r')
                st = [line.strip() for line in SFile]
                #print('=-=-=-=-=')
                wi, he = int(st[0]), int(st[1])
                if len(st[2]) == 5:
                    Fu = False
                else:
                    Fu = True

                if len(st[3]) == 5:
                    Mu = False
                else:
                    Mu = True
                SFile.close()
                return wi, he, Fu, Mu
    else:
        print('Перезапись')
        SFile = open('settings/sett.set', 'w')
        SFile.write(str(W) + '\n' + str(H) + '\n' + str(Full) + '\n' + str(Mus) + '\n')
        SFile.close()
        return W, H, Full, Mus


