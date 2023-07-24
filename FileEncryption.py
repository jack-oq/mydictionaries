import csv

infile = open('info_security.txt', 'r')
outfile = open('encrypted.txt', 'w')

reader = csv.reader(infile)

encryption_key = {
    'A': '9',
    'B': '8',
    'C': '7',
    'D': '6',
    'E': '5',
    'F': '4',
    'G': '3',
    'H': '2',
    'I': '1',
    'J': '0',
    'K': 'A',
    'L': 'B',
    'M': 'C',
    'N': 'D',
    'O': 'E',
    'P': 'F',
    'Q': 'G',
    'R': 'H',
    'S': 'I',
    'T': 'J',
    'U': 'K',
    'V': 'L',
    'W': 'M',
    'X': 'N',
    'Y': 'O',
    'Z': 'P',
    'a': 'q',
    'b': 'r',
    'c': 's',
    'd': 't',
    'e': 'u',
    'f': 'v',
    'g': 'w',
    'h': 'x',
    'i': 'y',
    'j': 'z',
    'k': '!',
    'l': '@',
    'm': '#',
    'n': '$',
    'o': '%',
    'p': '^',
    'q': '&',
    'r': '*',
    's': '(',
    't': ')',
    'u': '-',
    'v': '+',
    'w': '=',
    'x': '{',
    'y': '}',
    'z': '?'
}

encrypted_text = ""
for text in reader:
    for word in text:
        for char in word:
            if char in encryption_key:
                char = encryption_key.get(char)
            encrypted_text += char

outfile.write(encrypted_text)

infile.close()
outfile.close()
