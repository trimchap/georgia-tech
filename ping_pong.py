#--------------------------------------------------------------------
# Take a 2-tuple argument with the score of 2 players
# return a string: "keep playing" or "winner"
# You have to win by 2 in pingpong
#--------------------------------------------------------------------
def check_pingpong_winner(score):
    (player01, player02) = score
    if player01 < 21 and player02 < 21:
        return "Keep playing!"
    if player01-player02 >= 2:
        return "Player 1 wins!"
    if player02-player01 >= 2:
        return "Player 2 wins!"
    return "Keep playing!"

# Test ping pong score
print(check_pingpong_winner((19, 13)))
print(check_pingpong_winner((21, 13)))
print(check_pingpong_winner((19, 21)))
print(check_pingpong_winner((21, 20)))
print(check_pingpong_winner((25, 25)))
print(check_pingpong_winner((25, 27)))