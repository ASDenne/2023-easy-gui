import easygui, random
for n in range(1,7):
    print(n)
gibberish = ""
choices = "qazwxecrdtvfybu1234567890-09876543212345678909876543!@#$%^&*()_+|}{gvcn6y55gVJGUEhuitivmuoicghieo,emhvgtuchi!$%^&_+=-';/.,kBI5VTCY:><M2123456789                               imjkolo.imjnuhybtvfrcdexzxcvbnumi,koijhhgyufrtdvcvybihjh8t76f45d342367i8o9p;olk.,mnbjguioypk0p;,olmkjnZX3W4CEF5RGUY6TH7IUKLOJHGTFRDETS3D5FGhuytrsryuipo[o8i76fydewtsqxweirtyu9ijhg876dywdbfnm,.'[;kj9hg8edjf,"          ".=],-[0pm9op[.]4H56JY8UO,IUHYGFDETRDE5VRI67BTNYM8UYTG"
for n in range(0,random.randint(100,10000)):
    gibberish = gibberish + str(random.choices(choices))[2]
easygui.msgbox(gibberish)
