from django.shortcuts import render

# Create your views here.

def webapp(request):
    return render(request, 'webapp/index.html')