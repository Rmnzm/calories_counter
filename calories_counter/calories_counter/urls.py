"""calories_counter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import re_path
from django.urls import path
from calories import views
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('', views.index),
    path('home/', views.home),
    re_path(r"^contacts", TemplateView.as_view(template_name="calories/contacts.html")),
    path('form/', views.form_page),
    re_path(r"^about", TemplateView.as_view(template_name="calories/about.html", extra_context={"header": "About Site"})),
    re_path(r"^main", TemplateView.as_view(template_name="main.html")),
    re_path(r"calculator", TemplateView.as_view(template_name="calories/calculator.html")),
    path('products/<int:productId>/', views.products),
    path('users/', views.users),
    path('temporary/', views.temporary_redirect),
    path('permanent/', views.permanent_redirect),
]
