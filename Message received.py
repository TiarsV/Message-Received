import random
NumSize = 30

def give_me_numbers(size):
    count = 0
    StringOfNumbers = ""
    while count < size:
        StringOfNumbers = StringOfNumbers + str(random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',' ',' ']))
        count = count + 1
    return StringOfNumbers

if NumSize == 1:
    print(f"We have a message with 1 letter, and here it is {give_me_numbers(NumSize)}")
else: print(f"We have a message with {NumSize} letters, and here it is'{give_me_numbers(NumSize)}'")