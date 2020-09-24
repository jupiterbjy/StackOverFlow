from os import listdir

files = listdir()
extensions = set(i.split(".")[-1] for i in files)

file_association = {ext: [] for ext in extensions}

for file in files:
    file_association[file.split('.')[-1]].append(file)


print(file_association)
