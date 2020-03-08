def TopLevel():
    Response="Y"
    InputData=""
    Success=True
    while Response=="Y":
        InputData=GetInfo()
        if InputData[0]<"N":
            Success=WriteInfo(InputData,"File1.txt")
        else:
            Success=WriteInfo(InputData,"File2.txt")
        if not Success:
            Response="Y"
        else:
            Response=input("Enter Details for another student?(Y/N")")
