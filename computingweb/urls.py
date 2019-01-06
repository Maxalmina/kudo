"""computingweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from landing.views import landingView
from aboutus.views import labView
from publications.views import pubView
from products.views import *
from products.solver import answer
from products.solver4 import jawaban
from products.solver16 import hasil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingView, name=""),
    path('laboratory/',labView, name="laboratory"),
    path('publications/', pubView, name ="publications"),
    path('products/', productsView, name="products"),
    path('products4/', products4View, name="products4"),
    path('products16/', products16View, name="products16"),
    path('answer/', answer, name="answer"),
    path('jawaban/', jawaban, name="jawaban"),
    path('hasil/', hasil, name="hasil"),
]
