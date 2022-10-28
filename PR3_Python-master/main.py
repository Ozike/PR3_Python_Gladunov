from concurrent.futures import process
import multiprocessing
from typing import List
from Classes.AnaliseFile import AnaliseFile
from Classes.CreateFile import create_file, create_dir
from multiprocessing import Process
import os

#общие переменные
dir_path :str = './files'           # папка в которой создаются и анализируются файлы
processes :List[Process] = []       # массив процессов, в который добавляются действующие процессы

# процесс создания
def create_process(name:str):
    create_file(dir_path + '/' + name, 10, 1E5, 1E6)
    
def analise_process(name:str):
    file_analise = AnaliseFile(dir_path + '/' + name)
    file_analise.analise()
    file_analise.printResult()

if __name__ == '__main__':
    create_dir(dir_path)                                            # создаём папку
    
    for i in range(multiprocessing.cpu_count()):                    # перебор массива от 0 до количества процесоров
        name = f'Process-{i+1}-{os.getpid()}.txt'                   # составляем имя файла: Process-[номер процесса]-[пид процесса].txt
        processing = Process(target=create_process, args=(name,))   # создаём процесс, передаём аргументы - имя файла
        processing.start()                                          # запускаем процесс
        processes.append(processing)                                # добавляем процесс в лист действующих процессов
    [proc.join() for proc in processes]                             # в цикле очищаем все действующие процессы
    processes.clear()                                               # очищаем лист действующих процессов
    
    count_processes : int = 0
    for file in os.listdir(dir_path):
        processing = Process(target=analise_process, args=(file,))
        processing.start()
        processes.append(processing)
        count_processes+=1
        if(count_processes >= multiprocessing.cpu_count()): break
    [proc.join() for proc in processes]                             # в цикле очищаем все действующие процессы
    processes.clear()
    