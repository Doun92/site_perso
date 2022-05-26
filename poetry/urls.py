from django.urls import path

from . import views

from .models import Poème

# Cela permet aux templates de repérer les bons URLs (particulièrement utile lorsqu'il y aura de nombreuses app)
app_name = 'poèmes'


# URL management
urlpatterns = [
    path('index', views.index, name='index'),
    # path('<int:poeme_id>/', views.detail, name='detail'),
]

recueils = Poème.objects.values_list('recueil', flat=True).distinct()
# TODO fair une boucle fort dans cette liste et créer un url path par résultat de la liste (sans espace, bien sûr)
for recueil in recueils:
    url = recueil.replace(" ", "_")
    urlpatterns.append(path(f'{url}/<int:poeme_id>',
                       views.detail, name=f'{recueil}'))
