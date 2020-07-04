import pandas as pd

data = {
    "FullName": [
        r"dog\cat\cow\rover.doc",
        r"feline\cat\cow\digger.doc",
        r"dog\cat\cow\whatamess.doc",
        r"mouse\cat\mouse\jude.doc",
        r"anteater\cat\mouse\sam.doc",
        r"dog\cat\owl\audrey.doc",
    ],
    "LastWriteTime": [
        "2003-01-02",
        "2004-01-02",
        "2005-01-02",
        "2006-01-02",
        "2007-01-02",
        "2008-01-02",
    ],
}


def check_date(x):
    return pd.to_datetime(x) > pd.to_datetime('2004-06-23', yearfirst=True)


def files_count(x):
    return x.split('\\')[0]


df1 = pd.DataFrame(data)

func_dict = {'FullName': files_count, 'LastWriteTime': check_date}

df4 = df1.aggregate(func_dict)
print(df4, end='\n'*2)

df3_filtered = df4[df4['LastWriteTime']]
print(df3_filtered, end='\n'*2)

df2 = df3_filtered['FullName'].value_counts()
print(df2)
