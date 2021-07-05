from django.shortcuts import render
from .models import User



def user(request):
    if request.method == "POST":
        thank = False
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        user = User.objects.create_user(first_name=first_name, email=email, last_name=last_name, mobile=mobile)
        user.save()
        thank = "User created..!"
        return render(request, "index.html", {'thank': thank})
    print(request.POST)

    return render(request, 'index.html')
