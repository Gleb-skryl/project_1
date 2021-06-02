# Включили библиотеки**

import numpy as np


def game_core(x, y):
    # Создаем переменную, в которую помещаем произвольное число из заданного диапозона
    predict = np.random.randint(x, y+1)
    # Покажем это число
    print('Компьютер загадал число -', predict)
    # Создаем счетчик попыток
    count = 1
    # Предполагаем, что загаданное число будет являться серидиной диапозона
    number = (x+y) // 2
    # Выполняем операции до тех пор, пока не отгадаем число
    while number != predict:
        print(f"{count} - я попытка - число {number} в диапозоне от {x} до {y}")
        # Если загаданное число больше предполагаемого, то началом диапозона задаем предполагаеиое число
        if predict > number:
            x = number + 1
        else:
            # Если загаданное число меньше предполагаемого, то концом диапозона задаем предполагаеиое число
            y = number - 1
    # Изменяем предполагаемое число на середину нового диапозона
        number = (x+y) // 2
    # Увеличиваем счетчик на 1
        count += 1
    print(f"{count} - я попытка - число {number} в диапозоне от {x} до {y}")
    print(f"Поздравляем! Вы угадали число с {count} попытки!")
    return count


# Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
count_ls = []
np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
random_array = np.random.randint(1, 101, size=1000)
for item in random_array:
    count_ls.append(game_core(1, 100))
score = int(np.mean(count_ls))
print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
