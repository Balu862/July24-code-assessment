from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from books.serializer import BookSerializer
from books.models import BookModel
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def add(request):
    if request.method=="POST":
        mydata=JSONParser().parse(request)
        Bookdata=BookSerializer(data=mydata)
        if Bookdata.is_valid():
            Bookdata.save()
            return JsonResponse(Bookdata.data,safe=False,status=status.HTTP_200_OK)
        else:
            return JsonResponse(Bookdata.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        HttpResponse("POST is only valid")

@csrf_exempt
def viewall(request):
    if request.method=="GET":
        mydata=BookModel.objects.all()
        Bookdata=BookSerializer(mydata,many=True)
        return JsonResponse(Bookdata.data,safe=False,status=status.HTTP_200_OK)
    else:
        return HttpResponse("get method is only accepted",status.HTTP_400_BAD_REQUEST)
@csrf_exempt

def crud(request,id):
    try:
        Bookdetail=BookModel.objects.get(id=id)
    except:
        return HttpResponse("data is not present",)
    if request.method=="GET":
        Bookdata=BookSerializer(Bookdetail)
        return JsonResponse(Bookdata.data,safe=False,status=status.HTTP_200_OK)
    if request.method=="DELETE":
        Bookdetail.delete()
        return HttpResponse("Deleted successfully",status=status.HTTP_200_OK)
    if request.method=="PUT":
        mydata=JSONParser().parse(request)
        Bookdetail=BookSerializer(Bookdetail,data=mydata,status=status.HTTP_200_OK)
        if Bookdetail.is_valid():
            Bookdetail.save()
            return JsonResponse(Bookdetail.data,safe=False)
        else:
            return JsonResponse(Bookdetail.errors,status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt     
def name(request,bookname):
    try:
        Bookdetail=BookModel.objects.get(bookname=bookname)
    except:
        return HttpResponse("data is not present")
    if request.method=="GET":
        Bookdata=BookSerializer(Bookdetail)
        return JsonResponse(Bookdata.data,safe=False,status=status.HTTP_200_OK)
    else:
        return JsonResponse("use put method")
def index(request):
    return render(request,'index.html')