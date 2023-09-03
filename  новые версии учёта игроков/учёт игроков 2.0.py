UserInput = 0
PlayersCount = 0
while UserInput != 'закрыть сервер':
    print('Игроков на сервере в майнкрафте: ' + str(PlayersCount))
    print('Разрешить игроку зайти на Ваш сервер в майнкрафте? ( да/нет/закрыть сервер)')
    UserInput = input()
    if UserInput == 'да':
        print('игрок зашёл на сервер')
        PlayersCount = PlayersCount + 1
    elif UserInput == 'нет':
        print('Вы запретили игроку зайти на сервер ')
    elif UserInput == 'закрыть сервер':
        print('Вы закрыли Ваш сервер.')
    else:
        print('Некорректный ввод.')