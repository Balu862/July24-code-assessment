import re,logging
#logging.basicConfig(filename='Validate.log',level=logging.DEBUG)
def validates(name,rollno,admino,college,parentname,mobilenumber,email):
    valname=re.search("^[A-Z]{1}[a-z]{0,25}$",name)
    valroll=re.search("^[0-9]{0,4}$",rollno)
    valadmino=re.search("^[0-9]{0,5}$",admino)
    valcollege=re.search("^[A-Za-z]{0,25}$",college)
    valemail=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",email)
    valnumber=re.search("^(\+91)[6-9]\d{9}$",mobilenumber)
    valparentname=re.search("^[A-Z]{1}[a-z]{0,25}$",parentname)
    if valname and valemail and valparentname and valnumber and valadmino and valroll and valcollege:
        print("your Details are valid")
        logging.info("Your data are valid ",name,mobilenumber,parentname,admino,rollno,college,email)
        print(name)
        print(mobilenumber)
        print(parentname)
        print(admino)
        print(rollno)
        print(college,email)
        return True
    else:
        if not valnumber:
            print("Enter number properly")
            logging.error("number is not valid")
        if not valemail:
            print("Enter email properly")
            logging.error("Email is not valid")
        if not valname:
            print("Enter Name properly")
            logging.error("Name is not valid")
        if not parentname:
            print("En properly")
            logging.error("parentname is not valid")
        if not college:
            print("Enter college name properly")
            logging.error("College name is not valid")
        if not rollno:
            print("Enter rollno properly")
            logging.error("Rollno is not valid")
        if not admino:
            print("Enter admino properly")
            logging.error("admino is not valid")
        return False
def validatemarks(sub1marks,sub2marks,sub3marks,sub4marks,sub5marks):
    list1=[int(sub1marks),int(sub2marks),int(sub3marks),int(sub4marks),int(sub5marks)]
    t=0
    for i in list1:
        if i<0 or i>40:
            t=1
            break
    if t==0:
        logging.info("Your Marks are valid")
        return True
        
    else:
        logging.error("Marks are Not valid")
        return False
        