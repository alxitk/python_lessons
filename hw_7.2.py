# HW 7.2. Модифікувати рядок


def correct_sentence(text):
    text = text.capitalize()
    if not text.endswith("."):
        text += "."
    return text


print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greetings, Friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))
