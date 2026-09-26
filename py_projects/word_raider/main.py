import random
game_name ="Word Raider"
word_bank=[]

with open("word.txt","r") as word_file:
     for line in word_file:
         word_bank.append(line.rstrip().lower())

#print(word_bank)
word_select=random.choice(word_bank)
incorrect_letters=[]
misplaced_letters=[]
max_turn=6
used_turns=0

print(f"Welcome to {game_name}")
print(f"The word to guess has{len(word_select)} letters")
print(f"you have {max_turn} turns to guess the word ")

while used_turns<max_turn:
    guess=input("Guess a word (or type 'stop' to end the game) :").lower()
    if guess=="stop":
        break

    if len(guess) !=len(word_select) or not guess.isalpha():
        print("please enter a 5 letter word")
        continue

    index=0
    for letter in guess:
        if letter==word_select[index]:
           print(letter, end=' ')
           if letter in misplaced_letters:
               misplaced_letters.remove(letter)
        elif letter in word_select:
            if letter not in misplaced_letters:
               misplaced_letters.append(letter)
            print("_",end=' ')
        else:
            if letter not in incorrect_letters:
                incorrect_letters.append(letter)
            print("_",end=' ')

        index+=1

    if guess==word_select:
        print("Congratulations you guessed the word! ")
        break
    used_turns+=1
    if used_turns==max_turn:
        print(f"game over, you lost. The word was: {word_select}")
        break

    print("\n")
    print(f"Misplaced letters: {misplaced_letters}")
    print(f"Incorret letters:{incorrect_letters}")
    print(f"You have {max_turn - used_turns} turns left .")