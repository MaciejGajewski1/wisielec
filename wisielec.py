def hangman():
    import random
    word = ['Grudzień','Domek','Delfin','informatyka','autobus','impreza','laptop','śniadanie','wulkan','katastrofa','Pelikan','Tarantula','Smakosz','Piesełek','Huragan','Śnieżyca','Manekin','Kaktus','Kinoman','Port','Portfolio']
    rand_word = word[random.randint(0,20)]
    wrong = 0
    wisielec = [" ",
                "________      ",
                "|       |     ",
                "|       O     ",
                "|      /|\    ",
                "|       |     ",
                "|       |     ",
                "|      / \    ",
                "|             ",
                "|             ",
                "|____________ ",
                "/ | | | | | \ "]
                            
    board = ["__"] * len(rand_word)
    rletters = list(rand_word)
    win = False
    print("Gra w Wisielca")

    while wrong < len(wisielec):
        ask = "Zgadnij literę"
        guess = input(ask)
        if guess in rletters:
            print('\n')
            ind = rletters.index(guess)
            board[ind] = guess
            rletters[ind] = '$'
            print(" ".join(board))
        else:
            wrong += 1
            e = wrong + 1
            print("\n".join(wisielec[0:e]))
        if "__" not in board:
            print(" ".join(board))
            print("Wygrałeś, brawo!")
            win = True
            break
    if not win:
        print("\n".join(wisielec[0:]))
        print("Przegrałeś, słowo-zagadka to: {}".format(rand_word))

hangman()

    
