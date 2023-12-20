asciiList = []
binaryList = ["1101000","1101111","1110000","100000","1101111","1101110","100000","1100111","1101001","1110100","1101000","1110101","1100010"]
for i in range(13):
    num = int(input("Enter an int: "))
    asciiList.append(num)
correct = True
for i in range(13):
    if asciiList[i] != int(binaryList[i],2):
        correct = False
        break
sentence = "".join([chr(value) for value in asciiList])
for letter in asciiList:
    chr(letter)
    print(sentence)
if correct:
    print("Merry Christmas")
else:
    print("Incorrect Sentence")
