from django.db import models
from django.core.exceptions import ValidationError

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
    @property
    def valor_total(self):
        return self.quantidade*self.preco
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
    def save(self, *args, **kwargs):
        self.clean()
        if self.tipo_movimentacao == self.Tipo_movimentacao.COMPRA:
            self.produto_id.quantidade += self.quantidade_movimentada
        else:
            self.produto_id.quantidade -= self.quantidade_movimentada
        self.produto_id.save()
        super(Movimentacao, self).save(*args, **kwargs)
    def clean(self):
        if self.tipo_movimentacao == self.Tipo_movimentacao.VENDA and self.quantidade_movimentada > self.produto_id.quantidade:
            raise ValidationError("Quantidade insuficiente para venda")


    def __str__(self):
        return self.produto_id.nome + ' - ' + self.tipo_movimentacao
    
