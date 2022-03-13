from django.http import HttpResponse
from django.shortcuts import render
from projetodjango.entity import class_produto

produto1 = class_produto(1, "Tênis Nike", "Tenis preto, basket", 300.00, 10)
produto2 = class_produto(2, "Tênis Adidas", "Tenis branco, corrida", 230.00, 27)
produto3 = class_produto(2, "Tenis Puma", "Tenis preto, social", 280.00, 30)

lista_produtos = [produto1, produto2, produto3]


def produto(request):
    return render(request, "produto.html", {"lista_produtos":lista_produtos})


def addProduto(request):
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto', str)
        descricao = request.POST.get('descricao', str)
        valor = request.POST.get('valor', float)
        quantidade = request.POST.get('quantidade', int)
        id = len(lista_produtos) + 1
        produto = class_produto(id, nome_produto, descricao, valor, quantidade)
        lista_produtos.append(produto)
        return render(request, "add.html", {"lista_produtos":lista_produtos})
    else:
        return render(request, "add.html", {"lista_produtos":lista_produtos})