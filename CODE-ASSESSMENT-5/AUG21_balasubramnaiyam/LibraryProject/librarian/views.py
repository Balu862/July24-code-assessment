from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from librarian.serializer import LibrarianSerializer
from librarian.models import LibrarianModel
from rest_framework.parsers import JSONParser
from rest_framework import status

#,"address":"Harrypotter","mobilenumber":9489353985,"username":"balu@gmail.com","password":"msdasbc
@csrf_exempt
def add(request):
    if request.method=="POST":
        mydata=JSONParser().parse(request)
        print(1)
        Librariandata=LibrarianSerializer(data=mydata)
        print(mydata)
        if Librariandata.is_valid():
            Librariandata.save()
            return JsonResponse(Librariandata.data,safe=False,status=status.HTTP_200_OK)
        else:
            return JsonResponse(Librariandata.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        HttpResponse("POST is only valid")

@csrf_exempt
def viewall(request):
    if request.method=="GET":
        mydata=LibrarianModel.objects.all()
        Librariandata=LibrarianSerializer(mydata,many=True)
        return JsonResponse(Librariandata.data,safe=False,status=status.HTTP_200_OK)
    else:
        return HttpResponse("get method is only accepted",status.HTTP_400_BAD_REQUEST)
@csrf_exempt

def crud(request,id):
    try:
        Librariandetail=LibrarianModel.objects.get(id=id)
    except:
        return HttpResponse("data is not present",)
    if request.method=="GET":
        Librariandata=LibrarianSerializer(Librariandetail)
        return JsonResponse(Librariandata.data,safe=False,status=status.HTTP_200_OK)
    if request.method=="DELETE":
        Librariandetail.delete()
        return HttpResponse("Deleted successfully",status=status.HTTP_200_OK)
    if request.method=="PUT":
        mydata=JSONParser().parse(request)
        Librariandetail=LibrarianSerializer(Librariandetail,data=mydata)
        if Librariandetail.is_valid():
            Librariandetail.save()
            return JsonResponse(Librariandetail.data,safe=False)
        else:
            return JsonResponse(Librariandetail.errors,status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt     
def name(request,enroll_code):
    try:
        Librariandetail=LibrarianModel.objects.get(enroll_code=enroll_code)
    except:
        return HttpResponse("data is not present")
    if request.method=="GET":
        Librariandata=LibrarianSerializer(Librariandetail)
        return JsonResponse(Librariandata.data,safe=False,status=status.HTTP_200_OK)
    else:
        return JsonResponse("use put method")
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')