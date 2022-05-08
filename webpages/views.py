from django.shortcuts import render
import random

# Create your views here.
def cv(request):
    context = {'test':'test'}
    return render(request,'webpages/cv.html', context)

def homepage_fr(request):
    # Les images de Freyja
    freyja_pic = random.randint(0, 10)
    if freyja_pic < 10:
        freyja_pic = "0"+str(freyja_pic)

    # Liste des citations
    liste_citations = {
        "L'ignorant affirme, le savant doute, le sage réfléchit.": "Aristote",
        "Ce n'est pas un ami que l'ami de tout le monde.": "Aristote",
        "La qualité de l'expression verbale est d'être claire sans être banale.": "Aristote",
        "Un homme n'est que ce qu'il sait.": "Francis Bacon",
        "Les auteurs qui ont écrit sur le mépris de la gloire ont mis leur nom en tête du traité. ": "Francis Bacon",
        "Je voudrais vivre pour étudier, non pas étudier pour vivre.": "Francis Bacon",
        "On naît. On meurt. C'est mieux si entre les deux on a fait quelque chose.": "Francis Bacon",
        "Attendons un peu pour finir plus vite.": "Francis Bacon",
        "Les preuves sont un antidote contre le poison des témoignages.": "Francis Bacon",
        "La plaisanterie sert souvent de véhicule à la vérité.": "Francis Bacon",
        "Il bon d'être serviable, mais il faut bien montrer que c'est par estime et non par débonnaireté.": "Francis Bacon",
    }

    author, citation = random.choice(list(liste_citations.items()))

    context = {
        'freyja_pic': f'static/cat_pics/Freyja_{freyja_pic}.jpg',
        'citation': [author, citation]
    }
    return render(request,'webpages/fr/homepage.html', context)


def homepage_en(request):
    # Les images de Freyja
    freyja_pic = random.randint(0, 10)
    if freyja_pic < 10:
        freyja_pic = "0"+str(freyja_pic)

    # Liste des citations
    liste_citations = {
        "The ignorant asserts, the learned doubts, the wise reflects.": "Aristote",
        "It is not a friend that everyone's friend.": "Aristote",
        "The quality of the verbal expression is to be clear without being banal.": "Aristote",
        "A man is only what he knows.": "Francis Bacon",
        "The authors who have written about the contempt of glory have put their names at the head of the treaty.": "Francis Bacon",
        "I would like to live to study, not study to live.": "Francis Bacon",
        "We are born. We die. It's better if in between we have done something.": "Francis Bacon",
        "Let's wait a bit to finish faster.": "Francis Bacon",
        "Evidence is an antidote to the poison of testimony.": "Francis Bacon",
        "The joke often serves as a vehicle for the truth.": "Francis Bacon",
        "It is good to be helpful, but it must be shown that it is out of esteem and not out of debonairness.": "Francis Bacon",
    }
    author, citation = random.choice(list(liste_citations.items()))

    context = {
        'freyja_pic': f'static/cat_pics/Freyja_{freyja_pic}.jpg',
        'citation': [author, citation]
    }
    return render(request,'webpages/en/homepage.html', context)