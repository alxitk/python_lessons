# HW 8.2. Паліандром


def is_palindrome(text):
    result = True
    text = "".join(i.lower() for i in text if i.isalnum())
    for i in range(len(text)):
        if text[i] != text[-(i + 1)]:
            result = False

    return result


assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("ОК")
