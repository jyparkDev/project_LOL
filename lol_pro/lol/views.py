from django.shortcuts import render

def MainFunc(request):
    return render(request, 'main.html')
