import mysql.connector
from basicFunc import *
from dbConnect import *
from old import *
from young import *
from helperFunc import *             
   
        
login = input("Press 1. for Login\nPress 2. for SignUp\nRESPONSE -> ")
if(login=="1"):
   name = input("Please enter your UserName : ")
   auth = input("Choose OLD or YOUNG : ")
   dbInst1 = dbConnect(name,auth)
else:
   while(True):
     name = input("Please choose a unique UserName : ")
     auth = input("Choose OLD or YOUNG : ")
     print("\n")
     dbInst1 = dbConnect(name,auth)
     checkUniqueName = dbInst1.uniqueUserName()
     if(checkUniqueName==1):
       print("This name looks perfect.\n")
       break
     else:
       auth = "Not authorized."
       print("Sorry :( This name is taken.\n")
       continue

userProfileStatus = dbInst1.UserExistOrNot()
print("\n")
user = basicFunc(name,auth,userProfileStatus)

#if(auth=="OLD" or auth=="old"):

## Getting info through db or manually (building specific profile layer)
if(dbInst1.dataProvidedOrNot(2)==0):
  age = input("Please enter your age : ")
  _ = dbInst1.updateProfileData("age",age)
else:
  age = dbInst1.getProfileData(2)
       
if(dbInst1.dataProvidedOrNot(3)==0):   
  presentLocation = input("Please enter your Present Location : ")
  _ = dbInst1.updateProfileData("presentLocation",presentLocation)
else:
  presentLocation = dbInst1.getProfileData(3)
       
if(dbInst1.dataProvidedOrNot(4)==0):
  preferredLocation = input("Please enter your Preferred Location : ")
  _ = dbInst1.updateProfileData("preferredLocation",preferredLocation)
  print("\n")
else:
  preferredLocation = dbInst1.getProfileData(4)
  print("\n")
  
## Makiing instance of user specific profile based on authorization 
if(auth=="OLD" or auth=="old"):  
    specificProfile = old(name,auth,age,presentLocation,preferredLocation)
elif(auth=="YOUNG" or auth=="young"):
    specificProfile = young(name,auth,age,presentLocation,preferredLocation)
else: ("Authorization error! restart the application, then choose either YOUNG or OLD.")
    
## Makiing instance of user general profile    
GeneralProfile = user.profile(name,auth,age,presentLocation,preferredLocation)

while(True):
    opt = option(auth)
    space = "                    "

    #update specific profile info for both layer (young & old)
    if(opt=="1"):
      if(auth=="OLD" or auth=="old"):  
         specificAns1 = input("Please enter your Preferences for the Young : ")
         specificAns2 = input("Please specify health issues (IF ANY) else write NO : ")
      else:
         specificAns1 = input("Please enter your Profession : ")
         specificAns2 = input("Please specify the time you could devote to this service (in Hours Per Week) : ") 
      print("\n")
      specificProfile.profile.__init__(specificAns1,specificAns2)

    #Update profile code for both young and old layer        
    elif(opt=="2"):
      key = updateDriver(auth)
      if(key=="back"):
        continue
      if(key=="Invalid value"):
        print("RESULT -> Please select a valid number.\n")
        continue
      value = input("Enter new "+key+" : ")
      updateStatus = GeneralProfile.updateProfile(key,value)
      if(updateStatus == 0):
        Print("Error While Updating")
      else:    
        nextAction = input("MAIN_MENU -> UPDATE -> SUB_OPTIONS -> 1. Show Profile\n                                      2. Back")
        if(nextAction=="1"):
          GeneralProfile.showProfile()
        elif(nextAction=="2"):
          continue

    #Show own profile info    
    elif(opt=="3"):
      GeneralProfile.showProfile()

    #Search other users and take actions
    elif(opt=="4"):
      filterSearchOption = input("Choose 1. To Search By Name\n2. To Search By Role (YOUNG or OLD)\n3. To Search By Age\n4. To Search By Present Location\n5. To Search By Preferred Location\n6. To Search By Similar Intrests\n") 
      searchField,_ = getFieldIndex(filterSearchOption)
      searchValue = input("Enter the "+searchField+" you want to run the search for : ")
      print("\n")

      #Fetching all info for users returned as the search result and displaying it.
      profileArr, indvProfileArr = user.searchFunc(searchField,searchValue)
      print("USERS_WITH_"+searchField+"_AS_"+searchValue+" -> \n\n")
      i,b=1,1
      for y in indvProfileArr:
        a=1
        print(space+str(b))
        for z in y:
          field,_ = getFieldIndex(str(a))
          if(z!=None):
            print(space+field+" : "+z)
            if(a>4):break
            a=a+1
        print("\n")    
        b=b+1

      #Select the user you want to take the action to       
      selectUser = input("Press The Index(number) corresponding to a User to Select : ")
      a=1
      print("\n")
      for k in indvProfileArr[int(selectUser)-1]:
        field,_ = getFieldIndex(str(a))
        if(k!=None):
          print(space+field+" : "+k)
          if(a>4):break
          a=a+1
      print("\n")

      #Take action on selected user
      searchAction = input("Press 1. Request The user to let you take care\nPress 2. To review this user\nPress 3. For Going Back \n\n")
      if(searchAction=="1"):
        user.userToUserInteraction(indvProfileArr[int(selectUser)-1][0],"0")
        print("\n")
      elif(searchAction=="2"):
        review = input("Write a Review for "+indvProfileArr[int(selectUser)-1][0]+" : ")
        print("\n")
        user.userToUserInteraction(indvProfileArr[int(selectUser)-1][0],review)
        print("\n")
      else:
        continue

      #Show notification      
    elif(opt=="5"):
      tupleNotif = user.showNotification()
      print("NOTIFICATION -> ")
      if(len(tupleNotif)==0):
        print(space+" No Notification\n\n")
        continue
      else:   
        a=1
        for x in tupleNotif:
          if(x[2]=="Request Sent"): print(str(a)+" (Index No.)                "+x[1]+" has sent you a caring request.")
          if(x[2]=="Review"): print(str(a)+" (Index No.)                "+x[1]+" wrote "+x[3]+" as a review for you.")
          if(x[2]=="Request Denied"): print(str(a)+" (Index No.)                "+x[1]+" has denied your request for taking care.")
          if(x[2]=="Request Accepted"): print(str(a)+" (Index No.)                "+x[1]+" has accepted your request for taking care.")
          a=a+1
        print("\n")

        #Select notification you want to take action on
        selectNotif = input("Press the number corresponding to the notification to select : ")
        print("You selected "+tupleNotif[int(selectNotif)-1][2]+" by "+tupleNotif[int(selectNotif)-1][1]+"'s Notification\n\n")
        print("\n")

        #Take action on request notification
        if(tupleNotif[int(selectNotif)-1][2]=="Request Sent"):
            searchAction = input("Press 1. To accept the request\nPress 2. To Deny the Request\nPress 3. For Going Back \n\n")
            if(searchAction=="1"): user.userToUserInteraction(tupleNotif[int(selectNotif)-1][1],"1")
            elif(searchAction=="2"): user.userToUserInteraction(tupleNotif[int(selectNotif)-1][1],"2")
            elif(searchAction=="3"): continue
            else:
              print("Please choose 1, 2 or 3.\n")
              continue

        #Take action on review notification         
        if(tupleNotif[int(selectNotif)-1][2]=="Review") :
            searchAction = input("Press 1. To Review the User Back\nPress 2. For Going Back \n\n")
            if(searchAction=="1"):
              review = input("Write a Review for "+tupleNotif[int(selectNotif)-1][1]+" : ")
              user.userToUserInteraction(tupleNotif[int(selectNotif)-1][1],review)
              print("\n")
            elif(searchAction=="2"):
              continue
            else:
              print("Please choose 1 or 2.\n\n")
              continue

    #Option for exiting        
    elif(opt=="6"):
      print("Exiting") 
      break

    #for valid option
    else:
      print("RESULT -> Please select a VALID option.\n")  
    




