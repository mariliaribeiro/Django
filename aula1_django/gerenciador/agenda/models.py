from django.db import models


# cria tabela agenda.ItemAgenda com 5 colunas descritas abaixo
class ItemAgenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    
