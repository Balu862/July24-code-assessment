import doctors
from django.shortcuts import render

# Create your views here.
import re
from django.shortcuts import redirect, render
from django.http import JsonResponse,HttpResponse
from doctors.models import DoctorsModel
from doctors.serializer import DoctorsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests,json

# Create your views here.




def home(request):
    return render(request,'home.html')

@csrf_exempt
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password1=request.POST.get('password')
        data=DoctorsModel.objects.filter(email=username,password=password1)
        if data:
            userdata=DoctorsSerializer(data,many=True)
            request.session['user']=userdata.data
            return redirect(viewall)
    return render(request,'login.html')
@csrf_exempt
def add(request):
    if request.method=="POST":
        Doctordata=DoctorsSerializer(data=request.POST)
        print(Doctordata)
        if Doctordata.is_valid():
            Doctordata.save()
            print("save")
            return redirect(viewall)
        else:
            HttpResponse(Doctordata.errors)
    return render(request,'add.html')
@csrf_exempt
def viewall(request):
    if request.session.has_key('user'):
        a=request.session['user']
        a=a[0]
        data1=DoctorsModel.objects.filter(doctor_code=a['doctor_code'])
        Doctordata=DoctorsSerializer(data=data1,many=True)
        return  render(request,'viewall.html',{'data':data1})
    else:
        return redirect(login)

@csrf_exempt
def search(request):
    print(1)
    if request.method=="POST":
        print(1)
        rdata=request.POST.get('doctor_code')
        Doctordata=DoctorsModel.objects.filter(doctor_code=rdata)
        return render(request,'search.html',{'data':Doctordata})
    return render(request,'search.html')

@csrf_exempt
def updatehtml(request):
    
    return render(request,'update.html')

@csrf_exempt
def update(request):
    if request.method=="GET":
        rdata=request.GET.get('doctor_code')
        print(rdata)
        Doctordata=DoctorsModel.objects.filter(doctor_code=rdata)
        print(Doctordata)
        return render(request,'update.html',{'data':Doctordata})
    if request.method=="POST":
        print("update")
        rdata=request.POST.get('doctor_code')
        print(rdata)
        data1=DoctorsModel.objects.get(doctor_code=rdata)
        print("data",data1)
        rDoctor=DoctorsSerializer(request.POST)
        print(rDoctor.data)
        Doctordata=DoctorsSerializer(data1,data=rDoctor.data)
        print("Doctor",Doctordata)
        if Doctordata.is_valid():
            print("yes")
            Doctordata.save()
            print("saved")
            return redirect(viewall)
        else:
            print(Doctordata.errors)
            HttpResponse(Doctordata.errors)
    return render(request,'update.html')

@csrf_exempt
def delete(request):
    if request.method=="GET":
        print(1)
        rdata=request.GET.get('doctor_code')
        Doctordata=DoctorsModel.objects.filter(doctor_code=rdata)
        return render(request,'delete.html',{'data':Doctordata})
    if request.method=="POST":
        rdata=request.POST.get('doctor_code')
        data1=DoctorsModel.objects.get(doctor_code=rdata)
        data1.delete()
        return redirect(viewall)
    return render(request,'delete.html')


@csrf_exempt
def DoctorsCrud(request,doctor_code):
    try:
        Doctorsdata=DoctorsModel.objects.get(doctor_code=doctor_code)
    except DoctorsModel.DoesNotExist:
        return HttpResponse("Data is not present in Collection")
    if request.method=="GET":
        Doctorsdetails=DoctorsSerializer(Doctorsdata)
        return JsonResponse(Doctorsdetails.data,status=status.HTTP_200_OK)
    if request.method=="DELETE":
        Doctorsdata.delete()
        return HttpResponse("Deleted successfully",status=status.HTTP_200_OK)

    if request.method=="PUT":
        print(1)
        Doctorsdata1=JSONParser().parse(request)
        print(Doctorsdata1)
        Doctorsdetails=DoctorsSerializer(Doctorsdata,data=Doctorsdata1)
        print(Doctorsdetails)
        if Doctorsdetails.is_valid():
            Doctorsdetails.save()
            return JsonResponse(Doctorsdetails.data,safe=True,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Data is not valid")

@csrf_exempt
def searchapi(request):
    data=request.POST.get('name')
    print(data)
    details=DoctorsModel.objects.filter(name=data)
    print(details)
    Doctorsdata=DoctorsSerializer(details,many=True)
    print(Doctorsdata.data)
    return render(request,'search.html',{'data':Doctorsdata.data})
    # else:
    #     return HttpResponse(Doctorsdata.errors)
# @csrf_exempt
# def updatehtml(request):
#     print("abcd")
#     if request.method=="POST":
#         rid=request.POST.get('id')
#         details=DoctorsModel.objects.get(id=rid)
#         htmldata=DoctorsSerializer(request.POST)
#         print("html",htmldata.data)
#         Doctorsdata=DoctorsSerializer(details,data=htmldata.data)
#         print("Doctorsdata",Doctorsdata)
#         if Doctorsdata.is_valid():
#             print("its working")
#             Doctorsdata.save()
#             return redirect(viewapi)
#         else:
#             return HttpResponse(Doctorsdata.errors,status=status.HTTP_404_NOT_FOUND)
#     else:
#         return HttpResponse("Please check Your request method")
@csrf_exempt
def DoctorsAll(request):
    if request.method=="GET":
        Doctorsdetails=DoctorsModel.objects.all()
        for i in Doctorsdetails:
            print(i)
        Doctorsdata=DoctorsSerializer(Doctorsdetails,many=True)
        return JsonResponse(Doctorsdata.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def updateapi(request):
    data=request.POST.get('name')
    print(data)
    details=DoctorsModel.objects.filter(name=data)
    print(details)
    Doctorsdata=DoctorsSerializer(details,many=True)
    print(Doctorsdata.data)
    return render(request,'update.html',{'data':Doctorsdata.data})
@csrf_exempt
def createadd(request):
    if request.method=="POST":
        print(1)
        a=DoctorsSerializer(request.POST)
        print(a)
        dict1=JSONParser().parse(request)
        result=json.dumps(dict1)
        print(result)
        Doctorserial=DoctorsSerializer(data=dict1)
        #print(Doctorserial.errors)
        if (Doctorserial.is_valid()):
            print(1)
            Doctorserial.save()
            return JsonResponse(Doctorserial.data,status=status.HTTP_200_OK)
        else:
            print(Doctorserial.errors)
            return HttpResponse("Not saved",status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt   
def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
    return redirect(login)