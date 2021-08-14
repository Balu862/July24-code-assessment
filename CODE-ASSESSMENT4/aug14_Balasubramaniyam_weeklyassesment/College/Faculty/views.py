from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add(request):
    if request.method=="POST":
        name=request.POST.get("name")
        address=request.POST.get("address")
        department=request.POST.get("department")
        college=request.POST.get("college")
        dict1={"name":name,"address":address,"department":department,"college":college}
        result=json.dumps(dict1)
        return HttpResponse(result)
    else:
        HttpResponse("Get method is not allowed")