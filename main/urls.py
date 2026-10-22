from django.urls import path, include

from . import views

urlpatterns = [
    path('menu/', include('menu.urls')),
    path('', views.index, name='index'),
]