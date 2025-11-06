inputString = input()
while "FOO" in inputString:
    print("REPLACING")
    inputString = inputString.replace("FOO", "OOF", 1)
print(inputString)
