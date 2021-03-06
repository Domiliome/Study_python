import threading, time


def worker(num_thread):
    print(f'Старт потока №{num_thread}')
    time.sleep(1)
    print(f'Завершение работы потока №{num_thread}')
    time.sleep(1)


for i in range(2):
    # создаем экземпляры 'Thread' с функцией
    # 'worker()', которая запустится в отдельных 
    # трех потоках. Позиционные аргументы для 
    # функции 'worker()' передаются в кортеже `args`
    thread = threading.Thread(target=worker, args=(i,))
    # запускаем экземпляр `thread`
    thread.start()
