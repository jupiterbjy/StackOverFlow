item_dict = {
    "Guido_buy": 100,
    "Guido_sell": -100,
    "Ramalho_buy": 200,
    "Ramalho_sell": -200,
}


name = "Guido van Rossum"
type_ = "buy"

results = [
    item_dict[key]
    for key in [key_ for key_ in item_dict.keys() if type_ in key_]
    if set(name.split()) & set(key.split("_"))
]
print(results)


name = "Luciano Ramalho"
type_ = "sell"

results = [
    item_dict[key]
    for key in [key_ for key_ in item_dict.keys() if type_ in key_]
    if set(name.split()) & set(key.split("_"))
]

print(results)
