from django.shortcuts import render

def home(request):
    message="This is Rita's portfolio"
    return render(request, 'index.html', {"message":message})
