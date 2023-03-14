import easygui, random
a = easygui.enterbox(f"what is the first place you would like to visit")
b = easygui.enterbox(f"what is the second place you would like to visit")
c = easygui.enterbox(f"what is the third place you would like to visit")
easygui.msgbox(f"you would like to visit {a} most then {b} and then {c}")
