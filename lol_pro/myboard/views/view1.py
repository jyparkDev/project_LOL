'''
Created on 2020. 11. 5.

@author: hee jae
'''
from django.shortcuts import render

def Main(request):
    ss = "<div><b style='text-size:24px'>안녕</b></div>"
    return render(request, "main.html", {"ss": ss})