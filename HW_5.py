#EASY

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
base_dir = "/Users/ladybug/TestPython/"
for i in range(9):
    if not os.path.exists(os.path.join(base_dir, "dir_"+str(i+1))):
        os.mkdir(os.path.join(base_dir, "dir_"+str(i+1)))


list_dir=(os.listdir(base_dir))
print(list_dir)

for directory in list_dir:
    for j in range(9):
        if str(directory)=="dir_"+str(j+1):
            os.rmdir(str(base_dir+"/dir_"+str(j+1)))



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

files=(os.listdir())
for file in files:
    if os.path.isfile(os.path.join(file))==False:
        print(file)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
shutil.copy2(filename, 'copy.txt')

