text = input("Уведи рядок із великих символів W та B ->")
text += "a"
rez = ''
k = 1
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        k +=1
    else:
        rez += str(k)
        rez += text[i]
        k = 1

print(rez)
