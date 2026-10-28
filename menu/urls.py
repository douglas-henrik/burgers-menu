from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar_produto, name='register'),
    path('produto/<int:id>', views.consultar_produto, name='product'),
    path('produto/<int:id>/delete', views.deletar_produto, name='delete_product'),
]