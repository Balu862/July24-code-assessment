import logging
from validate import validates,validatemarks
import json,smtplib,logging
studentslist=[]
logging.basicConfig(filename='students.log',level=logging.DEBUG)
class Student:
    def __init__(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
        self.name=name
        self.rollno=rollno
        self.admno=admno
        self.college=college
        self.parentname=parentname
        self.mobilenumber=mobilenumber
        self.emailid=emailid
    
class Sem1Result(Student):
    def __init__(self, name, rollno, admno, college, parentname, mobilenumber, emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        super().__init__(name, rollno, admno, college, parentname, mobilenumber, emailid)
        self.sub1mark=sub1mark
        self.sub2mark=sub2mark
        self.sub3mark=sub3mark
        self.sub4mark=sub4mark
        self.sub5mark=sub5mark
    def add(self):
        if validates(self.name, self.rollno,self.admno, self.college, self.parentname,self. mobilenumber, self.emailid) ==True and validatemarks(self.sub1mark,self.sub2mark,self.sub3mark,self.sub4mark,self.sub5mark):
            total=40*5
            score=sub1mark+sub2mark+sub3mark+sub4mark+sub5mark
            dict1 ={"score":score,"total":total,"name":name,"rollno":rollno,"college":college,"parentname":parentname,"mobilenumber":mobilenumber,"emailid":emailid,"sub1mark":sub1mark,"sub2mark":sub2mark,"sub3mark":sub3mark,"sub4mark":sub4mark,"sub5mark":sub5mark}   
            studentslist.append(dict1)
try:
    if __name__ == "__main__":
        while(1):
            print("1)Add students details with marks : ")
            print("2)Display students In Json: ")
            print("3)Ranking Students in Json")
            print("4)send email to the students whose scores are less than 50%")
            print("5)exit")
            choice=int(input("Enter your choice : "))
            if choice==1:
                name=input("Enter the Student name : ")
                rollno=input("Enter your rollno : ")
                admno=input("Enter your admino : ")
                college=input("Enter your college : ")
                parentname=input("Enter your parentname : ")
                mobilenumber=input("Enter your mobilenumber with country code : ")
                emailid=input("Enter your Email: ")
                sub1mark=int(input("Enter your Sub1Marks : "))
                sub2mark=int(input("Enter your Sub2Marks : "))
                sub3mark=int(input("Enter your Sub3Marks : "))
                sub4mark=int(input("Enter your Sub4Marks : "))
                sub5mark=int(input("Enter your Sub5Marks : "))
                obj1=Sem1Result(name, rollno, admno, college, parentname, mobilenumber, emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)
                obj1.add()
                logging.info("Your data is Valid ")
                print(studentslist)
            if choice==2:
                studentsapi=json.dumps(studentslist)
                with open('Studentdetails.json','w+',encoding="utf-8") as f1:
                    f1.write(studentsapi)
                logging.info("students api is added")
            if choice==3:
                studentslist=sorted(studentslist,key=lambda i:i['score'],reverse=True)
                studentsapi=json.dumps(studentslist)
                print(studentsapi)
                with open('StudentdetailsRanking.json','w+',encoding="utf-8") as f1:
                    f1.write(studentsapi)
                    logging.info("students api is added based on Ranking")
            if choice==4:
                for i in studentslist:
                    if i['score']<int(i['total']*0.5):
                        message="dear "+parentname+"\n"+"your Son/Daughter "+ i["name"]+" as Scored lower marks please see their marks and contact me\n"
                        message=message+str(i)
                        print(message)
                        connection=smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("balu08062000@gmail.com","balu@123")
                        connection.sendmail("balu08062000@gmail.com",i["emailid"],message)
                        connection.quit
                        print("Mail sent")

                        logging.info("Ranking is Done")
            if choice==5:
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
