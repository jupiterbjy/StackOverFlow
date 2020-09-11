import pandas as pd

df = pd.DataFrame({'A': [3, 1, 2, 3],
                   'B': [5, 6, 7, 8]})

result = pd.DataFrame(index=df.index, columns=df.columns)

for col in df.columns:
    for index in df.index:
        result.loc[index, col] = df[col].shift(index).max()

print(result)
