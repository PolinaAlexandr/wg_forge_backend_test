from django.http import HttpResponse


def ping(request):
    return HttpResponse('"Cats Service. Version 0.1"')
