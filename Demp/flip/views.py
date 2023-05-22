from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        luname=request.POST['username']
        lpassword = request.POST['password']
        user=auth.authenticate(username=luname,password=lpassword)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid User")
            return redirect(login)
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        fpassword=request.POST['password1']
        if password==fpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username is Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email id  is Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=password,first_name=fname,last_name=lname,email=email)

                user.save();
                return redirect('login')
                print("User Created")
        else:
            messages.info(request,"passowrd not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
