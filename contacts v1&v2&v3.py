import easygui

contacts =[{"id":1,"first_name":"john","last_name":"jacobs","mobile":"027 1234 5678","email":"JohnJacobs@gov.co.nz"},
           {"id":2,"first_name":"josh","last_name":"jacob","mobile":"027 2468 1357","email":"JoshJacobs@G0v.co.nz"}]
action = easygui.buttonbox("do you want to add contact search list or print full list",choices=["add contact","search list","print full list","exit"])





for i in range(0,len(contacts)):
    for id,info in contacts[i].items():
        print(f"{id}:{info}")
    print("")
