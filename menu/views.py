from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Produto
from decimal import Decimal, InvalidOperation


# Create your views here.

def index(request):
    produtos = Produto.objects.all()

    return render(request, 'menu.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'GET':
        return render(request, 'register_product.html', {
            'nome': '',
            'preco': '',
            'erros': [],
        })

    elif request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        preco_text = request.POST.get('preco', '').strip()

        erros = {}

        if not nome:
            erros['nome'] = 'Informe o nome do produto.'
        elif len(nome) > 100:
            erros['nome'] = 'O nome deve ter no máximo 100 caracteres.'

        try:
            preco = Decimal(preco_text)

            if not preco.is_finite():
                erros['preco'] = 'Informe um preço válido.'
            elif preco <= 0:
                erros['preco'] = 'Preço deve ser maior que R$ 0'
            else:
                expoente = preco.as_tuple().exponent
                if isinstance(expoente, int) and expoente < -2:
                    erros['preco'] = 'Use até duas casas decimais.'
            
        except InvalidOperation:
            erros['preco'] = 'Campo de preço, não pode conter letras.'

        if erros:
            return render(request, 'register_product.html', {
                'nome': nome,
                'preco': preco_text,
                'erros': erros,
            })

        Produto.objects.create(nome= nome, preco= preco)
        messages.success(request, f'Produto {nome} cadastrado com sucesso')
        return redirect('menu:index')

        # return render(request, 'menu.html', {
        #    'nome': nome,
        #    'preco': preco_text,
        #    'erros': {},
        #    'mensagem': f'Produtro {nome} cadastrado',
        # })

    return HttpResponse(status=405)

def consultar_produto(request, id):
    produto = Produto.objects.get(id=id)
    
    return render(request, 'product.html', {'produto': produto})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)

    produto.delete()

    messages.success(request, f'Produto {produto.nome} deletado')
    return redirect('menu:index')