# HW 9.1. Визначити популярність певних слів у тексті


from collections import Counter


def popular_words(text, words) -> dict:
    """
    Determines the popularity of certain words in the text.
    """
    txt_counter = Counter(text.lower().split())

    result_dict = dict.fromkeys(words, 0)

    for key in result_dict.keys():
        if key in txt_counter:
            result_dict[key] = txt_counter[key]
    return result_dict


assert popular_words(
    """When I was One I had just begun When I was Two I was nearly new """,
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test1"
print("Ok")
