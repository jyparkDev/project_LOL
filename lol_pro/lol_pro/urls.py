"""lol_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lol import views
from django.urls.conf import include
# from myboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
#     path('/', views.MainFunc), # 메인
    path('', views.MainFunc), # 메인
    
    path('champion/', include('lol.urls1')), # 챔피언 분석
    path('statistics/', include('lol.urls2')), # 통계
    path('multi/', include('lol.urls3')), # 승률예측(멀티서치)
    path('board/', include('myboard.urls')), # 게시판
]
