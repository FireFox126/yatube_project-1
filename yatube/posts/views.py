from django.http import HttpResponse
from django.shortcuts import render

# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse('Черепашка')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def icecream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
# Create your views here.
