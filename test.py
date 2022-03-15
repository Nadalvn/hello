from random import randint
while True:
    print("Rock Paper Scissors ")
    print('Select: rock, paper, scissors')
    you = input("Player: ")
    print("------")
    bot = randint(0,2)

    if bot == 0:
        bot = "Rock"
    if bot == 1:
        bot = 'Paper'
    if bot == 2:
        bot = 'Scissors'
    print('Bot: ' + str(bot))
    if you == "rock":
        if bot == "Rock":
            print("------")
            print("Tie")
    if you == "scissors":
        if bot == "Scissors":
            print("------")
            print('Tie')
    if you == 'paper':
        if bot == 'Paper':
            print("------")
            print("Tie")
    w = "You win!"
    l = "You lose! Try again"
    r = 'rock'
    p = 'paper'
    s = 'scissors'
    if you == 'rock':
        if bot == 'Scissors':
            print("------")
            print(w)
    if you == s:
        if bot == 'Rock':
            print("------")
            print(l)
    if you == p:
        if bot == 'Rock':
            print("------")
            print(w)
    if you == r:
        if bot == "Paper":
            print("------")
            print(l)
    if you == s:
        if bot == "Paper":
            print("------")
            print(w)
    if you == p:
        if bot == 'Scissors':
            print("------")
            print(l)