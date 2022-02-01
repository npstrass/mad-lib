import requests

response = requests.get("http://madlibz.herokuapp.com/api/random")

lib = response.json()

title = lib['title']
blanks = lib['blanks']
value = lib['value']

inputs = []
result = []

for i in blanks:
    inputs.append(input(f"{i}: "))

num = min(len(value), len(inputs))
result = [None]*(num*2)
result[::2] = value[:num]
result[1::2] = inputs[:num]
result.extend(value[num:])
result.extend(inputs[num:])
del result[-1]

print(''.join([str(i) for i in result]))
