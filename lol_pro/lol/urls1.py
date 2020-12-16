from django.urls.conf import path
from lol.views import view2
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('statistics/', view2.StatisticsFunc),
    path('champion_detail', view2.StatisticsChaFunc),
    path('position/', view2.PositFunc),
    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)