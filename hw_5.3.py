# HW 5.3. hashtag
import string

original_text = 'Python Community'
original_text = 'i like python community!'
original_text = 'Should, I. subscribe? Yes!'
working_text = original_text.split()
result = '#'

for i, v in enumerate(working_text):
    if v[0].islower():
        # modified_text[i] = modified_text[i].capitalize()  # якщо регістр решти літер НЕ важливий
        working_text[i] = v[0].upper() + working_text[i][1:]  # якщо регістр решти літер важливий
    for j in working_text[i]:
        if j not in string.punctuation:
            result += j

print(f"{original_text} -> {result[:139] if len(result) > 140 else result}")