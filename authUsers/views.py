from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def registerUsers(request):

    if request.method == "GET":
        return render(request, 'register/register.html')
    
    elif request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        email = request.POST.get('e-mail')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if not password == confirm_password:
            return redirect('/auth/register')

        if len(password) < 6:
            return redirect('/auth/register')

        if User.objects.filter(username=username).exists():
            # O usuário já existe
            #return JsonResponse({'message': 'Username already exists!'}, status=400)
            return redirect('/auth/register')

        try:
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password,
            )
        except:
            return redirect('/auth/register')

        return redirect('/auth/register')


def authLogin(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) # authenticate make a validy if this datas exists.
        print(user)

        if user:

            login(request, user)
            return redirect('/exams/request_exams')
        
        else:

            return redirect('/auth/login')

