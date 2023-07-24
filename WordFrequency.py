#WordFrequency.py

import csv

infile = open('sometext.txt','r')

reader = csv.reader(infile,delimiter=' ')


#Get rid of punctuation
for word in reader:
    new_word = []
    for character in word:
        if character.isalpha() is True:
            new_word.append(character)
    #print(new_word)

#Count words
def count_word_frequency(word_list):
    word_frequency = {}
    for word in word_list:
        word = word.title()
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

word_dict = count_word_frequency(new_word)
#print(word_dict)

print('Word Frequency:')
print('------------------')
for word in word_dict:
    word = word.title()
    print()
    print(f'Word: {word}')
    print(f'Frequency: {word_dict[word]}')
print()
