a = input()
text = [a[i] for i in range(len(a))]

for i in range(len(text)):
    if text[i] == '-' or text[i] == '=':
        if text[i-1] == 'z' and text[i-2] == 'd':
            text[i] = '='
            text[i-1] = ''
            text[i-2] = ''
        else:
            text[i-1] = ''
            text[i] = '='

    elif text[i] == 'j' and text[i-1] == 'l':
        text[i-1] = ''
        text[i] = 'j'

    elif text[i] == 'j' and text[i-1] == 'n':
        text[i-1] = ''
        text[i] = 'j'

# text = [i for i in text if i]
text = ' '.join(text).split()
print(len(text))