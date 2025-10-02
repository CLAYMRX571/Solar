from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import News, New

def Newsviews(request):
    news = News.objects.all()  
    new = New.objects.all()
    paginator = Paginator(new, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'news': news,
        'new': new,
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj,
    }

    return render(request, 'news.html', context)

def lan_switch_news(request, lan):
    return redirect(f'/{lan}/news/')
