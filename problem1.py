import re

str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def replace_numerical_words(text):
    for word, replacement in str2num.items():
        text = text.replace(word, replacement)
    return text

def calculate_calibration_score(text):
    return sum(int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", text).split("\n"))

text = open("input1.txt").read()

print(calculate_calibration_score(replace_numerical_words(text)))