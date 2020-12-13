from django.shortcuts import render
# 여기는 통계 전용 페이지 입니다.

def QueryFunc(request):
    return render(request, 'multi/query.html')