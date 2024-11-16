phrase = input()
words = phrase.split()
dict = {w: len(w) for w in words}
print(dict)