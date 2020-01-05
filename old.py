from basicFunc import *
class old(basicFunc):
    def __init__(self,name,authentication,age,presentLocation,preferredLocation):
        print("SPECIFIC_PROFILE -> Customizing old layer of profile...\n")
        #basicFunc.profile(name,authentication,age,presentLocation,preferredLocation)
         
       
              
          
    class profile:
          def _init_(self,preferences,healthIssues):
              self.preferences = preferences
              self.healthIssues = healthIssues
              
          def showSpecificProfile(self):
              print("DETAILED_PROFILE -> Preferences of Youngsters : "+self.preferences+"\n")
              print("DETAILED_PROFILE -> Health Issues : "+self.healthIssues+"\n")
