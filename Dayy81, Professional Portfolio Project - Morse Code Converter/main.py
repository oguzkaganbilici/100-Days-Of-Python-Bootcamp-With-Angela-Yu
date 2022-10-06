morse_alphabet = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}


def alphabet_to_morse(text):
    new_word = ""
    new_text = text.split(" ")
    for i in text:
        i = i.upper()
        if i in morse_alphabet:
            mors = morse_alphabet.get(i)
            new_word = new_word + " " + mors
        if i == " ":
            pass
    return new_word


def morse_to_alphabet(text):
    new_word = ""
    for each_ in text.split(" "):
        for words, morse in morse_alphabet.items():
            if morse == each_:
                new_word += words
    return new_word


flag = True
while flag:
    choice = input("Do you want to encode('E') or decode?('D')/quit('Q'): ").lower()
    if choice == "e":
        word = input("Please write your sentence that you want to encode: \n")
        print("The morse code is: \n", alphabet_to_morse(word))
    elif choice == "d":
        word = input("Please write your morse code that you want to decode: \n")
        print("The morse code is: \n", morse_to_alphabet(word))

    elif choice == "q":
        print("Good Bye!")
        flag = False
    else:
        print("Try again!")


