from django.urls.conf import path
from myboard.views import view1
from myboard.views import view2

urlpatterns = [
#     path('list/', views.ListFunc),
    path('', view1.Main),
    path('list/', view2.ListFunc),
    path('insert/', view2.InsertFunc),
    path('insertok/', view2.InsertOkFunc),
    path('update/', view2.UpdateFunc),
    path('updateok/', view2.UpdateOkFunc),
    path('delete/', view2.DeleteFunc),
    path('deleteok/', view2.DeleteOkFunc),
    path('search/', view2.SearchFunc),
    path('content/', view2.ContentFunc),
    path('reply/', view2.ReplyFunc),
    path('replyok/', view2.ReplyOkFunc),
]