"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from app.models import Categoria, Produto
from app.forms import CategoriaForm, ProdutoForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # --- CATEGORIAS ---
    path('categorias/listar/', views.view_generica_listar, {
        'modelo': Categoria,
        'titulo': 'Categorias',
        'campos': ['id', 'nome'],
        'cabecalhos': ['ID', 'Nome'],
        'url_novo': 'categoria_criar',
        'url_editar': 'categoria_editar',
        'url_excluir': 'categoria_deletar'
    }, name='categoria_listar'),
    path('categorias/criar/', views.view_generica_criar, {
        'form_class': CategoriaForm,
        'titulo': 'Nova Categoria',
        'url_redirecionamento': 'categoria_listar'
    }, name='categoria_criar'),
    path('categorias/editar/<int:pk>/', views.view_generica_editar, {
        'modelo': Categoria,
        'form_class': CategoriaForm,
        'titulo': 'Editar Categoria',
        'url_redirecionamento': 'categoria_listar'
    }, name='categoria_editar'),
    path('categorias/deletar/<int:pk>/', views.view_generica_deletar, {
        'modelo': Categoria,
        'titulo': 'Excluir Categoria',
        'url_redirecionamento': 'categoria_listar'
    }, name='categoria_deletar'),
    
    # --- PRODUTOS ---
    path('produtos/listar/', views.view_generica_listar, {
        'modelo': Produto,
        'titulo': 'Produtos',
        'campos': ['id', 'nome', 'unidade_medida', 'preco', 'quantidade', 'categoria_id', 'valor_total'],
        'cabecalhos': ['ID', 'Nome', 'Unidade', 'Preço Unitário', 'Quantidade', 'Categoria', 'Valor Total'],
        'url_novo': 'produto_criar',
        'url_editar': 'produto_editar',
        'url_excluir': 'produto_deletar'
    }, name='produto_listar'),
    path('produtos/criar/', views.view_generica_criar, {
        'form_class': ProdutoForm,
        'titulo': 'Novo Produto',
        'url_redirecionamento': 'produto_listar'
    }, name='produto_criar'),
    path('produtos/editar/<int:pk>/', views.view_generica_editar, {
        'modelo': Produto,
        'form_class': ProdutoForm,
        'titulo': 'Editar Produto',
        'url_redirecionamento': 'produto_listar'
    }, name='produto_editar'),
    path('produtos/deletar/<int:pk>/', views.view_generica_deletar, {
        'modelo': Produto,
        'titulo': 'Excluir Produto',
        'url_redirecionamento': 'produto_listar'
    }, name='produto_deletar'),
    
    path('movimentacoes/comprar/', views.registrar_compra, name='registrar_compra'),
    path('movimentacoes/vender/', views.registrar_venda, name='registrar_venda'),
    path('movimentacoes/listar/', views.movimentacao_listar, name='movimentacao_listar'),
    
]
