import easygui

word = easygui.enterbox("what word do you want to convert")
output = word[0]
test = ""
if "our" in word:
    swap = word.index("our")
    output = word[0:swap]+"or"+word[swap+2:-0]
if "ise" in word:
    swap = word.index("ise")
    output = word[0:swap]+"ize"+word[swap+2:-0]
if "yse" in word:
    swap = word.index("yse")
    output = word[0:swap]+"yze"+word[swap+2:-0]

easygui.msgbox(f"the nz word {word} is spelt {output} in the us")
