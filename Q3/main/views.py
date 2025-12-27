from django.shortcuts import render

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.GET.POST("name")
        email = request.GET.POST("email")
        message = request.GET.POST("message")

        if name and email and message:
            return render(request,'form.html',{'success': True})
        
    return render(request,'form.html')