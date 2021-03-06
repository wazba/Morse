import os
import subprocess


Morse = {"a": "•-", "b": "-•••", "c": "-•-•", "d": "-••", "e": "•",
         "f": "••-•", "g": "--•", "h": "••••", "i": "••", "j": "•---",
         "k": "-•-", "l": "•-••", "m": "--", "n": "-•", "o": "---",
         "p": "•--•", "q": "--•-", "r": "•-•", "s": "•••", "t": "-",
         "u": "••-", "v": "•••-", "w": "•--", "x": "-••-", "y": "-•--",
         "z": "--••", " ": "\n",

         "A": "•-", "B": "-•••", "C": "-•-•", "D": "-••", "E": "•",
         "F": "••-•", "G": "--•", "H": "••••", "I": "••", "J": "•---",
         "K": "-•-", "L": "•-••", "M": "--", "N": "-•", "O": "---",
         "P": "•--•", "Q": "--•-", "R": "•-•", "S": "•••", "T": "-",
         "U": "••-", "V": "•••-", "W": "•--", "X": "-••-", "Y": "-•--",
         "Z": "--••"
         }

MorseV = {"a": "morse/A.mp4", "b": "morse/B.mp4", "c": "morse/C.mp4", "d": "morse/D.mp4", "e": "morse/E.mp4",
          "f": "morse/F.mp4", "g": "morse/G.mp4", "h": "morse/H.mp4", "i": "morse/I.mp4", "j": "morse/J.mp4",
          "k": "morse/K.mp4", "l": "morse/L.mp4", "m": "morse/M.mp4", "n": "morse/N.mp4", "o": "morse/O.mp4",
          "p": "morse/P.mp4", "q": "morse/Q.mp4", "r": "morse/R.mp4", "s": "morse/S.mp4", "t": "morse/T.mp4",
          "u": "morse/U.mp4", "v": "morse/V.mp4", "w": "morse/W.mp4", "x": "morse/X.mp4", "y": "morse/Y.mp4",
          "z": "morse/Z.mp4", " ": "morse/Space.mp4",

          "A": "morse/A.mp4", "B": "morse/B.mp4", "C": "morse/C.mp4", "D": "morse/D.mp4", "E": "morse/E.mp4",
          "F": "morse/F.mp4", "G": "morse/G.mp4", "H": "morse/H.mp4", "I": "morse/I.mp4", "J": "morse/J.mp4",
          "K": "morse/K.mp4", "L": "morse/L.mp4", "M": "morse/M.mp4", "N": "morse/N.mp4", "O": "morse/O.mp4",
          "P": "morse/P.mp4", "Q": "morse/Q.mp4", "R": "morse/R.mp4", "S": "morse/S.mp4", "T": "morse/T.mp4",
          "U": "morse/U.mp4", "V": "morse/V.mp4", "W": "morse/W.mp4", "X": "morse/X.mp4", "Y": "morse/Y.mp4",
          "Z": "morse/Z.mp4"
          }


def to_morse(text):
    os.system('clear')
    text1 = []
    morse = []
    Text = list(text)
    for i in range(0, len(Text)):
        os.system('clear')
        out = ''.join(text1)
        print("->", out)
        print("-->", Text[i], "<--")
        text1.append(Text[i])
        charter = Morse[Text[i]]
        print(charter)
        morse.append(charter)
        morse.append(" ")
        try:
            subprocess.call(["afplay", MorseV[Text[i]]])
        except:
            print("error")

    os.system('clear')
    out = ''.join(text1)
    out1 = ''.join(morse)
    print(out, ": ", out1)


def morseta():
    while 1 == 1:
        moi = input("Morseksi:  ")
        to_morse(moi)
