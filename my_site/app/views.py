from django.shortcuts import render

from .models import Menu, SubCategory


def index(request):
    template = 'app/index.html'
    menu = Menu.objects.all()
    context = {'menu': menu}
    return render(request, template, context)


def by_category(request, slug):
    template = 'app/by_category.html'
    subcat = SubCategory.objects.get(slug=slug)
    context = {'subcat': {subcat.name}}
    return render(request, template, context)

