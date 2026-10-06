from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import *

def home(request):
    return render(request, 'home.html')

# def categoria_criar(request):
#     if request.method == "POST":
#         form = CategoriaForm(request.POST)
#         if form.is_valid():
#             categoria = form.save()
#             return redirect('categoria_criar')
#     else:
#         form = CategoriaForm()
#     return render(request, 'comum/form_generico.html', {'form': form, 'titulo': 'Nova Categoria', 'url_cancelar': 'categoria_listar'})

# def categoria_listar(request):
#     categorias = Categoria.objects.all()
#     contexto = {
#         'titulo': 'Categorias',
#         'url_novo': 'categoria_criar',
#         'url_editar': 'categoria_editar',
#         'url_excluir': 'categoria_deletar',
#         'cabecalhos': ['ID', 'Nome'],
#         'linhas': [
#             {'id': c.id, 'valores': [c.id, c.nome]} for c in categorias
#         ]
#     }
#     return render(request, 'comum/listar_generico.html', contexto)

# def categoria_editar(request, pk):
#     categoria = get_object_or_404(Categoria, pk=pk)
#     if request.method == "POST":
#         form = CategoriaForm(request.POST, instance=categoria)
#         if form.is_valid():
#             categoria = form.save()
#             return redirect('categoria_listar')
#     else:
#         form = CategoriaForm(instance=categoria)
#     return render(request, 'comum/form_generico.html', {'form': form, 'titulo': 'Editar Categoria', 'url_cancelar': 'categoria_listar'})

# def categoria_deletar(request, pk):
#     categoria = get_object_or_404(Categoria, pk=pk)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect('categoria_listar')
#     contexto = {
#         'titulo': 'Excluir Categoria',
#         'item_nome': categoria.nome,
#         'url_cancelar': 'categoria_listar'
#     }
#     return render(request, 'comum/confirmar_exclusao_generico.html', contexto)

# def produto_criar(request):
#     if request.method == "POST":
#         form = ProdutoForm(request.POST)
#         if form.is_valid():
#             produto = form.save()
#             return redirect('produto_listar')
#     else:
#         form = ProdutoForm()
#     return render(request, 'comum/form_generico.html', {'form': form, 'titulo': 'Novo Produto', 'url_cancelar': 'produto_listar'})

# def produto_listar(request):
#     produtos = Produto.objects.all()
    
#     contexto = {
#         'titulo': 'Produtos',
#         'url_novo': 'produto_criar',
#         'url_editar': 'produto_editar',
#         'url_excluir': 'produto_deletar',
#         'cabecalhos': ['ID', 'Nome', 'Unidade', 'Preço Unitário', 'Quantidade', 'Categoria', 'Valor Total'],
#         'linhas': [
#             {
#                 'id': p.id, 
#                 'valores': [p.id, p.nome, p.unidade_medida, f'R$ {p.preco}', p.quantidade, p.categoria_id.nome, f'R$ {p.valor_total}']
#             } for p in produtos
#         ]
#     }
#     return render(request, 'comum/listar_generico.html', contexto)


# def produto_editar(request, pk):
#     produto = get_object_or_404(Produto, pk=pk)
#     if request.method == "POST":
#         form = ProdutoForm(request.POST, instance=produto)
#         if form.is_valid():
#             produto = form.save()
#             return redirect('produto_listar')
#     else:
#         form = ProdutoForm(instance=produto)
#     return render(request, 'comum/form_generico.html', {'form': form, 'titulo': 'Editar Produto', 'url_cancelar': 'produto_listar'})

# def produto_deletar(request, pk):
#     produto = get_object_or_404(Produto, pk=pk)
#     if request.method == "POST":
#         produto.delete()
#         return redirect('produto_listar')
#     contexto = {
#         'titulo': 'Excluir Produto',
#         'item_nome': produto.nome,
#         'url_cancelar': 'produto_listar'
#     }
#     return render(request, 'comum/confirmar_exclusao_generico.html', contexto)


def registrar_compra(request):
    if request.method == "POST":
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.tipo_movimentacao = Movimentacao.Tipo_movimentacao.COMPRA
            movimentacao.save()
            return redirect('movimentacao_listar')
    else:
        form = MovimentacaoForm()
    return render(request, 'comum/form_generico.html', {'form': form, 'titulo': 'Nova Compra', 'url_cancelar': 'movimentacao_listar'})

def registrar_venda(request):
    if request.method == "POST":
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.tipo_movimentacao = Movimentacao.Tipo_movimentacao.VENDA
            movimentacao.save()
            return redirect('movimentacao_listar')
    else:
        form = MovimentacaoForm()
    return render(request, 'comum/form_generico.html', {'form': form, 'titulo': 'Nova Venda', 'url_cancelar': 'movimentacao_listar'})

def movimentacao_listar(request):
    movimentacoes = Movimentacao.objects.all()
    contexto = {
        'titulo': 'Movimentações',
        'botoes_extras': [
            {'url': 'registrar_compra', 'label': '+ Registrar Compra'},
            {'url': 'registrar_venda', 'label': '+ Registrar Venda'}
        ],
        'cabecalhos': ['ID', 'Produto', 'Quantidade', 'Tipo', 'Data e Hora'],
        'linhas': [
            {
                'id': m.id, 
                'valores': [m.id, m.produto_id.nome, m.quantidade_movimentada, m.get_tipo_movimentacao_display(), m.data_hora.strftime('%d/%m/%Y %H:%M')]
            } for m in movimentacoes
        ]
    }
    return render(request, 'comum/listar_generico.html', contexto)


def view_generica_listar(request, modelo, titulo, campos, cabecalhos, url_novo=None, url_editar=None, url_excluir=None):
    
    registros = modelo.objects.all()        
    linhas = []
    for obj in registros:
        valores_da_linha = [getattr(obj, nome_do_campo) for nome_do_campo in campos]
        linhas.append({'id': obj.id, 'valores': valores_da_linha})

    contexto = {
        'titulo': titulo,
        'cabecalhos': cabecalhos,
        'linhas': linhas,
        'url_novo': url_novo,
        'url_editar': url_editar,
        'url_excluir': url_excluir,
    }
    return render(request, 'comum/listar_generico.html', contexto)


def view_generica_criar(request, form_class, titulo, url_redirecionamento):
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(url_redirecionamento)
    else:
        form = form_class()
        
    return render(request, 'comum/form_generico.html', {
        'form': form, 
        'titulo': titulo, 
        'url_cancelar': url_redirecionamento
    })


from django.shortcuts import render, redirect, get_object_or_404

def view_generica_editar(request, pk, modelo, form_class, titulo, url_redirecionamento):
    obj = get_object_or_404(modelo, pk=pk)
    
    if request.method == "POST":
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(url_redirecionamento)
    else:
        form = form_class(instance=obj)
        
    return render(request, 'comum/form_generico.html', {
        'form': form, 
        'titulo': titulo, 
        'url_cancelar': url_redirecionamento
    })


def view_generica_deletar(request, pk, modelo, titulo, url_redirecionamento):
    obj = get_object_or_404(modelo, pk=pk)
    
    if request.method == "POST":
        obj.delete()
        return redirect(url_redirecionamento)
    
    return render(request, 'comum/confirmar_exclusao_generico.html', {
        'titulo': titulo,
        'item_nome': str(obj), 
        'url_cancelar': url_redirecionamento
    })
