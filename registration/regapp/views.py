from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
def regi(request):
    if request.method== 'POST':
        username=request.POST['fname']
        password=request.POST['password']
        email=request.POST['emai']

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        print('user created')
        return redirect('/')
    return render(request, 'register.html')