from django.http import *


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
