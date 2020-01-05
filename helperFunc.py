def option(auth):
    if(auth=="OLD" or auth=="old"):
        optVal = input("MAIN_MENU -> 1. Update General Info\n             2. Update\n             3. Show Profile\n             4. Search Young peoples\n             5. Notification\n             6.Exit\n")
    elif(auth=="YOUNG" or auth=="young"):
        optVal = input("MAIN_MENU -> 1. Update General Info\n             2. Update\n             3. Show Profile\n             4. Search Old people\n             5. Notification\n             6.Exit\n")
    return optVal

def updateDriver(auth):
    updateVal = input("MAIN_MENU -> UPDATE -> 1. Age\n                       2. Present Location\n                       3. Preferred Location\n                       4. Back\n                       5. Other\n")
    if(updateVal=="1"):
       updateVal="age"
    elif(updateVal=="2"):
       updateVal="presentLocation"
    elif( updateVal=="3"):
       updateVal="preferredLocation"
    elif( updateVal=="4"):
       updateVal="back"
       
    elif(updateVal=="5"):
       Print("for future references.")
       updateVal="back"
    else:
       updateVal="Invalid value"
    return updateVal   

def getFieldIndex(optionChoosen):
    if(optionChoosen=="1"):
        index = 0
        field = "userName"
    elif(optionChoosen=="2"):
        index = 1
        field = "role"
    elif(optionChoosen=="3"):
        index = 2
        field = "age"
    elif(optionChoosen=="4"):
        index = 3
        field = "presentLocation"
    elif(optionChoosen=="5"):
        index = 4
        field = "preferredLocation"
    elif(optionChoosen=="6"):
        index = 5
        field = "specificAns1"
    else:
        index ="error"
        field="error"    
    return field,index 
