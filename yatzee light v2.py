import easygui, random
def rolling(player):
    reroll = "reroll"
    rolls = 0
    while reroll == "reroll" and rolls < 3:
        rolls += 1
        dice = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
        reroll = easygui.buttonbox(f"on {player} dice roll {rolls} \n rolled {dice[0]} {dice[1]} {dice[2]} {dice[3]} {dice[4]}",choices=["reroll","stick"])
    if reroll == "reroll":
        return 0
    if rolls > 3:
        return 0
    largest_streak = 0
    for n in range(1,7):
        streak = dice.count(n)
        if streak > largest_streak:
            largest_streak = streak
    if largest_streak == 5:
        return 50
    elif largest_streak == 4:
        return 30
    elif largest_streak == 3:
        return 10
    else:
        return 0

player_1 = easygui.enterbox("enter the name of player one",title="player 1")
player_2 = easygui.enterbox("enter the name of player two",title="player 2")
countinue = "Yes"
while countinue =="Yes":
    p1score = rolling(player_1)
    p2score = rolling(player_2)
    if p1score == p2score:
        msg = f"draw\n{player_1} tied with {player_2}\nthey both scored {p2score}"
    elif p1score > p2score:
        msg = f"{player_1} won\n{player_1} got {p1score} while {player_2} got {p2score}"
    else:
        msg = f"{player_2} won\n{player_2} got {p2score} while {player_1} got {p1score}"
    countinue = easygui.buttonbox(f"{msg}\n do you want to continue",choices=["Yes","No"])
