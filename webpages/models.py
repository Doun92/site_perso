from django.db import models

from django.core.validators import MinLengthValidator

from ckeditor.fields import RichTextField

# Create your models here.
class Citation(models.Model):
    citation_fr = models.CharField(max_length=2000)
    citation_en = models.CharField(max_length=2000)
    auteur_fr = models.CharField(max_length=100)
    auteur_en = models.CharField(max_length=100)

class Certification(models.Model):
    année = models.CharField(max_length=4, validators=[MinLengthValidator(4)])
    nom_certif = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    fichier = models.CharField(max_length=120)
    type_document = models.CharField(max_length=100)
    balise = models.CharField(max_length=100, blank=True)

class Experience(models.Model):
    de_année = models.CharField(max_length=30)
    à_année = models.CharField(max_length=30)
    entreprise = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    description = RichTextField()
    type_expérience = models.CharField(max_length=30, blank=True, null=True)
    main_point_1 = models.CharField(max_length=30, blank=True, null=True)
    main_point_2 = models.CharField(max_length=30, blank=True, null=True)
    main_point_3 = models.CharField(max_length=30, blank=True, null=True)
    main_point_4 = models.CharField(max_length=30, blank=True, null=True)
    main_point_5 = models.CharField(max_length=30, blank=True, null=True)
    fichier = models.CharField(max_length=50, blank=True, null=True)
    div_tag = models.CharField(max_length=50, blank=True, null=True)
