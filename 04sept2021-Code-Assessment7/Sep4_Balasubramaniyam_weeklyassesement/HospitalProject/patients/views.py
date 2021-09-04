from django.shortcuts import render

# Create your views here.
import re
from django.shortcuts import redirect, render
from django.http import JsonResponse,HttpResponse
from patients.models import PatientModel
from patients.serializer import PatientSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests,json

# Create your views here.



@csrf_exempt
def home(request):
    return render(request,'home.html')

@csrf_exempt
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password1=request.POST.get('password')
        data=PatientModel.objects.filter(email=username,password=password1)
        if data:
            userdata=PatientSerializer(data,many=True)
            request.session['user']=userdata.data
            return redirect(viewall)
    return render(request,'login.html')


@csrf_exempt
def add(request):
    if request.method=="POST":
        Patientdata=PatientSerializer(data=request.POST)
        print(Patientdata)
        if Patientdata.is_valid():
            Patientdata.save()
            print("save")
            return redirect(viewall)
        else:
            HttpResponse(Patientdata.errors)
    return render(request,'add.html')
@csrf_exempt
def viewall(request):
    if request.session.has_key('user'):
        a=request.session['user']
        a=a[0]
        data1=PatientModel.objects.filter(patient_code=a['patient_code'])
        Patientdata=PatientSerializer(data=data1,many=True)
        return  render(request,'viewall.html',{'data':data1})
    else:
        return redirect(login)

@csrf_exempt
def search(request):
    print(1)
    if request.method=="POST":
        print(1)
        rdata=request.POST.get('patient_code')
        Patientdata=PatientModel.objects.filter(patient_code=rdata)
        return render(request,'search.html',{'data':Patientdata})
    return render(request,'search.html')

@csrf_exempt
def updatehtml(request):
    
    return render(request,'update.html')

@csrf_exempt
def update(request):
    if request.method=="GET":
        rdata=request.GET.get('patient_code')
        print(rdata)
        Patientdata=PatientModel.objects.filter(patient_code=rdata)
        print(Patientdata)
        return render(request,'update.html',{'data':Patientdata})
    if request.method=="POST":
        print("update")
        rdata=request.POST.get('patient_code')
        print(rdata)
        data1=PatientModel.objects.get(patient_code=rdata)
        print("data",data1)
        rPatient=PatientSerializer(request.POST)
        print(rPatient.data)
        Patientdata=PatientSerializer(data1,data=rPatient.data)
        print("Patient",Patientdata)
        if Patientdata.is_valid():
            print("yes")
            Patientdata.save()
            print("saved")
            return redirect(viewall)
        else:
            print(Patientdata.errors)
            HttpResponse(Patientdata.errors)
    return render(request,'update.html')

@csrf_exempt
def delete(request):
    if request.method=="GET":
        print(1)
        rdata=request.GET.get('patient_code')
        Patientdata=PatientModel.objects.filter(patient_code=rdata)
        return render(request,'delete.html',{'data':Patientdata})
    if request.method=="POST":
        rdata=request.POST.get('patient_code')
        data1=PatientModel.objects.get(patient_code=rdata)
        data1.delete()
        return redirect(viewall)
    return render(request,'delete.html')


@csrf_exempt
def PatientCrud(request,patient_code):
    try:
        Patientdata=PatientModel.objects.get(patient_code=patient_code)
    except PatientModel.DoesNotExist:
        return HttpResponse("Data is not present in Collection")
    if request.method=="GET":
        Patientdetails=PatientSerializer(Patientdata)
        return JsonResponse(Patientdetails.data,status=status.HTTP_200_OK)
    if request.method=="DELETE":
        Patientdata.delete()
        return HttpResponse("Deleted successfully",status=status.HTTP_200_OK)

    if request.method=="PUT":
        print(1)
        Patientdata1=JSONParser().parse(request)
        print(Patientdata1)
        Patientdetails=PatientSerializer(Patientdata,data=Patientdata1)
        print(Patientdetails)
        if Patientdetails.is_valid():
            Patientdetails.save()
            return JsonResponse(Patientdetails.data,safe=True,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Data is not valid")

@csrf_exempt
def searchapi(request):
    data=request.POST.get('name')
    print(data)
    details=PatientModel.objects.filter(name=data)
    print(details)
    Patientdata=PatientSerializer(details,many=True)
    print(Patientdata.data)
    return render(request,'search.html',{'data':Patientdata.data})
    # else:
    #     return HttpResponse(Patientdata.errors)
# @csrf_exempt
# def updatehtml(request):
#     print("abcd")
#     if request.method=="POST":
#         rid=request.POST.get('id')
#         details=PatientModel.objects.get(id=rid)
#         htmldata=PatientSerializer(request.POST)
#         print("html",htmldata.data)
#         Patientdata=PatientSerializer(details,data=htmldata.data)
#         print("Patientdata",Patientdata)
#         if Patientdata.is_valid():
#             print("its working")
#             Patientdata.save()
#             return redirect(viewapi)
#         else:
#             return HttpResponse(Patientdata.errors,status=status.HTTP_404_NOT_FOUND)
#     else:
#         return HttpResponse("Please check Your request method")
@csrf_exempt
def PatientAll(request):
    if request.method=="GET":
        Patientdetails=PatientModel.objects.all()
        for i in Patientdetails:
            print(i)
        Patientdata=PatientSerializer(Patientdetails,many=True)
        return JsonResponse(Patientdata.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def updateapi(request):
    data=request.POST.get('name')
    print(data)
    details=PatientModel.objects.filter(name=data)
    print(details)
    Patientdata=PatientSerializer(details,many=True)
    print(Patientdata.data)
    return render(request,'update.html',{'data':Patientdata.data})
@csrf_exempt
def createadd(request):
    if request.method=="POST":
        print(1)
        a=PatientSerializer(request.POST)
        print(a)
        dict1=JSONParser().parse(request)
        result=json.dumps(dict1)
        print(result)
        Patienterial=PatientSerializer(data=dict1)
        #print(Patienterial.errors)
        if (Patienterial.is_valid()):
            print(1)
            Patienterial.save()
            return JsonResponse(Patienterial.data,status=status.HTTP_200_OK)
        else:
            print(Patienterial.errors)
            return HttpResponse("Not saved",status=status.HTTP_400_BAD_REQUEST)

def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
    return redirect(login)