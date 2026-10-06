from app.models import Movimentacao
from django import forms
from .models import *


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da categoria'})
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'unidade_medida', 'preco', 'quantidade', 'categoria_id']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'unidade_medida': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unidade de medida'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
            'categoria_id': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoria'})
        }


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto_id', 'quantidade_movimentada']
        widgets = {
            'produto_id': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Produto'}),
            'quantidade_movimentada': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'})
        }

