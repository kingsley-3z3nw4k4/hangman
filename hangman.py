def hangman():
    stage = 0
    wrong_guesses = ["","_______   ","|    |   ","|    0   ","|   /|\  ","|   / \  ","|        "]
    word = "goat"
    score_board = ['_']*len(word)
    win = False

    print("Welcome to Hang Man")

    while stage < len(wrong_guesses)-1:
        print('\n')
        guess = input('Guess a letter:... ')

        if guess in word:
            score_board[word.index(guess)] = guess
        else:
            stage += 1

        print(' '.join(score_board))
        print('\n'.join(wrong_guesses[0:stage+1]))

        if '_' not in score_board:
            print(f"\nYou win! The word was: {''.join(score_board)}")
            win = True
            break

    if not win:
        print('\nYou lose!')

hangman()
