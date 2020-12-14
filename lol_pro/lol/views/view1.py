from django.shortcuts import render
# 여기는 메인 페이지 입니다.
def MainFunc(request):
    return render(request, 'main.html')
