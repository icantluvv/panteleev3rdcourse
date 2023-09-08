player1, player2 = input().split()

def play_game(player1, player2):
    if player1 == player2:
        return "ничья"
    if (player1 == "камень" and player2 == "ножницы") or (player1 == "ножницы" and player2 == "бумага") or (player1 == "бумага" and player2 == "камень"):
        return "игрок 1 выиграл"
    else:
        return "игрок 2 выиграл"

result = play_game(player1, player2)
print(result)