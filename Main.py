import Morse as MorseE
import morse_decode as MorseD
import os
import time


def instructions():
    print("Press [E] to encode text to morse")
    print("Press [D] to decode morse to text")
    print("Press [C] to clear screen")
    print("Press [Q] to quit")


def user_text(encode):

    os.system('clear')
    if encode is True:
        print("Encoding text to morse...")
        text = input("Type your text: ")
        MorseE.to_morse(text)

    else:
        print("Decoding morse to text...")
        print("- is long and • (alt + Q) is short")
        text = input("Type your morse: ")
        os.system('clear')
        print("Your morse(",  text, ") is: ", MorseD.kk(text))

    time.sleep(2)
    main()


def main():
    instructions()
    user_input = input("User: ")
    if user_input == "E" or user_input == "e":
        user_text(True)
    elif user_input == "D" or user_input == "d":
        user_text(False)
    elif user_input == "C" or user_input == "c":
        os.system('clear')
        time.sleep(1)
        main()
    elif user_input == "Q" or user_input == "q":
        a = 0
        os.system('clear')
        for i in range(0, 33):
            for b in range(1, 4):
                a += 1
                os.system('clear')
                print(a, "% Quitting", "."*b)

        os.system('clear')
        print("100%")
        print("SEE YOU!")
        time.sleep(2)
        quit(7)
    else:
        os.system('clear')
        print("-----!READ!-----")
        main()


if __name__ == '__main__':
    main()
