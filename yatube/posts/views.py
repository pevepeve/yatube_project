from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком постов
def group_posts(request):
    return HttpResponse('Список постов')

# view-функция принимает параметр pk из path()
def group_post(request, slug):
    return HttpResponse(f'Пост id {slug}') 