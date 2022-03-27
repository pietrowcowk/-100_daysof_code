import pandas as pd

alphabet = pd.read_csv('nato-phonetic-alphabet.csv')

phonetic_dict =  {row.letter: row.code for (index, row) in alphabet.iterrows() }

def generate_phonetic():
    word = input('Enter a word:').upper()
    try:
        result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, enter only letters.')
        generate_phonetic()
    else:
        print(result)

generate_phonetic()