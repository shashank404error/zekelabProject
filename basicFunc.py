from dbConnect import *
from basicFunc import *
class basicFunc:

    def __init__(self,name,authentication,status):
        self.name=name
        self.authentication=authentication
        self.status = status
        if(status==0):
          dbInst4 = dbConnect(name,authentication)
          insertStatus = dbInst4.insertData(name,authentication,'NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL')
          if(insertStatus==1):
              print("BASIC_PROFILE -> ","profile created!")
              print("BASIC_PROFILE ->  Welcome "+self.name+", Registered as "+self.authentication+"\n")
          else:
              print("The user name is taken :( please try with a new user name.")
        elif(status==1):
          print("PROFILE -> ","Great To have you back "+self.name+"!")
        else:
          print("Some Internal error occured!")  
                
        
    def searchFunc(self,searchField,searchVal):
        dbInst5 = dbConnect(self.name,self.authentication)
        arrResult = dbInst5.searchUserAndGetName(searchField,searchVal)
        return arrResult
    
    def userToUserInteraction(self,sendTo,review):
        dbInst8 = dbConnect(self.name,self.authentication)
        if(review=="0"):
            updateNotifStatus = dbInst8.updateNotification(sendTo,"Request Sent","0")
            print("Request sent to "+sendTo)
        elif(review=="1"):
            updateNotifStatus = dbInst8.updateNotification(sendTo,"Request Accepted","1")
            print(sendTo+"'s Request Accepted")
        elif(review=="2"):
            updateNotifStatus = dbInst8.updateNotification(sendTo,"Request Denied","2")
            print(sendTo+"'s Request Denied")
        else:
            updateNotifStatus = dbInst8.updateNotification(sendTo,"Review",review)
            print("You reviewed "+sendTo)      

    def showNotification(self):
        dbInst7 = dbConnect(self.name,self.authentication)
        NotificationArr = dbInst7.getNotification()
        return NotificationArr
    
    class profile:
    
          def __init__(self,name,authentication,age,presentLocation,preferredLocation):
              self.authentication = authentication
              self.name = name
              self.age = age
              self.presentLocation = presentLocation
              self.preferredLocation = preferredLocation
              
          #createProfile(self):
          #removeProfile(self):
          def updateProfile(self,key,value):
              dbInst2 = dbConnect(self.name,self.authentication)
              status = dbInst2.updateProfileData(key,value)
              if(status == 1):
               updateStatus = 1   
               if(key=="authentication"):
                  self.authentication = value
               elif(key=="name"):   
                  self.name = value
               elif(key=="age"):   
                  self.age = value
               elif(key=="presentLocation"):   
                  self.presentLocation = value
               elif(key=="preferredLocation"):   
                  self.preferredLocation = value
              else:
                  updateStatus = 0
              return updateStatus    
               
          def showProfile(self):
              dbInst3 = dbConnect(self.name,self.authentication)
              print("DETAILED_PROFILE -> Name : "+dbInst3.getProfileData(0))
              print("DETAILED_PROFILE -> Signedin as : "+dbInst3.getProfileData(1))
              print("DETAILED_PROFILE -> Age : "+dbInst3.getProfileData(2))
              print("DETAILED_PROFILE -> Present Location : "+dbInst3.getProfileData(3))
              print("DETAILED_PROFILE -> Preferred Location : "+dbInst3.getProfileData(4)+"\n")
