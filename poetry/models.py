from django.db import models
from django.forms import CharField

from ckeditor.fields import RichTextField

# Create your models here.
class Poème(models.Model):
    poème = RichTextField()
    titre = models.CharField(max_length=400)
    recueil = models.CharField(max_length=400)
    numéro = models.PositiveSmallIntegerField()
