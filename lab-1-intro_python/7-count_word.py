text = input("Write Sentence and Press Enter:\n")

sentence = text.split(".")
print(sentence)

if len(sentence) > 1:
    for sent in sentence:
        sub_sentence = sent.split(",")
        print(sub_sentence)

        if len(sub_sentence) > 1:
            for sub_sen in sub_sentence:
                words = sub_sen.split(" ")