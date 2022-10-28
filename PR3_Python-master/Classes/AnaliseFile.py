from typing import List

class AnaliseFile:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path              # присваиваем объекту класса путь файла, который будем анализировать
        self.char_count :int = 0                # число символов в файле
        self.sogl_count : int = 0               # количество согласных
        self.glas_count : int = 0               # количество гласных
        self.word_repeat : List[int] = []       # массив с повторениями слов с разной длиной
        self.count_words :int = 0
        #в результате будет выглядеть как двумерный массив:
        #[[1, 13]
        #[4, 15]
        #[9, 12]
        #[3, 54]]
        # где 1 столбец - длина слова, 2 столбец - количество повторений слова с такой длиной.
       
    # функция анализа 
    def analise(self):
        file = open(self.file_path, 'r') #открываем файл, начинаем его анализировать
        try:
            while True:
                word = file.readline()          # читаем строку, тобишь слово, и присваиваем переменной для дальнейших манипуляций
                if word == '':                  # файл вернул пустую строку? ну иди поплакай хуй знает, не забудь соединение закрыть
                    file.close()
                    return None
                word = word.replace('\n', '')   # заменяем перенос строки '\n' на нихуя
                
                self.char_count += len(word)    # длина слова, будет количеством символов в слова, прибавляем к общему количеству
                self.__summ_sogl_count(word)    # суммируем согласные слова
                self.__summ_glas_count(word)    # суммируем гласные слова
                self.__summ_word_repeat(word)   # суммируем повторения слов с разной длиной
        finally:
            file.close()                # и ещё раз закрываем файл, НАВСЯКИЙ СЛУЧАЙ ЧТОБЫ ПОСЛЕ ОШИБОК НЕ ВИСЕЛИ ЭТИ ЕБУЧИЕ ПРОЦЕССЫ БЛЯЯЯЯТЬ
            self.word_repeat.sort()     # сортируем список повторов слов и их длины. Благо методы питона прекрасно всё это делают за нас)
            [self.increment_count_words(wordcount[1]) for wordcount in self.word_repeat]
            
    def increment_count_words(self, count: int):
        self.count_words += count
        
    def printResult(self):
        print('*'*70+'\n'
              f' Аналитика для файла {self.file_path}\n'+
              '*'*70+'\n'
              f' 1. Всего символов --> {self.char_count}\n'
              f' 2. Максимальная длина слова --> {self.word_repeat[len(self.word_repeat)-1][0]}\n'
              f' 3. Минимальная длина слова --> {self.word_repeat[0][0]}\n'
              f' 4. Средняя длина слова --> {round(self.char_count/self.count_words)}\n'
              f' 5. Количество гласных --> {self.glas_count}\n'
              f' 6. Количество согласных --> {self.sogl_count}\n'
              f' 7. Количество повторений с одинаковой длиной:\n')
        [print(f'\t * {word[0]} сим. >> {word[1]} повтор.') for word in self.word_repeat]
    
    # функция суммирования согласных
    def __summ_sogl_count(self, word):
        for char in word:                                 # перебираем буквы в слове
            if char.upper() in 'BCDFGHJKLMNPQRSTVWXZ':    # эта буква есть в строке согласных????
                self.sogl_count +=1                       # если есть - круто, сразу добавляем к общему кол-ву согласных    
    
    # функция суммирования гласных, логика та же, что и выше
    def __summ_glas_count(self, word):
        for c in word:
            if c.upper() in 'AEIOUY':
                self.glas_count +=1
    
    # функция суммирования повторений слов, если слова с такой длиной нет - добавляем
    def __summ_word_repeat(self, word):
        word_length = len(word)                             # получаем длину слова 
        for type_word in self.word_repeat:                  # перебираем типы слов (тобишь длину)
            if word_length == type_word[0]:                 # если длина слова совпадает (на позиции 0)
                type_word[1]+=1                             # то инкримируем количество слов с такой длиной (на позиции 1)
                return None                                 # и выходим из метода
        self.word_repeat.append([word_length, 1])           # но если такого слова не нашлось, то добавляем)