from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    print(request.user)
    return render(request,'home/home.html')  