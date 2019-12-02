import pyperclip
import string

text = pyperclip.paste()
title = text.translate(str.maketrans(dict.fromkeys(string.punctuation)))
words = title.split()
words = map(str.lower,words)
slug = '_'.join(words)
pyperclip.copy(slug)
