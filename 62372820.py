import re


def func(s, wanted):
    result = re.search('|'.join(wanted), s)
    return result.group(0)


want_list = ['hello', 'my', 'world']
strings = ['hhhellooo', 'mystery', 'go over the world']

for words in strings:
    print(func(words, want_list))
