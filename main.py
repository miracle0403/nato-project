import pandas

csv_file = pandas.read_csv("nato_phonetic_alphabet.csv")

dictt = {rows.letter : rows.code for (index, rows) in csv_file.iterrows()}

names = input("Please enter your name \n").upper()

try:
    name = [dictt[letter] for letter in names]
except KeyError:
    print("This format is not supported. Use only alphabets")
else:
    print(name)


