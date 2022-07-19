import random

from django.http import *
from django.shortcuts import render
from django.template.response import TemplateResponse

from .forms import UserForm


def index(request):
    """Вызывается функция RENDER, ей передаются объект запроса и путь к файлу шаблона"""
    """TemplateResponse - задерживает рендеринг шаблона, пока все не подргузится
        render - отображает шаблон сразу же как только увидел"""
    # data = {"header": "THIS HEADER", "message": "THIS MESSAGE"}  # example
    header = "Personal Data"  # обычная строка
    languages = ["English", "German", "Spanish"]  # список он же массив
    user = {"name": "Tom", "age": 23}  # словарь
    addr = ("Абрикосовая", 23, 45)  # кортеж
    n = random.randint(-99, 99)
    data = {"header": header, "langs": languages, "user": user, "address": addr, "n": n}
    return TemplateResponse(request, "index.html", context=data)


def form_page(request):
    """Вызывается функция рендер. Кторая ренднерит некоторую форму, поля которой заданы в классе UserForm в файлу
    forms.py
    Также форма отправляет текст из полей, в которые он был введен, при нажатии на Send. Текст отобразится на странице"""
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse("<h2>Hello, {0}</h2><br><h3>You are {1} years!</h3".format(name, age))
    else:
        userform = UserForm()
        return render(request, "form.html", {"form": userform})


def home(request):
    return TemplateResponse(request, "calories/home.html")


def products(request, productId):
    """Функция принимает обычный параметр productId, который передается через URL.
    Также из строки запроса извлекается значение параметра cat:request.GET.get("cat", "")
    первый аргумент - название параметра строки запроса
    второй аргумент - значение по умолчанию"""

    """По урлу products передается номер продукта и название категории в сокращении cat"""
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0} Category: {1}</h2>". format(productId, category)
    return HttpResponse(output)


def users(request):
    """Из строки запроса извлекаются значения параметров id и name"""

    """По урлу users передается имя и айди"""
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tome")
    output = "<h2>User</h2><h3>id: {0} name {1}</h3>".format(id, name)
    return HttpResponse(output)


def temporary_redirect(request):
    return HttpResponseRedirect("/about")


def permanent_redirect(reqeust):
    return HttpResponsePermanentRedirect("/")


def about(request):
    return HttpResponse("<h2>About</h2>")


def contacts(request):
    return HttpResponse("<h2>Contacts</h2>")


def status_300(request):
    return HttpResponseNotModified()


def status_400(request):
    return HttpResponseBadRequest("<h2>Bad Request - 400 status code</h2>")


def status_403(request):
    return HttpResponseForbidden("<h2>Forbidden - 403 status code</h2>")


def status_404(request):
    return HttpResponseNotFound("<h2>Not Found - 404 status code</h2>")


def status_405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed - 405 status code</h2>")


def status_410(request):
    return HttpResponseGone("<h2>Content is no longer here - 410 status code</h2>")


def status_500(request):
    return HttpResponseServerError("<h2>Something is wrong - 500 status code</h2>")

