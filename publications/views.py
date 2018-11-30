from django.shortcuts import render

# Create your views here.
def pubView(request):
    return render(request, 'publications/publications.html') 