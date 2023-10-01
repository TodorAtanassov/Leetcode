s = "Let's take LeetCode contest"

words = []
for word in s.split(' '):
    words.append(word[::-1])

print(' '.join(words))