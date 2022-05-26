from django.shortcuts import render
from django.http import Http404

from .models import Poème

# Create your views here.
def index(request):

    recueils = Poème.objects.values_list('recueil', flat=True).distinct()
    for recueil in recueils:
        recueils_ss_espaces = recueil.replace(" ", "_")

    context = {
        "poèmes":Poème.objects.all(),
        "recueil" : recueils_ss_espaces
        }
    return render(request,'poetry/index.html', context)


def detail(request, poeme_id):
    try:
        poeme = Poème.objects.get(pk=poeme_id)
    except Poème.DoesNotExist:
        raise Http404("Le poème n'existe pas.")
    return render(request,'poetry/detail.html', {'poeme':poeme})