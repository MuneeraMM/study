from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def regi(request):
    if request.method== 'POST':
        username=request.POST['fname']
        email=request.POST['emai']
        password=request.POST['password']
        confirmpassword=request.POST['cpassword']
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username aready used .!.')
                print("username aready used .!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'emai aready used .!.')
                print("emaiaready used .!")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                print('user created')
                return redirect('ogin')
        else:
            messages.info(request, 'Password incorrect.!.')
            print("password mismatching...")
            return redirect('register')
    else:
        return render(request, 'register.html')

def ogin(request):
    if request.method=='POST':
        username=request.POST.get('fname')
        password=request.POST.get('password')

        user =authenticate(username=username, password=password)
        if user is not None:
         # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
        # No backend authenticated the credentials
            messages.info(request,'not a user...')
            print('not authenticated user....')
            return redirect('ogin')
    else:
        return render(request,'login.html')