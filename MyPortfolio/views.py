from django.shortcuts import render

def home(request):
    message="This is sam's portfolio"
    return render(request, 'index.html', {"message":message})
