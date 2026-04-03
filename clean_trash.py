import os
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument('--trash_folder_path')
parser.add_argument('--age_thr', type=int)
deli = parser.parse_args()
trash_folder_path = deli.trash_folder_path
age = deli.age_thr
with open(trash_folder_path.rstrip("trash") + "clean_trash.log", 'w') as f:
    while True:
        for dir in os.walk(trash_folder_path):
            print(dir)
            if dir[1] == [] and dir[2] == []:
                f.write(f"{dir[0]}\n")
                os.rmdir(dir[0])
                continue
            for file in dir[2]:
                print(os.path.getmtime(dir[0] + '\\' + file))
                if os.path.getmtime(dir[0] + '\\' + file) >= age:
                    f.write(f"{dir[0] + '\\' + file}\n")
                    os.remove(dir[0] + '\\' + file)
        time.sleep(1)
