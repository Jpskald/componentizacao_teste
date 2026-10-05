from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome 

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    unidade_medida = models.CharField(max_length = 10)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Movimentacao(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    class Tipo_movimentacao(models.TextChoices):
        COMPRA = 'COMPRA', 'Compra'
        VENDA = 'VENDA', 'Venda'
    tipo_movimentacao = models.CharField(
        max_length = 10,
        choices = Tipo_movimentacao.choices,
        default = Tipo_movimentacao.COMPRA
    )
    quantidade_movimentada = models.IntegerField()
    data_hora = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.produto_id.nome + ' - ' + self.tipo_movimentacao
    
