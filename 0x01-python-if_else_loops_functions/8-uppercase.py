def uppercase(str):
    ns = ""
    for char in str:
        if (ord(char) in range(97, 123)):
            a = ord(char) - 32
            ns += chr(a)
        else:
            ns += char
    print(ns)
