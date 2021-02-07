import random


def play():
    print_opening_message()

    word_secret = load_word_secret()

    agreed_letter = initializes_correct_letters(word_secret)

    hang = False
    hit = False

    errors = 0

    hit = game_flow(hang, hit, word_secret, errors, agreed_letter)

    if hit:
        print("You win!")
    else:
        print("You lose")


def print_opening_message():
    print("************************************")
    print("****Welcome to the hangman game*****")
    print("************************************")


def load_word_secret():
    with open("words.txt") as file:
        words = [line.strip() for line in file]

    secret_word = words[random.randrange(0, len(words))].upper()
    return secret_word


def initializes_correct_letters(word):
    return ["_" for letter in word]


def find_letter_in_the_word(word, shot, agreed_letter):
    for index, letter in enumerate(word, start=0):
        if shot == letter:
            agreed_letter[index] = letter
    return agreed_letter


def game_flow(hang, hit, word_secret, errors, agreed_letter):
    attempts = 5
    while not hang and not hit:
        shot = input("What's the letter??")
        shot = shot.strip().upper()

        if shot in word_secret:
            find_letter_in_the_word(word_secret, shot, agreed_letter)
        else:
            errors += 1

        if errors == 5:
            hang = True

        if "_" not in agreed_letter:
            hit = True
        attempts = 5 - errors
        result_per_round(agreed_letter, attempts)
    print_final_result(attempts)
    return hit


def result_per_round(agreed_letter, attempts):
    print("now: {}".format(agreed_letter))
    print("attempts: {}".format(attempts))


def print_final_result(attempts):
    print("Remaining attempts: {}".format(attempts))
    print("Points: {}".format(20 * attempts))
    print("End of the game")


if __name__ == "__main__":
    play()
