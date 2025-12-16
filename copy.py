import os
import shutil

# Получаем список всех файлов в текущей директории
files = [f for f in os.listdir('.') if os.path.isfile(f)]
dist="C:\Новая папка"

# Фильтруем файлы по шаблону и условию
selected_files = []
for file in files:
    # Проверяем, что имя файла заканчивается на 14 цифр (дата 8 + время 6)
    test = file.split(".")[0]
    print(test[-6:])
    if len(test) >= 14 and test[-6:].isdigit():
        time_part = int(test[-6:])  # Последние 6 цифр как число (HHMMSS)
        if time_part > 140000:
            selected_files.append(file)

# Выводим результат
if selected_files:
    print("Выбранные файлы:")
    for f in selected_files:
        print(f)
else:
    print("Нет файлов, удовлетворяющих условию.")

for file in selected_files:
    shutil.copy2(file, os.path.join(dist, file))
    print(f"Файл {file} скопирован")