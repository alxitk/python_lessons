# HW 5.3. hashtag
import string

original_text = 'Python community'
original_text = 'i like python community!'
original_text = 'Should, I. subscribe? Yes!'
words = original_text.split()
result = []

for i, v in enumerate(words):

    words[i] = words[i].capitalize()

    for char in words[i]:
        if char not in string.punctuation:
            result.append(char)

result = '#' + ''.join(result[:140])

print(f"{original_text} -> {result}")
