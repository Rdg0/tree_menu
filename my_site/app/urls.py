from django.urls import path
from .views import index, by_category

app_name = 'app'


urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', by_category, name='by_category'),
]