import mysql.connector
from basicFunc import *
class dbConnect:
    mydb = mysql.connector.connect(host="remotemysql.com",user="KLt0ZLHDyW",password="TMDYEM5KsS",database="KLt0ZLHDyW")
    mycursor = mydb.cursor()
    def __init__(self,key1,key2):
        self.key1 = key1
        self.key2 = key2

    def UserExistOrNot(self):
        self.mycursor.execute("SELECT * FROM user where userName=\""+self.key1+"\" and role=\""+self.key2+"\"")
        myresult = self.mycursor.fetchall()
        if(len(myresult)!=0):
          status = 1
        else:
          status = 0
          
        return status

    def dataProvidedOrNot(self,fieldIndex):
        self.mycursor.execute("SELECT * FROM user where userName=\""+self.key1+"\" and role=\""+self.key2+"\"")
        myresult = self.mycursor.fetchall()
        if( myresult[0][fieldIndex]== None):
            status = 0
        else:
            status = 1
        return status

    def getProfileData(self,fieldIndex):
        self.mycursor.execute("SELECT * FROM user where userName=\""+self.key1+"\" and role=\""+self.key2+"\"")
        myresult = self.mycursor.fetchall()
        if( myresult[0][fieldIndex]== None):
            status = "Donot exist"
        else:
            status = myresult[0][fieldIndex]
        return status

    def updateProfileData(self,fieldName,newVal):
        sql="UPDATE user SET "+fieldName+" = \""+newVal+"\" where userName=\""+self.key1+"\" and role=\""+self.key2+"\""
        self.mycursor.execute(sql)
        err = self.mydb.commit()
        if(err==None):
           status = 1 
        else:
           status = 0
        return status

    def insertData(self,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10):
        sql="INSERT INTO user VALUES(\""+f1+"\",\""+f2+"\","+f3+","+f4+","+f5+","+f6+","+f7+","+f8+","+f9+","+f10+")"
        self.mycursor.execute(sql)
        err = self.mydb.commit()
        if(err==None):
           status = 1 
        else:
           status = 0
        return status

    def uniqueUserName(self):
        self.mycursor.execute("SELECT userName FROM user")
        myresult = self.mycursor.fetchall()
        status = 1
        for x in myresult:
            status = 1
            if(x[0]==self.key1):
                status = 0
                break
        return status

    def searchUserAndGetName(self,searchField,searchVal):
        self.mycursor.execute("SELECT * FROM user where "+searchField+" like '"+searchVal+"%'")
        myresult = self.mycursor.fetchall()
        arr = []
        arrIndv = []
        for x in myresult:
           valueGot = x[0]
           arrIndv.append(x)
           arr.append(valueGot)
        return arr,arrIndv  

    def updateNotification(self,sendTo,typeOfNotification,detail):
        self.mycursor.execute("SELECT notification FROM user where userName='"+sendTo+"'")
        myresult = self.mycursor.fetchall()
        if(myresult[0][0]==None):
            notif = 0
        else:
            notif= int(myresult[0][0])
        newNotif = notif + 1
        sql1="UPDATE user SET notification = '"+str(newNotif)+"' where userName='"+sendTo+"'"
        self.mycursor.execute(sql1)
        _ = self.mydb.commit()
        if(detail=="0" or detail=="1" or detail=="2"):
           sql="INSERT INTO notification VALUES('"+sendTo+"','"+self.key1+"','"+typeOfNotification+"','NULL')"
        else:
           sql="INSERT INTO notification VALUES('"+sendTo+"','"+self.key1+"','"+typeOfNotification+"','"+detail+"')" 
        self.mycursor.execute(sql)
        err = self.mydb.commit()

    def getNotification(self):
        self.mycursor.execute("SELECT * FROM notification where userName='"+self.key1+"'")
        myresult = self.mycursor.fetchall()
        arr = []
        for x in myresult:
            arr.append(x)    
        return arr
