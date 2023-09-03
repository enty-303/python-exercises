import time

UserInput = 0
PlayersCount = 0
while UserInput != 'закрыть сервер':
    print('Игроков на сервере в майнкрафте: ' + str(PlayersCount))
    print('Разрешить игроку зайти на Ваш сервер в майнкрафте? ( да/нет/закрыть сервер)')
    UserInput = input()
    if UserInput == 'да':
        for counter in range(1, 4):
            print('. ', end='')
            time.sleep(1)
        print('игрок зашёл на сервер')
        PlayersCount = PlayersCount + 1
    elif UserInput == 'нет':
        for counter in range(1, 4):
            print('. ', end='')
            time.sleep(1)
        print('Вы запретили игроку зайти на сервер ')
    elif UserInput == 'закрыть сервер':
        print('Закрытие сервера')
    else:
        print('Некорректный ввод.')
for counter in range(1, 4):
    print('. ', end='')
    time.sleep(1)
print('Вы закрыли Ваш сервер')