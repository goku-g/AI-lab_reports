text = input("Write Sentence and Press Enter:\n")

words = []
sentence = text.split(".")

for sub_sen in sentence:
    sen = sub_sen.split(",")

    for wrd in sen:
        for data in wrd.split(" "):
            if data != '':
                words.append(data)

print(words)
print("Words count in sentance is: {}".format(len(words)))