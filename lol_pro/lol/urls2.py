from django.urls.conf import path
from lol.views import view3

urlpatterns = [
    path('champion/', view3.ChampionFunc),
]