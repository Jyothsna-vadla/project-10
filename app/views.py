from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'Name':'jyo'}
    return render(request,'for loop.html',d)

