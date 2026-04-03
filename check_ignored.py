from os import walk
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--project_dir')
repozitory = parser.parse_args().project_dir
repozname = repozitory.split('\\')[-1]

ALLFILE = list(walk(repozitory))

def found(token):
    if token[0] == '*':
        token = token[1:]
        for x in ALLFILE:
            for file in x[2]:
                if token in file:
                    if x[0].split('\\')[-1] == repozname:
                        print(file, "ignored by expression", "*" + token)
                    else:
                        print(repozname + x[0].split(repozname)[-1] + '\\' + file, "ignored by expression", "*" + token)
                    break
    else:
        for x in ALLFILE:
            for file in x[2]:
                if token == file:
                    if x[0].split('\\')[-1] == repozname:
                        print(file, "ignored by expression", token)
                    else:
                        print(repozname + x[0].split(repozname)[-1] + '\\' + file, "ignored by expression", token)
                    break

with open(repozitory + "\\.gitignore", 'r') as f:
    lines = list(map(str.strip, f))

for file in lines:
    found(file)
