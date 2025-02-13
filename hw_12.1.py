# HW 12.1. Очистити текст від html-тегів

import codecs
import re


def delete_html_tags(html_file, result_file="cleaned.txt"):
    pattern = r"\<[^>]+>"
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()
    result_file = re.sub(pattern, "", html)
    return result_file





