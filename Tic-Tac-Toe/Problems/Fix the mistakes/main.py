text = input()
words = text.split()
for word in words:
    # finish the code here
    if not word.isdecimal() and word.isupper():
        word.lower()
        if word.startswith("WWW.") or word.startswith("HTTPS://") or word.startswith("HTTP://"):
            print(word)
    elif word.startswith("www.") or word.startswith("https://") or word.startswith("http://"):
        print(word)
    elif word.startswith("WWW.") or word.startswith("HTTPS://") or word.startswith("HTTP://"):
        print(word)
