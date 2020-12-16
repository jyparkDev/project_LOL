from django.urls.conf import path
from lol.views import view3
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('champion/', view3.ChampionFunc),
    path('tier/', view3.TierFunc),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)