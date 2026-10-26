from django.urls import path, include

from . import views

app_name = 'main'

urlpatterns = [
    path('menu/', include('menu.urls')),
    path('', views.index, name='index'),
]