import numpy as np


def game_core_v3(number):
    # Функция для поиска загаданного числа по диапазонам.
    # Итеративно делит диапозоны чисел на две части, ищет в каком из диапазонов находится число, вплоть до его нахождения 
    count = 0 
    min_number = 1
    max_number = 101
    predict = 0
    
    while predict != number:
        if number < int((max_number+min_number)/2):
            max_number = int((max_number+min_number)/2)
        elif number > int((max_number+min_number)/2):
            min_number = int((max_number+min_number)/2)
        else:
            predict = int((max_number+min_number)/2)  
        count +=1  
        
    return(count)
    
    
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)
