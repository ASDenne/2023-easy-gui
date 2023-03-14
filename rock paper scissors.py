import easygui, random
def into_no(object):
    if object == "paper":
        return 1
    elif object == "rock":
        return 2
    elif object == "scissors":
        return 3
    elif object == "nuke":
        return 0
    else:
        return -1
items = ["rock","paper","scissors","nuke"]
while easygui.buttonbox("want to play rock paper scissors",choices=["yes","no"])=="yes":
    P_move = easygui.buttonbox("choose your weapon",choices=items)
    R_move = random.choice(items)
    Pn = into_no(P_move)
    Rn = into_no(R_move)
    if Pn * Rn == 0:
        easygui.msgbox("someone played a nuke you both died end of game")
    elif Pn * Rn < 0:
        print("wrong input")
    elif P_move == R_move:
        easygui.msgbox(f"you both choose {P_move} so it was a draw")
    elif (Pn*Rn)%2 == 1:
        if Pn == 1:
            easygui.msgbox("you choose paper and they choose scissors so they win")
        else:
            easygui.msgbox("you choose scissors and they choose paper so you win ")
    elif Pn > Rn:
        easygui.msgbox(f"you choose {P_move} and they choose {R_move} so you lost")
    else:
        easygui.msgbox(f"you choose {P_move} and they choose {R_move} so you win")

