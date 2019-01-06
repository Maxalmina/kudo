from django.shortcuts import render

# Create your views here.
def productsView(request):
    return render(request, 'products/sudo.html')

def products4View(request):
    return render(request, 'products/sudo4.html')

def products16View(request):
    return render(request, 'products/sudo16.html')