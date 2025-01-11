from django.shortcuts import render
from .models import *
<<<<<<< HEAD
from django.core.paginator import Paginator
=======
>>>>>>> 89fcca4ffe10f3f3070a382d305293d40c0785fe


# Create your views here.
def main_page(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'shop/main_page.html', context)


def catalog_page(request):
    title = 'Каталог товаров'
    games = Game.objects.all()
    context = {
        'title': title,
        'games': games
    }
    return render(request, 'shop/catalog.html', context)


def basket_page(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'shop/basket.html', context)


def menu(request):
    return render(request, 'shop/menu.html')


# ==== Формы регистрации ====
def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    success = None

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if Buyer.objects.filter(name=name).exists():
            info['error'] = 'Пользователь уже существует'

        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'

        else:
            success = f'Приветствуем, {name}!'
            Buyer.objects.create(name=name, balance=999, age=age)

    context = {
        'error': info,
        'success': success,
        'users': users
    }


    return render(request, 'sign_up/registration_page.html', context)

# ==== Пагинация страниц ====
def news_list(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news.html', {'page_obj': page_obj})