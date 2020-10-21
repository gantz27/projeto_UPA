from django.db import models
from multiselectfield import MultiSelectField

As_especificacoes = (('item_key1', 'Clinico Geral'),
              ('item_key2', 'Otorrino'),
              ('item_key3', 'Infectologia'),
              
              ('item_key4', 'Pediatria'),
              ('item_key5', 'Dermatologia'),
              ('item_key6', 'Oftamologia'),

              ('item_key7', 'Neurologia'),
              ('item_key8', 'Ginecologia'),
              ('item_key9', 'Geriatria'),

              ('item_key10', 'Cardiologia'),
              ('item_key11', 'Neurologia'),
              ('item_key12', 'Nutrologia'),
                  )


class Upa(models.Model):
    cep = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    especificacoes = MultiSelectField(choices=As_especificacoes)
    descricao = models.TextField()

    def __str__(self):
        return self.cep
