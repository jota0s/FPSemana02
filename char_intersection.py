word1 = input()
word2 = input()

intersect = set(word1) & set(word2)

print("".join(sorted(intersect)))