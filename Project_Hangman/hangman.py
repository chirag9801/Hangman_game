import random
from words import word_list

def get_word():
    word= random.choice(word_list)
    return word.upper()

def play(word):
    word_completion= "_" * len(word)
    guessed=False
    guess_letters = []
    guess_words= []
    tries = 6
    print("Let's Play Hangman!!!")
    name = input("Enter name: ")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries >0:
        guess= input("please guess a letter: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guess_letters:
                print("you already guessed the letter", guess)
            elif guess not in word:
                print(guess,"not in word")
                tries-=1
                guess_letters.append(guess)
            else:
                print("Good Job", guess, "is in the word")
                guess_letters.append(guess)
                word_as_list= list(word_completion)
                indice = [i for i, letter in enumerate(word) if letter==guess]
                for index in indice:
                    word_as_list[index]=guess
                word_completion="".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True


        elif len(guess)== len(word) and guess.isalpha():
            if guess in guess_words:
                print("you already guess the word", guess)
            elif guess!=word:
                print(guess, "is not in the word")
                tries = -1
                guess_letters.append(guess)
            else:
                guessed =True
                word_completion = word

        else:
            print("Not a valid Guess...")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print(name," you guessed the word!, you win")
    else:
        print(name," sorry, no tries left. The word was " +word+ " better luck next time!")




def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word =get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()





