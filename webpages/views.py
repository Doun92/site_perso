from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'test':'test'}
    return render(request,'webpages/homepage.html', context)