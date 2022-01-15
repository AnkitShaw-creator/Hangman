import random as r
import string

file = open('dictionary.txt', 'r')
# print(file.read())


def get_word():
    # to create a list of words from the dictionary.txt
    dictionary = [s for s in file.readlines() if len(s) > 5 and '-' not in s]
    # print(dictionary)
    return r.choice(dictionary).upper().strip()


if __name__ == "__main__":

    word = get_word()  # getting a word from the dictonary
    print(word)
    # print(list(word))
    letters = set(word)
    alphabets = set(string.ascii_uppercase)
    user_choice = set()  # to keep track of what user has entered
    guessed_letter = set()  # to keep track of the letter that thhe user have already guessed
    lives = 6  # a variable to allow limited try to user

    while len(letters) > 0 and lives > 0: #loop to get the user input and check whether the letter is in the word or not
        guessed = [s if s in guessed_letter else '_' for s in word]
        print(' '.join(guessed))

        user_input = input().upper()

        if user_input in alphabets - user_choice:
            user_choice.add(user_input)
            if user_input in letters:
                guessed_letter.add(user_input)
                letters.remove(user_input)
            else:
                lives -= 1
                print(f'You have guessed incorrectly, remaining lives: {lives}')

        else:
            lives -= 1
            print(f'You have already guessed the letter, remaining lives: {lives}')

    # User wins if he guessed all the letter correctly and still has lives left, he will lose if the condition is not satisfied

    if len(letters) == 0 and lives > 0:
        print('Congratulation! You won!')
    else:
        print('Sorry! You lost')
