text = input("Write Sentence and Press Enter:\n")

l = len(text)
char_dct = {}

for i in range(l):
    temp_len = len(text[i:l])
    temp = []
    temp.append(text[i])

    for j in range(temp_len-1):
        # print(text[i], text[i+j+1])
        if text[i] == text[i+j+1]:
            temp.append(text[i])
    
    if text[i] not in char_dct:
        char_dct[text[i]] = len(temp)

for key in char_dct:
    print("Frequency of {} is {}".format(key, char_dct[key]))