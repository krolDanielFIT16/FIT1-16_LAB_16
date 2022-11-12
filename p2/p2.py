import unicodedata
import sys
import pylab

charset = {c for i in range(sys.maxunicode + 1) if unicodedata.category(c := chr(i)).startswith("P")}

with open("text.txt", encoding="utf-8") as f:
    text = f.read()
    text = "".join(list(filter(lambda x: x not in charset, list(text))))
    text = " ".join(text.split())

chars = {}

for char in text.split(" "):
    if char not in chars:
        chars[char] = 0
    chars[char] += 1

for i, char in enumerate(chars):
    pylab.bar(i*4, chars[char], width=3)
    pylab.annotate(char, xy=(i*4, chars[char]), xytext=(i*4, chars[char]+0.05), rotation=90, ha="center")
    print(char)

pylab.show()
