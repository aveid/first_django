from django.shortcuts import render
from .models import New


# Create your views here.
def get_all_news(request):
    news = New.objects.all()
    context = {
        "news": news
    }
    return render(request, 'news.html', context)
