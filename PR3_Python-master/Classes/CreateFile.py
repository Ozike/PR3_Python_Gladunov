from RandomWordGenerator import RandomWord
import random
import os

def create_dir(dir_path):
    try:                                            # Перед заполнением папки файлами, попробуем сначала создать папку
        os.mkdir(dir_path)                          # Создаём папку используя библиотеку OS, и отлавливаем ошибку
        print(f'Директория {dir_path} создана')     # Ошибку не поймали? отлично, говорим что папка успешно создана
    except Exception as e:                          # Ловим ошибки
        print(f'Директория {dir_path} выбрана')     # Ошибку ппоймали и вывели, что мы вабрали эту директорию, ну тип она уже существует)

def create_file(file_path, word_max_size :int, word_min_count :int, word_max_count):
        print(f'Заполнение данными файла \"{file_path}\"...')
        rand_words = RandomWord(word_max_size, constant_word_size=False)    # инициализируем класс рандомных слов
        word_count = random.randint(word_min_count, word_max_count)         # генерируем количество слов, (рандом от мин кол-ва до макс кол-ва)
        
        # создаём файл и заполняем данными:
        with open(file_path, 'a') as text_writer:
            [text_writer.write(rand_words.generate() + '\n') for i in range(word_count)] # генерируем слово, добавляем в конце переход строки '\n', проходим дальше по циклу