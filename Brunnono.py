def checkInput(input):
    if input >= '0' and input <= '9':
        return input
    return 0

while True:
    wordInput = str(input())
    if checkInput(wordInput[0]) == 0 or checkInput(wordInput[2]) == 0:
        print("input on x and y are not valid")
        break
    if wordInput[0] == '0' and wordInput[2] == '0':
        print("BroNoNoNo")
    elif wordInput[0] == '1' and wordInput[2] == '1':
        print("BroYesYesYes")
    elif wordInput[0] == '0' and wordInput[2] == '1':
        print("BroYesYesYes")


