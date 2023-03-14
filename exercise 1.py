import easygui, random
a = easygui.enterbox("Hi! what is your name?","name")
b = easygui.integerbox("how old are you","age")
print(a,b)
c = easygui.buttonbox("do you want to continue",
                      title="countinue?",choices=["yes","no","maybe"])
print(c)
if c != "no":
    n = random.randint(0,10000000000000)
    easygui.msgbox(f"hi {a} welcome to easygui this is our code for {b} year olds you are the {n} user","welcome")
