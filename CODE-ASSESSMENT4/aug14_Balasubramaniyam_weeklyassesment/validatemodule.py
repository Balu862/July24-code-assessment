import re
def validateproduct(date1):
    day=date1.split('-')
    if len(day[2])==4:
        for i in range(1000,2022):
            if int(day[2])==i:
                if len(day[1])==2:
                    for j in range(1,13):
                        if int(day[1])==j:
                            if len(day[0])==2:
                                for z in range(1,32):
                                    if z==int(day[0]):
                                        return True
def validate(name,email,pincode,mobile,lastmodified,place):
    valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",name)
    valnumber=re.search("^(\+91)[6-9]\d{9}$",mobile)
    valpincode=re.search("(^[5-9])[0-9]{5}$",pincode)
    valemail=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",email)
    valplace=re.search("[A-Z]{1}[^A-Z]{0,25}$",place)
    vallast=validateproduct(lastmodified)
    if valname and valnumber and valpincode and valemail and valplace and vallast:
        return True
    else:
        return False