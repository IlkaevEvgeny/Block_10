import threading
from datetime import datetime
import time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Измерение времени для функций
start_time_functions = datetime.now()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time_functions = datetime.now()
print(f"Работа функций {end_time_functions - start_time_functions}")

# Измерение времени для потоков
start_time_threads = datetime.now()

first_thread = threading.Thread(target=write_words, args=(10, "example5.txt"))
second_thread = threading.Thread(target=write_words, args=(30, "example6.txt"))
third_thread = threading.Thread(target=write_words, args=(200, "example7.txt"))
fourth_thread = threading.Thread(target=write_words, args=(100, "example8.txt"))

first_thread.start()
second_thread.start()
third_thread.start()
fourth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fourth_thread.join()

end_time_threads = datetime.now()
print(f"Работа потоков {end_time_threads - start_time_threads}")