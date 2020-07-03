students = int(input("Enter number of students: "))

grocery_multiplier = {
    'carrots': 5,
    'onions': 3,
    'peppers': 4,
    'hot dogs': 2,
    'hamburger': 1,
}

texts = []
for field, multiplier in grocery_multiplier.items():
    texts.append(f"{multiplier * students} {field}")

print('You will need ' + ', '.join(texts))
