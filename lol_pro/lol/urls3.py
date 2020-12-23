from django.urls.conf import path
from lol.views import view4

urlpatterns = [
    path('query/', view4.QueryFunc),
    path('requery/', view4.RequeryFunc),
]