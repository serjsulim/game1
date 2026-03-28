def reverse(text):
    rev_text = ''
    for i in range(len(text), 0, -1):
        rev_text += text[i-1]
    return rev_text

text = input("уведи текст -> ")
print(reverse(text))

