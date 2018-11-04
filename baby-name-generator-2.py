import random, string

letter_input_1 = input('choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter: ')
letter_input_2 = input('choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter: ')
letter_input_3 = input('choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter: ')
letter_input_4 = input('choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter: ')
letter_input_5 = input('choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter: ')

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstuvwxz"
letter = string.ascii_lowercase

def generator():  
    if letter_input_1 == "v":
        return random.choice(vowels)
    elif letter_input_1 == "c":
        return random.choice(consonants)
    elif letter_input_1 == "l":
        return random.choice(letter)
    else:
        return letter_input_1
    if letter_input_2 == "v":
        return random.choice(vowels)
    elif letter_input_2 == "c":
        return random.choice(consonants)
    elif letter_input_2 == "l":
         return random.choice(letter)
    else:
        return letter_input_2
    if letter_input_3 == "v":
        return random.choice(vowels)
    elif letter_input_3 == "c":
        return random.choice(consonants)
    elif letter_input_3 == "l":
        return random.choice(letter)
    else:
        return letter_input_3
    if letter_input_4 == "v":
        return random.choice(vowels)
    elif letter_input_4 == "c":
        return random.choice(consonants)
    elif letter_input_4 == "l":
        return random.choice(letter)
    else:
        return letter_input_4
    if letter_input_5 == "v":
        return random.choice(vowels)
    elif letter_input_5 == "c":
        return random.choice(consonants)
    elif letter_input_5 == "l":
        return random.choice(letter)
    else:
        return letter_input_5
        print(generator())
