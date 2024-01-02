import re

threshold = {'red': 12, 'blue': 14, 'green': 13}
total = 0
for x, line in enumerate(open("input2.txt")):
    res = re.findall(r'(\d+) (red|blue|green)', line)
    if not any(int(pull[0]) > threshold[pull[1]] for pull in res):
        total += x + 1
print(total)

total = 0
for line in open("input2.txt"):
    res = re.findall(r'(\d+) (red|blue|green)', line)
    values = {'red': 0, 'blue': 0, 'green': 0}
    for num, color in res:
        values[color] = max(values[color], int(num))
    total += values['red'] * values['green'] * values['blue']
print(total)