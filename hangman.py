import random, string, colorama, time #added color in various places
from words import words, nice, mean
from stickperson import hangman_pic #modified the visual a bit

def get_valid_word(words):
    word = random.choice(words[2:52])
    while '-' in word or ' ' in word:
        word = random.choice(words)   
    return word.upper()

#getting the different responses
nice = random.choice(nice)
mean = random.choice(mean)

print(f"""{colorama.Fore.LIGHTBLACK_EX}
      Welcome to hangman! The objective is simple, try and guess the word letter by letter
      before the figure is drawn in and is killed. Lets see if you have what it takes!\n
      If you would to play the game type in "play", but if you would like to quit type in "end"
      """)
time.sleep(1)

choice = input().upper()
while True:
    if choice == "PLAY":
        def hangman():
            word = get_valid_word(words)
            word_letters = set(word)
            alphabet = set(string.ascii_uppercase)
            used_letters = set()
            
            lives = 7
            
            #getting user input
            while len(word_letters) > 0 and lives > 0:
                #letters used
                print(f"{colorama.Fore.LIGHTWHITE_EX}\nYou have", lives, "lives left and, you have used these letters: ", " ".join(used_letters))
                
                #what current word is
                word_list = [letter if letter in used_letters else '-' for letter in word]
                print(hangman_pic[lives])
                print(f"{colorama.Fore.LIGHTWHITE_EX}Current word: ", " ".join(word_list))
                
                user_letter = input(f"{colorama.Fore.YELLOW}\nGuess a letter: ").upper()
                if user_letter in alphabet - used_letters:
                    used_letters.add(user_letter)
                    if user_letter in word_letters:
                        word_letters.remove(user_letter)
                        time.sleep(1)
                        print('')
                    
                    else:
                        lives = lives - 1 
                        print(f'{colorama.Fore.LIGHTWHITE_EX}\n Your letter,', user_letter, 'is not in the word.')
                        
                elif user_letter in used_letters:
                    print(f"{colorama.Fore.LIGHTWHITE_EX}\n How could you possibly forget, you have already guessed that letter. Please choose another letter.")
                
                else:
                    print("\n Sorry, that doesn't seem to be a valid letter, please try again!")
            
            if lives == 0:
                print(hangman_pic[lives])
                print(f"{colorama.Fore.CYAN}The word was {word}{colorama.Fore.LIGHTWHITE_EX}")
                print(mean)
                choice = input().upper()
                if choice != "PLAY":
                    print(f"{colorama.Fore.LIGHTWHITE_EX}Aw man sad to see you leave :((. Thank you for playing!")       
                    time.sleep(0.5)     
                    quit()
            else:
                print(nice)
                choice = input().upper()
                
        if __name__ == '__main__':
                hangman()
                
    elif choice == "END":
        print(f"{colorama.Fore.LIGHTWHITE_EX}Aw man sad to see you leave :((. Thank you for playing!")       
        time.sleep(0.5)     
        quit()
        
    else:
        print("Hmm seems like you didn't choose one of the two options, please make sure to either play or end!")
        choice = input().upper()