from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from jobs.forms import RegisterForm, LoginForm, ResumeForm, CredForm
from jobs.models import *
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


"""json"""


def register_list(request):
    reglist = list(Register.objects.values('UserID', 'UserType_id',
                                           'Email', 'MobileNumber',
                                           'GenderId__Name', 'Location'))
    return HttpResponse(json.dumps(reglist))


def login_list(request):
    loglist = list(Login.objects.values())
    return HttpResponse(json.dumps(loglist))


def resume_list(request):
    reslist = list(Resume.objects.values())
    return HttpResponse(json.dumps(reslist))


def usertypelist(request):
    usertypelist = list(UserType.objects.values())
    return HttpResponse(json.dumps(usertypelist))


def genderlist(request):
    genderlist = list(Gender.objects.values())
    return HttpResponse(json.dumps(genderlist))


"""forms"""


def reg(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return HttpResponse("Registered")
            except:
                pass
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})


def log(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return HttpResponse("Login Created")
            except:
                pass
    else:
        form = RegisterForm()
    return render(request, "login.html", {'form': form})


def res(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return HttpResponse("Submitted")
            except:
                pass
    else:
        form = ResumeForm()
    return render(request, "resume.html", {'form': form})


"""tables"""


def reg_table(request):
    form = list(Register.objects.values('UserID', 'UserType_id', 'Email', 'MobileNumber', 'GenderId__Name', 'Location'))
    return render(request, "register table.html", {'form': form})


def log_table(request):
    form = list(Login.objects.values('UserID_id', 'Password'))
    return render(request, "login table.html", {'form': form})


def res_table(request):
    form = list(Resume.objects.values('UserID_id', 'Content', 'File'))
    return render(request, "resume table.html", {'form': form})


"""post"""


@csrf_exempt
def register(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        users = Register()
        users.UserID = body['UserID']
        users.UserType = UserType.objects.get(UserType=body['UserType'])
        users.Email = body['Email']
        users.MobileNumber = body['MobileNumber']
        users.GenderId = Gender.objects.get(ID=int(body['GenderId']))
        users.Location = body['Location']
        users.save()
    return HttpResponse('registered')


@csrf_exempt
def create_login(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logs = Login()
        logs.UserID = Register.objects.get(UserID=body['UserID'])
        logs.Password = body['Password']
        logs.save()
    return HttpResponse('login created')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        UserID = body['UserID']
        Password = body['Password']
        loginobj = Login.objects.get(UserID=UserID)
        if loginobj is None:
            return HttpResponse("Invalid User ID")
        else:
            if loginobj.Password == Password:
                return HttpResponse("Success")
            else:
                return HttpResponse("Invalid credentials")


@csrf_exempt
def resume(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        users = Resume()
        users.UserID = Register.objects.get(UserID=body['UserID'])
        users.Content = body['Content']
        users.FileName = body['FileName']
        users.save()
    return HttpResponse('uploaded')


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload_file = fs.url(filename)
        return render(request, 'file upload.html', {
            'upload': upload_file
        })
    return render(request, 'file upload.html')
