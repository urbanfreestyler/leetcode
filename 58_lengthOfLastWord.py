def last_word(sentence):
    words = sentence.split()[::-1]
    i = 0
    while True:
        word = words[i] if len(words[i]) > 0 else None
        if word is not None:
            return len(word)
        i += 1
