from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add(request):
    if request.method=="POST":
        name=request.POST.get("name")
        admission=request.POST.get("admission")
        roll=request.POST.get("roll")
        college=request.POST.get("college")
        pname=request.POST.get("pname")
        dict1={"name":name,"admission":admission,"roll":roll,"college":college,"pname":pname}
        result=json.dumps(dict1)
        return HttpResponse(result)
    else:
        HttpResponse("Get method is not allowed")