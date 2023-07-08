from django.http import HttpResponse


def homePage(request):
    return HttpResponse("Blog app home")
