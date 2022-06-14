from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Roman!")


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


def about(request):
    return HttpResponse("<h2>About</h2>")


def contacts(request):
    return HttpResponse("<h2>Contacts</h2>")
