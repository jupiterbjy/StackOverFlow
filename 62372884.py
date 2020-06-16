
source = 'a s d f g h j k l ' * 2
list_of_strings = source.split()
target = 'a'

# infinite loop
for element in list_of_strings:
    if element in ('BUMP', 'NOPE'):
        continue
    idx = list_of_strings.index(element)
    s = 'BUMP' if target in element else 'NOPE'
    list_of_strings.insert(idx + 1, s)

print(f"input: {source.split()}")
print(f"output: {list_of_strings}")
