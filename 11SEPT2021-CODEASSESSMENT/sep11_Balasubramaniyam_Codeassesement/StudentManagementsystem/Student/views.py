from django.shortcuts import render,redirect,HttpResponse, resolve_url
from Student.models import StudentModel
from Student.serializer import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def Signup(request):
    if request.method=="POST":
        print(2)
        studentdata=StudentSerializer(data=request.POST)
        if studentdata.is_valid():
            studentdata.save()
            print("saved")
            return redirect(Login)
        else:
            print(studentdata.errors)
            return HttpResponse(studentdata.errors)
    
    return render(request,'register.html')
@csrf_exempt
def Login(request):
    print(1)
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        data=StudentModel.objects.filter(username=username,password=password)
        if data:
            userdata=StudentSerializer(data,many=True)
            userdata=userdata.data
            print(userdata)
            userdata=userdata[0]
            userdata=userdata['id']
            request.session['user']=userdata
            print(request.session['user'])
            return redirect(Index)
        else:
            return render(request,'login.html')
    return render(request,'login.html')

@csrf_exempt
def Index(request):
    if request.session.has_key('user'):
        udetail=request.session['user']
        data=StudentModel.objects.filter(id=udetail)
        return render(request,'index.html',{'data':data})
    else:
        return redirect(Login)
@csrf_exempt
def Update(request):
    if request.session.has_key('user'):
        id1=request.POST.get('id')
        print("ID1",id1)
        details=StudentModel.objects.get(id=id1)
        userdata=StudentSerializer(request.POST)
        userdetails=StudentSerializer(details,data=userdata.data)
        if userdetails.is_valid():
            userdetails.save()
            return redirect(Index)
        else:
            return HttpResponse(userdetails.errors)
    else:
        return redirect(Login)
@csrf_exempt   
def signout(request):
    if request.session.has_key('user'):
        del request.session['user']
    return redirect(Login)

