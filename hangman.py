secret_word = input("Enter the secret word : ")
guesses = 5
won = False
while guesses >= 0:
    user_guess = input("Guess the word : ").lower()
    if user_guess == secret_word:
        print(user_guess)
        won = True
        break
    for i in range(len(user_guess)):
        if user_guess[i] == secret_word[i]:
            print(user_guess[i],end="")
        else:
            print("_",end = "")
    print("")
    guesses-=1
print("You Won") if won  else print("You Lose")