import pymongo,logging,smtplib,json
from datetime import datetime,date
from validatemodule import validate
logging.basicConfig(filename='BloodBank.log',level=logging.DEBUG)
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydata=client["BloodDb"]
bloodcollection=mydata["Blood"]
class BloodBank:
    def adddonor(self,name,address,email,bloodgroup,pincode,mobile,lastdonated,place):

        dict1={"name":name,"address":address,"email":email,"bloodgroup":bloodgroup,"pincode":pincode,"mobile":mobile,"lastdonated":lastdonated,"place":place}
        insertresult=bloodcollection.insert_one(dict1)
        print(insertresult)
        logging.info("added successfully")


obj1=BloodBank()
try:
    while(1):
        print("1) add Donor")
        print("2) Search donor based on blood group ")
        print("3) Search Donor based on Bloodgroup and Place")
        print("4) Update all the details with their mobile number ")
        print("5) Delete the Donor using mobile Number ")
        print("6) Display the total number of Donors using each Blood group")
        print("7) Immediate notification to all via email ")
        print("8) Exit")
        option=int(input("Enter the option :"))
        if option==1:
            name=input("enter the name: ")
            address=input("Enter the addres: ")
            bloodgroup=input("Enter the blood group: ")
            email=input("Enter Your Email id : ")
            pincode=input("enter the pincode: ")
            mobile=input("Enter the Mobile(+91): ")
            lastdonated=input("Enter the lastdonate(dd-mm-year) : ")
            place=input("enter the place : ")
            if validate(name,email,pincode,mobile,lastdonated,place):
                obj1.adddonor(name,address,email,bloodgroup,pincode,mobile,lastdonated,place)
            else:
                print("Validation Error please Enter The Details Correct")
                logging.error("Validation Error")
        if option==2:
            blood=input("Enter the Blood Group: ")
            search=bloodcollection.find({"bloodgroup":blood})
            for i in search:
                print(i)
            logging.info("Donor searched with blood group")

        if option==3:
            blood=input("Enter the Blood group: ")
            place=input("Enter the area to search: ")
            search=bloodcollection.find({"$and":[{"bloodgroup":blood},{"place":place}]})
            for i in search:
                print(i)
            logging.info("Donor searched with blood group and Place")

        if option==4:
            mobile1=input("Enter the Mobile NUmber :")
            search=bloodcollection.find_one({},{"mobile":mobile1})
            if search:
                name=input("enter the name: ")
                address=input("Enter the addres: ")
                bloodgroup=input("Enter the blood group: ")
                email=input("Enter Your Email id : ")
                pincode=input("enter the pincode: ")
                lastdonated=input("Enter the lastdonate(dd-mm-year) : ")
                place=input("enter the place : ")
                result=bloodcollection.update_one({"mobile":mobile1},{"$set":{"name":name,"address":address,"email":email,"bloodgroup":bloodgroup,"pincode":pincode,"lastdonated":lastdonated,"place":place}})
                logging.info("Donor values are updated according to Mobile number ")
            else:
                print("Mobile Number Does not Exit Please CHeck the Mobile")
                logging.error("Mobile Number is Not registered")

        if option==5:
            mobile1=input("Enter the Mobile NUmber :")
            search=bloodcollection.delete_many({"mobile":mobile1})
            logging.info("Displayed the DOnor according to Mobile Number")

        if option==6:
            result=bloodcollection.aggregate([{"$group":{"_id":"$bloodgroup","Bloodgroups":{"$sum":1}}}])
            for i in result:
                print(i)
            logging.info("Blood Group counts are disolayed")

        if option==7:
            message=input("Enter the Message ")
            result=bloodcollection.find()
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("balu08062000@gmail.com","balu@123")
            for i in result:
                connection.sendmail("balu08062000@gmail.com",i["email"],message)
                print("Mail sent")
            connection.quit
            logging.info("Mail is Sent to all")
        if option==8:
            break
except ValueError:
    logging.error("please check whether the input has to written in int or string")
    print("please check whether the input has to written in int or string")
except IndexError:
    logging.error("your value is not in the index ")
    print("your value is not in the index ")
except KeyboardInterrupt:
    logging.error("terminal is interupted due to CTRL+C")
    print("terminal is interupted due to CTRL+C")
except:
    print("Something is Error please check it")
    logging.error("Error has been occured")