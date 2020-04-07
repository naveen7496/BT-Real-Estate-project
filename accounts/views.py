from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contacts


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You have successfully logged out')
        return redirect('index')


def register(request):
    if request.method == 'POST':
        # Register User
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Password Validation
        if password == password2:
            # check username
            if User.objects.filter(username=username):
                messages.error(request, 'THE USERNAME IS TAKEN')
                return redirect('register')
            else:
                if User.objects.filter(email=email):
                    messages.error(request, 'THE email alrady exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    email=email,
                                                    password=password)
                    user.save()
                    messages.success(request, 'you have successfully registered and can login')
                    return redirect('login')

        else:
            messages.error(request, 'Your Password did not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    user_contacts = Contacts.objects.all().order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    print(context)
    return render(request, 'accounts/dashboard.html', context)
