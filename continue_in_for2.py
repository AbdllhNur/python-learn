user_word = input("whats the word? ")

user_word = user_word.upper()

for letter in user_word:
    if letter in "AIUEO" : 
        continue
    else :
        print(letter, end="")