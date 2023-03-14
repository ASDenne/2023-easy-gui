import easygui
countinue = "yes"
while countinue == "yes":
    name = easygui.enterbox("enter the name of the school")
    kpc = easygui.integerbox("how many students allowed per class")
    k = easygui.integerbox(f"how many kids {name} between 10 and 1400",upperbound=1400)
    t = easygui.integerbox(f"how many teachers at {name} must be a number between 1 and 120",upperbound=120)
    if (k-1)//kpc+1 == t:
        easygui.msgbox(f"{name} has enough teachers per students")
    elif (k-1)//kpc+1 > t:
        easygui.msgbox(f"{name} has too many kids per teacher")
    else:
        easygui.msgbox(f"{name} has too many teachers per kid")
    countinue = easygui.choicebox("do you want to continue?",choices=["yes","no"])
