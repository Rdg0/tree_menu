from django.contrib import admin

from .models import Category, Menu, SubCategory

admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(SubCategory)