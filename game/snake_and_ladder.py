import random

ladder = {
    2: 53,
    12: 41,
    43: 76,
    64: 97,
}

snake = {
    10: 2,
    45: 31,
    59: 7,
    93: 4
}

def roll():
    return random.randint(1, 6)

while True:
    player_count = input('Enter Number of players 2-10: ')
    if player_count.isdigit():
        player_count = int(player_count)
        if 2 <= player_count and player_count <= 10:
            break
        else:
            print('Player Count Must be between 2-10 only')
    else:
        print('Invalid Option')

player_score = [0 for _ in range(player_count)]

player_turn = 0
while max(player_score) != 100:
    player_turn_score = roll()
    print('Player ' + str(player_turn+1), ' turn and rolled ', player_turn_score)
    if player_score[player_turn] + player_turn_score <= 100:
        player_score[player_turn] += player_turn_score
        if player_score[player_turn] in snake:
            player_score[player_turn] = snake[player_score[player_turn]]
            print('Player ', player_turn+1, ' Bitten by Snake and moving back to', player_score[player_turn])
        if player_score[player_turn] in ladder:
            player_score[player_turn] = ladder[player_score[player_turn]]
            print('Player ', player_turn+1, ' Found a ladder and moving to', player_score[player_turn])
    print('Player ', player_turn+1, ' Current Position - ', player_score[player_turn])
    player_turn += 1
    if player_turn == player_count:
        player_turn = 0
