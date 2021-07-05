from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import User



def user(request):
    thank = False

    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        user = User(first_name=first_name, email=email, last_name=last_name, mobile=mobile)
        user.save()
        thank = "User created..!"
        return HttpResponseRedirect("lol/", {'thank': thank})
    print(request.POST)

    return render(request, 'index.html')
