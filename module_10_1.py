import threading
import time
from time import sleep
raznica = 0
def write_words(word_count, file_name):

    start_time = time.time ()
    with open(file_name, 'w', encoding='utf-8') as file:
        global raznica
        for i in range(1, word_count+1):

            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)

    end_time = time.time()
    raznica += end_time - start_time


    print(f"Завершилась запись в файл {file_name}")



    if file_name == "example4.txt":
        print(f"Работа потоков: {round(raznica,3)}")
        raznica = 0

    if file_name == "example7.txt":
       print(f"Работа потоков: {round(raznica, 3)}")


write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
thread_1 = threading.Thread(target= write_words, args=(10,"example5.txt"))
thread_2 = threading.Thread(target= write_words, args=(30,"example6.txt"))
thread_3 = threading.Thread(target= write_words, args=(200,"example7.txt"))
thread_4 = threading.Thread(target= write_words, args=(100,"example8.txt"))
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()