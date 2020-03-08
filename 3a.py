def GetInfo():
    ID=""
    PreferredName=""
    Valid=False
    while not Valid:
        ID=input("enter a valid ID: ")
        if len(ID)==5 and ID[0]>="A" and ID[0]<="Z" and Id[1:].isnumeric():
            Valid=True
    PreferreName=input("enter a preferred name: ")
    return ID+"*"+preferredName
