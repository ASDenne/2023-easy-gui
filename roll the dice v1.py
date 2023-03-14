import easygui, random
rolls = []
for n in range(1,3):
    roller = []
    for r in range(0,2):
        roller.append(random.randint(1,6))
    easygui.msgbox(f"player {n} you rolled\n{roller[0]} and {roller[1]}\ntotal: {roller[0]+roller[1]}",f"player {n}")
