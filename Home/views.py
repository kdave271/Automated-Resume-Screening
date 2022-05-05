from django.shortcuts import HttpResponse, redirect, render

from Home.models import user


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        email_address = request.POST.get('email')
        user_type = request.POST.get('userType')
        password = request.POST.get('passwd')
        obj = user.objects.filter(
            email_address=email_address, user_type=user_type, password=password)
        if len(obj) == 1:
            firstName = (obj[0].first_name).capitalize()
            request.session['first_name'] = firstName
            return redirect('/applicantportal')
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email_address = request.POST.get('email')
        user_type = request.POST.get('userType')
        password = request.POST.get('passwd')
        users = user(first_name=first_name, last_name=last_name, email_address=email_address,
                     password=password, user_type=user_type)
        users.save()
    return render(request, 'signup.html')


def applicant(request):
    return render(request, 'applicantportal.html')
