from django.http import HttpResponse


def get_fisrt_page(request):
    text = "<h1> Hello world!!!</h1>"
    return HttpResponse(text)