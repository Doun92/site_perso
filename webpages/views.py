from itertools import product
from django.shortcuts import render
import random

from .models import Citation, Certification, Experience

# On trouve une citation aléatoire
def get_random_citation():
    len_database = len(Citation.objects.all())
    random_citation = random.randint(0, len_database)
    citation = Citation.objects.get(pk=random_citation)
    return citation

# Create your views here.
def cv(request):
    certification = Certification.objects.all()
    expérience = Experience.objects.all()

    context = {
        'test':'test',
        'certifications':certification,
        'expériences': expérience
    }
    return render(request,'webpages/cv.html', context)

def homepage_fr(request):
    # Les images de Freyja
    freyja_pic = random.randint(0, 10)
    if freyja_pic < 10:
        freyja_pic = "0"+str(freyja_pic)

    citation = get_random_citation()

    context = {
        'freyja_pic': f'static/cat_pics/Freyja_{freyja_pic}.jpg',
        # 'citation': [author, citation]
        'citation': citation,
        # 'test': len_database
    }
    return render(request,'webpages/fr/homepage.html', context)


def homepage_en(request):
    # Les images de Freyja
    freyja_pic = random.randint(0, 10)
    if freyja_pic < 10:
        freyja_pic = "0"+str(freyja_pic)

    citation = get_random_citation()

    context = {
        'freyja_pic': f'static/cat_pics/Freyja_{freyja_pic}.jpg',
        'citation': citation
    }
    return render(request,'webpages/en/homepage.html', context)