from django.urls.conf import path
from lol.views import view2

urlpatterns = [
    path('statistics/', view2.StatisticsFunc),
]