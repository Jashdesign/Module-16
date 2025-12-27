from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if username and email and password:
            return render(request,"register.html",{"success":True})
    
    return render(request,"register.html")