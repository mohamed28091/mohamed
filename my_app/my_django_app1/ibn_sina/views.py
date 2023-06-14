from django.shortcuts import render

# Create your views here.
def index(request):
    print(request)
    return render(request,'patient/index.html')

def doctor(request):
    return render(request,'doctor/index.html')