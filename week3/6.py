def reversed_sentance(sentance):
    split_words = sentance.split()
    result = []
    for i in range(len(split_words)):
        return split_words[::-1]
s = input()

converted_to_string = ""
list = reversed_sentance(s)

for word in list:
    converted_to_string += word + " "
print(converted_to_string)