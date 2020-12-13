from django.shortcuts import render
# 여기는 챔피언 분석 및 상세 페이지 입니다.

def StatisticsFunc(request):
    return render(request, 'champion/statistics.html')