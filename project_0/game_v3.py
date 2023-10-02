import numpy as np

def random_predict(number:int=1) -> int:
    """Угадываем число методом деления пополам

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0        # Счетчик попыток
    low = 1         # Нижняя граница диапазона для угадывания
    high = 100      # Верхняя граница диапазона для угадывания
    
    while True:     # Начало бесконечного цикла
        count += 1  # Увеличиваем счетчик попыток на 1
        predict_number = (low + high) // 2  # Получаем среднее значение между верхней и нижней границей
        
        if number == predict_number:  # Если угадали число
            return count              # Возвращаем количество попыток и завершаем функцию
        elif number > predict_number: # Если загаданное число больше предполагаемого
            low = predict_number + 1  # Смещаем нижнюю границу диапазона вверх
        else:                         # Если загаданное число меньше предполагаемого
            high = predict_number - 1 # Смещаем верхнюю границу диапазона вниз
    return(count)



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == "__main__":
    score_game(random_predict)