from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout


def login(request):
    if request.user.is_authenticated:
        return redirect('ecommerceapp:allProdCat')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            hiuser = User.objects.get(username=username)
            print(hiuser)
            if user is not None:
                auth.login(request, user)
                print(hiuser)
                return render(request,"index",{'username':request.user.username})
            else:
                messages.warning(request, "invalid credentials")
                return redirect('login')
        else:
            pass
        return render(request, "login.html")




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']

        if password == confirm_password:
            user = User.objects.create_user(username=username, first_name=name, password=password, email=email)
            user.save()

    return render(request, "register.html")