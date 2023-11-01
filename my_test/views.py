from django.http import HttpResponse
from django.shortcuts import render


def get_fisrt_page(request):
    text = "<h1> Hello world!!!</h1>"
    return HttpResponse(text)

def get_template_page(request):
    return render(request, 'test.html', {})