from django.shortcuts import render
from .models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all()

    return render(request, 'menu.html', {'produtos': produtos})