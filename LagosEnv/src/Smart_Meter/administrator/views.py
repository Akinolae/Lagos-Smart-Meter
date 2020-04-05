from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # validating passwords
        if password == password2:

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(
                        request, "Registration successful! You can now login")
                    return redirect('login')

        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')

    else:
        return render(request, 'administrator/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, "Incorrect username or password")
            return redirect('login')

    else:
        return render(request, 'administrator/login.html')


def logout(request):
    return redirect('login')


def dashboard(request):
    return render(request, 'administrator/dashboard.html')
