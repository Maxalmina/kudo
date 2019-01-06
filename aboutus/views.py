from django.shortcuts import render

# Create your views here.
def labView(request):
    return render(request, 'aboutus/aboutus.html')