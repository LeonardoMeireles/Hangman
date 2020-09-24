import random
from palavras import animais

hangman_pics = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

def show_hangman(fails):
    print(hangman_pics[fails])

def get_word():
    word = random.choice(animais) #escolhe uma palavra da lista "animais"
    return word.upper() #transforma "word" em letra maiuscula

def play(word):
    word_completion = []
    for i in range (0, len(word), 1):
        word_completion.append("_")
    guessed = False
    guessed_letters = []
    guessed_words = []
    fails = 0
    print("Let's play Hangman!")
    while fails != 6 and not guessed:
        show_hangman(fails)
        print (*word_completion)
        print("\n")
        guess = input("Guess a letter or the word: ").upper()
        if len(guess) == 1 and guess.isalpha():#guess é um char valido
            if guess in guessed_letters: #jogador já escolheu essa letra
                print("You've allready guessed that letter.")
            elif guess not in word: #guess incorreto
                print("Sorry but that letter is not in the word.")
                guessed_letters.append(guess)
                fails += 1
            else: #right guess
                print("Well done! That letter was in the word.")
                guessed_letters.append(guess)
                pos_acerto = [pos for pos, char in enumerate(word) if char == guess] #retorna a posição de todos os caracteres guess
                for i in range(len(pos_acerto)):
                    word_completion[pos_acerto[i]] = guess #insere o char em word_completion
                if "_" not in word_completion:
                    guessed = True
        
        elif len(guess) == len(word) and guess.isalpha():        #guess é uma palavra valida
            if guess != word:
                print("Sorry, wrong guess.")
                fails+=1
            else:
                print("Congratulations you guessed the word!")
                guessed = True

        else: #guess não é valido
            print("Invalid guess, please try again")
    print (show_hangman(fails))
    print (word)
    if guessed:
        print("You won!")
    else:
        print("You are out of tries, better luck next time!")

def main():
    word = get_word()
    play(word)
    while input("Do you wish to play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)
    print("Thanks for playing, see you next time!")

if __name__ == "__main__":
    main()